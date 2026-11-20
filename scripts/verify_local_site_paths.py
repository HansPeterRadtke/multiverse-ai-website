#!/usr/bin/env python3
"""Check public GitHub Pages internal assets, page navigation and fragments."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
PFX='/multiverse-ai-website/'
pages=sorted(p for p in R.rglob('index.html') if not any(part.startswith('.') for part in p.relative_to(R).parts))
failures=[];references=0
for page in pages:
 soup=BeautifulSoup(page.read_text(),'html.parser')
 for el in soup.select('[href],[src]'):
  for key in ('href','src'):
   val=el.get(key)
   if not val:continue
   parsed=urlsplit(val)
   if parsed.scheme or parsed.netloc or val.startswith('//'):continue
   if key=='href' and val in ('#',''):continue
   if parsed.path=='':target=page
   else:
    if parsed.path.startswith(PFX):target=R/parsed.path[len(PFX):]
    elif parsed.path.startswith('/'):
     failures.append((str(page.relative_to(R)),key,val,'unhandled absolute internal path'))
     continue
    else:target=page.parent/parsed.path
    target=Path(unquote(str(target)))
    if val.endswith('/') or parsed.path.endswith('/') or target.is_dir():target=target/'index.html'
   if target.exists():
    if target.suffix.lower() in ('.html',) and parsed.fragment:
     other=BeautifulSoup(target.read_text(),'html.parser')
     if other.find(id=unquote(parsed.fragment)) is None:
      failures.append((str(page.relative_to(R)),key,val,'missing fragment'))
    elif not parsed.path and parsed.fragment and soup.find(id=unquote(parsed.fragment)) is None:
     failures.append((str(page.relative_to(R)),key,val,'missing fragment'))
   else:failures.append((str(page.relative_to(R)),key,val,'missing file'))
   references+=1
print('CHECKED',len(pages),'pages and',references,'relative internal asset/link references')
if failures:
 for f in failures[:60]:print('FAIL',*f)
 raise SystemExit(1)
print('PASS: internal GitHub Pages links, media and anchor paths resolve to actual files')
