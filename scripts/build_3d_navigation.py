#!/usr/bin/env python3
"""Give 3D models a real top-level page instead of an anchor deep in Projects.

Existing /projects/#industrial-catalog links remain valid as historic links,
while main navigation always enters /3d/ at the page top.
"""
from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[1]
base='/multiverse-ai-website/'
projects=BeautifulSoup((root/'projects/index.html').read_text(),'html.parser')
section=projects.select_one('#industrial-catalog')
assert section is not None
# The cards and marketplace claims come unchanged from the existing verified catalog.
section.extract()
section['class']=['pf-section','container','pf-3d-products']
heading=section.select_one('.pf-section-top')
assert heading
heading.select_one('.pf-eyebrow').string='3D PRODUCTS / AVAILABLE MARKETPLACE LISTINGS'
heading.select_one('h2').string='Explore the industrial models.'
heading.select('p')[-1].string='These are downloadable 3D models, not physical machinery. Watch the animations, then check the product listing for included files and formats.'

page=BeautifulSoup((root/'projects/index.html').read_text(),'html.parser')
main=page.select_one('main#main')
assert main is not None
main.clear()
main['class']=['pf-3d-index']
hero=BeautifulSoup('''<section class="pf-hero container pf-3d-hero" id="top"><p class="pf-eyebrow">MULTIVERSE / A SEPARATE DIGITAL PRODUCT LINE</p><h1>Industrial 3D models<br><em>and animations.</em></h1><p class="pf-lead">Downloadable industrial models for visualization, animation and digital environments. This collection is separate from Multiverse software and AI research.</p><a class="pf-action pf-action-main" href="#catalog">Explore 3D products</a></section>''','html.parser').find('section')
main.append(hero)
section['id']='catalog'
main.append(section)
last=BeautifulSoup('''<section class="container pf-3d-end"><div><h2>Looking for software instead?</h2><p>Multiverse also develops business software and researches AI systems. Those are independent projects, not part of the 3D product catalog.</p></div><a class="pf-action pf-action-quiet" href="/multiverse-ai-website/technology/">Explore Software &amp; AI</a></section>''','html.parser').find('section')
main.append(last)
page.title.string='Industrial 3D Models & Animations | Multiverse'
meta=page.find('meta',attrs={'name':'description'})
if meta:meta['content']='Browse Multiverse industrial 3D assets and original animated product demonstrations, including forklifts, warehouse racking and loading-dock equipment.'
for tag in page.find_all('meta',attrs={'property':'og:title'}):tag['content']='Industrial 3D Models & Animations | Multiverse'
for tag in page.find_all('meta',attrs={'property':'og:description'}):tag['content']='Downloadable industrial 3D models and animations from Multiverse, with authentic product previews and marketplace listings.'
style=page.new_tag('link',href=base+'assets/3d-navigation.css',rel='stylesheet')
page.head.append(style)
(root/'3d').mkdir(exist_ok=True)
(root/'3d/index.html').write_text(str(page).rstrip()+'\n')

# Update top-level site navigation, including nested KMD research pages.
nav=(root/'scripts/align_software_navigation.py')
src=nav.read_text()
assert "base+'projects/#industrial-catalog'" in src or "base+'3d/'" in src
src=src.replace("base+'projects/#industrial-catalog'","base+'3d/'")
src=src.replace("rel=='projects/index.html'", "rel in ('3d/index.html','projects/index.html')")
src=src.replace("'projects/index.html','kmd/index.html'", "'projects/index.html','3d/index.html','kmd/index.html'")
nav.write_text(src)

# Contextual product links follow the new top-level destination; historical
# explicit catalog references and old URLs remain untouched elsewhere.
for path in (root/'index.html',root/'scripts/rebuild_software_home.py',root/'technology/index.html',root/'scripts/rebuild_software_page.py'):
 src=path.read_text()
 src=src.replace("projects/#industrial-catalog", "3d/")
 path.write_text(src)
print('WROTE /3d/; fixed site navigation source; preserved original Projects catalog')
