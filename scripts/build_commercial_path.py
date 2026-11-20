#!/usr/bin/env python3
"""Buyer-first, evidence-backed commercial and contact pages.

The contact form only builds a mailto draft on the visitor's device; no
third-party data collection, quote, or account-side action is implied.
"""
from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
base='/multiverse-ai-website/'

def render(path,markup,title,description):
    p=R/path
    soup=BeautifulSoup(p.read_text(),'html.parser')
    target=soup.select_one('main#main')
    assert target is not None,path
    new=BeautifulSoup(markup,'html.parser').select_one('main#main')
    assert new is not None,path
    target.replace_with(new)
    soup.title.string=title
    desc=soup.find('meta',attrs={'name':'description'})
    assert desc is not None,path
    desc['content']=description
    style=base+'assets/commercial-path.css'
    if not soup.select_one(f'link[href="{style}"]'):
        soup.head.append(soup.new_tag('link',href=style,rel='stylesheet'))
    p.write_text(str(soup).rstrip()+'\n')
    print('WROTE',path)

business='''<main id="main" class="cp-business">
  <section class="cp-hero container" id="top"><p class="cp-eyebrow">MULTIVERSE / COMMERCIAL TECHNOLOGY</p>
    <h1>Have a defined software problem—or need an existing technology component?</h1>
    <p class="cp-lead">Multiverse develops independent software, AI infrastructure and tools. A useful first conversation is about the problem, what you already use, and what a successful result would look like. Potential arrangements are considered individually, with clear scope and responsibilities.</p>
    <div class="cp-actions"><a class="cp-action cp-primary" href="#situations">See relevant situations</a><a class="cp-action cp-outline" href="/multiverse-ai-website/contact/">Describe your problem</a></div>
  </section>
  <section class="cp-situations" id="situations"><div class="container">
    <div class="cp-section-intro"><p class="cp-eyebrow">POTENTIAL FIT</p><h2>Three situations worth discussing.</h2><p>These are illustrative situations, not claims about completed customer contracts. Each should be evaluated against the actual software and technical constraints.</p></div>
    <div class="cp-situation-grid">
      <article><span class="cp-situation-type">AI SYSTEMS / DEVELOPMENT TEAMS</span><h3>Your AI model needs to work with tools.</h3><p>You already operate an AI model. To make it useful for longer work, it must interact with permitted tools, preserve task state and report what actually happened.</p><div class="cp-path-result"><strong>What could be evaluated?</strong><p>The open-source SWAAG agent runtime and whether a separately scoped component or adaptation is appropriate for your systems.</p></div><a href="/multiverse-ai-website/swaag/">Understand SWAAG and its limitations <span aria-hidden="true">↗</span></a></article>
      <article><span class="cp-situation-type">DATA & TESTING WORKFLOWS</span><h3>Your team repeats fragile manual steps.</h3><p>Files arrive in different formats, checks involve several tools, or engineers repeatedly prepare the same data before testing or analysis.</p><div class="cp-path-result"><strong>What could be evaluated?</strong><p>A reusable processing or test-automation component with defined inputs, outputs, checks and an agreed handover.</p></div><a href="https://github.com/HansPeterRadtke/all2text" target="_blank" rel="noopener noreferrer">See existing file-processing code <span aria-hidden="true">↗</span></a></article>
      <article><span class="cp-situation-type">TECHNOLOGY BUYERS / PARTNERS</span><h3>You need suitable technology without rebuilding everything.</h3><p>A reusable software component might be a better starting point than commissioning an entirely new system.</p><div class="cp-path-result"><strong>What could be evaluated?</strong><p>Owned components, potential technology transfer or licensing, and the required rights, responsibilities and acceptance criteria.</p></div><a href="/multiverse-ai-website/technology/#other-projects">Review the existing project portfolio <span aria-hidden="true">↗</span></a></article>
    </div>
  </div></section>
  <section class="cp-visual-proof" id="automation-evidence"><div class="container cp-visual-proof-grid"><div class="cp-visual-proof-photo"><img src="/multiverse-ai-website/assets/3d/agent-made/warehouse-exterior.webp" alt="Actual Blender Cycles render of an industrial warehouse, produced through agent-directed Blender and Python workflows" width="1600" height="900" loading="lazy"/><span>GENUINE EDITABLE BLENDER SCENE · NOT GENERATED CONCEPT ART</span></div><div class="cp-visual-proof-copy"><p class="cp-eyebrow">TANGIBLE AUTOMATION ENGINEERING</p><h2>See AI operating real production tools.</h2><p>My multi-machine system uses AI-directed Blender and Python workflows to build and animate industrial geometry, render original scenes and check the resulting files. The image is one real output—evidence of software operating tools rather than simply describing what to do.</p><p class="cp-visual-proof-status">Its workflow and technical receipts are inspectable. Some scenes still need realism improvements, and no unattended production-rate or cost-saving guarantee is claimed.</p><a class="cp-action cp-primary" href="/multiverse-ai-website/3d/">Explore the AI production system</a></div></div></section>
  <section class="cp-distinction"><div class="container cp-distinction-grid"><div><p class="cp-eyebrow">A CRITICAL DISTINCTION</p><h2>Open-source code and commercial agreements are different things.</h2><p>SWAAG is publicly available under the MIT license. Its published code can already be used under those terms; it is not being sold as an exclusive asset.</p><p>Other owned technology, additional deliverables or a defined adaptation could be discussed separately—but only after checking the rights, technical fit, scope, and handover obligations.</p></div><div class="cp-distinction-links"><a href="https://github.com/HansPeterRadtke/swaag" target="_blank" rel="noopener noreferrer">Inspect free SWAAG source code <span aria-hidden="true">↗</span></a><a href="/multiverse-ai-website/technology/">See what other software exists <span aria-hidden="true">↗</span></a></div></div></section>
  <section class="cp-process container"><div class="cp-section-intro"><p class="cp-eyebrow">A LOW-FRICTION FIRST STEP</p><h2>Tell me enough to judge whether there is a fit.</h2><p>A short description is sufficient. There is no need to send confidential project materials or negotiate a budget before discussing the underlying problem.</p></div>
    <div class="cp-process-grid"><div><span>01 / CURRENT SITUATION</span><strong>What task or process is difficult today?</strong><p>For example, a workflow spanning multiple internal applications or an AI integration that cannot reliably use its tools.</p></div><div><span>02 / DESIRED RESULT</span><strong>What would success look like?</strong><p>A defined output, accepted test, working component or measurable handover—rather than an open-ended staffing request.</p></div><div><span>03 / CONSTRAINTS</span><strong>Which systems or restrictions matter?</strong><p>Mention relevant software, interfaces or timing if known. Budget and contract details can come later if the project is relevant.</p></div></div>
    <div class="cp-process-actions"><a class="cp-action cp-primary" href="/multiverse-ai-website/contact/">Write a short inquiry</a><a class="cp-text-link" href="/multiverse-ai-website/about/">Learn more about the developer <span aria-hidden="true">↗</span></a></div>
    <p class="cp-note">These are potential discussions, not promises of immediate availability, guaranteed performance, or ongoing support. Responsibilities and deliverables must be established case by case.</p>
  </section>
</main>'''

contact='''<main id="main" class="cp-contact">
  <section class="cp-hero container" id="top"><p class="cp-eyebrow">CONTACT MULTIVERSE</p><h1>What software or technology problem are you trying to solve?</h1>
    <p class="cp-lead">Explain the current situation and the outcome you need. A short initial note is enough to decide whether the existing technology or a clearly bounded project might fit.</p>
  </section>
  <section class="cp-contact-section"><div class="container cp-contact-grid">
    <div class="cp-contact-aside"><p class="cp-eyebrow">START WITH THE PROBLEM</p><h2>Two or three sentences are enough.</h2><p>Helpful details include what happens today, what makes it difficult, and what a successful result would change. You can mention software or interfaces involved, but don't send private data or source code.</p>
      <div class="cp-contact-example"><span>EXAMPLE OF A USEFUL QUESTION</span><p>“We run a local language model, but need it to carry out a defined workflow using our development tools. Could your existing work be relevant?”</p><small>Illustrative inquiry only—not a real customer testimonial or confirmed engagement.</small></div>
      <div class="cp-direct-contact"><span>DIRECT EMAIL</span><a href="mailto:multiverse3dhpr@gmail.com?subject=Multiverse%20technology%20inquiry">multiverse3dhpr@gmail.com</a><small>This also works without using the form.</small></div>
    </div>
    <form class="inquiry-form cp-simple-form" id="inquiry-form"><p class="cp-form-title">Prepare an introductory email</p><p class="form-intro">The website does not collect or send your information. This opens a draft in your own email app; you review it and choose Send there.</p>
      <div class="form-row"><label>Contact name<input autocomplete="name" maxlength="120" name="name" placeholder="Your name" required type="text"></label><label>Reply email<input autocomplete="email" maxlength="200" name="email" placeholder="you@company.com" required type="email"></label></div>
      <label>Company (optional)<input autocomplete="organization" maxlength="160" name="company" placeholder="Company or organization" type="text"></label>
      <label>What is the problem, and what result do you need?<textarea maxlength="2100" name="problem" placeholder="A short description of the task, current difficulty, and desired outcome" required rows="6"></textarea></label>
      <label>Relevant tools or systems (optional)<input maxlength="260" name="systems" placeholder="For example: local AI, Python, APIs, test equipment" type="text"></label>
      <p class="cp-form-privacy">Please don't include passwords, personal records, confidential documents, proprietary source code, or other sensitive information in this first email. See the <a href="/multiverse-ai-website/privacy/">privacy policy</a>.</p>
      <button class="cp-action cp-primary cp-form-submit" type="submit">Prepare email in my mail app <span aria-hidden="true">↗</span></button><p aria-live="polite" class="form-status" id="form-status" role="status"></p>
    </form>
  </div></section>
</main>'''

render('opportunities/index.html',business,'Commercial Technology Opportunities | Multiverse','Discuss well-defined software technology opportunities: AI agents using tools, repeatable data and testing workflows, or a separately scoped software component. Understand what is open source and what could be agreed commercially.')
render('contact/index.html',contact,'Contact Multiverse | Discuss a Software Problem','Contact Multiverse about a specific software or technology challenge. Describe the current task and desired outcome, review an email draft, and send from your own mail application.')
