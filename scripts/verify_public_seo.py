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
copy=swaag.select_one('main').get_text(' ',strip=True)
for term in ('MIT', 'not a ready-made digital employee','No measured time savings','no published GitHub release','not a claim of uniqueness'):
 assert term.lower() in copy.lower(),('SWAAG landing missing boundary',term)
assert not swaag.find('meta',attrs={'property':'og:image'}),'Do not attach Wix product screenshots to SWAAG metadata'
print('PASS: all',len(pages),'public pages are indexed with consistent metadata, no fake SWAAG screenshots or missing boundaries')
