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
assert head and 'AI workers you can manage. Knowledge you can trust.' in head.get_text(' ', strip=True)
text = hero.get_text(' ', strip=True)
for phrase in ('independent software development business', 'SWAAG', 'background', 'KnowMoreDiRT', 'Late Order Monitor for Wix Stores', 'experimental'):
    assert phrase.lower() in text.lower(), ('Missing homepage introduction:', phrase)
assert 'Mira Chen' not in text, 'A fictional test person cannot headline the business homepage'
assert len(hero.select('.sw-home-example-image')) == 2, 'Project imagery must be shown inside explicitly labelled cards'
assert 'document search research' not in hero.get_text(' ', strip=True).lower()

wix = home.select_one('#software-proof')
assert wix
wt = wix.get_text(' ', strip=True)
for phrase in ('Wix Stores', 'shop owner', 'paid, unfulfilled orders', 'read-only', 'does not take customer orders', 'CSV'):
    assert phrase.lower() in wt.lower(), ('Missing store-owner explanation', phrase)
vids = wix.select('video')
assert len(vids) == 1 and vids[0].has_attr('muted')
assert 'wix-late-order-monitor-silent.mp4' in vids[0].select_one('source')['src']

kmd = home.select_one('#research-proof')
assert kmd
kt = kmd.get_text(' ', strip=True)
for phrase in ('semantic retrieval', 'discourse representation theory', 'fictional documents', 'not a production-ready search service', 'not for sale as a finished app'):
    assert phrase.lower() in kt.lower(), ('Missing research limits', phrase)
assert not kmd.select('details[open]'), 'Do not put test participant names in the default homepage content'
assert len(kmd.select('details')) == 1
assert 'Mira Chen' in kmd.select_one('details').get_text(' ', strip=True)
assert len(kmd.select('.sw-kmd-user-value > div')) == 3, 'Separate user workflow, intended benefit, and source-evidence feature'
assert 'fictional character' in kmd.select_one('details').get_text(' ', strip=True)
proof = json.loads((ROOT / 'assets/kmd/answer-proof.json').read_text())
assert proof['answer'] == 'Mira Chen' and proof['source'] == 'field_report.txt'
assert proof['answer'] in kmd.select_one('details').get_text(' ', strip=True)

kmd_page = page('kmd/index.html')
assert 'Find meaning in the chaos of your files.' in kmd_page.select_one('main h1').get_text(' ', strip=True)
assert len(kmd_page.select('#how-to-use .kmd-use-flow > div')) == 3
assert len(kmd_page.select('#user-benefits .kmd-benefit-cards article')) == 3
assert len(kmd_page.select('.kmd-meaning-research')) == 1
assert kmd_page.select_one('.kmd-hero-flow-illustration'), 'Make the intended workflow visible before the fictional test'
assert not kmd_page.select_one('.kmd-purpose-hero .kmd-focus-hero-art'), 'A large fictional test screenshot should not headline the project'
assert 'Conceptual workflow illustration' in kmd_page.select_one('.kmd-hero-flow-illustration').get_text(' ',strip=True)
assert 'public API still returns a plain answer string' in kmd_page.get_text(' ', strip=True)
assert 'broad understanding' in kmd_page.get_text(' ', strip=True)
assert kmd_page.select('main .kmd-focus-more details')
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
