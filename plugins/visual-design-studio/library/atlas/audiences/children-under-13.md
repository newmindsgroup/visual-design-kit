---
id: audience.children-under-13
axis: audience
name: Children under 13
aliases: [kids, children, young children, preschool, early readers, tweens, kids apps, family apps]
summary: Young users with limited reading, fine-motor and abstract-reasoning skills; design for huge targets, audio and icons, forgiving flows and parent-gated commerce under strict child-privacy law.
tags: [children, kids, coppa, preschool, early readers, parental gate, playful, edtech, tweens]
pairs_with: [industry.kids-family, industry.education-edtech, style.playful-bubbly, style.illustrative-narrative, style.flat-material, archetype.innocent, archetype.jester, archetype.caregiver, channel.native-app, channel.packaging]
avoid_with: [style.web-brutalist, style.dark-tech-developer, style.fashion-editorial-didone, style.grunge-punk-zine, archetype.outlaw]
version_timestamp: 2026-10-20 02:08:35 UTC
---

# Children under 13

## Who and what they need

- **Three bands, not one audience.** Ages 3-5 are pre-readers who navigate by pictures, sound and trial and error. Ages 6-8 are early readers who still decode words slowly. Ages 9-12 read fluently, want to feel older than they are, and reject anything that looks "babyish". Design and test per band.
- **Two users.** The child uses the product; a parent or teacher buys it, grants consent, sets limits and judges safety. Design a child surface and a separate, adult-gated parent surface.
- **Needs:** instant, consistent feedback; one clear thing to do per screen; success within seconds; no way to get lost, break something or spend money by accident; praise for effort rather than speed.
- **Physical reality:** small hands, imprecise taps, palm rejection problems, shared devices, sessions interrupted by adults, headphones rarely worn, volume often high.

## Design defaults

Values are working defaults; validate with children of the target band in short, moderated, parent-consented sessions.

| Variable | Default for this audience | General default | Source or reasoning |
| --- | --- | --- | --- |
| Minimum body text | 3-5: avoid required text, any label 28-32px; 6-8: 22-24px; 9-12: 18-20px | 16px | NN/g children's usability studies (2002, 2010) report slower reading and trouble with small type; px values are working defaults |
| Typeface | Single-storey a and g, open counters, distinct I/l/1: Andika (SIL OFL), Lexend (OFL), Nunito (OFL) | Any legible sans | Early-reader letterforms match school handwriting models |
| Target size | 3-5: 72-96px (about 19-25 mm); 6-8: 56-64px; 9-12: 48px; 16-24px gaps | 44px with 8px gaps | WCAG 2.2 SC 2.5.8 (24px floor) and 2.5.5 (44px) are minimums, not child targets |
| Gestures | Tap and simple drag with snap zones 1.5x object size; no long-press, double-tap, pinch or edge swipes | Full gesture set | Fine-motor development; accidental activation |
| Contrast | 7:1 for text, 3:1 for graphics; never color alone | 4.5:1 text | WCAG 2.2 SC 1.4.6 and 1.4.11; roughly 1 in 12 boys has red-green color vision deficiency |
| Reading level | Pre-readers: audio plus icons, no required text; 6-8: grade 1-3, 8 words per sentence; 9-12: grade 4-6, 14 words | Grade 8 | plainlanguage.gov short-sentence guidance, tightened; Flesch-Kincaid as a check, not proof |
| Line length | 30-45 characters, line-height 1.6, one sentence per line for early readers | 60-75ch | Early readers lose their place on long lines |
| Motion | Expressive feedback 200-400ms with springy easing is welcome; loops stop after 5s or offer pause; no flashing above 3 per second; honor reduced motion | 120-240ms, functional | WCAG 2.2 SC 2.2.2 and 2.3.1; photosensitive seizures |
| Information density | 3-5: 1 task and 1-3 choices per screen; 6-8: up to 6; 9-12: up to 9; no page scroll under age 8 | 5-9 choices | Working memory is smaller; use paged steps over scrolling |
| Session and attention | Activity unit 3-5 min (3-5), 5-10 (6-8), 10-20 (9-12); natural stopping points; no streak guilt | Task-based | Working default; pair with parent-set time limits |
| Error tolerance | Maximum: no fail states, unlimited retries, gentle redirection, undo everywhere, parental gate before purchases and links out | Standard validation | Apple App Store Review Guideline 1.3 (Kids Category); Google Play Families policy |

## Interaction and content

- **Audio first for pre-readers.** Use recorded human voice (not synthetic) for every instruction; highlight words as they are read; let a tap on any label repeat it.
- **Navigation:** persistent home button at 72px+, no hidden menus, at most two levels, icon plus spoken label. Put settings, accounts, purchases and external links behind a parental gate that needs an adult-level task (a randomized word problem or spelled-out number); confirm the current store rules before shipping.
- **Feedback:** respond within 100ms with motion and sound; celebrate effort ("You tried three ways!"), never display "wrong" in red with a buzzer.
- **Language:** concrete and literal; no idioms, sarcasm or abstractions; address the child as "you"; use a mascot guide with a consistent voice.
- **Safety by design:** no open chat or free-text sharing; use pre-moderated phrases or emoji pickers; avatars instead of photos; no real names; no location display.
- **Commerce and ads:** no manipulative mechanics (countdowns, loot boxes, confirmshaming, streak-loss warnings); keep any advertising clearly separate and age-appropriate.
- **Drag and drop:** forgiving drop zones, objects snap home when dropped elsewhere, never vanish.

## Visual tone

- **Palette:** saturated but disciplined, with dark text on bright chips because white on bright fails. Ink navy #1F2A44 (oklch 0.29 0.050 266) on sunny #FFC93C (oklch 0.86 0.159 86) is 9.28:1; on mint #7BDCB5 (oklch 0.82 0.109 166) 8.65:1; on coral #FF7A6B (oklch 0.73 0.165 28) 5.60:1; on cream #FFF8E7 (oklch 0.98 0.024 88) 13.47:1. White on that coral is only 2.55:1; use it on blue #2563EB (oklch 0.55 0.215 263) at 5.17:1 instead.
- **Shape:** radius 16-28px, 3-4px outlines optional, chunky 2.5-3px icon strokes at 48-64px, generous padding.
- **Type:** Andika or Lexend for reading; a friendly rounded display face (Baloo 2, Fredoka; both OFL) for titles only.
- **Illustration:** characters with clear expressions, varied skin tones, abilities and family structures; avoid frightening or sarcastic imagery.
- **Age-up for 9-12:** flatter shapes, tighter radius (8-12px), more texture, less mascot; tweens abandon products that look made for younger siblings.

## Pitfalls

- Designing for the parent's taste (muted pastel nursery palettes) when the child is the user; pastel-on-pastel fails contrast.
- One "kids" design for ages 3-12; it bores the oldest and defeats the youngest.
- Hidden or tiny close buttons on sheets and ads; accidental taps that trigger purchases.
- Variable-reward and streak mechanics that regulators now treat as dark patterns for minors.
- Autoplaying sound, nagging mascots, forced tutorials that cannot be skipped by a returning child.
- Using photos of real children without documented guardian consent and a safeguarding review.
- Treating readability scores as proof; test comprehension with children.

## Regulatory and compliance notes

These shape design; regimes and dates change.

- **COPPA (US):** verifiable parental consent before collecting personal information (including persistent identifiers, photos, voice, geolocation) from children under 13. The FTC's amended rule was published 22 April 2025, took effect 23 June 2025 and required compliance by 22 April 2026; changes include separate consent for third-party disclosure and written retention and security programs (verify against the Federal Register text). Design impact: consent flows in the parent surface, no behavioral ads, no persistent identifiers in analytics by default.
- **UK Age Appropriate Design Code (ICO Children's code):** 15 standards for under-18s including best interests of the child, high-privacy defaults, geolocation off, no nudge techniques that weaken privacy, and age-appropriate presentation.
- **GDPR Article 8:** parental consent below the digital age of consent, set between 13 and 16 by each EU member state. **EU DSA Article 28** guidelines (2025) address minors' privacy, safety and ads.
- **US states:** state age-appropriate design and kids' privacy laws are being litigated; the California AADC was partly reinstated by the Ninth Circuit in March 2026 (verify current status).
- **Platforms:** Apple Kids Category (no third-party analytics or advertising; parental gate for links, purchases) and Google Play Families policy are often stricter than law.
- **Advertising to children:** US CARU guidelines, UK CAP Code, and rules on paid random items vary by market.

Confirm requirements with counsel for the specific product and jurisdiction.

## Reference anchors

- Nielsen Norman Group, *Usability of Websites for Children* reports (2002; design guidelines for ages 3-12, 2010)
- W3C, *Making Content Usable for People with Cognitive and Learning Disabilities* (COGA) and WCAG 2.2
- Apple App Store Review Guidelines, Kids Category; Google Play Families policy
- UK ICO, *Age appropriate design: a code of practice for online services*
- PBS KIDS, Toca Boca, Khan Academy Kids, Sesame Workshop products for age-banded interaction design
- SIL International, Andika typeface (designed for literacy)
