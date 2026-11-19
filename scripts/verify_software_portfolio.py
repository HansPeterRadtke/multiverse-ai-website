#!/usr/bin/env python3
"""Validate every public portfolio item and the source-code navigation."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json
R=Path(__file__).resolve().parents[1]
source=json.loads((R/'production/public-software-portfolio.json').read_text())
projects=source['projects']
assert len(projects)>=8 and len(set(x['id'] for x in projects))==len(projects)
assert source['github_profile']=='https://github.com/HansPeterRadtke'
assert {x['id'] for x in projects}.issuperset({'swaag','all2text','voicebutton','keyboard','unity','typewriter'})
assert next(x for x in projects if x['id']=='keyboard')['source_url'] is None, 'Keyboard module is not in public Android Github checkout'
for project in projects:
 assert all(project.get(x) for x in ('title','category','status','purpose','workflow','benefit','limits')),project['id']
 if project['source_url']:
  parsed=urlparse(project['source_url'])
  assert parsed.scheme=='https' and parsed.hostname in ('github.com','www.youtube.com'),project['id']
  assert project['source_label'],project['id']
 else:
  assert not project['source_label'],project['id']
for name,expected in [('index.html',0),('technology/index.html',len(projects)),('projects/index.html',len(projects))]:
 soup=BeautifulSoup((R/name).read_text(),'html.parser')
 nodes=soup.select('.mv-project-card')
 assert len(nodes)==expected,(name,len(nodes),expected)
 for node in nodes:
  key=node['id'].removeprefix('project-')
  data=next((x for x in projects if x['id']==key),None)
  assert data is not None,(name,key)
  assert data['title'] in node.get_text(' ',strip=True),(name,key)
  assert 'Why it matters' in node.get_text(' ',strip=True),(name,key)
  if data['source_url']:
   assert node.select_one(f'a[href="{data["source_url"]}"]'),(name,key,'missing source link')
   assert node.select_one('.mv-source-link')['target']=='_blank', (name,key,'external opens new tab')
  else:
   assert not node.select_one('.mv-source-link'),(name,key,'invented public source')
 if name=='index.html':
  hero=soup.select_one('.sw-home-examples')
  assert hero.select_one('.mv-hero-swaag-link[href="#swaag"]')
  spotlight=soup.select_one('section#swaag')
  assert spotlight is not None
  copy=spotlight.get_text(' ',strip=True)
  for fragment in ('WHEN WOULD YOU NEED IT','WHAT SWAAG PROVIDES','What could this help you build?','developers','local-first'):
   assert fragment.lower() in copy.lower(),fragment
  assert spotlight.select_one('a[href="https://github.com/HansPeterRadtke/swaag"]')
  assert soup.select_one('.mv-source-proof'), 'Credibility proof should be compact, not a 9-card catalog'
 if name=='technology/index.html':
  assert soup.select_one('section#swaag.mv-swaag-compact')
 assert soup.select_one('a[href="https://github.com/HansPeterRadtke"]'),name
 assert soup.select_one('link[href="/multiverse-ai-website/assets/software-portfolio.css"]'),name
 print('VALID',name,expected,'real project descriptions')

for path in sorted(R.rglob('index.html')):
 soup=BeautifulSoup(path.read_text(),'html.parser')
 for selector in ('.desktop-nav','.mobile-nav'):
  nav=soup.select_one(selector)
  assert nav is not None,path
  links=nav.select('a')
  assert any(x.get('href')=='https://github.com/HansPeterRadtke' and x.get('target')=='_blank' for x in links),(path,selector)
  assert len(links)==6,(path,selector,len(links))
 footer=soup.select_one('.footer-grid .footer-links')
 assert footer and footer.select_one('a[href="https://github.com/HansPeterRadtke"]'),path
print('PASS: GitHub linked on every page; projects have sourced benefits and explicit release status')
