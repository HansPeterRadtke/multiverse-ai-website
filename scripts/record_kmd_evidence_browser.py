#!/usr/bin/env python3
"""Record a genuine browser walkthrough of the public KnowMoreDiRT evidence site.

Starts an isolated Chromium session under a private Xvfb display. Captures
what Chromium actually renders; does not synthesize a user interface or data.
Only user-authored fictional public demo records are shown.

Usage: python3 scripts/record_kmd_evidence_browser.py [OUT.mp4]
"""
from pathlib import Path
import base64
import json
import os
import signal
import subprocess
import sys
import time
import urllib.request
import websocket

BASE = "https://hanspeterradtke.github.io/multiverse-ai-website/kmd/evidence/"
WORK = Path("/data/var/multiverse-kmd/screen-record-demo-20261118")
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else WORK / "kmd-evidence-browser-raw.mp4")
DISPLAY = ":92"
PORT = 29392
SIZE = (1440, 900)
URL = f"http://127.0.0.1:{PORT}"
_workdir = WORK
_id = 0

def say(*args):
    print(time.strftime('%H:%M:%S', time.gmtime()), *args, flush=True)

def request(ws, method, params=None, timeout=11):
    global _id
    _id += 1
    idx = _id
    ws.send(json.dumps({"id": idx, "method": method, "params": params or {}}))
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        ws.settimeout(max(0.1, end-time.monotonic()))
        try:
            response = json.loads(ws.recv())
        except websocket.WebSocketTimeoutException:
            break
        if response.get("id") == idx:
            if response.get("error"):
                raise RuntimeError(f'{method}: {response["error"]}')
            return response.get("result", {})
    raise RuntimeError(f"timeout: {method}")

def js(ws, source):
    v = request(ws, "Runtime.evaluate", {"expression": source, "returnByValue":True})
    if v.get('exceptionDetails'):
        raise RuntimeError(f"JS error: {v['exceptionDetails']}")
    return v.get("result", {}).get("value")

def goto(ws, selector, align='start'):
    expr = f"""(()=>{{
const e=document.querySelector({json.dumps(selector)});
if(!e) return "MISSING";
const r=e.getBoundingClientRect();
const offset={85 if align=='start' else 130};
const y=Math.max(0,window.scrollY+r.top-offset);
window.scrollTo({{top:y,behavior:'smooth'}});
return JSON.stringify({{tag:e.tagName,offset:y}});
}})()"""
    result=js(ws,expr)
    say("SCROLL", selector, result)
    time.sleep(3)

def move_click(ws, selector, index=0):
    source = f"""(()=>{{
const es=[...document.querySelectorAll({json.dumps(selector)})];
const e=es[{index}];
if(!e) return null;
const r=e.getBoundingClientRect();
return JSON.stringify({{x:r.left+r.width/2, y:r.top+r.height/2, rect:[r.left,r.top,r.right,r.bottom], label:e.getAttribute('aria-label')}});
}})()"""
    result=js(ws,source)
    if not result:raise RuntimeError("Cannot locate clickable node: "+selector)
    coords=json.loads(result)
    x,y=coords['x'],coords['y']
    if not (20 < x < SIZE[0]-20 and 55 < y < SIZE[1]-20):
        raise RuntimeError("Click target offscreen "+str(coords))
    request(ws,'Input.dispatchMouseEvent',{'type':'mouseMoved','x':x,'y':y,'button':'none'})
    time.sleep(0.5)
    request(ws,'Input.dispatchMouseEvent',{'type':'mousePressed','x':x,'y':y,'button':'left','clickCount':1})
    request(ws,'Input.dispatchMouseEvent',{'type':'mouseReleased','x':x,'y':y,'button':'left','clickCount':1})
    say('CLICK', selector, index, coords['label'])
    time.sleep(2)

def terminate_group(proc):
    if not proc:return
    try:
        os.killpg(proc.pid, signal.SIGTERM)
    except ProcessLookupError:
        return

def main():
    WORK.mkdir(parents=True, exist_ok=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if Path("/tmp/.X11-unix/X92").exists():
        raise RuntimeError("X display 92 is already in use. Nothing touched.")
    try:
        urllib.request.urlopen(URL+"/json/version",timeout=0.5)
        raise RuntimeError("CDP port 29392 is already in use. Nothing touched.")
    except urllib.error.URLError:
        pass
    logs=[open(WORK / (name+'.log'),'w') for name in ('xvfb-demo', 'chrome-demo', 'ffmpeg-demo')]
    xvfb=chromium=ffmpeg=None
    browser_ws=None
    try:
        xvfb=subprocess.Popen(
            ['/usr/bin/Xvfb',DISPLAY,'-screen','0',f'{SIZE[0]}x{SIZE[1]}x24','-nolisten','tcp'],
            stdout=logs[0],stderr=subprocess.STDOUT,start_new_session=True)
        time.sleep(1)
        env={**os.environ,'DISPLAY':DISPLAY,'NO_AT_BRIDGE':'1'}
        chromium=subprocess.Popen(
            ['/snap/chromium/3583/usr/lib/chromium-browser/chrome',
             '--no-sandbox','--disable-gpu','--disable-dev-shm-usage',
             '--disable-extensions','--no-first-run','--disable-default-apps',
             '--disable-background-networking','--no-default-browser-check',
             '--user-data-dir=/home/hans/.cache/mv-kmd-screen-record-isolated',
             '--remote-debugging-port='+str(PORT), '--remote-allow-origins=*',
             f'--window-size={SIZE[0]},{SIZE[1]}','--kiosk',
             BASE],
            env=env,stdout=logs[1],stderr=subprocess.STDOUT,start_new_session=True)
        v=None
        for _ in range(36):
            try:
                v=json.load(urllib.request.urlopen(URL+"/json/version",timeout=0.4))
                break
            except Exception:
                time.sleep(0.4)
        if not v:raise RuntimeError("Could not launch isolated Chrome")
        tabs=json.load(urllib.request.urlopen(URL+"/json/list",timeout=3))
        t=next((a for a in tabs if a.get('type')=='page' and 'kmd/evidence' in a.get('url','')),None)
        if not t:raise RuntimeError("Public KMD evidence tab missing")
        page=websocket.create_connection(t['webSocketDebuggerUrl'],timeout=6,suppress_origin=True)
        browser_ws=page
        request(page,'Page.enable')
        request(page,'Runtime.enable')
        for _ in range(20):
            status=js(page,'JSON.stringify({title:document.title,nodes:document.querySelectorAll("#evidence-network .node").length,answer:!!document.querySelector("#answer-proof")})')
            current=json.loads(status or '{}')
            if current.get('nodes',0)>=15 and current.get('answer'):break
            time.sleep(0.5)
        else: raise RuntimeError("Site did not load verified evidence graph and answer")
        say('SITE_VERIFIED',current)
        js(page,"window.scrollTo({top:0,behavior:'instant'})")
        time.sleep(1)
        # Start video capture ONLY after a fully loaded browser, avoiding empty screens.
        ffmpeg=subprocess.Popen(
            ['/usr/bin/ffmpeg','-nostdin','-hide_banner','-loglevel','error',
             '-y','-f','x11grab','-draw_mouse','1','-video_size',f'{SIZE[0]}x{SIZE[1]}',
             '-framerate','24','-i',DISPLAY+'.0',
             '-vf','scale=1280:800:flags=lanczos,format=yuv420p',
             '-an','-c:v','libx264','-preset','veryfast','-crf','21',
             '-movflags','+faststart','-threads','4',str(OUT)],
            stdout=logs[2],stderr=subprocess.STDOUT,start_new_session=True)
        say('CAPTURE_STARTED',OUT)
        time.sleep(4)
        goto(page, '#answer-proof')
        say('PROOF_TEXT',js(page,'document.querySelector("#answer-proof .answer-value")?.innerText'))
        time.sleep(3)
        goto(page, '#explorer')
        say('GRAPH_COUNTS',js(page,'document.querySelector("#graph-stats")?.innerText'))
        time.sleep(2)
        goto(page, '.network-shell')
        move_click(page,'#evidence-network .node.ref',0)
        say('INSPECT_REF',js(page,'document.querySelector("#inspector-content")?.innerText?.slice(0,200)'))
        time.sleep(1)
        # Another node is an original document, linked directly to the indexed text.
        move_click(page,'#evidence-network .node.doc',1)
        say('INSPECT_SOURCE',js(page,'document.querySelector("#inspector-content")?.innerText?.slice(0,160)'))
        time.sleep(2)
        move_click(page,'#network-filters button[data-mode="contexts"]')
        time.sleep(2)
        goto(page,'.source-browser')
        time.sleep(5)
        goto(page,'.real-boundary')
        time.sleep(3)
        goto(page,'#answer-proof')
        time.sleep(4)
        say('CAPTURE_END')
        ffmpeg.send_signal(signal.SIGINT)
        ffmpeg.wait(timeout=18)
        if ffmpeg.returncode not in (0, 255):
            # ffmpeg commonly exits with 255 when stopped via SIGINT after writing valid MP4.
            raise RuntimeError(f'ffmpeg failed: {ffmpeg.returncode}, {Path(WORK/"ffmpeg-demo.log").read_text()[-550:]}')
        if OUT.stat().st_size < 100000:raise RuntimeError("Video unexpectedly small")
        probe=subprocess.run(
            ['/usr/bin/ffprobe','-v','error','-show_entries','format=duration,size:stream=codec_name,width,height,r_frame_rate,nb_frames','-of','json',str(OUT)],
            capture_output=True,text=True,timeout=8,check=True)
        say('CAPTURE_VERIFIED',probe.stdout.strip())
        Path(str(OUT)+'.json').write_text(probe.stdout,encoding='utf-8')
    finally:
        if browser_ws:
            browser_ws.close()
        if ffmpeg and ffmpeg.poll() is None:
            ffmpeg.send_signal(signal.SIGINT)
            try:ffmpeg.wait(timeout=8)
            except subprocess.TimeoutExpired:terminate_group(ffmpeg)
        terminate_group(chromium)
        terminate_group(xvfb)
        for f in logs:f.close()

if __name__=='__main__':main()
