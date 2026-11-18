#!/usr/bin/env python3
"""Generate conceptual KMD imagery with Thor's installed local Z-Image model.
No service evictions. Only run with an independently confirmed broker lease.
The outputs are artwork, never screenshots of functioning KMD software.
"""
import argparse, hashlib, json, subprocess, time
from pathlib import Path

MODEL=Path('/data/models/image/z-image-turbo-bf16')
OUTPUT=Path('/data/var/multiverse-kmd/generated')
PROMPTS={
 'evidence-universe': 'Cinematic premium technical illustration of a vast archive of documents feeding a luminous three-dimensional evidence graph with delicate threads directly connected to original source pages; sophisticated deep-navy atmosphere, emerald teal and amber highlights, high-quality editorial photography and CGI blending, physically plausible lighting, striking depth and material detail. No text, logos, fake software interfaces or product screenshots. Widescreen 16:9.',
 'context-chambers': 'High-end three-dimensional conceptual scientific illustration showing three separate architectural chambers for asserted meaning, hypothetical meaning and negation, all connected to original documents by exact evidence threads, structured context boundaries, photoreal materials, dark graphite, teal, amber and violet atmospheric lighting. Conceptual KMD presentation artwork, no text, no fake UI, 16:9.'
}
def broker():
    p=subprocess.run(['/data/bin/resource-broker-gpu','--need-gib','18'],capture_output=True,text=True,timeout=15)
    if p.returncode:
        raise SystemExit('Broker preflight failed: '+p.stderr[-250:])
    return json.loads(p.stdout)
def main():
    a=argparse.ArgumentParser()
    a.add_argument('--dry-run',action='store_true')
    a.add_argument('--render',action='store_true')
    a.add_argument('--broker-reservation-confirmed',action='store_true')
    a.add_argument('--concept',choices=list(PROMPTS),default='evidence-universe')
    a.add_argument('--seed',type=int,default=20261118)
    opts=a.parse_args()
    if opts.dry_run==opts.render:
        a.error('Choose exactly one of --dry-run or --render')
    snap=broker()
    print('BROKER',snap.get('admission_by_current_snapshot'),'SAFE_HEADROOM_GIB',round(snap.get('central_broker_gpu_headroom_after_reservations_bytes',0)/(1024**3),2),flush=True)
    print('CONCEPT',opts.concept,'PROMPT_HASH',hashlib.sha256(PROMPTS[opts.concept].encode()).hexdigest(),flush=True)
    if opts.dry_run:return
    if not opts.broker_reservation_confirmed:
        raise SystemExit('BLOCKED: verified broker reservation required; no services touched.')
    if snap.get('admission_by_current_snapshot')=='must_queue_or_free_capacity':
        raise SystemExit('BLOCKED: insufficient GPU memory; no services touched.')
    import psutil
    if psutil.virtual_memory().available < 18*(1024**3):
        raise SystemExit('BLOCKED: insufficient unified RAM; no services touched.')
    import torch
    from diffusers import ZImagePipeline
    if not torch.cuda.is_available():
        raise SystemExit('BLOCKED: CUDA unavailable.')
    if not (MODEL/'model_index.json').is_file():
        raise SystemExit('BLOCKED: image model missing.')
    OUTPUT.mkdir(parents=True,exist_ok=True)
    p=OUTPUT/('KMD-'+opts.concept+'-'+str(opts.seed)+'.png')
    if p.exists():raise SystemExit('Existing output protected: '+str(p))
    pipe=ZImagePipeline.from_pretrained(str(MODEL),torch_dtype=torch.bfloat16,variant='bf16',local_files_only=True,low_cpu_mem_usage=True,device_map='cuda')
    pipe.set_progress_bar_config(disable=True)
    t=time.monotonic()
    with torch.inference_mode():
        image=pipe(prompt=PROMPTS[opts.concept],height=576,width=1024,num_inference_steps=9,guidance_scale=0.0,max_sequence_length=512,generator=torch.Generator('cuda').manual_seed(opts.seed)).images[0]
    image.save(p)
    manifest={'output':str(p),'concept':opts.concept,'seconds':round(time.monotonic()-t,2),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'UNREVIEWED_CONCEPT_ART'}
    p.with_suffix('.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(manifest))
if __name__=='__main__':main()
