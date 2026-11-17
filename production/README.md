# Multiverse: real demonstration video production

Commercial priority and owner goals are in `/data/infra/docs/guidelines/agents/owner_commercial_goals_and_agent_priorities.md`. Cross-chat state, correct URLs, rights/privacy, and project mapping are in `/data/infra/docs/guidelines/projects/multiverse_business_website_and_video_handover_2026-11-17.md`. These are project production source files, not completed demonstration videos. No public website copy should imply these assets were captured before they actually exist.

## Exact production sequence

1. Verify the current source application and active agents, resource broker, and read-only operational status. Coordinate with the project agent using Raspi exchange. Do not stop current KMD indexing or hijack the one owner automation browser tab.
2. Create a small safe demonstration corpus or sandbox: public-domain or personally authored documents for knowledge queries, synthetic/test orders for Wix, and non-destructive sandbox accounts for browser automation. Never display owner accounts, customer records, credentials, internal infrastructure addresses, licensed book pages, unpublished intellectual property or proprietary data.
3. Record **actual functioning software**, ideally at 1920×1080 with cursor, no desktop notifications, large fonts and readable selections. Capture source version, UTC time, test prompt, expected evidence, result and limitations before editorial cuts. Keep unedited source footage privately outside Git, e.g. `/data/var/multiverse-media/source-recordings/`; never publish raw internal logs.
4. Apply the scene-by-scene scripts below only when matching observed behavior. Use AI-video generation for title cards, transitions or clearly conceptual diagrams, never as a substitute for real product behavior. Avoid fake testimonials, results, client names or non-working UI.
5. Use `scripts/prepare_demo_clip.sh INPUT.mp4 SLUG START_SECONDS DURATION_SECONDS OUTPUT_DIR` for a compact, silent proof clip, and a thumbnail poster. Review before embedding. Preserve source recordings and attribution privately.
6. Create one page/video per capability plus a homepage teaser. The existing site is live at `https://hanspeterradtke.github.io/multiverse-ai-website/`. Videos require a suitable external host or CDN; do not assume GitHub Pages is ideal for large media. Test autoplay muted, controls, captions, mobile layout, reduced motion, bandwidth and accessibility. Do not publish placeholders presented as evidence.

## Acceptance criteria

Each release must show a reproducible working test, identifiable real input, meaningful output, citations or confirmation evidence, correct status (prototype vs published product), no leaked sensitive material, no fabricated performance or revenue claims, signed-off publication rights, correct mobile and desktop playback, accessible captions, and a visible business inquiry CTA. For anything involving a future customer, support/licensing contracts remain case-specific and optional.

## Deliverables and scripts

- `knowmoredirt.md` — real retrieval walkthrough, source attribution, optional indexing progress.
- `autonomous-agents.md` — browser/agent automation, verification and controlled recovery.
- `late-order-monitor.md` — real Wix app behavior in a test store and read-only limits.
- `hero-loop.md` — cinematic brand teaser built from approved captured footage and conceptual transitions.
- `../scripts/prepare_demo_clip.sh` — ffmpeg encoding/poster helper, tested with a disposable local fixture, not actual footage.

Use the reusable clip materials on the website, LinkedIn Featured, serious B2B outreach and presentations. The **purpose is commercial proof and qualified inquiries**, not maximizing views or making entertainment videos.
