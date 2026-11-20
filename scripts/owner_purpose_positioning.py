#!/usr/bin/env python3
"""Apply latest owner-recording-derived SWAAG/KMD purposes after generic marketing.

Sources: original Jetson Aug 5/6 KMD, Sep 14/Oct 14 agent recordings;
Infra agent architecture and KMD knowledge design; source README and tests.
This is deliberately a separate last-pass override of older generated marketing.
"""
from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]


def section(markup):return BeautifulSoup(markup,'html.parser').find('section')

def render(name,apply):
    p=R/name
    doc=BeautifulSoup(p.read_text(),'html.parser')
    apply(doc)
    p.write_text(str(doc).rstrip()+'\n')
    print('OWNER PURPOSE',name)


def home(s):
    hero=s.select_one('section#top .sw-hero-copy');assert hero
    h=hero.select_one('h1');assert h
    h.replace_with(BeautifulSoup('<h1>AI workers you can manage. <em>Knowledge you can trust.</em></h1>','html.parser').find('h1'))
    lead=hero.select_one('.sw-lead');assert lead
    lead.clear();lead.append(BeautifulSoup('<strong>Multiverse is my independent software development business.</strong> SWAAG builds a persistent manager for background AI workers. KnowMoreDiRT researches fast, source-grounded reasoning across chaotic document collections. Their actual source code is available to inspect.','html.parser'))
    note=hero.select_one('.sw-home-intro-note');assert note
    note.string='The difference is not basic tool use or document search. It is how ongoing work is organized and how scattered information keeps its meaning.'
    btn=hero.select_one('.sw-hero-actions .sw-primary');assert btn
    btn.string='Explore SWAAG';btn['href']='#swaag'
    meta=s.find('meta',attrs={'name':'description'});assert meta
    meta['content']='Multiverse develops SWAAG for orchestrating background AI workers and KnowMoreDiRT for reasoning over chaotic files with semantic retrieval and DRT. Explore the code and evidence.'
    line=s.select_one('.mv-hero-swaag-link');assert line
    line.select_one('strong').string='SWAAG — one manager for many background workers'
    line.select_one('small').string='Keep the conversation; control the ongoing work'
    ai=s.select_one('.sw-home-example-ai');assert ai
    ai.select_one('strong').string='KnowMoreDiRT — make sense of messy information'
    ai.select('span')[-1].string='A raw-folder knowledge system combining semantic search with DRT-based context: who said what, when and under which conditions. Still an experimental research system.'
    # Put two flagships before the unrelated Wix product card.
    examples=s.select_one('.sw-home-examples');assert examples
    wix=examples.select_one('a.sw-home-example:not(.sw-home-example-ai)')
    if wix:
        wix.extract();ai.insert_after(wix)
    research=s.select_one('#research-proof');assert research
    wix_section=s.select_one('#software-proof');assert wix_section
    # The owner's two largest projects are SWAAG and KMD. Present both
    # before the published but narrower Wix application.
    research.extract();wix_section.insert_before(research)
    research.select_one('.sw-research-head .sw-kicker').string='FLAGSHIP RESEARCH · SOURCE-GROUNDED KNOWLEDGE'
    wix_section.select_one('.sw-section-heading .sw-kicker').string='PUBLISHED WIX APPLICATION · ORDER OPERATIONS'
    states=s.select('.sw-scope-inner > span')
    if len(states)==3:
        for target,markup in zip(states,[
          '<strong>SWAAG</strong> · open-source orchestration framework',
          '<strong>KnowMoreDiRT</strong> · research prototype',
          '<strong>Wix and 3D</strong> · published digital products',
        ]):
            target.clear();target.append(BeautifulSoup(markup,'html.parser'))
    h=research.select_one('h2');assert h
    h.replace_with(BeautifulSoup('<h2>KnowMoreDiRT — <em>find meaning in the file chaos.</em></h2>','html.parser').find('h2'))
    intro=research.select_one('.sw-research-head p:not(.sw-kicker)');assert intro
    intro.string=('Company knowledge hides in badly named files, deeply nested folders, inconsistent logs and outdated reports. A search match is not necessarily true in the requested context. KnowMoreDiRT combines file metadata, source-linked text and semantic retrieval with Discourse Representation Theory (DRT) to track referents, dates, claims and the conditions in which they apply. The goal is to find relevant information efficiently and reason across it without losing its meaning.')
    cards=research.select('.sw-kmd-user-value > div');assert len(cards)==3
    data=[
       ('MESSY FILES FIRST','No compulsory schema or naming convention.','The filesystem catalog stores paths and metadata; source text chunks retain precise source offsets.'),
       ('SEMANTIC RETRIEVAL','Locate related information beyond exact keywords.','Embeddings and bounded indexes narrow candidates without sending every file to an LLM for every comparison.'),
       ('SCOPED REASONING','Understand what a statement actually means.','DRT/DSPG represents referents, time, negation, reports, dreams and provenance. Real-world superiority is not yet verified.'),
    ]
    for card,(label,title,details) in zip(cards,data):
        card.select_one('span').string=label
        card.select_one('strong').string=title
        card.select_one('small').string=details


def swaag(s):
    hero=s.select_one('section.sa-hero');assert hero
    s.title.string='SWAAG | One Agent Manager, Background Workers — Multiverse'
    h=hero.select_one('h1');assert h
    h.replace_with(BeautifulSoup('<h1>One assistant to speak to. <em>Workers that keep moving.</em></h1>','html.parser').find('h1'))
    hero.select_one('.sa-lead').string=('SWAAG is a self-hosted orchestration framework. One manager stays responsive while background agents perform longer tasks; you can inspect their progress, questions, decisions and history, change priorities, or assign more work. Authorized autonomous continuation is configurable and disabled by default.')
    meta=s.find('meta',attrs={'name':'description'});assert meta
    meta['content']='SWAAG separates a persistent user-facing orchestrator from background workers, scheduling, shared resources, detailed history and optional authorized autonomous continuation.'
    flow=s.select_one('.sa-process');assert flow
    flow.select_one('.sa-process-title').string='ONE USER CONVERSATION · MANY SUPERVISED WORKERS'
    cards=flow.select('.sa-process-item');assert len(cards)==3
    data=[
       ('YOU','Talk to your team leader','Ask for status, change direction or start another job'),
       ('ORCHESTRATOR','Manage the worker plan','Supervise dependencies, resources, progress and questions'),
       ('WORKERS + HISTORY','Work independently; keep evidence','Worker actions, results, notes, checkpoints and recovery state'),
    ]
    for card,(label,title,desc) in zip(cards,data):
        card.select_one('span').string=label;card.select_one('strong').string=title;card.select_one('small').string=desc
    scenario=s.select_one('section.sa-use');assert scenario
    scenario.select_one('h2').string='One conversation with the manager. Work across many agents.'
    scenario.select_one('.sa-use-lead').string=('Multiple projects need investigation, testing, automation and follow-up. Some work is independent, some depends on earlier results. You want to remain available to direct the team, not manage a separate conversation for every worker.')
    steps=scenario.select('.sa-need-grid article');assert len(steps)==3
    data=[
       ('01 / YOUR CONTROL','One place to ask and redirect.','Request status, alter worker priorities or stop a task without manually monitoring every agent window.'),
       ('02 / THE ORCHESTRATOR','Plan parallel and dependent jobs.','Workers have explicit state and tool scopes; model scheduling and resource admission avoid treating shared compute as unlimited.'),
       ('03 / DURABLE HISTORY','Continue beyond a model context window.','Original messages, tool calls, results and worker events remain recoverable; relevant notes and source-backed projections are selected per task.'),
    ]
    for step,(label,title,body) in zip(steps,data):
        step.select_one('span').string=label;step.select_one('h3').string=title;step.select_one('p').string=body
    features=s.select('.sa-cap-grid > div');assert len(features)==4
    data=[
       ('Persistent manager for the user','One canonical conversation entry point coordinates background workers and current state.','Benefit: stay informed and intervene without managing every worker directly.'),
       ('Parallel workers and scheduling','Worker lifecycle, dependency plans, inference admission and liveness supervision coordinate work across available model resources.','Benefit: independent jobs can progress concurrently when capacity permits.'),
       ('Complete source history and task-specific context','Raw events persist while per-call model context selectively includes relevant history, notes and recoverable summaries.','Benefit: longer work retains evidence and context without overflowing the model.'),
       ('Authorized autonomous continuation','Durable wakeups, a user-authorized task backlog and optional autonomous work mode can extend tasks beyond an interactive turn.','Benefit: continue appropriate work when authorized; automatic idle dispatch is off by default.'),
    ]
    for feature,(title,body,benefit) in zip(features,data):
        feature.select_one('h3').string=title;feature.select_one('p').string=body;feature.select_one('span').string=benefit
    old=s.select_one('#baseline')
    if old:old.decompose()
    anchor=s.select_one('section#features');assert anchor
    baseline=section('''<section id="baseline" class="mv-baseline mv-baseline-agent"><div class="container"><p class="mv-proof-kicker">COMPARE CURRENT AGENT SYSTEMS</p><h2>Codex, Claude Code and Dots already use workers. What is SWAAG for?</h2><p class="mv-baseline-lead">Use an existing coding agent or hosted assistant if its workflow meets your needs. SWAAG is meant for developers who want to own and adapt the agent manager itself—not merely use an agent to complete a coding task.</p><div class="mv-baseline-cols"><article><span>EXISTING PRODUCTS</span><h3>Mature tools for getting work done.</h3><p>Codex and Claude Code have tools and subagents. Dots can maintain a conversation while agents work in parallel between interactions. They may offer stronger models, ready integrations, managed infrastructure and greater operational maturity.</p><div class="mv-baseline-links"><a href="https://learn.chatgpt.com/docs/agent-configuration/subagents" target="_blank" rel="noopener noreferrer">Codex subagents <span aria-hidden="true">↗</span></a><a href="https://claude.com/resources/articles/subagents-in-claude-code" target="_blank" rel="noopener noreferrer">Claude subagents <span aria-hidden="true">↗</span></a><a href="https://learn.chatgpt.com/docs/dots" target="_blank" rel="noopener noreferrer">Dots background agents <span aria-hidden="true">↗</span></a></div></article><article><span>SWAAG'S INSPECTABLE ARCHITECTURE</span><h3>Self-host your own team leader and worker runtime.</h3><p>Run configured local models and tool integrations, examine the orchestrator's decisions, worker histories and model scheduling, and adapt background policies, note-taking and recovery to your own software environment.</p><p class="mv-baseline-caveat">This is an architectural distinction, not a controlled benchmark win. Autonomous work requires explicit enablement and robust operational verification.</p><a href="https://github.com/HansPeterRadtke/swaag" target="_blank" rel="noopener noreferrer">Examine the open-source implementation <span aria-hidden="true">↗</span></a></article></div></div></section>''')
    anchor.insert_before(baseline)


def kmd(s):
    hero=s.select_one('.kmd-purpose-hero');assert hero
    s.title.string='KnowMoreDiRT | Knowledge from Chaotic Files — Multiverse'
    meta=s.find('meta',attrs={'name':'description'});assert meta
    meta['content']='KnowMoreDiRT researches fast semantic retrieval from chaotic raw folders using DRT/DSPG to retain source truth, identities, time and discourse scope.'
    h=hero.select_one('h1');assert h
    h.replace_with(BeautifulSoup('<h1>Find meaning in <em>the chaos of your files.</em></h1>','html.parser').find('h1'))
    ps=hero.select('.kmd-focus-copy > p');assert len(ps)>=3
    ps[0].string=('Company knowledge accumulates in wildly organized folders, forgotten reports, mixed logs and files without any agreed schema. A search result is not the same as an answer: what was said, by whom, when, and in what circumstances? KnowMoreDiRT researches how to reconstruct this meaning from the raw material.')
    ps[1].clear()
    ps[1].append(BeautifulSoup('<strong>The intended benefit:</strong> find relevant information quickly by meaning, and use Discourse Representation Theory (DRT) to avoid mixing up identities, past facts, claims, quotations and imaginary events. The system is still experimental; a superiority benchmark is not established.','html.parser'))
    diagram=hero.select_one('.kmd-flow-picture');assert diagram
    diagram.select_one('.kmd-picture-label').string='THE RESEARCH ARCHITECTURE — CONCEPT, NOT A LIVE SCREEN'
    tiles=diagram.select('.kmd-picture-card');assert len(tiles)==3
    for tile,(label,title,desc) in zip(tiles,[
      ('RAW INPUT','Messy files with original metadata','Folder trees, filenames and source-linked text chunks'),
      ('SEMANTIC SEARCH','Find relevant evidence by meaning','Vector and referent indexes narrow candidate passages'),
      ('DISCOURSE REASONING','Interpret context before answering','DRT/DRS ties identity, scope, time and evidence together'),
    ]):
        tile.select_one('span').string=label;tile.select_one('strong').string=title;tile.select_one('small').string=desc
    guide=s.select_one('#how-to-use');assert guide
    guide.select_one('h2').string='Start with messy files, not a clean database.'
    guide.select_one('.kmd-benefit-heading > p').string='The intended input is a folder of readable text, with arbitrary extensions, names and nested directories. The system extracts its own structure and retains exact source paths and offsets.'
    steps=guide.select('.kmd-use-flow > div');assert len(steps)==3
    for step,(title,body) in zip(steps,[
       ('Point it at the existing folder','Unstructured reports, logs, transcripts and raw text. No mandatory manifest, schema or manual file naming.'),
       ('Retrieve by semantic relevance','Embeddings and lexical/referent indexes narrow down likely evidence even when the question and source use different words.'),
       ('Interpret before answering','DRT/DSPG is intended to connect references, context and time across passages; the current public API still returns a plain answer string.'),
    ]):step.select_one('h3').string=title;step.select_one('p').string=body
    benefits=s.select('#user-benefits .kmd-benefit-cards article');assert len(benefits)==3
    for item,(title,body,behind) in zip(benefits,[
       ('No large reorganization first','Start with files and folders as they exist; keep the original structure and provenance.','Filesystem metadata catalog and source-offset-linked text chunks.'),
       ('Find related concepts efficiently','Vector similarity can propose relevant passages without asking an LLM to compare every single database entry.','Semantic embeddings plus bounded search indexes; performance needs empirical comparison.'),
       ('Do not mistake a dream or old claim for a fact','Dates, referents, negation, reports and fictional scope can completely change the meaning of otherwise identical statements.','DRT/DRS and DSPG representation of discourse conditions, identities, temporal events and exact evidence.'),
    ]):item.select_one('h3').string=title;item.select_one('p').string=body;item.select_one('.kmd-benefit-mapping span').string=behind
    headline=s.select_one('#user-benefits h2');assert headline
    headline.replace_with(BeautifulSoup('<h2>Find the right information. <em>Keep its meaning.</em></h2>','html.parser').find('h2'))
    old=s.select_one('#kmd-baseline')
    if old:old.decompose()
    anchor=s.select_one('#how-to-use');assert anchor
    baseline=section('''<section class="mv-baseline mv-kmd-baseline" id="kmd-baseline"><div class="container"><p class="mv-proof-kicker">THE CURRENT ALTERNATIVES</p><h2>Why not use Codex, Claude Code or GraphRAG?</h2><p class="mv-baseline-lead">For everyday file search or document Q&A, existing agents may be sufficient. GraphRAG and property-graph systems already combine LLM extraction, relationships and vectors. Semantic search and knowledge graphs alone are not unique.</p><div class="mv-baseline-cols"><article><span>WHAT OTHERS ALREADY DO</span><h3>Search documents and build knowledge graphs.</h3><p>General agents can explore files and synthesize answers. GraphRAG extracts entities, relationships and claims. These are valid existing approaches, not problems every company must replace with a new tool.</p><div class="mv-baseline-links"><a href="https://learn.chatgpt.com/docs/cli" target="_blank" rel="noopener noreferrer">Codex file tools <span aria-hidden="true">↗</span></a><a href="https://microsoft.github.io/graphrag/index/overview/" target="_blank" rel="noopener noreferrer">Microsoft GraphRAG <span aria-hidden="true">↗</span></a></div></article><article><span>KNOWMOREDIRT'S SCIENTIFIC APPROACH</span><h3>Build meaning with discourse representation.</h3><p>Start with arbitrary raw folders, keep filenames and source spans, use semantic indexes for candidate retrieval, then model referents, conditions, temporal evolution and quoted or imagined contexts with DRT/DRS. The aim is to distinguish what actually follows from the sources.</p><p class="mv-baseline-caveat">This is a specialized architecture and research hypothesis, not a measured superiority claim. General accuracy, scale and cold-query speed remain unproven.</p><a href="https://github.com/HansPeterRadtke/KnowMoreDiRT" target="_blank" rel="noopener noreferrer">Review the DRT/DSPG implementation <span aria-hidden="true">↗</span></a></article></div></div></section>''')
    anchor.insert_before(baseline)
    example=BeautifulSoup('''<div class="mv-scoped-example"><span>WHY DISCOURSE CONTEXT MATTERS</span><p>A document contains a law-like sentence, but another passage says it was part of a child's dream. Finding the sentence is easy; treating the dream as a real law is wrong. KnowMoreDiRT is built to keep the surrounding context and source attached to that statement, and to return unknown when real-world evidence is missing.</p><small>Illustrative hard-negative case from the original KMD recordings. Not a claim that every such case currently passes.</small></div>''','html.parser').find('div')
    baseline.select_one('.container').append(example)
    theory=BeautifulSoup('''<p class="mv-science-context">Scientific foundation: Discourse Representation Theory was introduced by Hans Kamp in the early 1980s, building on the wider tradition of formal linguistics and logic. <a href="https://plato.stanford.edu/entries/discourse-representation-theory/" target="_blank" rel="noopener noreferrer">Read the Stanford Encyclopedia account <span aria-hidden="true">↗</span></a>. Using this theory in software does not automatically prove that an AI system reasons correctly.</p>''','html.parser').find('p')
    baseline.select_one('.container').append(theory)

render('index.html',home)
render('swaag/index.html',swaag)
render('kmd/index.html',kmd)
