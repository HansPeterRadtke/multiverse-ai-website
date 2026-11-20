#!/usr/bin/env python3
"""Check the authentic Blender image portfolio and AI automation story."""
from pathlib import Path
from bs4 import BeautifulSoup
from hashlib import sha256
from PIL import Image
import json
R=Path(__file__).resolve().parents[1]
read=lambda path:BeautifulSoup((R/path).read_text(),'html.parser')
home=read('index.html');page=read('3d/index.html')
hero=page.select_one('.ap-hero');assert hero
h1=hero.select_one('h1').get_text(' ',strip=True)
assert 'AI-directed Blender workflows' in h1,h1
assert 'ChatGPT' in page.select_one('#pipeline').get_text(' ',strip=True)
assert 'my own network of machines' in hero.get_text(' ',strip=True)
assert 'one-click 3D generation service' in page.select_one('#pipeline').get_text(' ',strip=True)
assert len(page.select('#pipeline .ap-process-grid article'))==4
assert len(page.select('.ap-machine-grid > div'))==4
for machine in ('Nitro','Thor','Jetson','Raspi'):
 assert machine in page.select_one('.ap-machines').get_text(' ',strip=True),machine
assert 'not a claim that a single unified job' in page.select_one('.ap-machine-caveat').get_text(' ',strip=True)
assert len(page.select('#visual-proof figure'))==3
assert len(page.select('#motion-proof video'))==2
assert all(v.has_attr('controls') and v.get('preload')=='none' for v in page.select('#motion-proof video'))
assert 'not a guarantee' not in page.select_one('#catalog').get_text(' ',strip=True).lower()
assert len(page.select('#catalog .pf-card'))==3,'Do not remove existing published product links'
assert all(page.select_one(f'a[href="{url}"]') for url in (
'https://www.cgtrader.com/3d-models/industrial/industrial-machine/animated-electric-counterbalance-forklift',
'https://www.cgtrader.com/3d-models/industrial/industrial-machine/modular-warehouse-pallet-racking-and-safety-kit-13-pbr-assets',
'https://www.cgtrader.com/3d-models/industrial/industrial-machine/animated-warehouse-loading-dock-and-handling-kit-9-pbr-models'))
source=json.loads((R/'assets/3d/agent-made/source-receipts.json').read_text())
assert len(source)==3
for r in source:
 assert '/data/' not in json.dumps(r) and 'source_path_private' not in r,'Never publish private machine locations'
 f=R/r['image'];assert f.is_file();im=Image.open(f);im.verify()
 assert sha256(f.read_bytes()).hexdigest()==r['result_sha256']
 assert f.stat().st_size==r['result_bytes']
 assert r['source_sha256'] and len(r['source_sha256'])==64
 assert r['provenance']=='actual Blender Cycles scene render'
 assert r['quality_boundary']=='visual candidate; photographic realism not owner-certified'
 assert page.select_one(f'img[src="/multiverse-ai-website/{r["image"]}"]')
 print('VERIFIED_IMAGE',r['image'],r['result_bytes'],'B')
hp=home.select_one('#industrial-assets');assert hp
assert 'AI agents built this industrial 3D scene' in hp.select_one('h2').get_text(' ',strip=True)
assert hp.select_one('a[href="/multiverse-ai-website/3d/"]')
assert home.select_one('.ap-home-media img[src="/multiverse-ai-website/assets/3d/agent-made/warehouse-exterior.webp"]')
sections=[x.get('id') for x in home.select('main>section')]
assert sections.index('swaag')<sections.index('research-proof')<sections.index('industrial-assets')<sections.index('software-proof')
assert home.select_one('link[href="/multiverse-ai-website/assets/3d-agent-production.css"]')
assert page.select_one('link[href="/multiverse-ai-website/assets/3d-agent-production.css"]')
assert page.title.get_text(' ',strip=True)=='AI-Directed 3D Production with Blender | Multiverse'
print('PASS: authentic image hashes, automation workflow, machine roles, original video, buyer links and home hierarchy')
