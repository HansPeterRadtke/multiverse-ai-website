#!/usr/bin/env python3
"""Make buyer value relative to the 2026 agent/tool baseline legible.

Runs after other page generators, before URL/SEO refresh. All comparisons
are intended-fit explanations, not measured superiority claims. Uses source
READMEs and verified official competitor docs; preserves prototype caveats.
"""
from pathlib import Path
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]


def soup(section):
    return BeautifulSoup(section,'html.parser').find('section')


def put(path,fn):
    p=ROOT/path
    s=BeautifulSoup(p.read_text(),'html.parser')
    fn(s)
    style='/multiverse-ai-website/assets/market-differentiation.css'
    if not s.select_one(f'head link[href="{style}"]'):
        s.head.append(s.new_tag('link',href=style,rel='stylesheet'))
    p.write_text(str(s).rstrip()+'\n')
    print('POSITIONED',path)


def home(s):
    hero=s.select_one('section#top .sw-hero-copy');assert hero
    hero.select_one('h1').clear()
    h=BeautifulSoup('''<h1>When off-the-shelf tools <em>don't fit the work.</em></h1>''','html.parser').find('h1')
    hero.select_one('h1').replace_with(h)
    lead=hero.select_one('.sw-lead'); assert lead
    lead.clear(); lead.append(BeautifulSoup('''<strong>Multiverse is my independent software development business.</strong> I build local-first agent infrastructure, research context-aware document reasoning, and publish focused Python developer tools. The point is what existing products leave unresolved—not basic AI tool use.''','html.parser'))
    note=hero.select_one('.sw-home-intro-note');assert note
    note.string='See concrete code and published packages. Experimental capabilities are labeled, and no benchmark advantage is assumed.'
    hero.select_one('.sw-hero-actions .sw-primary').string='Find the right project'
    hero.select_one('.sw-hero-actions .sw-primary')['href']='#swaag'
    meta=s.find('meta',attrs={'name':'description'});assert meta
    meta['content']='Multiverse builds local-first AI agent infrastructure, researches context-aware document reasoning, and publishes focused Python tools. See use cases and real source code.'
    # The first hero item is the SWAAG project, not a feature list.
    line=s.select_one('.mv-hero-swaag-link')
    assert line
    line.select_one('strong').string='SWAAG — an agent runtime to inspect and adapt'
    line.select_one('small').clear()
    line.select_one('small').append('For your own models, tools and persistent task history')
    ai=s.select_one('.sw-home-example-ai');assert ai
    ai.select_one('strong').string='KnowMoreDiRT — context behind the answer'
    desc=ai.select('span')[-1]
    desc.string='Research into tracking people, changing facts, claims and their original passages across messy text. More than generic document Q&A is the goal—not an achieved benchmark.'
    proof=s.select_one('#research-proof');assert proof
    proof.select_one('h2').clear()
    proof.select_one('h2').append(BeautifulSoup('''KnowMoreDiRT — <em>when an answer needs its context.</em>''','html.parser'))
    intro=proof.select_one('.sw-research-head p:not(.sw-kicker)');assert intro
    intro.string=('A coding agent can already search documents and answer questions. The harder problem appears when an old report says a machine was fixed, a newer log shows a different state, or a quoted allegation is mistaken for fact. KnowMoreDiRT researches how to represent referents, time, claims and exact source passages so those distinctions are not lost. This is its intended benefit, not a proven advantage over current agents.')
    value=proof.select('.sw-kmd-user-value > div')
    assert len(value)==3
    entries=[('THE CURRENT BASELINE','Agents can read files and answer questions.','That alone is not a KnowMoreDiRT differentiator.'),('THE RESEARCH DIRECTION','Preserve who, when, what was claimed and where.','A discourse provenance graph retains references, contexts, times and source spans.'),('POTENTIAL USER BENEFIT','Reduce plausible answers from the wrong context.','Intended, not established against Codex, Claude Code or real archives.')]
    for target,(tag,name,caption) in zip(value,entries):
        target.select_one('span').string=tag
        target.select_one('strong').string=name
        target.select_one('small').string=caption
    # Small real product evidence, not another gigantic card grid.
    before=s.select_one('.sw-commercial')
    assert before
    existing=s.select_one('#capov')
    if existing:existing.decompose()
    feature=soup('''<section id="capov" class="mv-capov-strip"><div class="container mv-capov-layout"><div class="mv-capov-copy"><p class="mv-proof-kicker">A SMALL PUBLISHED PYTHON TOOL · ON PYPI</p><h2>Captain Obvious <span>— CapOv</span></h2><p>Fix simple, mechanical Python mistakes without asking an AI agent to rewrite your program. CapOv can clean up duplicate imports, add certain missing imports and repair selected bracket errors. Ruff already automates many Python fixes; CapOv is a smaller, simple CLI utility rather than a replacement for a full linter. Review edits before use.</p><div class="mv-capov-links"><a href="https://pypi.org/project/capov/" target="_blank" rel="noopener noreferrer">See the package on PyPI <span aria-hidden="true">↗</span></a><a href="https://github.com/HansPeterRadtke/capov" target="_blank" rel="noopener noreferrer">Read the source and tests <span aria-hidden="true">↗</span></a><a href="https://docs.astral.sh/ruff/linter/" target="_blank" rel="noopener noreferrer">Compare with Ruff <span aria-hidden="true">↗</span></a></div></div><div class="mv-capov-install"><span>INSTALL FROM PYPI</span><code>pip install capov</code><span>RUN ON A PYTHON FILE</span><code>python -m capov script.py</code><small>Published v0.1.6. Review the proposed edits before overwriting important files.</small></div></div></section>''')
    before.insert_before(feature)


def swaag(s):
    hero=s.select_one('section.sa-hero');assert hero
    h=hero.select_one('h1');assert h
    h.replace_with(BeautifulSoup('''<h1>Your own models. Your own tools. <em>An agent runtime you can inspect.</em></h1>''','html.parser').find('h1'))
    lead=hero.select_one('.sa-lead');assert lead
    meta=s.find('meta',attrs={'name':'description'});assert meta
    meta['content']='SWAAG is a local-first agent runtime for developers integrating their own models, tools, orchestration, event history and task controls. Compare with Codex and Claude Code.'
    lead.string=('Codex and Claude Code already run coding tasks and use tools. SWAAG is for developers building their own local-first agent infrastructure, with a persistent orchestrator, controlled tools, and reconstructable task events. These are inspectable design choices—not proven performance advantages.')
    old=s.select_one('#baseline');
    if old:old.decompose()
    anchor=s.select_one('section#features');assert anchor
    baseline=soup('''<section id="baseline" class="mv-baseline mv-baseline-agent"><div class="container"><p class="mv-proof-kicker">THE REAL 2026 BASELINE</p><h2>Why not simply use Codex or Claude Code?</h2><p class="mv-baseline-lead">Often you should. For regular repository coding, reviewing changes or running development commands, a mature coding agent may already be the simplest solution. Tool use and subagents are not unique to SWAAG.</p><div class="mv-baseline-cols"><article><span>USE AN EXISTING CODING AGENT WHEN</span><h3>Your goal is to get coding work done.</h3><p>You want established editing, terminal, code-review and delegation workflows without building or operating another agent runtime.</p><div class="mv-baseline-links"><a href="https://learn.chatgpt.com/docs/cli" target="_blank" rel="noopener noreferrer">Codex CLI documentation <span aria-hidden="true">↗</span></a><a href="https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more" target="_blank" rel="noopener noreferrer">Claude Code capabilities <span aria-hidden="true">↗</span></a></div></article><article><span>CONSIDER SWAAG WHEN</span><h3>Your product needs its own agent infrastructure.</h3><p>You want to integrate a local-first orchestrator with your own clients, model services, permitted tools, durable state, and precise rules for task handoff and recovery.</p><p class="mv-baseline-caveat">Not a drop-in guarantee or a benchmark win. The integration and operational testing are your responsibility; SWAAG is evolving source code.</p><a href="https://github.com/HansPeterRadtke/swaag" target="_blank" rel="noopener noreferrer">Inspect SWAAG's architecture <span aria-hidden="true">↗</span></a></article></div></div></section>''')
    anchor.insert_before(baseline)


def kmd(s):
    hero=s.select_one('.kmd-purpose-hero');assert hero
    s.title.string='KnowMoreDiRT | When Documents Disagree — Multiverse'
    meta=s.find('meta',attrs={'name':'description'});assert meta
    meta['content']='KnowMoreDiRT researches document context: source claims, changing facts, identities, time and evidence. Understand the goal beyond ordinary AI document Q&A and its current limits.'
    h=hero.select_one('h1');assert h
    h.replace_with(BeautifulSoup('''<h1>When documents disagree, <em>what should you believe?</em></h1>''','html.parser').find('h1'))
    ps=hero.select('.kmd-focus-copy > p')
    assert len(ps)>=3
    ps[0].string=("An AI agent can already read files and answer questions. But what if two documents disagree, or a reported claim is mistaken for fact? KnowMoreDiRT researches how to keep those distinctions instead of losing context during retrieval.")
    ps[1].clear()
    ps[1].append(BeautifulSoup('''<strong>The intended benefit:</strong> fewer plausible answers that mix up people, claims, time or sources. Experimental research, not measured superiority over modern agents.''','html.parser'))
    old=s.select_one('#kmd-baseline')
    if old:old.decompose()
    anchor=s.select_one('#how-to-use');assert anchor
    baseline=soup('''<section class="mv-baseline mv-kmd-baseline" id="kmd-baseline"><div class="container"><p class="mv-proof-kicker">THE EXISTING STANDARD</p><h2>What is different from asking Codex or Claude Code to read files?</h2><p class="mv-baseline-lead">A modern agent can open documents, search a repository and generate an answer. KnowMoreDiRT is researching a narrower, more difficult knowledge problem: representing who said what, what was asserted versus merely reported, when it was true, and which exact source supports a conclusion.</p><div class="mv-baseline-cols"><article><span>GENERAL-PURPOSE AGENT</span><h3>Retrieve relevant text and answer.</h3><p>For many everyday document questions, the tools people already have may be sufficient. KnowMoreDiRT is not positioned as a better general chatbot or finished document assistant.</p><div class="mv-baseline-links"><a href="https://learn.chatgpt.com/docs/cli" target="_blank" rel="noopener noreferrer">Codex CLI capabilities ↗</a><a href="https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more" target="_blank" rel="noopener noreferrer">Claude Code capabilities ↗</a></div></article><article><span>KNOWMOREDIRT RESEARCH</span><h3>Keep references, scope and conflicting evidence distinct.</h3><p>The DRT/DSPG design stores discourse referents, claims, contexts, temporal relationships and source spans. The intended outcome is fewer confidently wrong answers caused by conflating different contexts.</p><p class="mv-baseline-caveat">A prototype with strict fixture regressions and unresolved live-model/generalization performance. No demonstrated advantage over competing document agents.</p><a href="https://github.com/HansPeterRadtke/KnowMoreDiRT" target="_blank" rel="noopener noreferrer">Read the research source and evaluation limits <span aria-hidden="true">↗</span></a></article></div></div></section>''')
    anchor.insert_before(baseline)
    # The educational workflow remains after the research problem/baseline.
    note=s.select_one('.kmd-benefits-section .kmd-benefit-heading h2')
    if note:note.replace_with(BeautifulSoup('''<h2>Less context confusion. <em>Answers you can investigate.</em></h2>''','html.parser').find('h2'))


put('index.html',home)
put('swaag/index.html',swaag)
put('kmd/index.html',kmd)
