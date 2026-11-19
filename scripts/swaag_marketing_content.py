"""Marketing copy grounded in SWAAG README, docs/manual.md, docs/design-principles.md.

The audience is developers using self-hosted AI, NOT a promised turnkey enterprise product.
"""

def section(compact=False):
    if compact:
        return '''<section class="mv-swaag-spotlight mv-swaag-compact" id="swaag">
          <div class="container"><div class="mv-swaag-title"><p class="mv-projects-eyebrow">FEATURED OPEN-SOURCE AI AGENT FRAMEWORK</p><h2>SWAAG: when AI needs to use tools, not just talk.</h2><p>For developers already working with local AI models who want a foundation for assistants that can handle multi-step computer tasks.</p></div>
          <div class="mv-swaag-actions"><a class="mv-primary-link" href="https://github.com/HansPeterRadtke/swaag" target="_blank" rel="noopener noreferrer">Explore the SWAAG source code</a><a class="mv-github-link" href="/multiverse-ai-website/#swaag">See an example and the intended benefit <span aria-hidden="true">↗</span></a></div></div>
        </section>'''
    return '''<section class="mv-swaag-spotlight" id="swaag">
      <div class="container mv-swaag-title"><p class="mv-projects-eyebrow">FEATURED PROJECT · OPEN-SOURCE AI AGENT FRAMEWORK</p><h2>When an AI assistant needs to <em>do more than chat.</em></h2><p><strong>SWAAG</strong> is a local-first framework for building AI agents that can use tools, coordinate substantial tasks and keep a durable record of what happened.</p></div>
      <div class="container mv-swaag-whenhow"><div class="mv-swaag-need"><span>WHEN WOULD YOU NEED IT?</span><h3>You run an AI model, but the work also involves files, programs and many steps.</h3><p>For example, a developer wants an assistant to inspect project files, use permitted commands or APIs, run checks and report what succeeded. A chatbot answering questions alone does not provide the entire workflow.</p><strong>For developers, technical teams and builders of private AI tools.</strong></div>
      <div class="mv-swaag-process"><span>WHAT SWAAG PROVIDES</span><div><b>1</b><p><strong>Describe a task</strong><small>A persistent controller handles the conversation instead of forcing the user to manage separate agents.</small></p></div><div><b>2</b><p><strong>Use tools and workers</strong><small>Configured capabilities can interact with files, software tools and specialized task workers.</small></p></div><div><b>3</b><p><strong>Inspect progress and results</strong><small>Durable history and task state support progress reporting, recovery and verification.</small></p></div></div></div>
      <div class="container mv-swaag-bottom"><div><strong>What could this help you build?</strong><p>A tool-using AI assistant without writing orchestration, task history and worker management from scratch. Its local-first design can suit teams running their own models and tools.</p><p class="mv-swaag-status">Real open-source implementation; still in development. No promise of unattended production reliability, guaranteed time savings or suitability for every organization.</p></div><div class="mv-swaag-actions"><a class="mv-primary-link" href="https://github.com/HansPeterRadtke/swaag" target="_blank" rel="noopener noreferrer">Inspect the SWAAG source code <span aria-hidden="true">↗</span></a><a class="mv-github-link" href="https://github.com/HansPeterRadtke/swaag/blob/main/docs/manual.md" target="_blank" rel="noopener noreferrer">Read the implementation manual <span aria-hidden="true">↗</span></a></div></div>
    </section>'''


def small_proof():
    return '''<section class="mv-source-proof" id="engineering"><div class="container mv-source-proof-layout">
      <div><p class="mv-projects-eyebrow">MORE SOURCE-BACKED WORK</p><h2>Real code, not just technology claims.</h2><p>Other public projects include <strong>all2text</strong> for preparing mixed file collections, <strong>Android software</strong> such as the Voice Button recorder, and <strong>Unity packages</strong> for reusable game systems. Each serves a different user; they are not one bundled product.</p></div>
      <div class="mv-source-proof-links"><a class="mv-primary-link" href="/multiverse-ai-website/technology/#other-projects">Explore the software portfolio</a><a class="mv-github-link" href="https://github.com/HansPeterRadtke" target="_blank" rel="noopener noreferrer">Inspect my public GitHub code <span aria-hidden="true">↗</span></a></div>
    </div></section>'''


def hero_link():
    return '''<a class="mv-hero-swaag-link" href="#swaag"><span>FEATURED OPEN-SOURCE AI AGENT SYSTEM</span><strong>SWAAG: a framework for agents that use real computer tools</strong><small>When you need more than a chatbot <span aria-hidden="true">↗</span></small></a>'''
