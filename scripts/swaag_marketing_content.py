"""Buyer-oriented SWAAG descriptions grounded in current public source code.

Audience: engineering/technology teams considering tools, not consumers buying a
turnkey AI assistant. Sources: README.md, docs/design-principles.md,
docs/manual.md, LICENSE and tests in public HansPeterRadtke/swaag. Marketing
research evidence is documented separately. Do not fabricate past customers.
"""


def section(compact=False):
    if compact:
        return '''<section class="mv-swaag-spotlight mv-swaag-compact" id="swaag">
          <div class="container"><div class="mv-swaag-title">
            <p class="mv-projects-eyebrow">SWAAG · OPEN-SOURCE AI AGENT RUNTIME</p>
            <h2>Already running an AI model? What if it needs to use your tools?</h2>
            <p>SWAAG is a framework for developers building assistants that work with software tools, coordinate multi-step tasks and preserve inspectable task state. It is a starting point for an integration, not a ready-to-use business assistant.</p>
          </div><div class="mv-swaag-actions"><a class="mv-primary-link" href="/multiverse-ai-website/#swaag">See the use case and benefits</a><a class="mv-github-link" href="https://github.com/HansPeterRadtke/swaag" target="_blank" rel="noopener noreferrer">Inspect SWAAG code <span aria-hidden="true">↗</span></a></div></div>
        </section>'''
    return '''<section class="mv-swaag-spotlight" id="swaag">
      <div class="container mv-swaag-title">
        <p class="mv-projects-eyebrow">FEATURED OPEN-SOURCE PROJECT · SWAAG</p>
        <h2>Your AI can answer questions. <em>Can it handle the work?</em></h2>
        <p>SWAAG is software for developers who want to connect an AI model with real programs, files and other tools. Its aim is to provide the agent infrastructure needed to manage tasks with multiple steps and preserve evidence of what happened.</p>
      </div>
      <div class="container mv-swaag-whenhow">
        <div class="mv-swaag-need">
          <span>THE SITUATION</span>
          <h3>Your engineering team runs a local AI model. A useful task needs more than a chat response.</h3>
          <p>Imagine asking an assistant to help investigate a software change. The work may involve examining files, using permitted developer tools, running tests, analyzing errors and reporting the outcome. A language model alone does not provide reliable access, coordination or durable task records.</p>
          <strong>Intended users: developers and engineering teams building their own AI-enabled workflows.</strong>
          <small class="mv-swaag-scenario-note">Illustrative use case, not a claimed customer deployment or a proven autonomous code-change demonstration.</small>
        </div>
        <div class="mv-swaag-process">
          <span>THE INFRASTRUCTURE SWAAG PROVIDES</span>
          <div><b>1</b><p><strong>One entry point for the task</strong><small>A persistent orchestrator decides whether and how substantive work needs workers.</small></p></div>
          <div><b>2</b><p><strong>Workers with configured tool access</strong><small>Agent workers can call permitted capabilities, including external integrations, instead of merely describing actions.</small></p></div>
          <div><b>3</b><p><strong>Inspectable state and progress</strong><small>Durable events, task state and recovery mechanisms provide a basis for seeing what happened and checking work.</small></p></div>
        </div>
      </div>
      <div class="container mv-swaag-outcomes">
        <div><span>WHY THIS MAY BE USEFUL</span><h3>Start with an agent foundation rather than building the infrastructure from zero.</h3><p>For teams already running local models, SWAAG offers implemented building blocks for tool orchestration, long-lived work and task records. That could make developing a controlled AI workflow more practical, but real results depend on the connected models, tools and tests.</p></div>
        <div><span>WHAT MAKES IT WORTH INSPECTING?</span><h3>The implementation is public.</h3><p>Read the source, setup manual and tests instead of relying on marketing promises. SWAAG is MIT-licensed open-source software; the code is available free under that license, and it is not being advertised as an exclusive product for sale.</p></div>
      </div>
      <div class="container mv-swaag-bottom">
        <div><strong>Current status</strong><p>A real, evolving developer framework—not a turnkey employee, a ready-made corporate deployment or a guarantee of reliable unattended task completion.</p><p class="mv-swaag-status">No verified customer time savings, benchmark superiority or enterprise certification is claimed.</p></div>
        <div class="mv-swaag-actions"><a class="mv-primary-link" href="https://github.com/HansPeterRadtke/swaag" target="_blank" rel="noopener noreferrer">Examine SWAAG on GitHub <span aria-hidden="true">↗</span></a><a class="mv-github-link" href="https://github.com/HansPeterRadtke/swaag/blob/main/docs/manual.md" target="_blank" rel="noopener noreferrer">Read the manual <span aria-hidden="true">↗</span></a><a class="mv-github-link" href="/multiverse-ai-website/opportunities/">Discuss a separate technology opportunity <span aria-hidden="true">↗</span></a></div>
      </div>
    </section>'''


def small_proof():
    return '''<section class="mv-source-proof" id="engineering"><div class="container mv-source-proof-layout">
      <div><p class="mv-projects-eyebrow">IMPLEMENTATION EVIDENCE</p><h2>You can inspect the actual work.</h2><p>GitHub contains the source of SWAAG, <strong>all2text</strong> for preparing mixed file collections, <strong>Android applications</strong>, <strong>Unity packages</strong> and other tools. Each project has a different purpose and status. Public code is evidence of engineering work—not a guarantee that it is a finished commercial product.</p></div>
      <div class="mv-source-proof-links"><a class="mv-primary-link" href="https://github.com/HansPeterRadtke" target="_blank" rel="noopener noreferrer">Browse public source code</a><a class="mv-github-link" href="/multiverse-ai-website/technology/#other-projects">See the other projects and their uses <span aria-hidden="true">↗</span></a></div>
    </div></section>'''


def hero_link():
    return '''<a class="mv-hero-swaag-link" href="#swaag"><span>FLAGSHIP OPEN-SOURCE DEVELOPMENT PROJECT</span><strong>SWAAG — AI agents that can work with computer tools</strong><small>Why a developer might need it <span aria-hidden="true">↗</span></small></a>'''
