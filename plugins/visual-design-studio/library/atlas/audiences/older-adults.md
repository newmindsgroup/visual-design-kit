---
id: audience.older-adults
axis: audience
name: Older Adults (65+)
aliases: [seniors, older adults, elderly, retirees, silver surfers, 65 plus, boomers, aging users]
summary: Adults 65+ with varied digital skill and age-related changes in vision, dexterity and memory; design for large text, 7:1 contrast, large targets, patient flows and a human support route.
tags: [older adults, seniors, aging, large text, high contrast, healthcare, retirement, accessibility]
pairs_with: [style.civic-plain, style.clinical-calm, style.flat-material, industry.healthcare-provider, industry.insurance, industry.government-civic, industry.fintech-banking, archetype.caregiver, archetype.everyperson, channel.print-collateral]
avoid_with: [style.glass-spatial, style.kinetic-experimental-type, style.y2k-cyber, style.soft-ui-neumorphic, style.dark-tech-developer]
version_timestamp: 2026-10-20 02:08:35 UTC
---

# Older Adults (65+)

## Who and what they need

- **Not one group.** A 66-year-old product manager and an 86-year-old first-time smartphone user share an age label, not a skill level. Segment by digital confidence, vision, dexterity and whether a family member helps.
- **Common changes:** reduced contrast sensitivity and glare tolerance, yellowing of the lens (blue-dark and blue-green pairs blur), presbyopia, hearing loss, tremor or arthritis that makes precision taps hard, slower recall of multi-step procedures. Many have more than one.
- **Needs:** legibility without asking for it, predictability, time, clear labels instead of icon guesswork, confirmation before irreversible actions, and a human they can call.
- **Behavior (NN/g senior studies, 2002 with updates through 2019):** older users read more of the page, struggle with small targets, hover menus and double-click, distrust unexpected popups, and often blame themselves for errors. They are not less capable users; they are less forgiven by bad design.
- **Context:** tablets and large phones, shared household devices, healthcare portals, banking, benefits, telehealth, family photos and video calls.

## Design defaults

| Variable | Default for this audience | General default | Source or reasoning |
| --- | --- | --- | --- |
| Minimum body text | 18px (20px for health and money detail); floor 16px; layouts survive OS text at 200% | 16px | WCAG 2.2 SC 1.4.4 and 1.4.10; Apple Dynamic Type; NN/g senior usability |
| Target size | 48px with 8-12px spacing; primary buttons full width on phones | 44px | Material 48dp; WCAG 2.5.5; NN/g on small-target errors |
| Contrast | 7:1 for body text, 4.5:1 for large text, 3:1 for icons and borders | 4.5:1 | WCAG 2.2 SC 1.4.6 (AAA); contrast sensitivity falls with age |
| Reading level | Grade 6-8, sentences under 20 words, no jargon or abbreviations | Grade 8 | plainlanguage.gov; health-literacy guidance from NIH and CDC (verify) |
| Line length | 50-70 characters, line-height 1.5-1.6, left-aligned, never justified | 60-75ch | WCAG 2.2 SC 1.4.8 (max 80 characters) |
| Motion | 250-400ms ease-out; no auto-advancing carousels, parallax or scroll-jacking; every moving element can be paused | 120-240ms | WCAG 2.2 SC 2.2.2 and 2.3.3 |
| Information density | Low: one primary task per screen, 5 to 7 choices, visible text labels beside every icon | Medium | COGA guidance on limiting choices; NN/g |
| Session and timeouts | Warn 60 seconds or more before timeout (WCAG minimum is 20 seconds) and allow extension; save progress; avoid timeouts under 20 minutes in forms | Standard | WCAG 2.2 SC 2.2.1 and 2.2.6 |
| Error tolerance | Very high: review step before submit, undo, plain error text near the field, support phone number on every screen | Inline validation | WCAG SC 3.3.1, 3.3.3, 3.3.4 |
| Authentication | Allow paste and password managers, SMS code autofill, biometrics; no puzzles or memory tests | MFA | WCAG 2.2 SC 3.3.8 (AA) |
| Weight and type | Regular 400 or heavier body; no light weights; humanist sans with open apertures | Any | Thin strokes vanish with reduced contrast sensitivity |

## Interaction and content

- **Labels over icons.** Every control has a visible word; icon-only is acceptable only for universal ones (search, close) and still carries an accessible name.
- **Make state obvious:** show current step ("Step 2 of 4"), underline links, make selected states differ by shape and weight not hue alone.
- **Avoid:** hover-only menus, drag-and-drop as the sole method, double-tap, long-press, swipe-only navigation, tiny dropdowns, infinite scroll, CAPTCHAs with puzzles.
- **Forms:** one question per screen for complex tasks; labels above fields; examples in hint text, not placeholders; tolerant input for dates, phone numbers and spaces.
- **Confirm consequences** in plain words ("This sends $250 to Jane Smith today. You cannot cancel it.") with a clear "Go back" option.
- **Offer assisted modes:** large-text mode, simplified home screen, delegated or proxy access for a trusted family member, print and phone alternatives. Apple's Assistive Access and Android's simple launchers show demand.
- **Scam awareness:** state what you will never ask for, avoid false urgency in your own messages, and give a way to verify a communication.
- **Help:** visible phone number, callback option, human chat, captioned short videos, large-print PDF.

## Visual tone

- **Dignified, warm, high-contrast.** Ink #1A1A1A on white is 17.40:1; on warm paper #F4F1EA (oklch 0.96 0.010 87) it is 15.43:1. Primary blue #0B4A9E (oklch 0.43 0.149 258) is 8.44:1 on white; danger #B42318 (oklch 0.50 0.182 30) 6.57:1; success #14602F (oklch 0.43 0.107 150) 7.65:1. Secondary text #595959 is 7.00:1 on white, about the lightest gray to allow.
- **Type:** Atkinson Hyperlegible (OFL, Braille Institute), Source Sans 3, Public Sans or Noto Sans; commercial: Frutiger, Myriad Pro. Use sentence case, never all caps for sentences.
- **Imagery:** real people 65+ in varied, active, ordinary situations; avoid stock "grandparent holding a tablet" and the pill-organizer cliché.
- **Avoid childish or clinical beige.** Respect says "capable adult", not "patient".

## Pitfalls

- Light gray text and 12-14px captions; neumorphic or glass surfaces that erase edges.
- Designing only for vision and forgetting hearing (captions), motor (tremor) and cognition (memory, attention).
- A digital-only service with no phone, mail or in-person route.
- Short session timeouts that discard half-completed forms.
- Condescending tone, oversimplified content, or "senior mode" that removes useful features.
- Testing with young staff pretending to be old; recruit real participants and include assistive tech users.
- Scammy-looking urgency (countdowns, "act now") that mimics fraud patterns.

## Regulatory and compliance notes

- **US:** ADA Title III applies to public-facing business sites in practice via WCAG 2.1/2.2 AA expectations in settlements and case law; ADA Title II web rule (DOJ, 2024) requires WCAG 2.1 AA for state and local government with compliance dates starting April 2026 (verify exact dates in the Federal Register); Section 508 for federal ICT and procurement.
- **EU:** European Accessibility Act applies from 28 June 2025 to consumer banking, e-commerce, e-books, transport ticketing and electronic communications services, with a microenterprise exemption for services; EN 301 549 is the harmonized standard.
- **UK:** Equality Act 2010 duty of reasonable adjustments; public-sector sites follow WCAG 2.2 AA via GOV.UK practice.
- **Medicare marketing (US):** CMS Medicare communications guidelines set minimum font sizes for required marketing materials (12-point, large print 18-point; verify the current CMS manual).
- **Age in marketing:** US ECOA, Fair Housing and ADEA limit age-based targeting in credit, housing and employment advertising.
- **Financial safeguards:** trusted-contact and elder-exploitation rules (for example FINRA Rule 2165) influence delegated-access and alert flows.

Confirm requirements with counsel for the specific product and jurisdiction.

## Reference anchors

- Nielsen Norman Group, *Usability for Senior Citizens* and later *Seniors as Web Users* reports
- W3C WAI-AGE, *Web Accessibility for Older Users: A Literature Review* and *Developing Websites for Older People*
- WCAG 2.2 (W3C Recommendation, October 2023); plainlanguage.gov Federal Plain Language Guidelines
- Apple Human Interface Guidelines: Accessibility, Dynamic Type; Apple Assistive Access
- GOV.UK Design System for plain forms and error messages
- Braille Institute, Atkinson Hyperlegible typeface
