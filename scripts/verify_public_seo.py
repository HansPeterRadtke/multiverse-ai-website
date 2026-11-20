#!/usr/bin/env python3
"""Check static site search metadata, canonical references and sitemap completeness."""
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup
import sys
R=Path(__file__).resolve().parents[1]
ORIGIN='https://hanspeterradtke.github.io/multiverse-ai-website/'
def canonical(page):
 rel=page.relative_to(R)
 return ORIGIN if rel==Path('index.html') else ORIGIN+'/'.join(rel.parts[:-1])+'/'

pages=sorted(p for p in R.rglob('index.html') if not any(part.startswith('.') for part in p.relative_to(R).parts))
expected={canonical(p) for p in pages}
assert len(expected)==len(pages)>=12

tree=ET.parse(R/'sitemap.xml')
entries={x.text for x in tree.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
assert entries==expected,('sitemap mismatch',expected-entries,entries-expected)
assert '/multiverse-ai-website/sitemap.xml' in (R/'robots.txt').read_text()

for p in pages:
 soup=BeautifulSoup(p.read_text(),'html.parser')
 url=canonical(p)
 refs=[x for x in soup.select('head link') if 'canonical' in (x.get('rel') or [])]
 assert len(refs)==1 and refs[0].get('href')==url,(p,'canonical')
 for prop,attr,value in [('og:url','property',url),('og:title','property',soup.title.get_text(' ',strip=True)),('og:description','property',soup.select_one('meta[name=description]')['content'])]:
  nodes=soup.find_all('meta',attrs={attr:prop})
  assert len(nodes)==1 and nodes[0].get('content')==value,(p,prop)
  assert not any(x.get('content','').startswith('http:') for x in nodes),(p,'insecure link')
 for name in ('twitter:card','twitter:title','twitter:description'):
  assert len(soup.find_all('meta',attrs={'name':name}))==1,(p,name)
 for link in soup.select('a[href]'):
  if link.get('href','').startswith('https://github.com/') and link.get('target')=='_blank':
   assert set(link.get('rel') or [])=={'noopener','noreferrer'},(p,'external source link rel')
 print('SEO_OK',p.relative_to(R),url)

swaag=BeautifulSoup((R/'swaag/index.html').read_text(),'html.parser')
assert swaag.select_one('main h1')
assert 'SWAAG' in swaag.title.get_text(' ',strip=True)
assert len(swaag.select('.sa-need-grid article'))==3
assert len(swaag.select('.sa-cap-grid > div'))==4
assert len(swaag.select('.sa-faq details'))==4
assert len(swaag.select('#evaluation .sa-evaluation-grid article'))==4
assert swaag.select_one('.sa-proof-links a[href="#evaluation"]'), 'Evidence section should be reachable from source links'
source_links={
 'tests/test_history_replay.py',
 'tests/test_tools.py',
 'tests/test_storage_boundaries.py',
 'tests/test_control_authority.py',
 'tests/test_agent_workspace_recovery.py',
}
base='https://github.com/HansPeterRadtke/swaag/blob/main/'
for file in source_links:
 links=swaag.select(f'#evaluation a[href="{base+file}"]')
 assert len(links)==1,(file,len(links))
 assert links[0].get('target')=='_blank'
assert 'presence does not demonstrate that the latest suite passes' in swaag.select_one('.sa-evaluation-limit').get_text(' ',strip=True)
assert 'Python compatibility' in swaag.select_one('.sa-evaluation-limit').get_text(' ',strip=True)

copy=swaag.select_one('main').get_text(' ',strip=True)
for term in ('MIT', 'It is an evolving developer framework','No measured time savings','no published GitHub release','not a claim of uniqueness'):
 assert term.lower() in copy.lower(),('SWAAG landing missing boundary',term)
preview=swaag.find('meta',attrs={'property':'og:image'})
assert preview and preview.get('content','').endswith('/assets/brand/multiverse-social-preview.png'), 'SWAAG must show brand artwork, never an invented product screenshot'
for page in pages:
 doc=BeautifulSoup(page.read_text(),'html.parser')
 image=doc.find('meta',attrs={'property':'og:image'})
 assert image and image.get('content','').startswith(ORIGIN),(page,'missing public preview')
 assert doc.find('meta',attrs={'name':'twitter:image'}),(page,'twitter image')
 assert doc.find('meta',attrs={'name':'twitter:card'})['content']=='summary_large_image',(page,'card type')

print('PASS: all',len(pages),'public pages are indexed with consistent metadata, no fake SWAAG screenshots or missing boundaries')
