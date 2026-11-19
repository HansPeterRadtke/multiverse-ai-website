# SWAAG positioning: checked alternatives and claim boundaries (2026-11-19)

This is a marketing claim-control document, not a benchmark or a recommendation that a prospective user prefers SWAAG. Sources were reviewed against current public docs on November 19, 2026. The purpose is to avoid inventing uniqueness, sales ROI, or false competitor weaknesses.

## Competitive alternatives and overlap

- **LangGraph**: official [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) describes a low-level runtime for stateful, long-running agents with durable execution, streaming, and human-in-the-loop controls. It is therefore misleading to claim that SWAAG alone supports stateful agents or iterative workflows.
- **Temporal**: [Durable AI docs](https://docs.temporal.io/ai) and [reference architecture](https://go.temporal.io/platform-hub/ai-engineering/ai-reference-architecture) describe long-running, durable AI workflows, tools, orchestrator state, retries, approvals, and inspectable workflow history. Do not call SWAAG the only persistent agent runtime.
- **OpenAI Agents SDK**: official [agents documentation](https://openai.github.io/openai-agents-python/agents/), [tracing documentation](https://openai.github.io/openai-agents-python/tracing/) and [non-OpenAI model options](https://openai.github.io/openai-agents-python/models/) include tools, handoffs, guardrails, sessions, tracing, and configurable non-OpenAI or OpenAI-compatible backends. Do not claim either observability or model portability is unique to SWAAG.
- **Microsoft Agent Framework Durable Extension**: [official docs](https://learn.microsoft.com/en-us/agent-framework/hosting/azure-functions) describe checkpoints, multi-agent orchestration, failure recovery and self-hosted hosting options; no claim that SWAAG is categorically the only private/self-hosted alternative.
- **Haystack**: [official source](https://github.com/deepset-ai/haystack) describes modular tool-using agents, context engineering, memory, pipeline workflows and provider-independent use. Do not claim generic tool support or context management is a novel category.
- **Temporal Agent Harness**: [community project](https://github.com/temporal-community/temporal-agent-harness) is another durable, composable agent harness. Even the name "harness" and human approval features are not distinct market differentiators.

## Honest positioning for SWAAG

SWAAG is a small, public, MIT-licensed, local-first Python framework developed by Hans-Peter Radtke. Its current public README and `docs/design-principles.md` describe a persistent orchestrator as the sole ordinary human conversation layer, optional worker delegation, exact bounded context accounting, source-backed semantic history projections, executable tool boundaries, durable event history and provider-specific capability discovery. The architecture explicitly assigns meaning-based choices to the model and exact/mechanical checks to deterministic code.

These *design choices and concrete public code* are what prospective developers can assess. Whether these choices provide a measurable advantage for a given application over competing frameworks remains unproven. Project version in public `pyproject.toml` is 0.1.0 and no GitHub Releases were visible at the time of review. The project is not claimed to be a turnkey service or enterprise-certified solution.

## Meaningful user situations, not fabricated examples

**Engineering team with local AI model and tools**: a developer wants to experiment with controlling a multistep workflow involving files, tests, commands, APIs and verification. Instead of assembling every layer of a framework, the developer could evaluate SWAAG's orchestrator, tool boundaries and event history. This is *a hypothetical buyer scenario*, not an actual paying user or proven time savings.

**Technical group integrating its own assistant frontends**: its app uses speech or chat input and wants one canonical control layer that can decide when to start a worker rather than letting the frontend route work. SWAAG's public README documents that entry contract. This is an engineering architecture use case, not a completed certified client app.

**Company investigating self-managed tool execution**: some teams prefer or require control over local models and deployment. SWAAG supports local llama.cpp-backed use; security, data residency, compliance and reliability depend on actual deployment and cannot be promised by a repository or licence.

## Commercial rights, evidence, and call to action

SWAAG is licensed MIT; anyone can already use the public code on those terms, including commercial use subject to the license. It is inaccurate to offer those published rights as exclusive property for purchase. A *different* technology acquisition, owned add-on, or separately agreed bounded implementation would need verified rights, scope, terms, and independent commercial authorization.

The GitHub README, manual, code, and tests are the proof of implementation. Proof of enterprise suitability would require a relevant environment, competing baselines, repeated task tests, failure recovery evidence, safety review and acceptance criteria. Do not invent customer logos, testimonials, verified buyer ROIs or benchmark victories.

## Website direction

The homepage provides a quick SWAAG use case and GitHub link. The dedicated `/swaag/` page explains who needs this, the envisioned usage, what SWAAG actually implements, current limitations, public MIT rights, and developer proof. The general Software & AI page retains the broader portfolio. Internal pages should expose accurate canonical URLs and sitemap entries so someone searching for relevant agent runtime concepts can find the page.
