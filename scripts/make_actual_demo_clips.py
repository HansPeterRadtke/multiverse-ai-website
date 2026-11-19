#!/usr/bin/env python3
"""Reproducible public-safe silent clips of genuine, existing Blender product animations.
No synthetic UI or generated speech is used. Original sources stay untouched.
"""
from pathlib import Path
from subprocess import run,check_output
import json
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
SRC=Path('/data/src/3d-commercial-asset-feasibility')
OUT=ROOT/'assets/demos'; OUT.mkdir(parents=True,exist_ok=True)
VIDEOS={
 'animated-forklift':SRC/'acb1eee/outputs/commercial_release_20261014_physical_steering/videos/forklift_steering_and_continuous_motion_v4.mp4',
 'industrial-machinery':SRC/'acb1eee/outputs/commercial_release_20261014_physical_steering/videos/industrial_machinery_pack_motion_corrected_v4.mp4',
 'warehouse-racking':SRC/'new-products-20261014/outputs/new_products_release_20261016/modular-pallet-storage-safety-kit-v1/media/modular-pallet-storage-safety-kit-v1_showcase.mp4',
 'warehouse-loading-dock':SRC/'new-products-20261014/outputs/new_products_release_20261016/loading-dock-handling-kit-v1/media/loading-dock-handling-kit-v1_showcase.mp4',
}
POSTER_SECS={'animated-forklift':7.0,'industrial-machinery':39.0,'warehouse-racking':1.0,'warehouse-loading-dock':1.0}
for key,src in VIDEOS.items():
 assert src.is_file(),src
 info=json.loads(check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(src)]))
 dur=float(info['format']['duration']); dst=OUT/(key+'.mp4');poster=OUT/(key+'-poster.webp')
 if not dst.exists():
  run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',str(src),'-vf','scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=24','-c:v','libx264','-preset','medium','-crf','25','-pix_fmt','yuv420p','-an','-movflags','+faststart',str(dst)],check=True)
 if not poster.exists():
  temp=OUT/(key+'-poster.jpg')
  run(['ffmpeg','-y','-hide_banner','-loglevel','error','-ss',str(POSTER_SECS[key]),'-i',str(src),'-frames:v','1','-vf','scale=960:540:force_original_aspect_ratio=decrease,pad=960:540:(ow-iw)/2:(oh-ih)/2','-q:v','2',str(temp)],check=True)
  with Image.open(temp) as im:im.convert('RGB').save(poster,'WEBP',quality=80,method=6)
  temp.unlink()
 vid=json.loads(check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(dst)]))
 streams=vid['streams']
 assert any(x['codec_type']=='video' for x in streams) and not any(x['codec_type']=='audio' for x in streams)
 actual_dur=float(vid['format']['duration']); assert 10<actual_dur<90
 txt=key.replace('-',' ').capitalize()
 captions=f'WEBVTT\n\n00:00:00.000 --> 00:00:{actual_dur:06.3f}\nGenuine rendered animation of the {txt} product. This is a digital 3D model, not physical equipment.\n'
 (OUT/(key+'.vtt')).write_text(captions)
 print('VALIDATED',key,'seconds',round(actual_dur,2),'bytes',dst.stat().st_size,'poster',poster.stat().st_size,flush=True)
