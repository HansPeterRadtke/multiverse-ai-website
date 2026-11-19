#!/usr/bin/env python3
"""Render source-backed actual projects throughout the Multiverse website.

Only public, owner-established project descriptions are shown. A public GitHub
repository is evidence of available code, NOT proof of production-readiness.
"""
from pathlib import Path
from bs4 import BeautifulSoup
from html import escape
import json

R=Path(__file__).resolve().parents[1]
data=json.loads((R/'production/public-software-portfolio.json').read_text())
items=data['projects']
root='https://github.com/HansPeterRadtke'
assert data['github_profile']==root


def e(value):return escape(str(value),quote=True)
def source_link(p):
 if p['source_url']:
  return f'<a class="mv-source-link" href="{e(p["source_url"])}" target="_blank" rel="noopener noreferrer">{e(p["source_label"])} <span aria-hidden="true">↗</span></a>'
 return '<span class="mv-source-missing">Not yet published in the public repositories</span>'

def card(p,detailed=False):
 workflow=f'<p class="mv-project-process"><b>How it works:</b> {e(p["workflow"])}</p>' if detailed else ''
 limits=f'<details class="mv-project-details"><summary>Current limitations</summary><p>{e(p["limits"])}</p></details>'
 return f'''<article class="mv-project-card" id="project-{e(p['id'])}">
  <div class="mv-project-topline"><span class="mv-project-category">{e(p['category'])}</span><span class="mv-project-status">{e(p['status'])}</span></div>
  <h3>{e(p['title'])}</h3>
  <p class="mv-project-purpose">{e(p['purpose'])}</p>
  <p class="mv-project-benefit"><b>Why it matters:</b> {e(p['benefit'])}</p>
  {workflow}
  {limits}
  <div class="mv-project-links">{source_link(p)}</div>
 </article>'''

def soup_section(markup):return BeautifulSoup(markup,'html.parser').find('section')

def header(title,eyebrow,intro):
 return f'<div class="container mv-projects-heading"><p class="mv-projects-eyebrow">{e(eyebrow)}</p><h2>{e(title)}</h2><p>{e(intro)}</p></div>'


def replace_home():
 from swaag_marketing_content import section as swaag_section, small_proof, hero_link
 p=R/'index.html';s=BeautifulSoup(p.read_text(),'html.parser')
 old_feature=s.select_one('section#swaag')
 if old_feature:old_feature.decompose()
 original=s.select_one('section#engineering')
 assert original is not None
 original.replace_with(soup_section(small_proof()))
 before=s.select_one('section#software-proof')
 assert before is not None
 before.insert_before(soup_section(swaag_section(compact=False)))
 hero=s.select_one('.sw-home-examples')
 if hero:
  for previous in hero.select('.sw-home-other-projects,.mv-hero-swaag-link'):previous.decompose()
  banner=BeautifulSoup(hero_link(),'html.parser').find('a')
  first=hero.select_one('a.sw-home-example')
  if first:first.insert_before(banner)
  else:hero.insert(0,banner)
 style='/multiverse-ai-website/assets/software-portfolio.css'
 if not s.select_one(f'link[href="{style}"]'):s.head.append(s.new_tag('link',href=style,rel='stylesheet'))
 p.write_text(str(s).rstrip()+'\n')
 print('HOME featured SWAAG use case, supporting code evidence; no equal-weight catalog')


def replace_technology():
 p=R/'technology/index.html';s=BeautifulSoup(p.read_text(),'html.parser')
 from swaag_marketing_content import section as swaag_section
 old_feature=s.select_one('section#swaag')
 if old_feature:old_feature.decompose()
 before=s.select_one('section#published')
 assert before is not None
 before.insert_before(soup_section(swaag_section(compact=True)))
 section=s.select_one('section#agents') or s.select_one('section#other-projects')
 assert section is not None
 markup=f'''<section class="mv-projects-section mv-projects-alt" id="other-projects"><span id="agents" class="mv-legacy-anchor" aria-hidden="true"></span>
  {header('More software and AI projects','SOURCE-VERIFIED PROJECTS','Each entry explains its specific purpose, the potential user benefit, and its current status. Public code is linked where available; several projects are still prototypes.')}
  <div class="container mv-project-grid">{''.join(card(x,True) for x in items)}</div>
  <div class="container mv-projects-actions"><a class="mv-primary-link" href="/multiverse-ai-website/projects/">Browse the whole portfolio</a><a class="mv-github-link" href="{root}" target="_blank" rel="noopener noreferrer">View my GitHub source code <span aria-hidden="true">↗</span></a></div>
 </section>'''
 section.replace_with(soup_section(markup))
 hero=s.select_one('.sw-sub-links')
 if hero and not hero.select_one('a[href="#other-projects"]'):
  a=s.new_tag('a',href='#other-projects');a['class']=['sw-textlink'];a.string='More projects: SWAAG, Android, Unity and utilities ↘'
  hero.append(a)
 style='/multiverse-ai-website/assets/software-portfolio.css'
 if not s.select_one(f'link[href="{style}"]'):
  s.head.append(s.new_tag('link',href=style,rel='stylesheet'))
 p.write_text(str(s).rstrip()+'\n')
 print('TECHNOLOGY',len(items),'detailed project entries')


def replace_projects():
 p=R/'projects/index.html';s=BeautifulSoup(p.read_text(),'html.parser')
 generic=s.select_one('#engineering')
 if generic:generic.decompose()
 current=s.select_one('#software-catalog')
 if current:current.decompose()
 industrial=s.select_one('#industrial-catalog')
 assert industrial
 markup=f'''<section class="mv-projects-section" id="software-catalog">
   {header('Additional software projects','BEYOND THE TWO MAIN DEMONSTRATIONS','The portfolio also includes self-hosted agents, Android applications, data tools, Unity packages, a typing trainer and a media workflow. Status labels distinguish public code, working prototypes and private development.')}
   <div class="container mv-project-grid">{''.join(card(x) for x in items)}</div>
   <div class="container mv-projects-actions"><a class="mv-primary-link" href="/multiverse-ai-website/technology/#other-projects">Read the project details</a><a class="mv-github-link" href="{root}" target="_blank" rel="noopener noreferrer">Public GitHub code <span aria-hidden="true">↗</span></a></div>
 </section>'''
 industrial.insert_before(soup_section(markup))
 # Legacy links to the generic Engineering section still lead to the software catalog.
 anchor=s.new_tag('span',id='engineering');anchor['class']=['mv-legacy-anchor']
 s.select_one('#software-catalog').insert(0,anchor)
 style='/multiverse-ai-website/assets/software-portfolio.css'
 if not s.select_one(f'link[href="{style}"]'):
  s.head.append(s.new_tag('link',href=style,rel='stylesheet'))
 p.write_text(str(s).rstrip()+'\n')
 print('PROJECTS',len(items),'actual projects added to directory')


def about_github():
 p=R/'about/index.html';s=BeautifulSoup(p.read_text(),'html.parser')
 old=s.select_one('#github-open-source')
 if old:old.decompose()
 main=s.select_one('main#main'); assert main
 section=soup_section(f'''<section id="github-open-source" class="container mv-about-github">
   <div><p class="mv-projects-eyebrow">PUBLIC SOURCE CODE</p><h2>Explore the code on GitHub.</h2>
   <p>My <a href="{root}" target="_blank" rel="noopener noreferrer">GitHub profile</a> contains public repositories for SWAAG, all2text, KnowMoreDiRT, Android, Unity and other projects. Some repositories are experimental; a public code repository does not necessarily mean the software is commercially released.</p></div>
   <div class="mv-about-github-links"><a href="{root}" target="_blank" rel="noopener noreferrer">Open my GitHub profile <span aria-hidden="true">↗</span></a><a href="/multiverse-ai-website/technology/#other-projects">Browse explained software projects <span aria-hidden="true">↗</span></a></div>
 </section>''')
 main.append(section)
 style='/multiverse-ai-website/assets/software-portfolio.css'
 if not s.select_one(f'link[href="{style}"]'):s.head.append(s.new_tag('link',href=style,rel='stylesheet'))
 p.write_text(str(s).rstrip()+'\n')
 print('ABOUT GitHub profile and curated project link')


def main():
 replace_home();replace_technology();replace_projects();about_github()
if __name__=='__main__':main()
