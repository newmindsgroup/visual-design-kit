---
id: industry.fintech-banking
axis: industry
name: Fintech and Banking
aliases: [fintech, banking, neobank, bank, payments, personal finance, wealth management, lending, credit union]
summary: Money products where trust, clarity and control come first; differentiation now comes from tone, craft and transparency rather than blue-and-shield symbolism.
tags: [finance, banking, payments, money, trust, fintech, neobank, wealth, lending, security]
pairs_with: [style.swiss-international, style.corporate-modern, style.quiet-minimal, style.neo-brutalist, archetype.ruler, archetype.sage, archetype.everyperson, channel.native-app, channel.web-app]
avoid_with: [style.grunge-punk-zine, style.y2k-cyber, archetype.jester]
version_timestamp: 2026-10-20 01:42:00 UTC
---

# Fintech and Banking

## Audience and jobs to be done

- **Everyday banking users:** check balance in seconds, move money confidently, avoid fees and surprises, understand what happened to their money.
- **Savers and investors:** see progress toward goals, understand risk and returns in plain language, trust that advice is not a sales pitch.
- **Small businesses:** get paid, reconcile, manage cash flow, issue cards to staff, export to accounting.
- **Underserved and first-time users:** build credit, avoid predatory products, feel respected rather than judged.
- **Anxious moments:** fraud alerts, declined payments, debt, disputes. Design for stress, not just delight.

## Trust signals

- Precise, consistent numbers: tabular figures, exact cents, clear positive/negative, timestamps on every transaction.
- Regulatory and protection statements in the right place (deposit insurance, licensing, "not FDIC insured" for investments) without burying the product in fine print.
- Visible security: biometric login, device management, transaction notifications, card freeze in one tap.
- Transparent pricing: fees, APR/APY and FX rates before confirmation, not after.
- Recognizable support: human contact routes, response times, plain-language help.
- Stability cues: real company information, partner bank disclosure, status page, no broken or placeholder content.

## Category conventions

- Balance first on the home screen, then recent activity, then actions (send, request, pay, transfer).
- Confirmation screens summarizing amount, recipient, fee, arrival time before any irreversible action; success state with reference number.
- Blue, navy and green dominate legacy banking; neobanks moved to black, white and one vivid accent, or cards as hero objects.
- Card visuals as product hero; app screenshots in phone frames on marketing pages.
- Charts limited to spending categories, balance over time and portfolio performance.

## Where to differentiate

- **Tone:** plain-spoken, human, occasionally witty in low-stakes moments (never in fraud or debt flows).
- **Transparency as design:** show fee math, FX rate, time-to-arrive; make "what happens next" explicit.
- **Craft of numbers:** beautiful typography for figures (tabular, large, well-spaced decimals) is a brand asset.
- **Color beyond blue:** warm neutrals, deep greens, black with a signature accent, or bold flat color fields.
- **Physical card and packaging:** material, edge color, vertical orientation and unboxing are differentiators.

## Category clichés

- Shields, padlocks, piggy banks, upward arrows, handshakes, coins showering.
- Navy-blue gradients with a glowing credit card floating in 3D.
- Stock photos of smiling couples looking at a laptop or a phone.
- "Banking, reimagined." / "Finance made simple." headlines.
- Purple-to-pink gradient neobank look that every 2018-2022 startup used.

## Regulatory and compliance notes

These shape design; confirm exact requirements with counsel for the specific product and jurisdiction.

- **Disclosures:** deposit insurance statements (FDIC in the US, FSCS in the UK) and partner-bank disclosure for non-bank fintechs; investment products need "not insured, may lose value" style statements; APR/APY presentation rules (US Truth in Lending and Truth in Savings).
- **Marketing rules:** UK FCA financial promotions rules (fair, clear, not misleading; risk warnings for investments and crypto); US SEC/FINRA advertising rules for investment products.
- **Accessibility:** banks are frequent targets of accessibility litigation (ADA in the US); the European Accessibility Act applies to banking services in the EU from June 2025. Treat WCAG 2.2 AA as the minimum.
- **Privacy and security:** GDPR/CCPA consent and data minimization; PCI DSS scope affects how card data entry is designed (use the payment provider's hosted fields).
- **Strong customer authentication:** PSD2 SCA in the EU/UK requires two-factor flows for many payments; design step-up authentication without dead ends.

## Key deliverables and screens

- Marketing site: hero with product promise, pricing/fees page, security page, legal disclosures, help center.
- App: onboarding with identity verification (KYC), home/balance, transaction list and detail, send/request flow, card controls, statements, notifications, settings and security.
- Brand: logo, card design, app icon, motion for success/failure states, notification copy system.
- Investor/partner decks and compliance-ready email templates.

## Voice and content

- Plain language (aim for reading grade 6-8), active voice, no jargon without definition.
- Numbers formatted for the locale; negative amounts shown with a minus sign and color plus text, never color alone.
- Error and decline messages say what happened, why (when allowed), and what to do next.
- Celebrate quietly: "Sent. Arrives in about 2 minutes." beats confetti.

## Recommended directions

- **Category-expected:** `style.corporate-modern` + `archetype.ruler` + `tier.premium`: navy or deep green on warm white, refined sans, restrained motion. Safe and credible; differentiate through numeral typography and transparency.
- **Adjacent:** `style.swiss-international` or `style.editorial-magazine` + `archetype.sage`: borrowed from financial publishing and consultancies; strong grid, bold numerals, opinionated content. Feels expert rather than salesy.
- **Category-breaking:** `style.neo-brutalist` + `archetype.everyperson` (for `audience.teens-gen-z`): flat saturated color, thick outlines, chunky type, honest copy. High recall, signals "not your parents' bank". Risk: can read as unserious for large balances; keep transactional screens calm and conventional.

## Metrics that matter

- Onboarding and KYC completion rate, time to first funded account.
- Successful payment rate, failed or abandoned transfer rate at confirmation.
- Support contacts per 1,000 active users (especially "where is my money" and fee questions).
- App store rating and accessibility complaints.
- Marketing: application starts, qualified sign-ups, cost per funded account.

## Reference anchors

- Monzo and Starling (UK) for plain-language tone and hot-coral / teal identities
- Revolut and Wise for transparent fee and FX presentation
- Stripe for developer-grade product marketing and documentation design
- Robinhood for the 2010s mobile-first investing aesthetic and its regulatory scrutiny over gamified UX
- Mercury (business banking) for restrained dark/light premium fintech
- GOV.UK Design System patterns for plain-language forms and error messages
