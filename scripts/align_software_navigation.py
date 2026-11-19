#!/usr/bin/env python3
"""One navigation vocabulary across all public pages; business software is primary."""
from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
base='/multiverse-ai-website/'
items=[('Software & AI',base+'technology/','software'),('3D models',base+'projects/#industrial-catalog','assets'),('Business',base+'opportunities/','business'),('About',base+'about/','about'),('Contact',base+'contact/','contact')]
for p in sorted(R.rglob('index.html')):
 s=BeautifulSoup(p.read_text(),'html.parser')
 rel=str(p.relative_to(R))
 active='software' if rel in ('technology/index.html','kmd/index.html','kmd/evidence/index.html') else ('assets' if rel=='projects/index.html' else ('business' if rel=='opportunities/index.html' else ('about' if rel=='about/index.html' else ('contact' if rel=='contact/index.html' else ''))))
 header=s.select_one('header.site-header')
 if header:
  for selector in ('.desktop-nav','.mobile-nav'):
   nav=header.select_one(selector)
   if nav:
    nav.clear()
    for label,href,typ in items:
     a=s.new_tag('a',href=href);a['class']=['nav-link']+(['active'] if active==typ else []);a.string=label;nav.append(a)
  cta=header.select_one('a.header-cta')
  if cta and rel in ('index.html','technology/index.html','projects/index.html','kmd/index.html','kmd/evidence/index.html'):
   cta.clear();cta.string='See software example';cta['href']=base+'#software-proof'
  elif cta:
   cta.clear();cta.string='Discuss a software problem';cta['href']=base+'contact/'
  if rel=='index.html' and cta:
   cta.string='Watch the software'
 footer=s.select_one('.footer-grid .footer-links')
 if footer:
  footer.clear()
  for label,href,_ in items:
   a=s.new_tag('a',href=href);a.string=label;footer.append(a)
  a=s.new_tag('a',href=base+'projects/');a.string='All projects';footer.append(a)
 p.write_text(str(s)+'\n')
 print('NAV',rel,active)
