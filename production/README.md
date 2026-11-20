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

## KnowMoreDiRT visual showroom and local generator admission (November 18, 2026)

The first fully editable KMD architecture deck, icon mark, seven rendered slide previews and PDF have been **created with the installed PPT Master on Jetson** and published to `https://hanspeterradtke.github.io/multiverse-ai-website/kmd/`. The authoritative public assets and visual viewer are in `assets/kmd/` and `kmd/index.html`. Page and downloadable PPTX/PDF returned HTTP 200 after the GitHub Pages deployment. These are **architectural illustrations, not live application screenshots**. Project docs were read from the canonical KMD repository and active Raspi worktree. Current source-backed implementation is distinct from planned cross-chunk identity and discourse improvements. The created source PPT Master workspace is on Jetson at `/data/var/ppt-master/workspaces/kmd-visual-20261117_ppt169_20261117`, not an Infra report.

The owner also has local AI image and video model assets, including Z-Image Turbo BF16 on Thor, Wan2.1 family on Thor, and HunyuanVideo 1.5 on Jetson. **Presence of weights does not mean an active service or available memory.** On November 18, Thor's read-only resource broker returned `must_queue_or_free_capacity` for an 18 GiB image job. Existing LLM/voice processes were not stopped. A guarded image-generation recipe is versioned as `scripts/kmd_zimage_concepts.py` and mirrored on Thor at `/data/var/multiverse-kmd/kmd_zimage_concepts.py`. Its dry-run successfully checked the live broker and emitted exact prompt identities. It blocks unsafe rendering until an actual broker reservation is confirmed, sufficient unified memory exists, and the installed Diffusers/PyTorch pipeline imports successfully. **No generated KMD Z-Image images or HunyuanVideo clips were produced.** Once capacity is available and the model stack passes import tests, run a controlled single concept first, review the image before publication, then consider tasteful backgrounds, transitions and true KMD footage. Never preempt the running owner's models for promotional artwork.

## Nitro local Z-Image Turbo — working render path (18 November 2026)

**Successfully rendered two distinct KMD conceptual images** on Nitro (NVIDIA RTX 3060 Laptop GPU, 6 GiB nominal VRAM), without unloading other services. Saved originals and metadata in `/data/var/multiverse-kmd/zimage-nitro/`. The render used the local ~20 GiB Z-Image Turbo BF16 model, *sequential CPU/GPU offload*, 768×448 pixels, six inference steps, and a 4-thread bound. CPU RAM stayed safely above the guard threshold. Actual results are embedded, with honest concept-art captions, in `/kmd/`; the homepage KMD card also uses the context image.

Earlier attempts failed due to **shared Nitro Python dependency versions**, not model absence. The shared environment was deliberately not modified. An isolated dependency overlay was established at `/data/var/multiverse-kmd/zimage-nitro/venv/lib/python3.12/site-packages` with `transformers==4.51.3`, `tokenizers==0.21.4`, and `onnxruntime==1.22.1`. The existing shared `/data/venv/bin/python` supplies CUDA PyTorch and Diffusers; prepend the isolated overlay with `PYTHONPATH` when launching. This resolved both the missing `Qwen3Model` import and the old ONNX Runtime / NumPy 2 ABI issue. Never change the shared /data/venv just to reproduce this job.

**Reproducible command** (requires a *currently granted* Raspi central GPU-broker reservation that covers approximately two GiB GPU and adequate host RAM; the script does not obtain or renew its own lease):

```bash
export PYTHONPATH=/data/var/multiverse-kmd/zimage-nitro/venv/lib/python3.12/site-packages
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export TOKENIZERS_PARALLELISM=false
/data/venv/bin/python scripts/kmd_zimage_nitro.py --dry-run --concept context-chambers
nice -n 15 /data/venv/bin/python scripts/kmd_zimage_nitro.py --concept context-chambers --broker-reservation-confirmed
```

The script preserves existing output files and checks available CPU/CUDA RAM during inference. All outputs are generated *art*, not footage or proof of KMD retrieval behavior. The specific two images at `assets/kmd/concepts/evidence-archive.webp` and `assets/kmd/concepts/context-chambers.webp` were reviewed, optimized for the web, published to GitHub Pages, and HTTP-checked. The raw generated images remain in Nitro runtime, not in the public image-source repository.

**Remaining:** full-length high-quality local video is not solved by this image-generation success. Jetson's five-frame Wan pipeline is proven only as a minimal inference test; longer runs need a safer memory-bounded strategy. Real KnowMoreDiRT source-cited retrieval footage is the highest-value next commercial demonstration.

## November 18 — real KMD source-provenance capture and interactive viewer

A dedicated externally hosted provenance explorer is live at
`https://hanspeterradtke.github.io/multiverse-ai-website/kmd/evidence/`.
It is linked from the KMD presentation page.

**Verifiable basis:** on Raspi, an isolated KMD initialize() call ingested three new, expressly fictional source documents in
`/data/var/multiverse-kmd/real-kmd-demo-20261118/corpus/`.
The actual code revision was `1696136`. KMD indexed 3 documents, 10 text chunks, 29 source spans, 19 mentions, 11 **candidate** referents, 3 contexts and 20 context assignments. Its SQLite graph integrity check returned `ok`. SHA-256 of all source files was independently compared with KMD's stored hashes and matched.

The serialized output `assets/kmd/demo-graph.json` contains actual source/span/mention/referent/context records, not invented graph edges or customer records. The viewer's link drawing uses actual relations from KMD's exported store: files to chunks, chunks to candidate referents, and chunks to contexts. JavaScript is in `assets/kmd/evidence.js`, styling in `assets/kmd/evidence.css`, and the responsive page in `kmd/evidence/index.html`. Verified on the publicly deployed GitHub Pages site, with 27 actual graph nodes and no browser JS exceptions; clicking a candidate referent correctly displays source-file references.

**Important limitations:** this bounded indexing capture intentionally set `KMD_LLM_DRS_INGEST=0` and `KMD_LLM_INGEST=0`; it does not claim that model-driven DRS ingestion was validated. A separate real model-backed public API test on the same fictional corpus used an isolated localhost-only relay to Thor's Qwen3.8-27B Q8 model. The first query reached `query_drs_start` and `bounded_query_start` but did not yield a public answer before a 240-second bounded timeout. **No generated answer was fabricated or published.** The owner-visible web viewer states that question answering is evaluated separately. The temporary localhost relay was stopped after the test; there are no active synthetic-demo query processes.

To continue: coordinate with the active KMD research worker; diagnose model-assisted question latency and structured response limits with an isolated benchmark (do not alter the shared production service), achieve a correctly verified answer with evidence in the public API, and only then record real on-screen question/answer/source-jump behavior. The present working explorer already supplies truthful live visual evidence of KMD's indexing and provenance architecture, and is suitable for use as a demonstrative slide or clip only if labeled a separate read-only visualization of real KMD records.

## November 18 — reproducible, genuine KMD browser walkthrough video

A fifty-one-second (1280 × 800 H.264, 24 fps) **real isolated Chromium X11 capture** was recorded from the existing public KMD evidence explorer. This is browser footage, **not** AI-generated interface animation, fictitious screen data, or live inference during the video. The explorer displays actual indexed source records (from explicitly fictional authored documents) and a recorded, independently model-verified, source-grounded KMD public-API answer. In the video, a browser scrolls to the verified answer and supporting passage, opens the source graph, clicks a candidate referent, clicks an indexed original file, changes graph relationship filters, reads original source cards, and returns to the answer. This does not imply KMD answers arbitrary documents reliably or quickly.

Public video asset: assets/kmd/kmd-evidence-browser-walkthrough.mp4.
Poster: assets/kmd/kmd-evidence-walkthrough-poster.webp.
Caption track: assets/kmd/kmd-evidence-walkthrough-captions.vtt.
Reproduction script: scripts/record_kmd_evidence_browser.py.

The capture uses a fresh, standalone Chromium process on its own Xvfb display with its own temporary profile and a separate debug port, **not** the user's authenticated Chromium profile or the registered owner automation tab. Recording uses ffmpeg X11 grab and x264. It checks the loaded source graph before recording, verifies actual click-driven inspector changes, terminates only its own processes, and uses ffprobe to verify the final MP4. The raw verified capture is retained on Nitro under /data/var/multiverse-kmd/screen-record-demo-20261118 for future editing. Browser screen contents use only public synthetic demonstration data. The movie has no synthetic voice or licensed music; proper narration is a separate optional enhancement.

We deliberately embed the original browser recording on the KMD website in a visibly labeled proof section, **ahead of** the AI-generated conceptual art gallery. The website must not call this a live model-execution recording.

## November 18 — source-revision validation and interactive comparison

A second real KMD public API test used a separate one-file fictional source snapshot containing the reviewer Elena Frost, rather than Mira Chen, with the exact same original question. KMD's locally model-generated Q4 source DRS was refreshed and accepted for the changed source (two DRS conditions, three referents). The valid Q8 query DRS was reused from cache; the Q8 independent verifier was **freshly invoked** for the changed source and accepted the answer Elena Frost with exact supporting source text. This is not merely changing text in a mock interface. No historic Mira Chen verifier response was reused, and the source's SHA-256 was checked. The first cold test reached accepted ingestion but hit its bounded timeout during verification; the second test reused that accepted source DRS and completed the new verification. Consequently, we do not claim a successful single cold run or general accuracy/latency.

The externally hosted evidence explorer now has an interactive source-revision comparison at kmd/evidence/#source-revision. Both displayed cases are **recorded real KMD public API results** against separate fictional snapshots. The switch only displays the stored results; it does not execute an LLM. Sanitized real results and explicit limitation flags are in assets/kmd/revision-proof.json; client code is in assets/kmd/revision.js. UI toggling in both directions was tested in real Chromium, and the public page and its proof JSON passed HTTP 200. Original private run receipts are under Raspi /data/var/multiverse-kmd/kmd-source-change-20261118. The KMD branch's dated technical note documents the result and source-cache constraints.


## Buyer-centered SWAAG positioning (November 19, 2026)

The marketing source selection and reading notes are in `production/marketing-positioning-2026-11-19.md`. The homepage no longer displays nine equal-weight products: instead it highlights one buyer-relevant situation for SWAAG and uses GitHub/other projects as source-code credibility. SWAAG messages are maintained in `scripts/swaag_marketing_content.py`. The persistent renderer `scripts/render_software_portfolio.py` inserts it into both Home and Software & AI. The remaining nine project descriptions stay available in the specialist directory; they should not dominate the first buyer-facing page. The design deliberately distinguishes a *developer framework* from a verified customer deployment, and does not invent saved-time metrics or customer success stories. The research is partial and focused on marketing use cases; no claim to have fully read all private marketing books.

## Public software portfolio and GitHub source links (November 19, 2026)

The source-backed projects in the homepage, Software & AI page, and general Projects directory are rendered from `production/public-software-portfolio.json`. The human-facing descriptions separate a project's practical purpose, expected benefit, basic workflow and actual release stage.

Render with `python3 scripts/render_software_portfolio.py`; this is repeatable and preserves the Wix, KnowMoreDiRT and 3D products. `scripts/rebuild_software_home.py` and `scripts/rebuild_software_page.py` automatically call the matching portfolio renderer so those content sections survive subsequent rebuilds. After adding or removing public pages, run `python3 scripts/align_software_navigation.py` to maintain consistent navigation, footer and GitHub links.

The public GitHub account is `https://github.com/HansPeterRadtke`; it has a repository for SWAAG and other software, but some live worktrees, including the adaptive Android keyboard, are **not** represented by the public GitHub source. Do not link an unpublished module to an unrelated public directory or imply that merely publishing source is a consumer/store release. Do not disclose private project hosts, financial strategy implementations, live customer data or token/secrets.

Offline validation: `python3 scripts/verify_software_portfolio.py`, `python3 scripts/verify_top_navigation.py`, `python3 scripts/verify_clarity.py` and the existing site-link and browser regression checks. Public changes still require inspecting Git status, reviewing owned changes and verifying the GitHub Pages deployment. Updating the public **GitHub profile account** or creating a special profile README repository is a separate action and is not performed by this website renderer.

## Dedicated SWAAG landing page and discoverability (Nov 19, 2026)

The canonical buyer-focused SWAAG page is `/swaag/`. Its generator is `scripts/build_swaag_landing.py`, with CSS in `assets/swaag-landing.css`. It is an honest developer framework explanation, not a demo of a fictitious working product. The home SWAAG spotlight and Software & AI catalog link to it.

Competitive and feature-claim constraints are documented in `production/swaag-competitive-context-2026-11-19.md` with public official sources. Distinguish real source-backed orchestration, tool boundaries and state persistence from unmeasured benefits. LangGraph, Temporal, and other frameworks have overlapping capabilities; no benchmark superiority has been established. SWAAG is MIT-licensed public source, version `0.1.0` without a verified published GitHub release. Do not market its public code as an exclusive paid acquisition.

The previous hard-coded sitemap omitted major public pages. `scripts/refresh_public_seo.py` now enumerates actual page files, generates an accurate sitemap, canonical references, Open Graph URL/title/description, and neutral Twitter summaries. It does not add analytics or third-party trackers, and it deliberately avoids fake screenshots for SWAAG. Regenerate all affected pages with `python3 scripts/build_public_site.py`; it runs the generators in their required order and leaves publication separate. Run `python3 scripts/verify_public_seo.py` as well as the existing content, navigation, file-link and Chromium browser tests before pushing. Verifying GitHub Pages is separate and should follow deployment.


## Buyer qualification and website contact (November 19, 2026)

The Business and Contact pages are generated by `scripts/build_commercial_path.py` and styled with `assets/commercial-path.css`. Buyer scenarios are hypotheses grounded in public source work, not fabricated customers or proof of demand. They highlight real situations relevant to local AI tool integration, file/test automation and separately owned technology components. The page differentiates freely available MIT SWAAG from separately contracted work or owned rights. No contract, pricing, availability or support is automatically promised.

The contact interface builds a `mailto:` draft on the visitor's device using `assets/site.js` and has **no website data-collection backend**. Three inputs are required (name, reply email, short description of the problem and desired outcome); company and relevant systems are optional. Budget, timeframe and intrusive early questions were removed. The visitor must review and send from their own email application. `mailto:` handling depends on the browser and installed mail program, so there is a prominent direct email alternative. Never claim the message was sent merely because the email draft opened.

Regenerate with `python3 scripts/build_public_site.py`, then check `scripts/verify_commercial_path.py`, `scripts/verify_public_seo.py`, the general link audit, and browser/mobile behavior. The site does not implement analytics pixels, visitor tracking, real lead metrics, or a promise of quick availability.

## Technical buyer-evidence section (November 20, 2026)

The SWAAG landing page has a dedicated `#evaluation` section. It links to real public test files for history replay/tampering, tool permission checks, session-path boundaries, delegated user instruction authority and process-error recovery. This responds to buyers' reasonable questions about how tool-using agents handle failure, and it provides direct code inspection rather than invented customer claims. Tests *existing* is not the same as tests *passing*, which is explained explicitly. `scripts/build_swaag_landing.py` and `assets/swaag-landing.css` own this content. `scripts/verify_public_seo.py` asserts all five source links, the four evaluation cards and the no-guarantees language; Chromium checks the section at desktop, tablet and phone widths.

Current marketing context (private, not bundled into the public site) lives at `/data/var/multiverse-kmd/website-clarity-20261120/agent-buyer-evidence-2026-11-20.md`, citing the 2026 G2 buyer study, Deloitte/EY surveys, OpenHands and LangGraph. Those surveys demonstrate general reported buyer concerns but do **not** establish SWAAG customer demand, ROI or reliability. The SWAAG repo is independently owned by its main project; its runtime compatibility and full tests must be verified by that owner rather than silently modified by website marketing work.

## Current baseline comparison and user-interface research (Nov 20, 2026)

The user correctly rejected describing AI tool use and generic document Q&A as innovations. The current buyer-focused copy is owned by `scripts/market_differentiation.py`, which runs **after** the base page generators and **before** navigation and SEO refresh. It updates the homepage, SWAAG and KnowMoreDiRT in one deterministic pass and adds a compact proof of the published CapOv (`pip install capov`) package; its styles are `assets/market-differentiation.css`. The package also appears in the secondary software catalog through `production/public-software-portfolio.json`. Keep this build order rather than hand-editing generated pages that are overwritten by the next build.

For honest current benchmarks: Codex and Claude Code already run tools, edit code, use subagents and read files. SWAAG's inspectable local-first framework and KMD's context/provenance research *may* fit specialized workflows, but superiority, enterprise reliability and reduced mistakes have not been measured against those products. KMD's public API does **not** deliver citation objects with every response. CapOv is a real PyPI package v0.1.6, not a claim of unique linting capability or assured safe fixes; compare with Ruff, and note that current isolated bundled tests did not all pass. Do not equate package downloads with users or advertise fictitious adoption statistics.

UI sources reviewed in the owner's Raspi Library: Oxford's *Introduction to Human–Computer Interaction* (2025), especially chapters 23 and 27; Nielsen Norman Group's Ten Usability Heuristics poster; and the original Laws of UX pages for familiar navigation, proximity, choice load and visual hierarchy. These support plain task language, grouping comparison and evidence, keeping the mobile interface legible, and direct action labels—not larger headlines alone. The selection and limitations are documented in `production/baseline-positioning-and-ux-2026-11-20.md`, not an untrue statement that every library item was read.

Regenerate using `python3 scripts/build_public_site.py`; verify with `scripts/verify_market_positioning.py`, `scripts/verify_clarity.py`, `scripts/verify_public_seo.py`, `scripts/verify_software_portfolio.py`, the global link audit and desktop/mobile browser checks including the original Wix/KMD videos. No third-party analytics, user tracking or unverified benchmark graphics are added.

## Agent-directed 3D production showcase (Nov 20, 2026)

The 3D destination and homepage now demonstrate the **locally orchestrated AI production capability**, not merely CGTrader products. Three original Cycles scene renders are sourced from Nitro's guarded warehouse/dock development history and have public WebP renders with exact source checksums. Four measured/documented tool roles (Nitro, Thor, Jetson, Raspi) and four production steps explain how agent-driven Blender/Python construction, materials, animation, QA and export fit into a self-owned system. Two existing real project animation videos are embedded with user controls; marketplace catalogs remain secondary and unchanged. No fake image-generated screenshots or owner-photorealism approval claims are used.

Rebuild with `python3 scripts/build_public_site.py`; the final `scripts/position_3d_automation.py` step is integrated into the pipeline. Avoid calling the old standalone `scripts/build_3d_navigation.py` *after* this without subsequently running the full build; that old script generates only the product catalog and would discard the updated automation marketing until rebuilt. Validate with `python3 scripts/verify_3d_agent_production.py`, browser/mobile video QA and the normal other site regressions. Full truth/asset/machine/quality-source notes: `production/3d-ai-production-evidence-2026-11-20.md`. The source-receipt JSON is public-safe; absolute local source file paths stay in a private QA document under `/data/var/multiverse-kmd/`.

## 3D engineering proof follow-up (November 20, 2026)

`#engineering-proof` on the dedicated 3D page now shows an **independently checked, bounded geometry correction** from a November 10 Blender development study: original ~7.1 mm floating forklift wheel gap corrected to ~0.03 mm, 29 native Cycles still comparisons, and 9 sampled clear dock-opening rays. A public-safe JSON document contains only source receipt hashes, interpreted values, and limitations; full private Blender scenes and machine file paths were not published. This is a technical code/workflow proof, **not** a real-world safety test or assertion that all AI-run production is autonomous. Gallery imagery comes from different revisions.

The builder step `scripts/add_3d_evidence_case.py` runs after `scripts/position_3d_automation.py`, replacing a redundant generic benefits block with the single case. Validate with `python3 scripts/verify_3d_evidence_case.py`, normal site/navigation/SEO tests, source receipt checks and actual browser QA. Preserve other agents' ongoing 3D source changes and other website worktrees.

## First-screen source-backed previews and AI production navigation (Nov 20, 2026)

The owner values visible evidence of working software and agent-operated applications more than a sales catalog. The homepage's first-screen preview generator is `scripts/refine_home_proof_first.py` (styles `assets/home-proof-first.css`), run after all product and 3D generators and before navigation/SEO. It retains the SWAAG team-manager lead, replaces the previously duplicated KnowMoreDiRT card text with a concise truthful research preview, and adds a genuine original Blender warehouse render linked to the AI production page. The published Wix application stays accessible through a smaller hero link and its complete dedicated, playable demonstration lower on the homepage. This avoids positioning AI-generated 3D as simply a model shop and does not invent a ready KMD UI or successful agent benchmark.

The shared top navigation now labels its existing dedicated `/3d/` destination **AI 3D Production** rather than **3D models**, reflecting the underlying multi-machine Blender/Python production system. `scripts/align_software_navigation.py` owns this label on all twelve pages (desktop, mobile and footer); it is never a deep `#` scroll. The `scripts/verify_top_navigation.py`, `scripts/verify_home_proof_first.py`, and `scripts/verify_local_site_paths.py` tests protect consistent navigation, accurate source images, appropriate project maturity labels, accessible links, and the original Wix playback. Browser acceptance separately exercises 1440/768/390/360 viewport widths, real nav and card clicks, and silent video playback. The authentic agent/Blender screen recording is requested from the separate 3D production worker and is not claimed finished by this website update.
