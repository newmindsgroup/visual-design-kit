---
id: tier.value
axis: tier
name: Value / Mass Market
aliases: [value, mass market, budget, discount, low price, economy, everyday low price, private label, hard discount]
summary: Price is the hero; the design signals savings, clarity and speed with loud color, heavy sans type, big numerals and dense, honest layouts that stay disciplined rather than cheap-looking.
tags: [value, budget, discount, mass market, price-led, private label, promotional, utility, savings]
pairs_with: [industry.ecommerce-dtc, industry.food-beverage-cpg, industry.marketplaces-platforms, industry.fashion-apparel, style.flat-material, style.playful-bubbly, style.data-dense-utilitarian, style.bold-geometric-sport, archetype.everyperson, audience.low-bandwidth-entry-devices]
avoid_with: [style.classic-luxury-serif, style.fashion-editorial-didone, industry.luxury-goods, audience.affluent-hnwi]
version_timestamp: 2026-10-20 02:08:35 UTC
---

# Value / Mass Market

## Signals

- **The promise:** "Good enough for the job, at a price that respects your budget." Value shoppers are smart, not poor; they compare, and they distrust anything that looks like it hides a markup.
- **What the eye reads as value:**
  - Price is the largest or highest-contrast element, set in heavy numerals, often with a unit price.
  - Saturated primaries (yellow, red, blue) and flat color blocks that read from 5 meters away.
  - Dense grids of products, multipacks, bundles and "3 for 2" mechanics.
  - Heavy sans or condensed type, uppercase headlines, simple badges and ribbons.
  - Plain materials, direct-printed packaging, standard sizes, visible product through windows.
  - Utility copy: benefit in 2-4 words, no ornament.
- **Disciplined value is a strong brand:** Aldi, Lidl, IKEA, Uniqlo and Muji show that low price and high design coherence coexist. The failure is clutter, not low price.
- **Where this tier sits** (illustrative price per 50 ml of moisturizer; varies by market):

| Tier | Core promise | Indicative price | Buying logic |
| --- | --- | --- | --- |
| **Value** | Same job, lowest cost | $1-4 | Price comparison, habit, promotions |
| Mid-market | Reliable, smart choice | $8-25 | Reviews, familiarity, benefits |
| Premium | Better materials and expertise | $35-90 | Quality evidence, brand story |
| Luxury | Desire, heritage, symbol | $200-500 | Emotion, status, craftsmanship |
| Ultra-luxury | Rarity, bespoke, discretion | $600-2,000+ | Relationship, provenance, access |

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Barlow Condensed ExtraBold, Archivo (width and weight axes), Anton or Oswald (all OFL); commercial: Druk, Knockout, Trade Gothic Bold Condensed |
| Body font | Roboto, Open Sans or Source Sans 3 (OFL); system-ui fallback; commercial: Helvetica Neue |
| Scale and size | Ratio 1.333; display 48-96px at weight 800-900, line-height 0.95-1.05; price numerals 1.5-3x body; body 16-18px / 1.4-1.5 |
| Tracking and case | Display uppercase, 0 to +0.01em; labels uppercase bold +0.04em |
| Weights | 400 and 700/800; no weights below 400 |
| Palette | Signal yellow #FFD100 (oklch 0.87 0.179 93); price red #D8232A (oklch 0.57 0.213 26); trust blue #0A3D91 (oklch 0.39 0.148 261); ink #1A1A1A (oklch 0.22 0 0); white #FFFFFF; shelf grey #F2F2F2 (oklch 0.96 0 0) |
| Checked pairs | Ink on yellow 11.91:1; white on red 5.01:1; white on blue 10.05:1; blue on yellow 6.88:1; ink on grey 15.55:1; red on yellow only 3.43:1 (large text or graphics only) |
| Proportions | 60% white or grey, 25% one saturated brand color, 10-15% price and promo accent |
| Spacing and density | 8px base; section gaps 24-48px; product grid 4-6 per row desktop, 2 on mobile |
| Radius, borders, shadow | Radius 0-6px; 2px solid borders; badges as starbursts or ribbons; no soft shadows (hard offset 0 2px at most) |
| Layout and grid | 12 columns, 16px gutters, edge-to-edge color bands, sticky price and basket bar on mobile |
| Imagery | Cut-out packs on white or flat color, hard flash lighting, multipack arrays, price-per-unit callouts, real use-case comparisons |
| Packaging and material | HDPE or PET tub or tube, direct print or shrink sleeve, 1-2 spot colors, color-coded variants, stackable standard formats, mono-material for cost and recycling |
| Motion | 100-150ms, cubic-bezier(0.2, 0, 0, 1); functional only (add to basket, price update); no entrance choreography; fast loads |
| Price presentation | Price first and largest; unit price beside it; was/now only when genuinely true; total with fees shown up front |
| Same product: moisturizer | 250 ml yellow-and-blue tub, "Daily Moisture" in condensed caps, "$2.49" at 56px, "3 for 2" starburst, dermatologist-tested icon, variants by color band |

## Imagery and copy

- **Imagery:** clear product shots, hands using the product, shelf-ready packs, comparison charts of size or quantity. Real people over polished models; photography can be bright and slightly flat. Avoid fake luxury cues (gold gradients, marble, silhouette models).
- **Copy:** short, literal and numerical. "Pay less. Get more." beats "Smart savings, reimagined." Lead with the benefit and the price; give unit prices; state conditions plainly ("Offer ends Sunday").
- **Voice:** friendly, direct, a touch of humor; never condescending about budget. Avoid shame words (cheap, poor); prefer smart, fair, everyday.
- **Promotions:** at most one or two badges per viewport so each can work; ending dates real; coupon codes copy with one tap.
- **Trust substitutes for polish:** return policy, price-match promise, reviews, clear delivery cost, visible customer service.
- **Performance is part of the tier:** many value shoppers use entry-level phones; see `audience.low-bandwidth-entry-devices`.

## Pitfalls

- **Price-signal mismatch.** The design says one tier while the price or product says another. Over-signaling (luxury look, mass price) triggers "too good to be true" suspicion and counterfeit associations; under-signaling (value look, premium price) invites price resistance and leaves margin unclaimed. Audit every cue (type, color, material, imagery, copy, price display, where it is sold); the eye reads the weakest cue first, so keep all cues within one tier step.
- **Masstige drift.** "Masstige" (mass plus prestige) names mass-market brands priced above the mass tier that borrow prestige cues; the term was popularized by Silverstein and Fiske in "Luxury for the Masses" (Harvard Business Review, 2003). A value brand adding gold foil, serif type and marble photography without changing price, product or distribution is faking masstige and confuses its shopper. Earn the move: change the product and price first, then the cues.
- **Clutter mistaken for value.** Ten badges, five fonts and no hierarchy read as chaotic, not cheap. Keep one grid, one type system and one promo mechanic per view.
- **Promotion fatigue and misleading prices.** Constant starbursts blunt each other. Fake "was" prices and drip fees draw regulators: the EU requires price reductions to reference the lowest price in the prior 30 days (Directive 2019/2161), the UK's Digital Markets, Competition and Consumers Act 2024 targets drip pricing and fake reviews (in force 2025; verify), and the US FTC has fee-disclosure rules of limited scope (verify). Confirm with counsel.
- **Accessibility traps:** yellow with white text, red on yellow at 3.43:1, condensed heavy type below 14px, text baked into badge images, color-only sale cues.
- **No ownable asset.** If the only identity is "cheap", competitors undercut you. Choose a signature color, shape, voice or format.
- **Bloated pages.** Autoplay video and heavy scripts defeat the audience; keep first load under about 500 KB where possible.

## Reference anchors

- Aldi and Lidl private-label packaging and store design
- IKEA catalog, wayfinding and product-label system
- Uniqlo and Muji for disciplined, low-ornament value retail
- Costco Kirkland Signature and Walmart Great Value as large-scale private-label identities
- Loblaw "No Name" generics (1978 plain yellow packaging) as an early value design icon
- Michael Silverstein and Neil Fiske, *Trading Up* (2003) and "Luxury for the Masses" (HBR, 2003)
