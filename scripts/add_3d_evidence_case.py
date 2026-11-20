#!/usr/bin/env python3
"""Show real recorded Blender engineering QA, without publishing private scenes.

Runs after the 3D catalog+production builder. Reads only a source-verified,
sanitized evidence summary bundled with the static site. Does not trigger Blender,
model inference, network requests, or third-party publication.
"""
from pathlib import Path
from bs4 import BeautifulSoup
import json

ROOT=Path(__file__).resolve().parents[1]
checkpoint=ROOT/'assets/3d/agent-made/warehouse-engineering-checkpoint.json'
data=json.loads(checkpoint.read_text())
metrics=data['results']
assert metrics['forklift_wheel_ground_gap_mm_before_approx']==7.1
assert metrics['forklift_wheel_ground_gap_mm_after_at_most']==0.03
assert metrics['fixed_seed_native_cycles_stills_examined']==29
assert metrics['sampled_rays_through_open_loading_bay']==9

page=ROOT/'3d/index.html'
s=BeautifulSoup(page.read_text(),'html.parser')
for old in s.select('section.ap-proof-case'):
    old.decompose()
# The original longer benefits panel restated the same feature claims. Replace
# it with one narrow, checkable case rather than increase page complexity.
for old in s.select('section.ap-capability'):
    old.decompose()
target=s.select_one('section#visual-proof')
assert target is not None
heading=target.select_one('h2')
assert heading is not None
heading.clear()
heading.append(BeautifulSoup('The renders are real. <em>The checks are recorded.</em>', 'html.parser'))
intro=target.select_one('.ap-intro')
assert intro is not None
intro.string='Actual Blender scene renders, not generated stock imagery. The engineering record below belongs to a separate development revision; the rendered gallery and tested scene have distinct quality-review status.'
html='''<section class="ap-proof-case" id="engineering-proof"><div class="container ap-proof-inner">
  <div class="ap-proof-description"><p class="ap-kicker">ONE RECORDED DEVELOPMENT CHECKPOINT</p>
    <h2>Software found the problem. <em>Another check confirmed the fix.</em></h2>
    <p>During work on a separate industrial warehouse scene, Blender/Python geometry checks exposed a forklift hovering above the modeled floor. The scripted correction reduced the gap, and a fresh Blender process verified the saved scene. The same study checked changes across native Cycles renders and a modeled loading-dock opening.</p>
    <a class="ap-proof-record" href="/multiverse-ai-website/assets/3d/agent-made/warehouse-engineering-checkpoint.json">Inspect the recorded checks <span aria-hidden="true">↗</span></a>
  </div>
  <div class="ap-proof-results" aria-label="Measured geometry and render checks">
    <div><strong>7.1 <span>→</span> 0.03 mm</strong><p>Approximate wheel-to-floor gap before and after the Blender geometry correction</p></div>
    <div><strong>29</strong><p>Native Cycles stills examined across the development study</p></div>
    <div><strong>9</strong><p>Sampled rays confirming clear passage through the modeled dock opening</p></div>
  </div>
  <p class="ap-proof-limits">The measurements describe specific private development scenes, not the gallery render pictured above. They demonstrate bounded engineering checks—not full autonomy, photographic-quality acceptance, or physical machinery safety. The original source scenes are not publicly distributed here.</p>
</div></section>'''
block=BeautifulSoup(html,'html.parser').find('section')
target.insert_after(block)
page.write_text(str(s).rstrip()+'\n')
print('ADDED ONE SOURCE-CHECKED 3D QA CASE, WITHOUT PRIVATE SCENE IMAGES')
