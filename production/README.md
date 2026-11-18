# Multiverse: real demonstration video production

Commercial priority and owner goals are in `/data/infra/docs/guidelines/agents/owner_commercial_goals_and_agent_priorities.md`. Cross-chat state, correct URLs, rights/privacy, and project mapping are in `/data/infra/docs/guidelines/projects/multiverse_business_website_and_video_handover_2026-11-17.md`. These are project production source files, not completed demonstration videos. No public website copy should imply these assets were captured before they actually exist.

## Exact production sequence

1. Verify the current source application and active agents, resource broker, and read-only operational status. Coordinate with the project agent using Raspi exchange. Do not stop current KMD indexing or hijack the one owner automation browser tab.
2. Create a small safe demonstration corpus or sandbox: public-domain or personally authored documents for knowledge queries, synthetic/test orders for Wix, and non-destructive sandbox accounts for browser automation. Never display owner accounts, customer records, credentials, internal infrastructure addresses, licensed book pages, unpublished intellectual property or proprietary data.
3. Record **actual functioning software**, ideally at 1920×1080 with cursor, no desktop notifications, large fonts and readable selections. Capture source version, UTC time, test prompt, expected evidence, result and limitations before editorial cuts. Keep unedited source footage privately outside Git, e.g. `/data/var/multiverse-media/source-recordings/`; never publish raw internal logs.
4. Apply the scene-by-scene scripts below only when matching observed behavior. Use AI-video generation for title cards, transitions or clearly conceptual diagrams, never as a substitute for real product behavior. Avoid fake testimonials, results, client names or non-working UI.
5. Use `scripts/prepare_demo_clip.sh INPUT.mp4 SLUG START_SECONDS DURATION_SECONDS OUTPUT_DIR` for a compact, silent proof clip, and a thumbnail poster. Review before embedding. Preserve source recordings and attribution privately.
6. Create one page/video per capability plus a homepage teaser. The existing site is live at `https://hanspeterradtke.github.io/multiverse-ai-website/`. Videos require a suitable external host or CDN; do not assume GitHub Pages is ideal for large media. Test autoplay muted, controls, captions, mobile layout, reduced motion, bandwidth and accessibility. Do not publish placeholders presented as evidence.

## Acceptance criteria

Each release must show a reproducible working test, identifiable real input, meaningful output, citations or confirmation evidence, correct status (prototype vs published product), no leaked sensitive material, no fabricated performance or revenue claims, signed-off publication rights, correct mobile and desktop playback, accessible captions, and a visible business inquiry CTA. For anything involving a future customer, support/licensing contracts remain case-specific and optional.

## Deliverables and scripts

- `knowmoredirt.md` — real retrieval walkthrough, source attribution, optional indexing progress.
- `autonomous-agents.md` — browser/agent automation, verification and controlled recovery.
- `late-order-monitor.md` — real Wix app behavior in a test store and read-only limits.
- `hero-loop.md` — cinematic brand teaser built from approved captured footage and conceptual transitions.
- `../scripts/prepare_demo_clip.sh` — ffmpeg encoding/poster helper, tested with a disposable local fixture, not actual footage.

Use the reusable clip materials on the website, LinkedIn Featured, serious B2B outreach and presentations. The **purpose is commercial proof and qualified inquiries**, not maximizing views or making entertainment videos.

## KnowMoreDiRT visual showroom and local generator admission (November 18, 2026)

The first fully editable KMD architecture deck, icon mark, seven rendered slide previews and PDF have been **created with the installed PPT Master on Jetson** and published to `https://hanspeterradtke.github.io/multiverse-ai-website/kmd/`. The authoritative public assets and visual viewer are in `assets/kmd/` and `kmd/index.html`. Page and downloadable PPTX/PDF returned HTTP 200 after the GitHub Pages deployment. These are **architectural illustrations, not live application screenshots**. Project docs were read from the canonical KMD repository and active Raspi worktree. Current source-backed implementation is distinct from planned cross-chunk identity and discourse improvements. The created source PPT Master workspace is on Jetson at `/data/var/ppt-master/workspaces/kmd-visual-20261117_ppt169_20261117`, not an Infra report.

The owner also has local AI image and video model assets, including Z-Image Turbo BF16 on Thor, Wan2.1 family on Thor, and HunyuanVideo 1.5 on Jetson. **Presence of weights does not mean an active service or available memory.** On November 18, Thor's read-only resource broker returned `must_queue_or_free_capacity` for an 18 GiB image job. Existing LLM/voice processes were not stopped. A guarded image-generation recipe is versioned as `scripts/kmd_zimage_concepts.py` and mirrored on Thor at `/data/var/multiverse-kmd/kmd_zimage_concepts.py`. Its dry-run successfully checked the live broker and emitted exact prompt identities. It blocks unsafe rendering until an actual broker reservation is confirmed, sufficient unified memory exists, and the installed Diffusers/PyTorch pipeline imports successfully. **No generated KMD Z-Image images or HunyuanVideo clips were produced.** Once capacity is available and the model stack passes import tests, run a controlled single concept first, review the image before publication, then consider tasteful backgrounds, transitions and true KMD footage. Never preempt the running owner's models for promotional artwork.

## Nitro local Z-Image Turbo — working render path (18 November 2026)

**Successfully rendered two distinct KMD conceptual images** on Nitro (NVIDIA RTX 3060 Laptop GPU, 6 GiB nominal VRAM), without unloading other services. Saved originals and metadata in `/data/var/multiverse-kmd/zimage-nitro/`. The render used the local ~20 GiB Z-Image Turbo BF16 model, *sequential CPU/GPU offload*, 768×448 pixels, six inference steps, and a 4-thread bound. CPU RAM stayed safely above the guard threshold. Actual results are embedded, with honest concept-art captions, in `/kmd/`; the homepage KMD card also uses the context image.

Earlier attempts failed due to **shared Nitro Python dependency versions**, not model absence. The shared environment was deliberately not modified. An isolated dependency overlay was established at `/data/var/multiverse-kmd/zimage-nitro/venv/lib/python3.12/site-packages` with `transformers==4.51.3`, `tokenizers==0.21.4`, and `onnxruntime==1.22.1`. The existing shared `/data/venv/bin/python` supplies CUDA PyTorch and Diffusers; prepend the isolated overlay with `PYTHONPATH` when launching. This resolved both the missing `Qwen3Model` import and the old ONNX Runtime / NumPy 2 ABI issue. Never change the shared /data/venv just to reproduce this job.

**Reproducible command** (requires a *currently granted* Raspi central GPU-broker reservation that covers approximately two GiB GPU and adequate host RAM; the script does not obtain or renew its own lease):

```bash
export PYTHONPATH=/data/var/multiverse-kmd/zimage-nitro/venv/lib/python3.12/site-packages
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export TOKENIZERS_PARALLELISM=false
/data/venv/bin/python scripts/kmd_zimage_nitro.py --dry-run --concept context-chambers
nice -n 15 /data/venv/bin/python scripts/kmd_zimage_nitro.py --concept context-chambers --broker-reservation-confirmed
```

The script preserves existing output files and checks available CPU/CUDA RAM during inference. All outputs are generated *art*, not footage or proof of KMD retrieval behavior. The specific two images at `assets/kmd/concepts/evidence-archive.webp` and `assets/kmd/concepts/context-chambers.webp` were reviewed, optimized for the web, published to GitHub Pages, and HTTP-checked. The raw generated images remain in Nitro runtime, not in the public image-source repository.

**Remaining:** full-length high-quality local video is not solved by this image-generation success. Jetson's five-frame Wan pipeline is proven only as a minimal inference test; longer runs need a safer memory-bounded strategy. Real KnowMoreDiRT source-cited retrieval footage is the highest-value next commercial demonstration.
