#!/usr/bin/env python3
"""Check buyer relevance, offer boundaries, form handling and email privacy."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse
R=Path(__file__).resolve().parents[1]

business=BeautifulSoup((R/'opportunities/index.html').read_text(),'html.parser')
contact=BeautifulSoup((R/'contact/index.html').read_text(),'html.parser')

assert business.select_one('main h1') is not None
s=business.select_one('main').get_text(' ',strip=True)
for phrase in ('AI model', 'manual steps', 'technology', 'MIT', 'exclusive', 'success', 'scope'):
 assert phrase.lower() in s.lower(),('Missing opportunity explanation',phrase)
assert len(business.select('#situations article'))==3
assert business.select_one('a[href="/multiverse-ai-website/contact/"]')
assert business.select_one('a[href="https://github.com/HansPeterRadtke/all2text"]')
assert 'customer testimonial' not in s.lower()
assert 'guaranteed performance' in s.lower(), 'Must explicitly disclaim performance guarantees'

form=contact.select_one('main form#inquiry-form')
assert form is not None
required=[x.get('name') for x in form.select('[required]')]
assert required==['name','email','problem'],required
optional=[x.get('name') for x in form.select('input[name],textarea[name]') if x.get('name') not in required]
assert optional==['company','systems'],optional
assert not form.select('input[name="budget"],input[name="timeline"],input[name="impact"],input[name="consent"]')
assert form.select_one('textarea[name="problem"]')['maxlength']=='2100'
assert contact.select_one('a[href^="mailto:multiverse3dhpr@gmail.com"]')
assert 'own email app' in form.get_text(' ',strip=True)
assert 'does not collect or send' in form.get_text(' ',strip=True)
assert 'passwords' in form.get_text(' ',strip=True)
assert not form.select('[action], [method]')
assert not contact.select('script[src^="https://"]')
js=(R/'assets/site.js').read_text()
for fragment in ("new FormData(form)","'name'","'email'","'problem'","'systems'",'encodeURIComponent','mailto:multiverse3dhpr@gmail.com','window.location.href = uri'):
 assert fragment in js,('broken email draft',fragment)
assert "get('budget'" not in js and "get('timeline'" not in js and "get('impact'" not in js
assert 'fetch(' not in js and 'XMLHttpRequest' not in js and 'localStorage' not in js

for file in (R/'opportunities/index.html',R/'contact/index.html'):
 soup=BeautifulSoup(file.read_text(),'html.parser')
 assert soup.select_one('head link[href="/multiverse-ai-website/assets/commercial-path.css"]')
 assert len(soup.select('main h1'))==1
 print('QUALIFIED_PATH',file.relative_to(R),'main title:',soup.select_one('main h1').get_text(' ',strip=True))
print('PASS: buyer scenarios and rights; minimal form; transparent local mailto; no server collection')
