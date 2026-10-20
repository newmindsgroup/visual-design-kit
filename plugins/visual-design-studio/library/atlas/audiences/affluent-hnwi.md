---
id: audience.affluent-hnwi
axis: audience
name: Affluent and High-Net-Worth
aliases: [hnwi, uhnw, affluent, wealthy clients, private clients, private banking, family office, luxury clients, mass affluent]
summary: Time-poor, privacy-conscious and often 50+ clients who judge a brand by discretion, service and flawless execution; design for quiet confidence, human escalation, low friction and legible type.
tags: [affluent, hnwi, wealth, private banking, luxury clients, concierge, discretion, family office, privacy]
pairs_with: [style.classic-luxury-serif, style.quiet-minimal, style.editorial-magazine, industry.luxury-goods, industry.fintech-banking, industry.real-estate-proptech, archetype.ruler, tier.premium, tier.luxury, tier.ultra-luxury]
avoid_with: [style.playful-bubbly, style.vibrant-gradient-saas, tier.value, archetype.jester]
version_timestamp: 2026-10-20 02:08:35 UTC
---

# Affluent and High-Net-Worth

## Who and what they need

- **Definitions vary by source.** Capgemini's World Wealth Report counts high-net-worth individuals as holding US$1 million or more in investable assets (excluding primary residence, collectibles and consumables). Wealth-intelligence firms such as Altrata define ultra-high-net-worth at US$30 million or more in net worth. "Mass affluent" is a looser band below US$1 million. Confirm the definition your client uses.
- **Segments differ:** founders and executives (time-poor, decisive), inheritors and next-generation heirs (digital-native, values-driven), retirees (older-adult needs apply), and families with advisors, assistants and family-office staff who act on their behalf.
- **Needs:** discretion and privacy, speed with zero friction, a named human who knows them, edited choice instead of catalog sprawl, trust that nothing will go wrong, and recognition without ostentation.
- **Skews older.** Many wealth holders are 55+, so legibility rules from `audience.older-adults` apply even when the brand tone is understated.
- **Context:** iPad and iPhone, assistants managing accounts, multiple currencies and time zones, travel, shared access across entities (trusts, companies, family members).

## Design defaults

| Variable | Default for this audience | General default | Source or reasoning |
| --- | --- | --- | --- |
| Minimum body text | 17-18px; captions 13px or more; never 11px gray on cream | 16px | Older-skewing readership; WCAG 1.4.4; NN/g senior usability |
| Target size | 44-48px, generous spacing; no tiny text links in dense footers | 44px | WCAG 2.5.5; Apple HIG |
| Contrast | Body 7:1 or better, secondary text 4.5:1, dark mode supported; brass and stone tones are decoration unless they pass | 4.5:1 | WCAG 1.4.3, 1.4.6 |
| Reading level | Grade 8-10, confident and economical; sentences under 20 words; precise numbers; no hype | Grade 8-10 | plainlanguage.gov; executives skim |
| Line length | 55-70 characters for editorial copy; wide margins | 60-75ch | Editorial convention |
| Motion | 300-500ms ease-out, no bounce, no gamification, no confetti; instant response to input | 120-240ms | Quiet confidence; reduce-motion respected |
| Information density | Low to medium on marketing; medium-high in portfolio and statement views, where they expect depth and export | Medium | Private-banking reporting norms |
| Session and attention | Short, high-intent, multi-device handoffs; "speak to your advisor" always visible; callback within a promised window | Self-serve | Service-led relationships |
| Error tolerance | Near zero for glitches, typos and downtime; every failure names a human contact and a time frame | Standard | A flaw reads as carelessness |
| Privacy defaults | Minimal data collection, discreet notifications (no amounts on lock screen), passkeys or biometrics, device and travel management | Opt-out tracking | High-value fraud and social-engineering targets |
| Access model | Delegated roles for assistants, advisors and family members; entity switcher; audit trail | Single user | Real usage patterns |

## Interaction and content

- **Concierge-first journeys.** Replace "Buy now" with "Request", "Reserve", "Speak with an advisor" or "Arrange a private viewing", then back it with a real response-time promise.
- **Edited choice:** present 6-12 considered options with provenance, craft or performance detail, not 10,000 SKUs. Provide private-appointment booking, waitlist or allocation only when genuinely true; never fake scarcity.
- **Onboarding with KYC:** explain why each document is needed, allow advisor-assisted completion, secure uploads, status tracking and a named contact.
- **Wealth views:** consolidated holdings across custodians, entity and family structure views, performance with clear methodology, tax and statement documents, secure vault, export to PDF and spreadsheet.
- **Security without friction:** step-up authentication for transfers, trusted devices, out-of-band confirmation of changes, clear phishing guidance, travel notices.
- **Voice and copy:** understated and exact. Avoid "exclusive", "elite" and "VIP" as adjectives; show rather than claim. Plain disclosures, no jargon walls, and a human-sounding error message.
- **Channels:** email, secure messaging and phone; many clients use iMessage or WhatsApp with advisors, so define compliant channels for records.

## Visual tone

- **Quiet confidence, material richness, restraint.** Ivory #F6F3EC (oklch 0.96 0.010 87) with ink #16181A (oklch 0.21 0.005 248) is 16.06:1; deep green #1F3B34 (oklch 0.33 0.037 176) carries ivory text at 10.93:1; secondary #5E5A52 (oklch 0.47 0.014 85) is 6.19:1. Brass #8A6E3F (oklch 0.55 0.073 79) is only 4.32:1 on ivory, so use it for rules and large display; for brass text use #6E5426 (oklch 0.46 0.072 80) at 6.40:1. On dark #0F1714 (oklch 0.20 0.013 170), champagne #C8AE7A (oklch 0.76 0.075 84) is 8.49:1.
- **Type:** serif display (Newsreader, Fraunces, Cormorant Garamond; OFL; commercial: Canela, GT Super, Tiempos Headline) with a quiet grotesque body (Hanken Grotesk, Instrument Sans; commercial: Söhne, Graphik). Caps labels at 12px, +0.08em.
- **Geometry:** 0-4px radius, 1px hairlines, almost no shadow, section spacing 96-160px, photography with natural light, grain and a material close-up.
- **Imagery:** real places, objects, craftsmanship and people in natural contexts; avoid private jets, champagne towers, gold-on-black clichés and "wealthy couple on a yacht" stock.

## Pitfalls

- Equating luxury with unreadability: 11px stone-on-cream text, hairline weights and hidden navigation.
- Exclusivity theater: "request access" gates with no response, fake "only 2 left" scarcity.
- Ostentation (gold foil, script type, black-and-gold everything). Many wealth holders prefer understatement.
- Friction in the name of security that blocks a time-poor client, or glitches that signal carelessness.
- Hiding contact details and prices behind forms; assuming everyone wants a DM or chatbot instead of a person.
- Designing for the principal only; assistants, advisors and heirs are users too.
- Generalizing: new-money entrepreneurs, inherited wealth and retirees want different tones. Interview, do not assume.

## Regulatory and compliance notes

- **Financial promotions:** UK FCA financial promotion rules include exemptions for certified high-net-worth individuals (income of at least £100,000 or net assets of at least £250,000, with prescribed statements) and sophisticated investors; the FCA tightened promotion rules for high-risk investments in 2023-2024 (verify what applies). US accredited-investor status under SEC Regulation D (generally income above US$200,000, or US$300,000 jointly, or net worth above US$1 million excluding primary residence, or certain licenses) shapes who may see offerings and how self-certification flows must work. Check current thresholds.
- **Advertising by advisers:** US SEC Marketing Rule (testimonials, endorsements, performance advertising) and FINRA communications rules; UK FCA Consumer Duty.
- **Onboarding:** KYC and AML, sanctions and politically exposed person checks, FATCA and CRS reporting; design the flow to explain and minimize collected data.
- **Privacy and security:** GDPR, CCPA, financial-privacy rules (US GLBA), breach notification; discreet notification content.
- **Accessibility:** ADA and EAA still apply, and the audience skews older; do not trade compliance for atmosphere.
- **Luxury goods:** authenticity claims, origin and sustainability claims (EU Green Claims proposals, FTC Green Guides) need substantiation.

Confirm requirements with counsel for the specific product and jurisdiction.

## Reference anchors

- Capgemini, *World Wealth Report* and Altrata (formerly Wealth-X), *World Ultra Wealth Report* for segment definitions (verify latest editions)
- Private banks such as Julius Baer and Coutts for client-portal conventions; Mercury for restrained fintech craft
- Aman, Rolls-Royce Motor Cars, Loro Piana and Hermès for restrained, service-led brand experience
- Monocle and *Financial Times: How To Spend It* for editorial tone and curation
- Jean-Noël Kapferer and Vincent Bastien, *The Luxury Strategy* (2009)
- Nielsen Norman Group senior usability reports for legibility defaults
