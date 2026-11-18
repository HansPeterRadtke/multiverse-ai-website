#!/usr/bin/env python3
"""Reproducible KMD Z-Image Turbo conceptual art on Nitro (RTX 3060, CPU/GPU offload).

Only the pre-existing local model is used. Never changes the system Python
environment or unloads other services. Production outputs must be reviewed.
Use with an independently granted and verified resource broker reservation.
"""
import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

MODEL = Path("/data/models/image/z-image-turbo-bf16")
DEFAULT_OUTPUT = Path("/data/var/multiverse-kmd/zimage-nitro")
PROMPTS = {
    "evidence-archive": (
        "High-budget cinematic science documentary still. Vast majestic archive of "
        "original engineering documents, antique books and elegant laboratory reports, "
        "composed in a monumental architectural interior. Hundreds of precise fine "
        "glowing teal threads connect individual original paper pages to an intricate "
        "central glass evidence sculpture, emphasizing credible source provenance. "
        "Wide-angle perspective, rich physically plausible shadows, amber-gold "
        "highlights, polished photorealistic materials, atmospheric blue and teal "
        "volumetric light, deep contrast, exquisite cinematic production design. "
        "Absolutely no text, letters, UI, people, fake data or logos."
    ),
    "context-chambers": (
        "A sophisticated cinematic illustration of three interconnected yet clearly "
        "separate chambers inside a monumental futuristic knowledge archive. "
        "A deep emerald green chamber represents a confirmed fact, a warm golden "
        "chamber represents a hypothetical possibility, and a deep amethyst chamber "
        "represents a negated statement. Each chamber contains beautiful floating "
        "paper documents with fine luminous filaments connecting them to a central "
        "transparent geometric evidence prism. Photoreal glass and stone, highly "
        "detailed production design, powerful architectural composition, moody "
        "volumetric light, exquisite crisp detail, dramatic depth and contrast. "
        "No words, lettering, logos, charts or software UI."
    ),
}
OVERLAY = Path("/data/var/multiverse-kmd/zimage-nitro/venv/lib/python3.12/site-packages")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--concept", choices=sorted(PROMPTS), default="evidence-archive")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--broker-reservation-confirmed", action="store_true")
    parser.add_argument("--width", type=int, default=768)
    parser.add_argument("--height", type=int, default=448)
    parser.add_argument("--steps", type=int, default=6)
    parser.add_argument("--seed", type=int, default=20261118)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if args.width % 16 or args.height % 16 or not (1 <= args.steps <= 30):
        parser.error("Width/height must be multiples of 16 and steps must be 1–30.")
    prompt = PROMPTS[args.concept]
    report = {"concept": args.concept, "prompt": prompt, "seed": args.seed,
              "steps": args.steps, "width": args.width, "height": args.height,
              "model_path": str(MODEL),
              "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()}
    if args.dry_run:
        print(json.dumps(report, indent=2))
        return
    if not args.broker_reservation_confirmed:
        raise SystemExit("BLOCKED: reserve GPU memory with central broker on Raspi first.")
    for path in [MODEL / "model_index.json", OVERLAY / "transformers", OVERLAY / "onnxruntime"]:
        if not path.exists():
            raise SystemExit("BLOCKED: expected local model/dependency missing: " + str(path))
    # The current process must be launched with PYTHONPATH set to the isolated overlay.
    if str(OVERLAY) not in os.environ.get("PYTHONPATH", "").split(":"):
        raise SystemExit("BLOCKED: PYTHONPATH must include the isolated Nitro dependency overlay.")
    import psutil
    import torch
    from diffusers import ZImagePipeline
    if psutil.virtual_memory().available < 30 * 1024**3:
        raise SystemExit("BLOCKED: less than 30 GiB available host RAM.")
    if not torch.cuda.is_available():
        raise SystemExit("BLOCKED: CUDA unavailable.")
    if torch.cuda.mem_get_info()[0] < 2 * 1024**3:
        raise SystemExit("BLOCKED: less than 2 GiB CUDA memory available.")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    path = args.output_dir / ("KMD-" + args.concept + "-" + str(args.seed) + ".png")
    if path.exists():
        raise SystemExit("BLOCKED: existing output file protected: " + str(path))
    torch.set_num_threads(4)
    started = time.monotonic()
    print("START", args.concept, torch.cuda.get_device_name(0), flush=True)
    pipe = ZImagePipeline.from_pretrained(
        str(MODEL), torch_dtype=torch.bfloat16,
        variant="bf16", local_files_only=True, low_cpu_mem_usage=True)
    if psutil.virtual_memory().available < 9 * 1024**3:
        raise SystemExit("BLOCKED: memory too low after model loading.")
    pipe.enable_sequential_cpu_offload(gpu_id=0)
    pipe.set_progress_bar_config(disable=True)

    def check_memory(pipe_obj, step, timestep, kwargs):
        available = psutil.virtual_memory().available
        print("INFERENCE_STEP", step, "free_GiB", round(available / 1024**3, 1), flush=True)
        if available < 5 * 1024**3:
            raise RuntimeError("Stopped due to low available host RAM")
        return kwargs

    with torch.inference_mode():
        image = pipe(prompt=prompt, width=args.width, height=args.height,
                     num_inference_steps=args.steps,
                     guidance_scale=0.0, max_sequence_length=128,
                     generator=torch.Generator("cuda").manual_seed(args.seed),
                     callback_on_step_end=check_memory).images[0]
    image.save(path)
    report.update({"status": "UNREVIEWED_CONCEPT_ART_NOT_SOFTWARE_SCREENSHOT",
                   "output": str(path), "seconds": round(time.monotonic()-started, 2),
                   "output_sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    path.with_suffix(".json").write_text(json.dumps(report, indent=2) + "\n")
    print("SUCCESS", str(path), report["seconds"], flush=True)


if __name__ == "__main__":
    main()
