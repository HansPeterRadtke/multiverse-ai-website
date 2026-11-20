#!/usr/bin/env python3
"""Regression checks: top-level navigation never points deep into page content."""
from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
expected=['Software & AI','AI 3D Production','Business','About','Contact','GitHub ↗']
for file in sorted(R.rglob('index.html')):
 if '.git' in file.parts:continue
 page=BeautifulSoup(file.read_text(),'html.parser')
 for selector in ('header nav.desktop-nav','header nav.mobile-nav'):
  nav=page.select_one(selector)
  assert nav is not None,(file,selector)
  anchors=nav.select('a')
  assert [a.get_text(' ',strip=True) for a in anchors]==expected,(file,selector)
  for a in anchors:
   assert not a['href'].split('/')[-1].startswith('#'),(file,selector,a['href'])
   assert '#' not in a['href'],(file,'top menu item must open a page',a['href'])
  assert anchors[1]['href']=='/multiverse-ai-website/3d/',(file,anchors[1]['href'])
  assert anchors[-1]['href']=='https://github.com/HansPeterRadtke' and anchors[-1]['target']=='_blank'
  assert anchors[-1].get('rel') == ['noopener','noreferrer']
new=BeautifulSoup((R/'3d/index.html').read_text(),'html.parser')
assert 'AI-directed Blender workflows' in new.select_one('main h1').get_text(' ',strip=True)
assert len(new.select('main .pf-card'))>=3
assert new.select_one('nav.desktop-nav a.active').get_text(' ',strip=True)=='AI 3D Production'
assert len(new.select('main .pf-card a[href$=".mp4"]'))>=3
assert new.select_one('link[href="/multiverse-ai-website/assets/3d-navigation.css"]')
old=BeautifulSoup((R/'projects/index.html').read_text(),'html.parser')
assert old.select_one('#industrial-catalog') is not None, 'Preserve old links to product catalog'
assert (R/'assets/3d-navigation.css').is_file()
print('PASS: all top-level menus open dedicated pages; 3D starts at top; existing catalog remains linked')
