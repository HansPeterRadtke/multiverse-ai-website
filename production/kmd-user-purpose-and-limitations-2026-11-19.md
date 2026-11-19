# KnowMoreDiRT: public value proposition, workflow, feature/benefit separation

Authoritative source of user-facing purpose: current Raspi `/data/src/github/KnowMoreDiRT/README.md`, `docs/public_api.md`, and `docs/architecture.md` (November 19, 2026). Nitro source is considerably behind Raspi; do not use its README as authority for current model integration.

## Who and why

Someone has a folder tree containing years of readable text: reports, project notes, transcripts, logs, tables written as text, and related source files. They need a specific fact without manually opening/searching every document. The desired benefit is less searching and less file preparation, with a path to inspect the original evidence behind any answer. These are *intended benefits*, not independently established cost/time savings or broadly validated enterprise capabilities.

## What a user actually does

1. Supply an existing folder path to `knowmoredirt.initialize(folder_path)`. It recursively scans readable source text; no schema or manifest is required.
2. Ask a normal-language question with `knowmoredirt.question(text)`.
3. Receive an answer as a plain string. Source paths, spans and provenance are held internally. The public API does **not yet** return a list of citations and the website is **not** a live, general document-query frontend.

Normal runtime requires an available local llama.cpp-compatible model endpoint; initialization fails clearly if it is unavailable. Do not present raw binary PDF and image OCR as supported input without separate verified extraction.

## Feature -> user benefit (different from implementation)

- Raw folder traversal, no special external format -> fewer manual steps to prepare a text collection.
- Ordinary-language questions and source-based answer generation -> aim to reduce having to hunt through filenames and read documents manually.
- Internal source spans, documents, provenance and verification -> aim to let results be investigated rather than treated as unsupported AI claims. Public answer remains plain text.
- Local model integration -> a local technical deployment path, **not** a guarantee of security, confidentiality or compliance.
- DRT and DSPG discourse representations of entities, contexts, temporal relationships and coreferences -> potentially more meaningful answers than isolated keyword search, **but robust cross-document reference resolution and contextual reasoning are ongoing research, not validated features**.

## What is genuinely proven

An isolated source-backed fictional one-file test returned the correct name from `field_report.txt` in the public question API, with independently validated source grounding. Separate recorded revision tests showed changed test-file content changing the answer. Technical evidence is in website `assets/kmd/answer-proof.json`, `assets/kmd/revision-proof.json`, and `kmd/evidence/`. Some intermediate model work was cached. Neither synthetic test establishes broad generalization, performance, correctness on arbitrary archives, human-time savings or production suitability.

## Site architecture

The homepage briefly introduces intended workflow and user benefit, with an explicit prototype status and links to the dedicated `/kmd/` page. The dedicated page shows purpose, concrete user actions, intended benefits with technical features subordinate, bounded test evidence, and only then optional architecture details (including the two-call Python API). The hero contains a labeled *concept illustration*, not a fabricated live UI or a fictional person presented as a company employee. `/kmd/evidence/` is the detailed fictional-test evidence viewer.

The old silent evidence video is retained untouched and labeled as playback of previously computed test data. Multiverse's other products, the published Wix app and industrial digital models, are separate.

Deployment QA: verify all local links and main/regression tests; test desktop and true mobile device emulation; confirm demo video still plays; ensure no public page implies that real company data was analyzed or that `question()` returns citations when it currently returns plain text.
