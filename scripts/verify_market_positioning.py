#!/usr/bin/env python3
"""Enforce project purpose from owner recordings, and truthful competitors/limits."""
from pathlib import Path
from bs4 import BeautifulSoup
import json
R=Path(__file__).resolve().parents[1]
read=lambda name:BeautifulSoup((R/name).read_text(),'html.parser')
home=read('index.html');swaag=read('swaag/index.html');kmd=read('kmd/index.html');tech=read('technology/index.html')

assert 'AI workers you can manage. Knowledge you can trust.' in home.select_one('h1').get_text(' ',strip=True)
assert 'background AI workers' in home.select_one('.sw-lead').get_text(' ',strip=True)
assert 'chaotic document collections' in home.select_one('.sw-lead').get_text(' ',strip=True)
assert len(home.select('.sw-home-example-image'))==2
assert home.select_one('.mv-hero-swaag-link') and home.select_one('.sw-home-example-ai')
assert home.select_one('.sw-home-examples').select_one('.sw-home-example-ai') is not None
hero=swaag.select_one('section.sa-hero')
assert 'Workers that keep moving.' in hero.select_one('h1').get_text(' ',strip=True)
assert 'background agents' in hero.get_text(' ',strip=True)
assert 'disabled by default' in hero.get_text(' ',strip=True)
assert 'team leader' in home.select_one('#swaag').get_text(' ',strip=True).lower()
for term in ('worker','orchestrator','progress','history','questions','continuation','autonomous'):
 assert term.lower() in (home.select_one('#swaag').get_text(' ',strip=True)+' '+swaag.select_one('main').get_text(' ',strip=True)).lower(),term
assert 'automatic background dispatch is disabled by default' in home.select_one('#swaag').get_text(' ',strip=True)
assert len(swaag.select('.sa-need-grid article'))==3
assert len(swaag.select('.sa-cap-grid > div'))==4
assert len(swaag.select('#evaluation .sa-evaluation-grid article'))==4
comparison=swaag.select_one('#baseline');assert comparison
for term in ('Codex','Claude Code','Dots','background','own','architectural distinction','explicit enablement'):
 assert term.lower() in comparison.get_text(' ',strip=True).lower(),('swaag comparison',term)
for u in ('https://learn.chatgpt.com/docs/agent-configuration/subagents','https://claude.com/resources/articles/subagents-in-claude-code','https://learn.chatgpt.com/docs/dots'):
 assert comparison.select_one(f'a[href="{u}"]'),u

assert 'Find meaning in the chaos of your files.' in kmd.select_one('main h1').get_text(' ',strip=True)
main=kmd.select_one('main').get_text(' ',strip=True)
for term in ('Discourse Representation Theory','semantic','folder','referents','time','schema','source','research','experimental'):
 assert term.lower() in main.lower(),('KMD purpose',term)
assert len(kmd.select('#how-to-use .kmd-use-flow > div'))==3
assert len(kmd.select('#user-benefits .kmd-benefit-cards article'))==3
assert len(kmd.select('#kmd-baseline'))==1
for term in ('Codex','Claude Code','GraphRAG','semantic','scientific','not a measured superiority'):
 assert term.lower() in kmd.select_one('#kmd-baseline').get_text(' ',strip=True).lower(),('KMD competitors',term)
assert kmd.select_one('#kmd-watch video')
assert 'plain answer string' in main
assert 'Research prototype' in kmd.select_one('.kmd-purpose-hero').get_text(' ',strip=True)

assert 'SWAAG' in tech.select_one('#swaag').get_text(' ',strip=True)
cap=home.select_one('#capov');assert cap
for phrase in ('Captain Obvious','pip install capov','v0.1.6','PyPI','Ruff','Review'):
 assert phrase.lower() in cap.get_text(' ',strip=True).lower(),phrase
for u in ('https://pypi.org/project/capov/','https://github.com/HansPeterRadtke/capov','https://docs.astral.sh/ruff/linter/'):
 assert cap.select_one(f'a[href="{u}"]')
projects=json.loads((R/'production/public-software-portfolio.json').read_text())['projects']
capproj=next(x for x in projects if x['id']=='capov')
assert 'not fully green' in capproj['limits']
assert capproj['source_url']=='https://github.com/HansPeterRadtke/capov'
for name in ('index.html','swaag/index.html','kmd/index.html'):
 assert read(name).select_one('link[href="/multiverse-ai-website/assets/market-differentiation.css"]'),name
print("PASS: SWAAG worker-management and KMD DRT purpose; current alternatives; research limits; CapOv")
