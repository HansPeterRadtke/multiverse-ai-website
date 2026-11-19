#!/usr/bin/env python3
"""Explain KMD as a folder-questioning workflow, not as a DRT graph product.
Uses current Raspi public API docs and the website's scoped source test proof.
"""
from pathlib import Path
from bs4 import BeautifulSoup
import json

R=Path(__file__).resolve().parents[1];BASE='/multiverse-ai-website/'
proof=json.loads((R/'assets/kmd/answer-proof.json').read_text())
assert proof['answer']=='Mira Chen' and proof['source']=='field_report.txt'

def fragment(markup):
    return BeautifulSoup(markup,'html.parser').find('section')

p=R/'kmd/index.html'; s=BeautifulSoup(p.read_text(),'html.parser')
assert s.select_one('.kmd-focus-hero') and s.select_one('.kmd-focus-watch')
if not s.select_one('.kmd-purpose-hero'):
    hero=fragment('''<section class="kmd-focus-hero container kmd-purpose-hero">
      <div class="kmd-focus-copy">
        <span class="focus-product-tag">KNOWMOREDIRT / AI KNOWLEDGE RESEARCH</span>
        <h1>Ask questions about <em>the files you already have.</em></h1>
        <p>Imagine a folder containing years of reports, meeting notes, logs and transcripts. You need a fact, but you don't know which document contains it. KnowMoreDiRT is research into a system that reads those files and lets you ask a question in ordinary language.</p>
        <p class="kmd-purpose-promise"><strong>The point:</strong> find useful information without searching through every document yourself—and keep enough information about the original text to check the answer.</p>
        <div class="kmd-focus-actions"><a class="focus-primary" href="#how-to-use">How someone would use it ↓</a><a class="focus-secondary" href="#kmd-watch">See the recorded research test ↓</a></div>
        <p class="kmd-purpose-status">Research prototype. Not a ready-to-use document-search website or a proven solution for arbitrary company archives.</p>
      </div>
      <figure class="kmd-hero-flow-illustration" aria-label="Illustrated intended KnowMoreDiRT workflow"><div class="kmd-flow-picture"><div class="kmd-picture-label">HOW IT IS INTENDED TO WORK</div><div class="kmd-picture-card kmd-picture-files"><span>YOUR EXISTING FOLDER</span><strong>Reports, notes, logs, transcripts</strong><small>Readable text files, including subfolders</small></div><div class="kmd-picture-arrow" aria-hidden="true">↓</div><div class="kmd-picture-card kmd-picture-question"><span>YOUR QUESTION</span><strong>Ask in ordinary language</strong><small>No special database query required</small></div><div class="kmd-picture-arrow" aria-hidden="true">↓</div><div class="kmd-picture-card kmd-picture-result"><span>INTENDED OUTPUT</span><strong>Short answer from the files</strong><small>Source details retained internally for inspection</small></div></div><figcaption>Conceptual workflow illustration. Not a live interface or proof of general answer accuracy.</figcaption></figure>
    </section>''')
    s.select_one('.kmd-focus-hero').replace_with(hero)

    use=fragment('''<section class="kmd-use-section" id="how-to-use"><div class="container">
      <div class="kmd-benefit-heading"><span class="focus-product-tag">THE USER'S WORKFLOW</span><h2>What would you actually do with it?</h2><p>The intended way to use KnowMoreDiRT is straightforward. It currently exposes a small Python interface, not a finished drag-and-drop consumer application.</p></div>
      <div class="kmd-use-flow">
        <div><span>01 / YOUR DOCUMENTS</span><h3>Choose an existing folder</h3><p>Point the system to a folder of readable text. It can contain subfolders, notes, logs, transcripts, and other readable text files.</p></div>
        <div><span>02 / YOUR QUESTION</span><h3>Ask in everyday language</h3><p>For example: “Who reviewed the report?” or “Which reference fixed the problem?” You do not need to construct a database query.</p></div>
        <div><span>03 / THE RESULT</span><h3>Receive a short answer</h3><p>The public API returns plain text. KMD also keeps source links and evidence internally; its separate demonstration explorer shows those records for a limited test.</p></div>
      </div>
      <p class="kmd-flow-note">Today these steps are called through Python, with a local AI model available. A polished end-user interface and automatic citations in each public API response are not established features.</p>
    </div></section>''')
    benefits=fragment('''<section class="kmd-benefits-section" id="user-benefits"><div class="container">
     <div class="kmd-benefit-heading"><span class="focus-product-tag">WHY WOULD SOMEONE WANT THIS?</span><h2>Less hunting through files. <em>More useful answers.</em></h2><p>These are the benefits the project is designed to provide. The available small tests do not yet establish these outcomes at business scale.</p></div>
     <div class="kmd-benefit-cards">
       <article><span class="kmd-benefit-type">USER BENEFIT</span><h3>Use the folders you already have</h3><p>Instead of manually converting text files into a special format, begin with existing folders of readable text.</p><div class="kmd-benefit-mapping"><b>Feature behind it</b><span>Recursive raw-folder scanning and text ingestion, with no required special input schema.</span></div></article>
       <article><span class="kmd-benefit-type">USER BENEFIT</span><h3>Ask instead of opening files one by one</h3><p>The goal is to find a fact without guessing which filename or phrase to search for first.</p><div class="kmd-benefit-mapping"><b>Feature behind it</b><span>Natural-language questions, bounded text retrieval and source-based answer generation.</span></div></article>
       <article><span class="kmd-benefit-type">USER BENEFIT</span><h3>Check where information came from</h3><p>A supported answer should be traceable to its original text instead of becoming an unsupported AI assertion.</p><div class="kmd-benefit-mapping"><b>Feature behind it</b><span>Internal source spans, document paths and provenance records. Public answers are currently plain strings.</span></div></article>
     </div>
    </div></section>''')
    watch=s.select_one('.kmd-focus-watch')
    watch.insert_before(use)
    watch.insert_before(benefits)
    s.select_one('.kmd-focus-explain').decompose()

    # Explain the recorded test in the context of the hoped-for user workflow.
    watch.select_one('.focus-product-tag').string='WHAT HAS ACTUALLY BEEN TESTED'
    watch.select_one('h2').clear();watch.select_one('h2').append('A limited experiment. ')
    em=s.new_tag('em');em.string='With inspectable source evidence.';watch.select_one('h2').append(em)
    for t in watch.select('.focus-screen-head'):
      for content in list(t.contents):
        if isinstance(content,str) and 'PREVIOUSLY RECORDED EVIDENCE' in content:content.replace_with(' PREVIOUSLY RECORDED TEST EVIDENCE ')

    # Keep the existing technical presentation available only on request.
    more=s.select_one('.kmd-focus-more');assert more
    label=more.select_one('.focus-product-tag');label.string='FOR TECHNICAL READERS'
    details=more.select('details')
    if details:
      details[0].select_one('summary').clear()
      details[0].select_one('summary').append('How the internal technology works')
      plus=s.new_tag('span');plus.string='+';details[0].select_one('summary').append(plus)
      explanation=s.new_tag('p'); explanation.string='Behind the simple folder-and-question workflow, the system uses local AI, a structured discourse representation, a SQLite-backed source graph, and bounded retrieval to reason about text while retaining original evidence. These are implementation details, not extra tasks for a user.'
      details[0].select_one('.kmd-details-body').insert(0,explanation)
      api=s.new_tag('pre'); code=s.new_tag('code');code.string='import knowmoredirt as kmd\nkmd.initialize("/path/to/your/folder")\nanswer = kmd.question("Who reviewed the field report?")';api.append(code)
      detail_body=details[0].select_one('.kmd-details-body');detail_body.insert(1,api)
      caveat=s.new_tag('p');caveat.string='The public interface currently returns only the answer text. The source graph and diagnostics are internal; the public research explorer is a separate demonstration, not a general citation interface.';detail_body.insert(2,caveat)
    if len(details)>1:
      details[1].select_one('summary').clear()
      details[1].select_one('summary').append('What works today, and what is still unproven')
      plus=s.new_tag('span');plus.string='+';details[1].select_one('summary').append(plus)

    cta=s.select_one('.kmd-focus-cta')
    if cta and cta.select_one('h2'):cta.select_one('h2').string='Have an archive of documents that is difficult to search?'

    # metadata, styling
    s.title.string='KnowMoreDiRT | Ask Questions About Existing Files — Multiverse'
    meta=s.find('meta',attrs={'name':'description'})
    if meta:meta['content']='KnowMoreDiRT explores asking ordinary-language questions about existing folders of readable files. Learn the user workflow, intended benefits, actual features and research limitations.'
    for meta in s.find_all('meta',attrs={'property':'og:description'}):meta['content']='The purpose, workflow and intended user benefits of KnowMoreDiRT, with clearly distinguished technical implementation and verified research limits.'
    head=s.select_one('head');style=s.new_tag('link',href='/multiverse-ai-website/assets/kmd/user-benefits.css',rel='stylesheet');head.append(style)
    p.write_text(str(s).rstrip()+'\n')

KMD_RESEARCH_NOTE = '<div class="kmd-meaning-research"><div><span class="kmd-benefit-type">LONGER-TERM RESEARCH GOAL</span><h3>Understand context, not just match words</h3><p>Ordinary search can find a word. Many real questions depend on relationships: who did something, what “she” refers to in a later sentence, or how a status changed over time. KnowMoreDiRT is researching how to preserve that context across source text.</p></div><p><strong>Current limit:</strong> broad understanding across many documents, pronouns, identity changes and time has not yet been demonstrated reliably. This is a research direction, not an already-proven user feature.</p></div>'

# Additional experimental capability: meaningful context between sentences,
# distinct from currently verified basic question answering.
if not s.select_one('.kmd-meaning-research'):
    supplement = BeautifulSoup(KMD_RESEARCH_NOTE, 'html.parser').find('div')
    target = s.select_one('#user-benefits .container')
    assert target is not None
    target.append(supplement)
    p.write_text(str(s).rstrip()+'\n')


# Home explanation: make value, workflow, and feature/readiness distinct, not more jargon.
p=R/'scripts/rebuild_software_home.py';home=p.read_text()
old='<strong>KnowMoreDiRT — answers from documents</strong>\n      <span>An experimental system for finding answers in documents and checking the original evidence.</span>'
new='<strong>KnowMoreDiRT — ask your own files</strong>\n      <span>Designed for people with folders of reports, notes and logs: ask a question rather than hunt through every file. The goal is an answer backed by original text. Still research, not a finished app.</span>'
assert old in home or new in home
if old in home:home=home.replace(old,new)
old='<h2>KnowMoreDiRT — <em>find answers and check their sources.</em></h2>'
new='<h2>KnowMoreDiRT — <em>ask questions about your documents.</em></h2>'
assert old in home or new in home
if old in home:home=home.replace(old,new)
old='A company may have thousands of documents. KnowMoreDiRT explores how local AI could find an answer and point to the exact passage in the original file. The aim is to make answers easier to check, rather than simply trusting the AI.'
new='Imagine you have many folders of reports, notes, logs and transcripts. Instead of opening files one by one, the goal is to point KnowMoreDiRT at a folder, ask a question in everyday language, and receive a short answer. The system keeps source evidence internally so results can be investigated rather than blindly trusted.'
assert old in home or new in home
if old in home:home=home.replace(old,new)
marker='<div class="sw-kmd-concept" aria-label="The research goal, not a claim of production readiness">'
assert marker in home
benefit_intro='''<div class="sw-kmd-user-value"><div><span>WHAT YOU DO</span><strong>Choose a folder and ask a question.</strong><small>Current interface: two Python functions, not a finished web app.</small></div><div><span>WHAT IT AIMS TO SAVE</span><strong>Time searching through scattered files.</strong><small>Intended benefit; large real-world collections are not yet validated.</small></div><div><span>WHY IT MAY BE MORE TRUSTWORTHY</span><strong>The answer has source records behind it.</strong><small>Evidence stays inside the system; public API still returns plain text.</small></div></div>\n  '''
if 'sw-kmd-user-value' not in home:home=home.replace(marker,benefit_intro+marker,1)
old='<a class="sw-button sw-primary" href="{url(\'kmd/evidence/#answer-proof\')}">Inspect the recorded test evidence</a>'
new='<a class="sw-button sw-primary" href="{url(\'kmd/\')}">See how KnowMoreDiRT is intended to work</a><a class="sw-textlink" href="{url(\'kmd/evidence/#answer-proof\')}">Inspect the limited test evidence ↗</a>'
assert old in home or new in home
if old in home:home=home.replace(old,new)
p.write_text(home)

# Software page: user intent first, technical/readiness second.
p=R/'scripts/rebuild_software_page.py';t=p.read_text()
old='KnowMoreDiRT: answer a question and show the source'
new='KnowMoreDiRT: ask questions about existing files'
assert old in t or new in t
if old in t:t=t.replace(old,new)
old='The problem:</strong> a document answer is difficult to trust without knowing exactly where it came from.'
new='The problem:</strong> useful information is scattered across many reports, notes and log files. Searching manually is time-consuming.'
assert old in t or new in t
if old in t:t=t.replace(old,new)
old='<p><strong>The recorded test:'
new='<p><strong>The intended workflow:</strong> point KMD at an existing folder of readable text, ask a question in normal language, and receive a plain answer. Source context is held internally so the result can be investigated. This could reduce manual searching, but the benefit is not yet validated at business scale.</p><p><strong>The limited fictional test:'
assert old in t or new in t
if old in t:t=t.replace(old,new)
old='Read about the project ↗'
t=t.replace(old,'See how the system would be used ↗')
p.write_text(t)

# Products directory description without implying that generic knowledge answers are a ready product.
p=R/'projects/index.html';t=p.read_text()
old='Explores a way to answer questions about documents while retaining links to original source evidence. A controlled fictional test can be inspected.'
new='Designed for searching your existing folders of reports, notes and logs by asking questions. A limited test returned an answer backed by an original source passage; broader use is still research.'
if old in t:t=t.replace(old,new)
p.write_text(t)

print('UPDATED KMD purpose, user workflow, intended benefits, implementation and verification limits')
