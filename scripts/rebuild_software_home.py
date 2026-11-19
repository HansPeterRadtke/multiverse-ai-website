#!/usr/bin/env python3
"""Build a self-explanatory business homepage with scoped source-backed examples.

This is a portfolio of independently developed work, not a store checkout,
not an employer-affiliated site, and not a production claim for KMD.
"""
from pathlib import Path
from html import escape
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = '/multiverse-ai-website/'
url = lambda relative: BASE + relative

proof = json.loads((ROOT / 'assets/kmd/answer-proof.json').read_text())
assert proof['question'] == 'Who reviewed the Falcon Test Plan?'
assert proof['answer'] == 'Mira Chen'
assert 'Mira Chen reviewed the Falcon Test Plan' in proof['source_excerpt']
question = escape(proof['question'])
answer = escape(proof['answer'])
source = escape(proof['source'])
excerpt = escape(proof['source_excerpt'].splitlines()[1])

main = f'''<main id="main">
<section class="sw-hero sw-home-hero" id="top"><div class="container sw-hero-grid">
  <div class="sw-hero-copy">
    <p class="sw-kicker">MULTIVERSE · INDEPENDENT SOFTWARE & TECHNOLOGY PROJECTS</p>
    <h1>Build AI that can use tools.<br><em>Not just answer questions.</em></h1>
    <p class="sw-lead"><strong>Multiverse is my independent software development business.</strong> I build agent frameworks, software automation and data tools. SWAAG is the main open-source example: technology for developers connecting AI models to real computer work.</p>
    <p class="sw-home-intro-note">The source code is public where available, so you can inspect the engineering before considering any separate technology opportunity.</p>
    <div class="sw-hero-actions"><a class="sw-button sw-primary" href="#swaag">Why teams use SWAAG</a><a class="sw-button sw-outline" href="https://github.com/HansPeterRadtke" target="_blank" rel="noopener noreferrer">Inspect the public code ↗</a></div>
  </div>
  <div class="sw-home-examples" aria-label="Selected SWAAG, software product and AI research projects">
    <a class="sw-home-example" href="#software-proof">
      <img class="sw-home-example-image" src="{url('assets/focus/wix-dashboard-poster.webp')}" alt="Preview of the real Late Order Monitor dashboard" width="1280" height="720" loading="eager">
      <span class="sw-proof-status">PUBLISHED SOFTWARE · FOR ONLINE SHOP OWNERS</span>
      <strong>Late Order Monitor for Wix Stores</strong>
      <span>This app helps a shop owner review <em>orders already placed in their own Wix store</em>. It does not sell anything or take payments on this website.</span>
      <small>See how the application works <span aria-hidden="true">↗</span></small>
    </a>
    <a class="sw-home-example sw-home-example-ai" href="#research-proof">
      <img class="sw-home-example-image sw-research-visual" src="{url('assets/kmd/kmd-evidence-walkthrough-poster.webp')}" alt="Preview of the KnowMoreDiRT source-evidence research viewer" width="1280" height="800" loading="eager">
      <span class="sw-proof-status">AI RESEARCH · NOT A FINISHED PRODUCT</span>
      <strong>KnowMoreDiRT — ask your own files</strong>
      <span>Designed for people with folders of reports, notes and logs: ask a question rather than hunt through every file. The goal is an answer backed by original text. Still research, not a finished app.</span>
      <small>See the project and a limited test <span aria-hidden="true">↗</span></small>
    </a>
    <a class="sw-home-3d-link" href="{url('3d/')}">Also: a separate catalog of animated industrial 3D models <span aria-hidden="true">↗</span></a>
  </div>
</div></section>
<section class="sw-scope" aria-label="Project readiness"><div class="container sw-scope-inner">
  <span><strong>Software app</strong> · published for Wix store owners</span>
  <span><strong>Document AI</strong> · experimental research</span>
  <span><strong>3D assets</strong> · separately listed products</span>
</div></section>
<section class="sw-software" id="software-proof"><div class="container">
  <div class="sw-section-heading">
    <p class="sw-kicker sw-ink-kicker">01 / PUBLISHED SOFTWARE · FOR WIX STORE OWNERS</p>
    <h2>Late Order Monitor — <em>an app for managing existing shop orders.</em></h2>
    <p>For businesses that operate an online shop using <strong>Wix Stores</strong>. When customers place orders in that shop, the owner needs to know which paid orders have not been shipped yet. This separate, read-only app displays those orders, helps identify older ones, and lets the owner export a follow-up list.</p>
    <p class="sw-not-a-store"><strong>Important:</strong> Multiverse does not take customer orders here. The screenshot below is from a sample Wix shop's order dashboard, not a Multiverse checkout.</p>
  </div>
  <div class="sw-owner-flow" aria-label="How the published Wix application is used">
    <div><span>1 · EXISTING SHOP</span><strong>Customer orders arrive in a Wix store</strong></div>
    <b aria-hidden="true">→</b>
    <div><span>2 · LATE ORDER MONITOR</span><strong>The app displays paid, unfulfilled orders</strong></div>
    <b aria-hidden="true">→</b>
    <div><span>3 · SHOP OPERATOR</span><strong>Reviews the list and exports it for follow-up</strong></div>
  </div>
  <div class="sw-software-grid">
    <figure class="sw-video-wrap">
      <figcaption class="sw-video-heading"><span>REAL DEMO · SAMPLE WIX STORE ORDER DATA</span><span>26 seconds · silent with captions</span></figcaption>
      <video aria-label="Late Order Monitor read-only Wix Stores app showing existing sample orders and filters" controls muted playsinline preload="metadata" poster="{url('assets/focus/wix-dashboard-poster.webp')}" width="1280" height="720">
        <source src="{url('assets/focus/wix-late-order-monitor-silent.mp4')}" type="video/mp4">
        <track kind="captions" src="{url('assets/late-order-captions.vtt')}" srclang="en" label="English captions" default>
        Your browser cannot play the video.
      </video>
    </figure>
    <div class="sw-software-steps">
      <p class="sw-mini-tag">WHAT THE SHOP OWNER CAN DO</p>
      <div><span>1</span><p><strong>See unfulfilled orders</strong><small>Read orders already recorded by their Wix store.</small></p></div>
      <div><span>2</span><p><strong>Spot older orders</strong><small>Filter by age to decide which need follow-up.</small></p></div>
      <div><span>3</span><p><strong>Export a CSV list</strong><small>Keep a follow-up list without changing order status.</small></p></div>
      <p class="sw-readonly-note">The app cannot place orders, take payment, or ship anything.</p>
      <a class="sw-button sw-dark" href="https://multiverse-salvatorquaro1-0a0e.wix-site-host.com/" target="_blank" rel="noopener noreferrer">Read about the published Wix app <span aria-hidden="true">↗</span></a>
    </div>
  </div>
</div></section>
<section class="sw-research" id="research-proof"><div class="container">
  <div class="sw-research-head"><div>
    <p class="sw-kicker">02 / AI PROJECT · DOCUMENT ANSWERS WITH SOURCES</p>
    <h2>KnowMoreDiRT — <em>ask questions about your documents.</em></h2>
    <p>Imagine you have many folders of reports, notes, logs and transcripts. Instead of opening files one by one, the goal is to point KnowMoreDiRT at a folder, ask a question in everyday language, and receive a short answer. The system keeps source evidence internally so results can be investigated rather than blindly trusted.</p>
    <p>So far, this page shows evidence from a <strong>limited test using fictional documents</strong>. It is not a production-ready search service or an AI system running new queries directly on this website.</p>
  </div><span class="sw-state">RESEARCH PROTOTYPE · NOT FOR SALE AS A FINISHED APP</span></div>
  <div class="sw-kmd-user-value"><div><span>WHAT YOU DO</span><strong>Choose a folder and ask a question.</strong><small>Current interface: two Python functions, not a finished web app.</small></div><div><span>WHAT IT AIMS TO SAVE</span><strong>Time searching through scattered files.</strong><small>Intended benefit; large real-world collections are not yet validated.</small></div><div><span>WHY IT MAY BE MORE TRUSTWORTHY</span><strong>The answer has source records behind it.</strong><small>Evidence stays inside the system; public API still returns plain text.</small></div></div>
  <div class="sw-kmd-concept" aria-label="The research goal, not a claim of production readiness">
    <div><span>DOCUMENTS</span><strong>A collection of files containing facts</strong></div>
    <b aria-hidden="true">→</b>
    <div><span>QUESTION</span><strong>Ask the research system about those files</strong></div>
    <b aria-hidden="true">→</b>
    <div><span>ANSWER + SOURCE</span><strong>Inspect the original evidence before trusting it</strong></div>
  </div>
  <div class="sw-kmd-details">
    <div><h3>What has actually been tested?</h3><p>A controlled one-file experiment returned the expected answer and identified the supporting text. The system used local models and cached intermediate results. That does not establish general performance across real company document collections.</p><a class="sw-button sw-primary" href="{url('kmd/')}">See how KnowMoreDiRT is intended to work</a><a class="sw-textlink" href="{url('kmd/evidence/#answer-proof')}">Inspect the limited test evidence ↗</a></div>
    <details><summary>See the fictional test example</summary>
      <div class="sw-kmd-example"><p><strong>Question:</strong> {question}</p><p><strong>Answer returned:</strong> {answer} <span class="sw-fictional">(fictional character in a test file)</span></p><p><strong>Original passage in {source}:</strong> <q>{excerpt}</q></p><p>This example verifies one controlled case, not general reliability.</p></div>
    </details>
  </div>
</div></section>
<section class="sw-engineering" id="engineering"><div class="container sw-engineering-layout">
  <div><p class="sw-kicker sw-ink-kicker">03 / SOFTWARE ENGINEERING WORK</p><h2>Automation and AI development.</h2><p>Other projects include software that connects applications and APIs, performs defined computer tasks, and checks the results. There is also work on local language models, data processing and software testing. These are separate engineering efforts—not a claim that one finished AI product can already do everything.</p><p>For a business project, the next step would be to identify a concrete task and assess what existing code can actually be reused or adapted.</p></div>
  <div class="sw-workflow"><p class="sw-mini-tag">EXAMPLE ENGINEERING TASK, NOT A PRODUCT DEMO</p>
    <div><strong>Receive a defined task</strong><span>Specific input and expected result</span></div><i aria-hidden="true">↓</i>
    <div><strong>Run the required software</strong><span>Use an API, application or automation tool</span></div><i aria-hidden="true">↓</i>
    <div><strong>Check what happened</strong><span>Verify before reporting completion</span></div>
    <small>Illustrative workflow. No customer deployment is claimed.</small>
    <a class="sw-textlink sw-ink-link" href="{url('technology/')}">Explore the software engineering work <span aria-hidden="true">↗</span></a>
  </div>
</div></section>
<section class="sw-commercial"><div class="container sw-commercial-layout"><div>
  <p class="sw-kicker">TECHNOLOGY & COMMERCIAL OPPORTUNITIES</p><h2>Interested in a specific software project?</h2>
  <p>Multiverse can discuss an existing software component, technology acquisition, or a clearly scoped adaptation where the requirements, available technology and responsibilities can be agreed in advance.</p>
  <a class="sw-button sw-primary" href="{url('contact/')}">Contact Multiverse</a>
</div><div class="sw-commercial-steps"><p>A USEFUL INQUIRY EXPLAINS</p><span>The existing task or process</span><span>What software or data is involved</span><span>The result the business needs</span></div></div></section>
<section class="sw-other" id="industrial-assets"><div class="container sw-other-layout">
  <img src="{url('assets/portfolio/forklift.webp')}" width="640" height="360" alt="A 3D model of an industrial forklift" loading="lazy">
  <div><p class="sw-kicker">A SEPARATE PRODUCT CATEGORY</p><h2>Industrial 3D models and animations</h2><p>Multiverse also publishes downloadable 3D models of machinery and warehouse equipment for use in visualizations and digital scenes. These have their own listings and are not connected to the Wix application or KnowMoreDiRT.</p><a class="sw-textlink" href="{url('3d/')}">Browse the 3D product catalog <span aria-hidden="true">↗</span></a></div>
</div></section>
</main>'''

source = (ROOT / 'index.html').read_text()
start = source.index('<main id="main">')
end = source.index('</main>', start) + len('</main>')
source = source[:start] + main + source[end:]
source = re.sub(r'<title>.*?</title>', '<title>Multiverse | Independent Software, AI Research & Digital Products</title>', source, count=1)
source = re.sub(r'<meta content="[^"]*" name="description"/>', '<meta content="Multiverse is an independent development business with a published Wix Stores order-monitoring application, AI document-search research, software engineering, and separate 3D digital assets." name="description"/>', source, count=1)
source = re.sub(r'<meta content="[^"]*" property="og:description"/>', '<meta content="Learn what Multiverse builds, who each project is for, and which software is published versus experimental." property="og:description"/>', source, count=1)
(ROOT / 'index.html').write_text(source)
from render_software_portfolio import replace_home
replace_home()
print('Rebuilt homepage from verified source status: Wix published, KMD prototype, 3D separate')
