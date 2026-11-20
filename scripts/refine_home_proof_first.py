#!/usr/bin/env python3
"""Make the first screen show SWAAG, authentic KMD proof and AI-made 3D.

The full published Wix demo remains in its existing homepage section. These
previews are source-backed and do not invent agent screenshots or benchmark wins.
This final pass runs after all page and 3D generators, before common nav/SEO.
"""
from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
page=R/'index.html'
s=BeautifulSoup(page.read_text(),'html.parser')
old=s.select_one('section#top .sw-home-examples');assert old
manager=old.select_one('a.mv-hero-swaag-link');assert manager
assert manager.get('href')=='#swaag'
manager.extract()
content='''<div class="sw-home-examples hp-proof-previews" aria-label="Explore the two flagship AI systems and a real AI-directed Blender production result">
  <a class="sw-home-example sw-home-example-ai hp-proof-card hp-proof-kmd" href="/multiverse-ai-website/kmd/">
    <img class="sw-home-example-image sw-research-visual" width="1280" height="800" loading="eager" decoding="async" src="/multiverse-ai-website/assets/kmd/kmd-evidence-walkthrough-poster.webp" alt="Actual limited KnowMoreDiRT source-evidence research walkthrough"/>
    <span class="sw-proof-status">KMD · RESEARCH PROTOTYPE</span>
    <strong>KnowMoreDiRT — understand messy files</strong>
    <span>Semantic search finds relevant evidence. DRT reasoning aims to keep track of who, when and context; still experimental.</span>
    <small>Explore KMD research <span aria-hidden="true">↗</span></small>
  </a>
  <a class="sw-home-example hp-proof-card hp-proof-3d" href="/multiverse-ai-website/3d/">
    <img class="sw-home-example-image" width="1600" height="900" loading="eager" decoding="async" src="/multiverse-ai-website/assets/3d/agent-made/warehouse-exterior.webp" alt="Genuine Blender Cycles render of a modeled three-bay industrial warehouse, produced through AI-directed Blender and Python workflows"/>
    <span class="sw-proof-status">AI 3D PRODUCTION · REAL BLENDER RENDER</span>
    <strong>AI agents build real 3D scenes</strong>
    <span>My agents operate Blender and Python to build, animate and check editable industrial models. Realism is still improving.</span>
    <small>See the production workflow <span aria-hidden="true">↗</span></small>
  </a>
  <a class="hp-proof-wix" href="#software-proof">Also published: Late Order Monitor for Wix Stores <span aria-hidden="true">↗</span></a>
</div>'''
replacement=BeautifulSoup(content,'html.parser').find('div')
manager['class']=list(dict.fromkeys((manager.get('class') or [])+['hp-proof-manager']))
replacement.insert(0,manager)
old.replace_with(replacement)
link='/multiverse-ai-website/assets/home-proof-first.css'
if not s.select_one(f'head link[href="{link}"]'):
 s.head.append(s.new_tag('link',href=link,rel='stylesheet'))
page.write_text(str(s).rstrip()+'\n')
print('HOME: SWAAG manager + actual KMD proof + authentic AI 3D render; Wix remains in dedicated published-app section')
