#!/usr/bin/env python3
"""Regression checks for unambiguous business and demonstration descriptions."""
from pathlib import Path
import json
import subprocess
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]

def page(relative):
    return BeautifulSoup((ROOT / relative).read_text(), 'html.parser')

home = page('index.html')
hero = home.select_one('.sw-hero')
assert hero is not None
head = hero.select_one('h1')
assert head and 'What is Multiverse?' in head.get_text(' ', strip=True)
text = hero.get_text(' ', strip=True)
for phrase in ('independent development business', 'Late Order Monitor for Wix Stores', 'shop owner', 'orders already placed', 'research', 'not orders taken by Multiverse'):
    assert phrase.lower() in text.lower(), ('Missing homepage introduction:', phrase)
assert 'Mira Chen' not in text, 'A fictional test person cannot headline the business homepage'
assert not hero.select('img'), 'Unexplained Wix dashboard image may not precede the product explanation'

wix = home.select_one('#software-proof')
assert wix
wt = wix.get_text(' ', strip=True)
for phrase in ('Wix Stores', 'shop', 'read-only', 'does not take customer orders', 'CSV'):
    assert phrase.lower() in wt.lower(), ('Missing store-owner explanation', phrase)
vids = wix.select('video')
assert len(vids) == 1 and vids[0].has_attr('muted')
assert 'wix-late-order-monitor-silent.mp4' in vids[0].select_one('source')['src']

kmd = home.select_one('#research-proof')
assert kmd
kt = kmd.get_text(' ', strip=True)
for phrase in ('experimental', 'fictional documents', 'not a production-ready search service', 'not for sale as a finished app'):
    assert phrase.lower() in kt.lower(), ('Missing research limits', phrase)
assert not kmd.select('details[open]'), 'Do not put test participant names in the default homepage content'
assert len(kmd.select('details')) == 1
assert 'Mira Chen' in kmd.select_one('details').get_text(' ', strip=True)
assert 'fictional character' in kmd.select_one('details').get_text(' ', strip=True)
proof = json.loads((ROOT / 'assets/kmd/answer-proof.json').read_text())
assert proof['answer'] == 'Mira Chen' and proof['source'] == 'field_report.txt'
assert proof['answer'] in kmd.select_one('details').get_text(' ', strip=True)

kmd_detail = page('kmd/evidence/index.html').get_text(' ', strip=True).lower()
assert 'fictional person' in kmd_detail and 'not a multiverse employee' in kmd_detail

assert home.select_one('nav.desktop-nav a')['href'].endswith('/technology/')
assert (ROOT / 'assets/software-first.css').is_file()
assert (ROOT / 'scripts/rebuild_software_home.py').is_file()

# The original Wix proof clip must remain truly silent, not just muted by HTML.
video = ROOT / 'assets/focus/wix-late-order-monitor-silent.mp4'
streams = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-show_streams', '-of', 'json', str(video)]))['streams']
assert any(x['codec_type'] == 'video' for x in streams)
assert not any(x['codec_type'] == 'audio' for x in streams)
print('PASS: clear business introduction; shop-owner audience; fictional KMD test hidden and labeled; original video silent; expected navigation')
