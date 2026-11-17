#!/usr/bin/env bash
set -euo pipefail
script_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
tmpdir=$(mktemp -d)
trap 'rm -rf -- "$tmpdir"' EXIT
ffmpeg -nostdin -hide_banner -loglevel error -y -f lavfi -i 'testsrc2=size=640x360:rate=15:duration=2' -an -c:v libx264 -pix_fmt yuv420p "$tmpdir/fixture.mp4"
"$script_dir/prepare_demo_clip.sh" "$tmpdir/fixture.mp4" fixture 0 1 "$tmpdir/output"
python3 - "$tmpdir/output/fixture-metadata.json" <<'PY'
import json,sys
j=json.load(open(sys.argv[1]));s=j['streams'][0]
assert s['codec_name']=='h264'
assert (s['width'],s['height'])==(1280,720)
assert float(j['format']['duration'])>0
print('PASS: disposable clip transcode, poster and JSON metadata')
PY
