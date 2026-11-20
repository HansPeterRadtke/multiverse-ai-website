#!/usr/bin/env python3
"""Homepage first-screen proof: truthful, clickable, accessible source-backed media."""
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image
R=Path(__file__).resolve().parents[1]
s=BeautifulSoup((R/'index.html').read_text(),'html.parser')
hero=s.select_one('#top');assert hero
previews=hero.select_one('.hp-proof-previews');assert previews
assert len(previews.select(':scope > a'))==4
assert [x.get('class')[0] for x in previews.select(':scope > a')]==[
 'mv-hero-swaag-link','sw-home-example','sw-home-example','hp-proof-wix']
assert previews.select_one('.hp-proof-manager[href="#swaag"]')
assert len(previews.select('.hp-proof-card'))==2
for card,href,expected_image in [
 ('hp-proof-kmd','/multiverse-ai-website/kmd/','/multiverse-ai-website/assets/kmd/kmd-evidence-walkthrough-poster.webp'),
 ('hp-proof-3d','/multiverse-ai-website/3d/','/multiverse-ai-website/assets/3d/agent-made/warehouse-exterior.webp')]:
 item=previews.select_one('.'+card); assert item is not None
 assert item.get('href')==href
 img=item.select_one('img');assert img and img.get('src')==expected_image
 assert img.get('alt') and len(img['alt'])>20
 assert img.get('width') and img.get('height')
 path=R/expected_image.removeprefix('/multiverse-ai-website/')
 with Image.open(path) as im:
  assert im.width==int(img['width']) and im.height==int(img['height']),(path,im.size)
 assert not item.select('[aria-hidden="true"]:not(:has(> *))') or all(x.get_text(' ',strip=True) in ('↗','') for x in item.select('[aria-hidden="true"]'))
 assert len(item.select('strong'))==1
 assert item.select_one('small')
assert 'RESEARCH PROTOTYPE' in previews.select_one('.hp-proof-kmd').get_text(' ',strip=True)
assert 'experimental' in previews.select_one('.hp-proof-kmd').get_text(' ',strip=True).lower()
assert 'Genuine Blender' in previews.select_one('.hp-proof-3d img')['alt']
assert 'Realism is still improving' in previews.select_one('.hp-proof-3d').get_text(' ',strip=True)
assert previews.select_one('.hp-proof-wix[href="#software-proof"]')
assert not previews.select_one('.sw-home-3d-link'), 'No outdated link presenting AI production as merely a catalog'
assert len(previews.select('.sw-home-example-image'))==2
assert 'a separate catalog of animated industrial 3D models' not in hero.get_text(' ',strip=True)
assert s.select_one('#swaag') and s.select_one('#research-proof') and s.select_one('#industrial-assets') and s.select_one('#software-proof')
assert s.select_one('#software-proof video'), 'Published Wix demo must remain'
assert s.select_one('head link[href="/multiverse-ai-website/assets/home-proof-first.css"]')
for file in sorted(R.rglob('index.html')):
 page=BeautifulSoup(file.read_text(),'html.parser')
 for selector in ('header nav.desktop-nav','header nav.mobile-nav'):
  nav=page.select_one(selector)
  assert nav,(file,selector)
  link=nav.select('a')[1]
  assert link.get_text(' ',strip=True)=='AI 3D Production',(file,selector)
  assert link.get('href')=='/multiverse-ai-website/3d/'
 assert 'AI 3D Production' in page.select_one('.footer-links').get_text(' ',strip=True)
print('PASS: two genuine preview images, plain benefit copy, scoped prototypes, 3D top-level identity and published Wix demo')
