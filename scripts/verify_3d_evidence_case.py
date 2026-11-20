#!/usr/bin/env python3
"""Verify grounded industrial-scene engineering case and guard misleading claims."""
from pathlib import Path
from bs4 import BeautifulSoup
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[1]
case=ROOT/'assets/3d/agent-made/warehouse-engineering-checkpoint.json'
record=json.loads(case.read_text())
assert record['recorded_utc_date']=='2026-11-10'
assert record['status'].startswith('Specific source and geometry checks')
r=record['results']
assert r['forklift_wheel_ground_gap_mm_before_approx']==7.1
assert r['forklift_wheel_ground_gap_mm_after_at_most']==0.03
assert r['fixed_seed_native_cycles_stills_examined']==29
assert r['sampled_rays_through_open_loading_bay']==9
assert r['additional_modeled_cartons']==111
assert r['new_pallets']==15
assert len(record['source_receipts'])==6
assert len(set(x['name'] for x in record['source_receipts']))==6
assert all(len(x['sha256'])==64 and all(c in '0123456789abcdef' for c in x['sha256']) for x in record['source_receipts'])
assert '/data/' not in case.read_text() and '/home/' not in case.read_text()
assert 'separate development revisions' in record['scene_and_presentation_relationship']
assert len(record['important_limitations'])>=4
s=BeautifulSoup((ROOT/'3d/index.html').read_text(),'html.parser')
sections=s.select('main > section')
ids=[x.get('id') for x in sections]
assert ids.index('pipeline') < ids.index('visual-proof') < ids.index('engineering-proof') < ids.index('motion-proof') < ids.index('catalog')
assert len(s.select('section.ap-proof-case'))==1
assert not s.select('section.ap-capability'), 'Repeated generic benefits panel should be removed'
assert len(s.select('#engineering-proof .ap-proof-results > div'))==3
proof=s.select_one('#engineering-proof')
assert proof and 'separate industrial warehouse scene' in proof.get_text(' ',strip=True)
for text in ('7.1','0.03 mm','29','9','not full autonomy','not publicly distributed'):
 assert text.lower() in proof.get_text(' ',strip=True).lower(),('Missing caveat',text)
assert proof.select_one('a[href="/multiverse-ai-website/assets/3d/agent-made/warehouse-engineering-checkpoint.json"]')
assert len(s.select('#visual-proof img'))==3
assert len(s.select('#motion-proof video'))==2
assert len(s.select('#catalog .pf-card'))==3
assert s.select_one('link[href="/multiverse-ai-website/assets/3d-agent-production.css"]')
assert s.select_one('meta[property="og:image"]')['content']=='https://hanspeterradtke.github.io/multiverse-ai-website/assets/3d/agent-made/warehouse-exterior.webp'
assert 'Actual Blender Cycles render' in s.select_one('meta[property="og:image:alt"]')['content']
assert 'The renders are real. The checks are recorded.' in s.select_one('#visual-proof h2').get_text(' ',strip=True)
print('PASS: exactly one truthful 3D case; source-linked values; caveats; original renders, motion and buyer listings intact')
