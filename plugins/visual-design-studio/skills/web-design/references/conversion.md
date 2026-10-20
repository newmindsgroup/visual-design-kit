# Conversion and ethical persuasion

Version-Timestamp: 2026-10-20 02:04:32 UTC

Conversion comes from clarity, relevance and trust, then from removing friction. Persuasion is legitimate when it helps people decide with true information; it becomes a dark pattern when it exploits them, and in many jurisdictions it becomes illegal. Regulatory notes below shape design; confirm requirements with counsel for the specific product and jurisdiction.

## Diagnose before redesigning

A useful lens is WiderFunnel's LIFT model: **value proposition** (the engine), **relevance** and **clarity** (amplifiers), **anxiety** and **distraction** (inhibitors), **urgency** (only when real). Score each page section against these, then fix the biggest gap.

Evidence sources, cheapest first: analytics funnels and drop-off by device, session recordings (with consent and masking), on-page polls ("What's stopping you from signing up today?"), five-second tests, usability tests, then A/B tests (see `ux-design` [research methods](../../ux-design/references/research-methods.md) for power calculations).

## Value proposition clarity

- **Five-second test:** show the page for 5 seconds; people should be able to say what it is, who it is for, and what to do next.
- **Headline formula options:** outcome for audience ("Payroll for restaurants, done in 10 minutes a week"); the job itself ("Send invoices that get paid faster"); a sharp contrast with the status quo. Avoid slogans that could belong to any company ("Built for the future of work").
- **Specifics beat adjectives:** numbers, names, time saved, concrete features. "Exports to QuickBooks and Xero" beats "integrates with your tools".
- **Message match:** the landing page headline repeats the promise of the ad, email or search query that brought the visitor.
- **Show the product:** real UI, real photography, a short demo video (under about 90 seconds) or an interactive tour.

## Social proof

| Type | Strongest form | Placement |
| --- | --- | --- |
| Customer logos | Recognizable to the target audience, with permission | Directly under the hero |
| Testimonials | Specific result, full name, role, company, photo, with consent | Next to the claim they support and near the CTA |
| Case studies | Problem, solution, measured result, named customer | Linked from features and pricing |
| Ratings and reviews | Third-party platform score with count and source, linked | Hero or near price |
| Usage numbers | Precise, current, sourced ("12,481 teams as of March 2026") | Proof strip |
| Certifications and security | SOC 2, ISO 27001, PCI, accessibility conformance, with dates | Pricing, security page, checkout |
| Press and awards | Named outlet or award with year | Proof strip or about page |

**Rules from US law:** the FTC's Endorsement Guides (revised 2023) require that testimonials reflect honest opinions and typical results or clearly disclose what is typical, and that material connections (payment, free product, employment) are disclosed. The FTC's Trade Regulation Rule on Consumer Reviews and Testimonials (16 CFR Part 465, effective October 2024) bans fake or AI-generated fake reviews, buying positive reviews, undisclosed insider reviews, suppressing negative reviews, and fake social-media indicators such as purchased followers.

## Reduce friction

- **Form length:** every field must change what happens next. Ask for email first; collect company, role and phone later or enrich them. For sales demos, 3-5 fields is a common ceiling. Field patterns are in `ui-design` [forms](../../ui-design/references/forms.md).
- **Distraction:** remove global navigation from paid-traffic landing pages; keep a logo link and the footer's legal links.
- **Anxiety:** answer the top objection next to the CTA (price, commitment, data use, setup effort); show security and privacy details where data is asked for.
- **Risk reversal:** free trial, freemium tier, money-back guarantee, "cancel anytime", only when true and easy to use.
- **Speed:** every second of load delay costs attention; meet the [performance](performance.md) budgets.
- **Mobile:** tap-friendly CTAs (48px), sticky CTA bar on long pages, wallets and autofill in checkout.

## Ethical persuasion

Allowed and effective when truthful: real scarcity (actual stock levels), real deadlines (an event date, a sale that really ends), real popularity ("Most chosen by teams of 10-50"), defaults that serve the user, reminders the user asked for, anchoring with a genuine reference price, and progress indicators.

The test: would the visitor feel deceived if they saw how this was built? Would the claim survive a regulator's request for substantiation?

## Dark-pattern rules

Do not design any of these. Each row lists the pattern, why it fails, and the fix.

| Pattern | Example | Fix |
| --- | --- | --- |
| Fake urgency | Countdown timer that resets on reload; "Offer ends tonight" every night | Real deadlines only, stated with the date |
| Fake scarcity or popularity | "Only 2 left" or "38 people viewing" when untrue | Show real stock or nothing |
| Confirmshaming | "No thanks, I don't like saving money" | Neutral decline: "No thanks" |
| Sneak into basket | Pre-added insurance, donations or warranties | Opt-in add-ons, unchecked by default |
| Drip pricing and hidden costs | Fees revealed at the last step | Total price, including mandatory fees, from the first price shown |
| Forced continuity | Trial silently converts to paid | Clear terms before sign-up, reminder before the first charge, easy cancel |
| Roach motel / obstruction | Sign up online, cancel only by phone | Cancel through the same channel, in no more steps |
| Trick questions | Double negatives in consent checkboxes | One plain, positive statement per choice |
| Interface interference | "Accept" as a big button, "Reject" as faint text | Equal visual weight for equivalent choices |
| Nagging | Repeated pop-ups after a "no" | Respect the answer for a reasonable period |
| Disguised ads | Ads styled as content or navigation | Label ads clearly |
| Forced action | Must share contacts or create an account to see prices | Ask only what the task needs |
| Bait and switch | Advertised plan unavailable at checkout | Honor what was advertised |
| Privacy-intrusive defaults | Data sharing on by default | Privacy-protective defaults |

**Where the rules come from (as of 2026):**

- **United States.** Section 5 of the FTC Act (unfair or deceptive practices) and the FTC staff report *Bringing Dark Patterns to Light* (2022). ROSCA (Restore Online Shoppers' Confidence Act) requires clear disclosure of material terms, express informed consent and a simple cancellation method for online negative-option subscriptions. The FTC's 2024 amendments to the Negative Option Rule ("click to cancel") were vacated by the Eighth Circuit on 8 July 2025, but ROSCA and state automatic-renewal laws (California's among the strictest) still apply. The FTC's Rule on Unfair or Deceptive Fees (in force May 2025) requires total-price display for live-event tickets and short-term lodging. Under the California Consumer Privacy Act regulations and several other state privacy laws, consent obtained through dark patterns is not valid consent.
- **European Union.** The Unfair Commercial Practices Directive (2005/29/EC) bans misleading and aggressive practices, with an Annex I blacklist banned in all circumstances, including falsely stating that a product is available only for a very limited time. The Omnibus Directive (EU) 2019/2161 added: any announced price reduction must show the lowest price of the previous 30 days; fake reviews and undisclosed paid rankings are banned; personalized pricing must be disclosed. The Consumer Rights Directive bans pre-ticked boxes for extra payments and requires the order button to make the payment obligation clear; an online withdrawal function for distance contracts applies from 19 June 2026 (Directive (EU) 2023/2673). The Digital Services Act, Article 25, prohibits online platforms from designing interfaces that deceive, manipulate or materially impair users' free and informed decisions. GDPR consent must be freely given, specific, informed and unambiguous; pre-ticked consent boxes are invalid (CJEU, *Planet49*, 2019), and the EDPB's Guidelines 03/2022 catalog deceptive design patterns. A Digital Fairness Act aimed at dark patterns, subscription traps and addictive design has been announced but not yet adopted; check its status.
- **United Kingdom.** The Digital Markets, Competition and Consumers Act 2024 (consumer provisions in force since 6 April 2025) lets the CMA fine directly, bans fake reviews outright, and requires mandatory fees in the headline price.
- **India.** The CCPA's Guidelines for Prevention and Regulation of Dark Patterns (November 2023) name 13 patterns, including false urgency, basket sneaking, confirmshaming, forced action, subscription traps, interface interference, bait and switch, drip pricing, disguised ads and nagging.

## Cookie and consent banners as conversion surfaces

- First layer: "Accept all", "Reject all" and "Customize" with equal prominence (EU and UK regulators, including the EDPB cookie banner taskforce and the CNIL, have treated a missing first-layer reject option as non-compliant).
- No tracking tags fire before consent where consent is required.
- The banner must not cover the main CTA or hide focused elements (WCAG 2.4.11); place it at the bottom, keyboard reachable, without trapping focus unless it is a true modal.
- A persistent "Cookie settings" link in the footer.
- Stack and tooling choices are in [stack selection](stack-selection.md).

## Measure and iterate

- Primary metric per page (sign-ups, demo requests, purchases), with guardrails (refund rate, churn in 30 days, unsubscribe rate, support contacts).
- Segment by device and traffic source; mobile and paid traffic usually behave differently.
- Test big changes first (value proposition, offer, page structure) before button colors.
- A variant that wins by deceiving is not a win; its cost arrives as refunds, chargebacks, complaints and regulator attention.
