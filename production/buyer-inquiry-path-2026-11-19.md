# Buyer inquiry path — November 19, 2026

## Goal and audience

The Business and Contact pages exist to help a relevant technology buyer recognize an application for verified existing software and send a low-friction inquiry about a separately scoped component, bounded adaptation or valid technology rights. The owner prefers independent technology products and bounded one-off transactions rather than staffing, generic hourly services, indefinite support or automatically accepting commercial commitments.

The site currently has no observed conversion statistics, active marketing campaign, reported sale, customer case study, or validated buyer willingness to pay. The scenarios are illustrative hypotheses grounded in SWAAG, all2text and other public code—not claims of completed client work.

## Research support

- Raspi private Knowledge Library: `money-and-business/complete-open-university-books-2026/sales-and-marketing/2026-digital-marketing-fundamentals-mcmaster-university-2026-385a258fa.pdf`, full website design chapter 2 reviewed. Its website-goal and CTA sections distinguish the visitor's intent from the site's intended conversion and emphasize relevant offers, plain language, real evidence, and usability testing. Source details and methodology limits in `marketing-positioning-2026-11-19.md`.
- MIT OCW Marketing Management Voice of the Customer materials: identify actual customer needs before assuming an engineering feature is a purchasing reason. Hypothetical buyer cases here need validation in real customer discovery, not more confident slogans.
- [UK Parliament design system, designing forms](https://designsystem.parliament.uk/how-tos/designing-forms/): collect only necessary information. The contact form does not ask for budget or a deadline before initial fit.
- [Google Search Central, helpful people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content): the site must explain what the user needs and demonstrate first-hand experience, rather than fabricating testimonials or SEO copy.

## Three buyer situations

1. Local/self-hosted AI needs to use internal software tools. `github.com/HansPeterRadtke/swaag` is public MIT-licensed agent infrastructure. Buyers can use that code free under the license; a separate owned component or bounded integration would require distinct scope and rights. Not a certified enterprise product.
2. Repeated file processing or test workflows are manual. `github.com/HansPeterRadtke/all2text` shows real file normalization and manifest output, and the engineering workflow could be evaluated for a narrowly defined deliverable. No customer ROI, time saved or successful external integration has been verified.
3. A buyer wants to evaluate existing proprietary components or licensed technology rather than building everything from scratch. Only verifiably owned and transferable technology can be discussed as an exclusive commercial asset. Do not imply that public MIT source is exclusive.

These are not three equal product SKUs, and no rates, price list, bookings or SLA are offered by the static site. The original published Wix application and digital 3D assets retain their separate sales paths.

## Contact method and privacy

No server-side contact API exists. The visitor can click a direct Gmail address or provide a contact name, reply address and problem/desired outcome, plus optional company and systems. JavaScript builds a `mailto:` draft on their own device. The visitor must review and send in their own email application; the website does not transmit or store the form submission. Because browser/protocol handlers vary, a direct email link is retained as fallback. The privacy page describes GitHub Pages hosting, potential mail-provider handling and the absence of website analytics.

## Acceptance tests

- `python3 scripts/build_public_site.py`: regenerates buyer pages along with the current site and SEO metadata.
- `python3 scripts/verify_commercial_path.py`: verifies legal boundaries, form fields and privacy semantics; `node tests/test_site_js.cjs`: exercises required form validation, constructed mailto URI and mobile navigation in a mocked DOM, without sending a message.
- Chromium desktop and mobile: validate the opportunity-to-contact navigation, all 3 situation cards, required input labels, visible direct email fallback, no overlapping content and mobile menu.
- Public release check: GitHub Pages workflow success and 200 responses for both pages and CSS/JS. No tracking service is installed; there are no measured qualified inquiries yet.
