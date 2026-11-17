#!/usr/bin/env bash
# Condense OWNER-APPROVED real source footage; no invented behavior, uploads, or server dependencies.
set -euo pipefail
if (( $# != 5 )); then
  echo 'Usage: prepare_demo_clip.sh INPUT.mp4 SLUG START_SECONDS DURATION_SECONDS OUTPUT_DIR' >&2
  exit 2
fi
source_video=$1
slug=$2
start=$3
duration=$4
out_dir=$5
if [[ ! -f "$source_video" || ! "$slug" =~ ^[a-z0-9][a-z0-9-]{0,60}$ ]]; then
  echo 'Input must exist and slug must contain lowercase letters, digits, or hyphens.' >&2
  exit 2
fi
python3 - "$start" "$duration" <<'PY'
import sys,math
start,duration=(float(x) for x in sys.argv[1:])
if not (math.isfinite(start) and math.isfinite(duration) and start>=0 and 0<duration<=600):
 raise SystemExit('Invalid start or duration; duration must be between zero and ten minutes.')
PY
command -v ffmpeg >/dev/null
command -v ffprobe >/dev/null
mkdir -p -- "$out_dir"
master="$out_dir/$slug.mp4"
poster="$out_dir/$slug-poster.jpg"
meta="$out_dir/$slug-metadata.json"
ffmpeg -nostdin -hide_banner -loglevel error -y -ss "$start" -i "$source_video" -t "$duration" \
  -vf 'fps=30,scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2:color=0x080e1b,format=yuv420p' \
  -an -c:v libx264 -preset medium -crf 24 -movflags +faststart "$master"
ffmpeg -nostdin -hide_banner -loglevel error -y -i "$master" -frames:v 1 -q:v 2 "$poster"
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate:format=duration,size -of json "$master" > "$meta"
python3 - "$meta" <<'PY'
import json,sys
j=json.load(open(sys.argv[1]));stream=j['streams'][0]
if (stream['width'],stream['height'],stream['codec_name']) != (1280,720,'h264'):
 raise SystemExit('Output verification failed')
print('Verified local H.264 clip and poster. Review before publication.')
PY
printf '%s\n%s\n%s\n' "$master" "$poster" "$meta"
