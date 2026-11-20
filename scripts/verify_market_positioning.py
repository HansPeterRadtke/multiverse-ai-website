#!/usr/bin/env python3
"""Guard comparison-to-real-baseline, CapOv public proof, and prototype limits."""
from pathlib import Path
from bs4 import BeautifulSoup
import json
R=Path(__file__).resolve().parents[1]
read=lambda n:BeautifulSoup((R/n).read_text(),'html.parser')
home=read('index.html');swaag=read('swaag/index.html');kmd=read('kmd/index.html')
assert 'off-the-shelf tools' in home.select_one('h1').get_text(' ',strip=True).lower()
assert 'not basic AI tool use' in home.select_one('.sw-lead').get_text(' ',strip=True)
assert home.select_one('#swaag') and home.select_one('#software-proof') and home.select_one('#research-proof')
assert 'Codex' in home.select_one('#research-proof').get_text(' ',strip=True)
assert 'intended benefit' in home.select_one('#research-proof').get_text(' ',strip=True).lower()
assert 'not a production-ready search service' in home.select_one('#research-proof').get_text(' ',strip=True).lower()
assert len(home.select('#capov'))==1
cap=home.select_one('#capov')
for phrase in ('Captain Obvious','pip install capov','v0.1.6','review','PyPI'):
 assert phrase.lower() in cap.get_text(' ',strip=True).lower(),phrase
for url in ('https://pypi.org/project/capov/','https://github.com/HansPeterRadtke/capov','https://docs.astral.sh/ruff/linter/'):
 assert len(cap.select(f'a[href="{url}"]'))==1
assert 'without asking an AI agent' in cap.get_text(' ',strip=True)
assert 'Review edits before use' in cap.get_text(' ',strip=True)

assert len(swaag.select('#baseline'))==1
swaag_text=swaag.select_one('#baseline').get_text(' ',strip=True)
for x in ('Codex','Claude Code','mature coding agent','tool use and subagents are not unique','your own clients','model services','not a drop-in guarantee'):
 assert x.lower() in swaag_text.lower(),x
assert swaag.select_one('#features') and swaag.select_one('#evaluation')
assert 'not proven performance advantages' in swaag.select_one('.sa-lead').get_text(' ',strip=True)
assert len(kmd.select('#kmd-baseline'))==1
kt=kmd.select_one('#kmd-baseline').get_text(' ',strip=True)
for x in ('Codex','Claude Code','who said what','merely reported','when it was true','not positioned as a better general chatbot','no demonstrated advantage'):
 assert x.lower() in kt.lower(),x
assert 'Experimental research' in kmd.select_one('.kmd-purpose-hero').get_text(' ',strip=True)
assert kmd.select_one('#how-to-use') and kmd.select_one('#kmd-watch')
assert kmd.select_one('.kmd-hero-flow-illustration')
assert 'public API returns plain text' in kmd.get_text(' ',strip=True)
projects=json.loads((R/'production/public-software-portfolio.json').read_text())['projects']
capproj=next(x for x in projects if x['id']=='capov')
assert capproj['source_url']=='https://github.com/HansPeterRadtke/capov'
assert 'PyPI' in capproj['status']
assert 'not a replacement' in capproj['limits']
assert 'not fully green' in capproj['limits']
assert (R/'assets/market-differentiation.css').is_file()
for name in ('index.html','swaag/index.html','kmd/index.html'):
 assert read(name).select_one('head link[href="/multiverse-ai-website/assets/market-differentiation.css"]'),name
print('PASS: real competitor baseline; KMD context boundaries; CapOv authentic PyPI utility; no invented superiority/adoption')
