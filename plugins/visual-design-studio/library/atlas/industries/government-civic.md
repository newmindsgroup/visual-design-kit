---
id: industry.government-civic
axis: industry
name: Government and Civic
aliases: [government, public sector, civic tech, city, municipality, agency, public service, gov.uk, federal, state and local, elections]
summary: Public services used by everyone, often under stress and without a choice; success is task completion, plain language, accessibility and earned trust rather than brand expression.
tags: [government, civic, public-sector, forms, services, accessibility, plain-language, city, elections, benefits]
pairs_with: [style.civic-plain, style.clinical-calm, style.swiss-international, style.flat-material, archetype.everyperson, archetype.caregiver, audience.low-literacy-plain-language, audience.disability-accessibility-first, audience.older-adults, channel.web-app]
avoid_with: [style.y2k-cyber, style.grunge-punk-zine, style.maximalist-eclectic, archetype.outlaw]
version_timestamp: 2026-10-20 01:59:13 UTC
---

# Government and Civic

## Audience and jobs to be done

- **Residents applying for something:** benefits, licenses, permits, visas, taxes, school places. They want to know if they qualify, what to bring, how long it takes, and what happens next.
- **People in a crisis:** unemployment, disaster aid, a missing document, a deadline. Stress narrows attention and reading ability; design for the worst day.
- **People with limited digital access or skills:** older adults, people on prepaid phones, people with low literacy or limited English, assistive-technology users.
- **Caseworkers and front-line staff:** internal tools used all day; need dense, fast, keyboard-friendly interfaces and audit trails.
- **Business owners:** register, report, pay, renew, usually on desktop and often through an agent.
- **Voters and civic participants:** find a polling place, read a ballot, comment on a plan, report a pothole.
- **Journalists, researchers and watchdogs:** open data, meeting records, budgets.

## Trust signals

- Unmistakably official source: government domain (.gov, .gov.uk), the standard "official website" banner in the US, crest or seal used per rules.
- One service, one URL, one clear start button; no third-party look-alike domains for transactions.
- Plain statements of what happens to data, how long a decision takes and how to appeal.
- Consistency across agencies: the same header, footer, form patterns and error messages, which is the point of a shared design system.
- Published accessibility statement, last-updated dates, and a human contact route (phone, in-person, language help).
- Receipts and confirmation pages with reference numbers and "what happens next" timelines.

## Category conventions

- Text-first pages, a single-column layout (about 66 characters per line), large 19-20px body text, generous spacing, strong visible focus.
- Start-to-finish "one question per page" forms with a progress summary and a check-your-answers page before submission (GOV.UK pattern).
- Black, white and one dark institutional blue or a flag-derived palette; yellow focus states; sentence case headings.
- Sans-serif system: GOV.UK Transport/GDS Transport (restricted use), Public Sans (USWDS, OFL), Source Sans or Roboto fallbacks.
- Components are shared and versioned: start button, text input, radios, date input, error summary, notification banner, task list.
- Documents as PDFs and long pages; address and phone details in the footer.

## Where to differentiate

- **Service design before visual design:** remove steps, reuse known data (tell us once), show eligibility early, add status tracking. This outperforms any rebrand.
- **Tone:** warm and direct without being cute; a person is speaking, not a department.
- **Multi-channel coherence:** web, SMS, letters, phone script and counter signage use the same words and reference numbers.
- **Content design as a craft:** user-tested page titles, short sentences, defined terms, translated versions that are reviewed by speakers.
- **Place identity for cities and regions:** a flexible visual system for events, transit, culture and tourism, kept separate from transactional pages.
- **Open working:** publish the design system, research, service performance and accessibility results.

## Category clichés

- Flag, eagle, landmark silhouette or skyline as the whole identity; stock photos of handshakes and diverse crowds.
- Hero carousels of leadership photo ops above the task people came for.
- Acronym-heavy navigation organized by org chart instead of user need.
- PDF forms and "download, print, sign, scan, email" journeys; CAPTCHAs on read-only pages.
- A brand refresh that changes the logo but not the service.

## Regulatory and compliance notes

- **Section 508 (US federal):** the Revised 508 Standards incorporate WCAG 2.0 Level A and AA by reference for federal agencies' ICT; most agencies test to WCAG 2.1 or 2.2 AA in practice. Section 504 reaches recipients of federal funds. Procurement asks for an Accessibility Conformance Report (VPAT).
- **ADA Title II web rule (US state and local government):** the DOJ final rule of April 2024 requires WCAG 2.1 AA for web content and mobile apps. DOJ's April 2026 interim final rule moved the compliance dates to 26 April 2027 for entities with populations of 50,000 or more and 26 April 2028 for smaller entities and special districts; further rulemaking was signaled. Verify current dates against the Federal Register.
- **UK:** the Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018 require an accessibility statement; GOV.UK guidance sets WCAG 2.2 AA as the standard to meet. EU Web Accessibility Directive 2016/2102 uses EN 301 549.
- **Plain language and forms (US):** the Plain Writing Act of 2010 covers federal documents; the Paperwork Reduction Act requires an OMB control number and burden statement on federal information collections; 21st Century IDEA Act (2018) sets expectations for accessible, consistent, secure, mobile-friendly federal sites.
- **Seals and insignia:** federal law restricts reproduction of official seals and badges (see 18 U.S.C. 701 and 713), and the UK Royal Arms and Crown logo have usage rules. Do not use them in concepts or mockups for non-government work.
- **Language access:** Title VI of the Civil Rights Act and state or local language-access policies can require translated key content and interpreter routes; verify current federal guidance. Translated pages need the same accessibility.
- **Privacy:** Privacy Act notices on forms that collect personal data, retention rules, and the GDPR for EU bodies. Avoid third-party trackers on service pages.
- **Elections:** US EAC Voluntary Voting System Guidelines and state rules govern ballots; AIGA's Design for Democracy ballot-design research applies.

Confirm requirements with counsel for the specific product and jurisdiction.

## Key deliverables and screens

- Design system: tokens, components, patterns (check answers, task list, error summary, confirmation), content style guide, accessibility acceptance criteria.
- Service journeys: eligibility checker, start page, multi-step form, document upload, identity verification, status tracker, notifications, appeal.
- Website information architecture by user need; search that handles misspellings and synonyms.
- Print and offline: letters, forms, counter signage, SMS templates, call-center scripts.
- Staff tools: case management with keyboard shortcuts and full audit history.
- City or agency identity: logo, flexible graphic system, wayfinding, vehicles, uniforms, emergency alert templates.

## Voice and content

- Reading age 9-11 for general public content; sentence length around 15-20 words; active voice; one idea per paragraph.
- Name the task, not the department: "Renew your driver's license", not "Division of Motor Vehicles Credential Services".
- Explain terms once, avoid acronyms on first use, and give dates in full ("Friday 3 May 2026").
- Error messages say what to fix: "Enter your date of birth as 27 3 2007."
- Never promise a decision date the system cannot meet.

## Recommended directions

- **Category-expected:** `style.civic-plain` + `archetype.everyperson` for `audience.low-literacy-plain-language`: system fonts or an open sans, 19-20px text, strong focus states, one question per page. The right default for transactions.
- **Adjacent:** `style.clinical-calm` + `archetype.caregiver`, borrowed from health services (NHS-style): reassuring blues, plain illustrations, tested reading flows. Suits benefits, health and family services where the user is anxious.
- **Category-breaking:** `style.kinetic-experimental-type` + `archetype.creator` for city, culture and tourism identity: a generative logo and typographic system that changes with the event or neighborhood. Risk: erodes recognition and authority if it leaks into transactional pages, animation can fail reduced-motion and cognitive-accessibility needs, and critics call it wasteful. Keep services on the plain system.

## Metrics that matter

- Task completion rate and time to complete for the top 5 services; digital take-up versus phone and paper.
- Error rate by form field, abandonment by step, and calls to the contact center per 1,000 transactions.
- Accessibility defects found in audits and user testing with assistive-technology users.
- Content findability: search success, page-feedback "was this useful", readability scores.
- Cost per transaction and processing time; user satisfaction (CSAT) by segment.

## Reference anchors

- GOV.UK Design System and the GDS Service Standard: https://design-system.service.gov.uk/
- U.S. Web Design System (USWDS): https://designsystem.digital.gov/
- NHS digital service manual for health-adjacent public services
- Australian Government Design System and Singapore's Government Design System for national-scale systems
- Code for America and 18F for civic-tech practice and open working
- AIGA Design for Democracy for ballot and election design
- City of Melbourne's flexible identity as a place-brand reference (observe, do not copy)
