#!/usr/bin/env python3
"""Keep every published page discoverable with a correct sitemap/canonical URL.

Original content and declared descriptions remain authoritative. This script only
synchronizes URL metadata, open graph summaries and the sitemap from actual pages.
No analytics, tracking or fabricated product reviews are added.
"""
from pathlib import Path
from urllib.parse import quote
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET

R=Path(__file__).resolve().parents[1]
ORIGIN='https://hanspeterradtke.github.io/multiverse-ai-website/'


def canonical(page):
    rel=page.relative_to(R)
    if rel == Path('index.html'):return ORIGIN
    assert rel.name=='index.html',page
    return ORIGIN+'/'.join(quote(x) for x in rel.parts[:-1])+'/'


def meta(s, name, value, attr='name'):
    entries=s.find_all('meta',attrs={attr:name})
    if entries:
        tag=entries[0]
        for extra in entries[1:]:extra.decompose()
    else:
        tag=s.new_tag('meta');tag[attr]=name;s.head.append(tag)
    tag['content']=value


def link(s, rel, href):
    matches=[a for a in s.head.find_all('link') if rel in (a.get('rel') or [])]
    if matches:
        a=matches[0]
        for x in matches[1:]:x.decompose()
    else:
        a=s.new_tag('link');a['rel']=[rel];s.head.append(a)
    a['href']=href


pages=sorted(p for p in R.rglob('index.html') if not any(part.startswith('.') for part in p.relative_to(R).parts))
assert len(pages)>=10,('unexpected site page count',len(pages))
urls=[]
for p in pages:
    s=BeautifulSoup(p.read_text(),'html.parser')
    assert s.head and s.title, p
    title=s.title.get_text(' ',strip=True)
    assert title and 'Multiverse' in title,p
    desc=s.find('meta',attrs={'name':'description'})
    assert desc and len(desc.get('content',''))>40,p
    descstr=desc['content'].strip()
    assert 40<=len(descstr)<=280,(p,'description too long or missing',len(descstr))
    url=canonical(p)
    link(s,'canonical',url)
    meta(s,'og:title',title,'property')
    meta(s,'og:description',descstr,'property')
    meta(s,'og:url',url,'property')
    meta(s,'og:type','website','property')
    meta(s,'twitter:card','summary_large_image')
    meta(s,'twitter:title',title)
    meta(s,'twitter:description',descstr)
    # Brand art is not a simulated agent screenshot. Preserve the real 3D render.
    if p==R/'3d/index.html':
        image='assets/3d/agent-made/warehouse-exterior.webp'
        alt='Actual Blender Cycles render of a modeled three-bay industrial warehouse'
    else:
        image='assets/brand/multiverse-social-preview.png'
        alt='Multiverse brand artwork: independent software and AI systems'
    assert (R/image).is_file(),('Missing social image',image)
    meta(s,'og:image',ORIGIN+image,'property')
    meta(s,'og:image:alt',alt,'property')
    meta(s,'twitter:image',ORIGIN+image)
    p.write_text(str(s).rstrip()+'\n')
    urls.append(url)

# Sitemap covers every real URL, including the dedicated SWAAG, 3D,
# KnowMoreDiRT and previously omitted project/evidence pages.
ET.register_namespace('','http://www.sitemaps.org/schemas/sitemap/0.9')
ns='http://www.sitemaps.org/schemas/sitemap/0.9'
root=ET.Element('{'+ns+'}urlset')
for addr in sorted(urls):
    node=ET.SubElement(root,'{'+ns+'}url')
    ET.SubElement(node,'{'+ns+'}loc').text=addr
ET.ElementTree(root).write(R/'sitemap.xml',encoding='utf-8',xml_declaration=True)
(R/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+ORIGIN+'sitemap.xml\n')
print('SEO UPDATED',len(pages),'pages / canonical URLs / OG / sitemap; no new data collection')
for addr in urls:print(' ',addr)
