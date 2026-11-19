# Multiverse marketing positioning research and messaging controls — November 19, 2026

## Sources actually reviewed

The owner's Raspi Knowledge Library is authoritative for private marketing references: `/data/var/Knowledge Library/money-and-business/`, indexed read-only by `/data/bin/knowledge-library search-business`. Relevant primary sources found and checked:

- *Principles of Marketing* (complete open Canadian edition, 2022), PDF original pp. 51–53, chapter 2.1 "The Value Proposition," and pp. 189–191, chapter 5 on targeting. The publisher's own definition makes the buyer's desired benefit and target market the basis of a value proposition, with distinct propositions for distinct buyer groups. It explicitly cautions against foregrounding the seller's profits rather than external customer needs. Original publisher: https://openlibrary-repo.ecampusontario.ca/jspui/handle/123456789/1705 . Verified on Raspi in `money-and-business/business-textbooks/2022-principles-of-marketing-canadian-edition.pdf`.
- *Business Startup and Entrepreneurship: Canada* (2021), PDF chapter around original p. 124, discusses why a client should buy or engage a vendor; source surfaced through the library full-text index. Original publisher: https://open.umn.edu/opentextbooks/textbooks/business-startup-and-entrepreneurship-canada .
- MIT OpenCourseWare *Marketing Management: Analytics, Frameworks and Applications* (2015), scanned text excerpt via verified fulltext business index, focuses on structuring actual customer needs rather than feature inventory. Official course: https://ocw.mit.edu/courses/15-810-marketing-management-analytics-frameworks-and-applications-fall-2015/ .
- *The Power of Selling* (2010, university-hosted complete open textbook), library search returns its discussion that a product's presentation must address buyer needs and may rely on a real demo rather than only assertion. Original publisher https://open.umn.edu/opentextbooks/textbooks/the-power-of-selling .
- Current Infra owner-specific commercial objectives `/data/infra/docs/guidelines/agents/owner_commercial_goals_and_agent_priorities.md` and business website handover `/data/infra/docs/guidelines/projects/multiverse_business_website_and_video_handover_2026-11-17.md` describe inbound interest for high-value bounded transactions, minimal support and no generic hourly staffing service.

These references guide *structure*, not a claim that a particular landing page or sale is proven to convert. Other marketing sources exist in the private library and were not all read fully; avoid implying exhaustive coverage or quoting copied textbook passages into the public repo.

## Communication strategy

Primary audience for SWAAG: developers/technical teams working with local/self-hosted models who need actual tool-using, multi-step agents, observable task state and a reusable implementation. Secondary audience: technology buyers considering whether a component could be acquired/licensed or adapted for a bounded use case. SWAAG is not yet a turnkey service or plug-and-play product for general nontechnical buyers.

Make visitor situation visible, then the result they desire, then explain how the technology could help and link proof:

1. Situation: 'Our local AI answers questions but cannot manage repeatable, multi-step work involving files, programs and tools.'
2. Desired outcome: 'I want a foundation for an assistant that coordinates tools, delegates substantial tasks, tracks what happened, and supports checks or recovery.'
3. Product: SWAAG is an open-source agent harness with a persistent orchestrator, durable workers/event history, constrained tool and policy boundaries, and configurable local model backends.
4. Benefit: reduces the need to build these framework components from scratch and *could* make complex task progress more traceable. No unsupported hours-saved, success-rate, production deployment, military/medical compliance or guaranteed autonomy claims.
5. Proof: direct `https://github.com/HansPeterRadtke/swaag` and specific README, `docs/design-principles.md`, `docs/manual.md`, `tests/` and installation instructions. Code shows real implementation; a repository is not evidence of reliable execution in an arbitrary buyer environment.

Keep Wix, KMD and industrial 3D separate examples because they serve different buyer groups. Do not crowd the first screen with nine equal-weight cards. Other code-based projects are credibility references that belong in a secondary portfolio directory. A section that merely lists 'SWAAG, keyboard, all2text...' is a list of technologies, not an answer to customer needs. The public GitHub link is the source-code proof, not the main selling proposition.

## Claims boundary and acceptance

SWAAG local-first, orchestration and durability are source-backed; broader autonomy/voice/commercial reliability is work in progress. Distinguish documented architectural feature, working code, local test, and verified deployment. On the website say 'a foundation for building...' / 'designed to...' rather than 'will save x hours', 'fully autonomous', or 'enterprise-ready'. The marketing source files are private; only this own original summary may be published.

Acceptance: buyer understands in under 30 seconds what SWAAG is for, who should look at it, when they would need it, how it works in ordinary language, where actual code lives and whether it's a ready-to-use service. Desktop/mobile visuals and links must be checked and published GitHub Pages reviewed after deployment.
