"""User-focused SWAAG positioning from Infra source rules and owner recordings.

Semantic role boundary: the human-facing orchestrator remains available while
workers run. Configurable idle modes do not imply enabled 24/7 autonomous work.
"""


def section(compact=False):
    if compact:
        return '''<section class="mv-swaag-spotlight mv-swaag-compact" id="swaag">
        <div class="container"><div class="mv-swaag-title">
          <p class="mv-projects-eyebrow">SWAAG · ORCHESTRATED AI WORKERS</p>
          <h2>One assistant to talk to. Multiple workers to manage the work.</h2>
          <p>A persistent orchestrator keeps the conversation separate from tool-heavy jobs. Workers carry out longer tasks while the manager tracks progress, questions, resources and history. Optional authorized background continuation is configurable rather than always on.</p>
        </div><div class="mv-swaag-actions"><a class="mv-primary-link" href="/multiverse-ai-website/swaag/">See how SWAAG organizes work</a><a class="mv-github-link" href="https://github.com/HansPeterRadtke/swaag" target="_blank" rel="noopener noreferrer">Inspect source code <span aria-hidden="true">↗</span></a></div></div>
        </section>'''
    return '''<section class="mv-swaag-spotlight" id="swaag">
      <div class="container mv-swaag-title">
        <p class="mv-projects-eyebrow">SWAAG · SELF-HOSTED AUTONOMOUS AGENT FRAMEWORK</p>
        <h2>Keep talking to your assistant. <em>Let the workers do the work.</em></h2>
        <p>With SWAAG, the intended experience is one persistent assistant acting as a team leader. It delegates longer work to background agents, coordinates independent and dependent tasks, and keeps their state and history available when you return.</p>
      </div>
      <div class="container mv-swaag-whenhow">
        <div class="mv-swaag-need">
          <span>THE USER'S PROBLEM</span>
          <h3>Why should you have to supervise every agent individually?</h3>
          <p>Imagine several software projects needing investigation, tests, documentation and follow-up. You want to ask what is running, add another job, change priorities, or stop one worker without losing the progress of the others.</p>
          <strong>The goal is to manage outcomes from one conversation, not babysit a collection of agent windows.</strong>
          <small class="mv-swaag-scenario-note">Illustrative use case. A fully autonomous 24/7 deployment and measured saved operator time are not claimed.</small>
        </div>
        <div class="mv-swaag-process">
          <span>THE ORCHESTRATED WORKFLOW</span>
          <div><b>1</b><p><strong>One responsive conversation</strong><small>The persistent user-facing orchestrator answers status questions and receives new instructions while workers have their own lifecycles.</small></p></div>
          <div><b>2</b><p><strong>Workers and dependencies</strong><small>Separate jobs can be delegated, scheduled, run concurrently where resources permit, and connected when one result is needed by another.</small></p></div>
          <div><b>3</b><p><strong>Durable memory and control</strong><small>Source events, task status, notes and context projections support inspection and recovery without relying only on the model's current context window.</small></p></div>
        </div>
      </div>
      <div class="container mv-swaag-outcomes">
        <div><span>THE PRACTICAL BENEFIT</span><h3>Stay available for decisions while the detailed work continues.</h3><p>Inspect a worker's progress, reprioritize a task or ask another question without treating each worker as a separate chatbot. SWAAG's event records also provide a basis for history analysis, notes and contextual recall instead of losing everything when a model context fills up.</p></div>
        <div><span>CONTINUATION, WITH USER CONTROL</span><h3>Approved work can persist beyond one conversation.</h3><p>Durable worker plans and wakeups support authorized backlogs and an optional autonomous-continue mode. Those modes are deliberate configuration choices; automatic background dispatch is disabled by default. Notes, history analysis and self-improvement are ongoing engineering objectives, not guaranteed unattended services.</p></div>
      </div>
      <div class="container mv-swaag-bottom">
        <div><strong>Implementation and current boundaries</strong><p>SWAAG is a real MIT-licensed, local-first Python framework with public orchestrator, worker, scheduler and history code. It remains an evolving developer system: the quality of any autonomous result depends on the models, permissions, tools, configuration and verification.</p><p class="mv-swaag-status">No claim of universal reliability or tested superiority over Codex, Claude Code, Dots or other agent frameworks.</p></div>
        <div class="mv-swaag-actions"><a class="mv-primary-link" href="/multiverse-ai-website/swaag/">Explore SWAAG's architecture</a><a class="mv-github-link" href="https://github.com/HansPeterRadtke/swaag" target="_blank" rel="noopener noreferrer">Read the actual source <span aria-hidden="true">↗</span></a><a class="mv-github-link" href="/multiverse-ai-website/opportunities/">Discuss a separate technology opportunity <span aria-hidden="true">↗</span></a></div>
      </div>
    </section>'''


def small_proof():
    return '''<section class="mv-source-proof" id="engineering"><div class="container mv-source-proof-layout">
      <div><p class="mv-projects-eyebrow">SOURCE CODE, NOT A GENERIC AI CLAIM</p><h2>You can inspect the real engineering.</h2><p>Alongside SWAAG and KnowMoreDiRT, public repositories contain <strong>all2text</strong> for preparing mixed files, <strong>Android software</strong>, <strong>Unity packages</strong> and other focused tools. Public code is evidence of implementation—not a guarantee of commercial readiness.</p></div>
      <div class="mv-source-proof-links"><a class="mv-primary-link" href="https://github.com/HansPeterRadtke" target="_blank" rel="noopener noreferrer">Browse the GitHub code</a><a class="mv-github-link" href="/multiverse-ai-website/technology/#other-projects">Explore the projects and their uses <span aria-hidden="true">↗</span></a></div>
    </div></section>'''


def hero_link():
    return '''<a class="mv-hero-swaag-link" href="#swaag"><span>FLAGSHIP PROJECT · BACKGROUND AGENT ORCHESTRATION</span><strong>SWAAG — one manager, multiple background workers</strong><small>Work keeps its state while you keep control <span aria-hidden="true">↗</span></small></a>'''
