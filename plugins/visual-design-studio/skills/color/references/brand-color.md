# Brand color

Version-Timestamp: 2026-10-20 02:07:10 UTC

A brand color is ownable when the category does not already use it, it fits the brand's idea, and it is specified so precisely that every printer, screen and supplier reproduces the same thing. Ownership usually comes from a combination (hue plus lightness plus chroma plus a signature pairing), not from a hue name.

## Method

1. **Map the category.** Collect the primary brand colors of 8-12 competitors and adjacent brands. Convert each to OKLCH (`python3 ../../../library/scripts/color_tools.py convert '#hex'`) and plot them on hue (angle) and lightness (radius) or in a simple table. Read the industry entry's *Category conventions* and *Where to differentiate* (`python3 ../../../library/scripts/atlas.py show industry.<slug>`).
2. **Find white space.** Look for an empty hue, or an occupied hue at a different lightness or chroma (deep forest green in a bright-green category), or an unexpected pairing (black with acid yellow in a navy category).
3. **Tie it to the idea.** The archetype entry (`archetype.*`, *Visual translation*) and the brand strategy give the reason. A color without a reason is decoration.
4. **Decide belong or break.** Regulated, high-trust categories may want to stay near convention and differentiate with a secondary color or neutral. Challenger brands break. State the risk.
5. **Test in use** (below), then build the ramp ([OKLCH ramps](oklch-ramps.md)) and the UI roles ([palette architecture](palette-architecture.md)).
6. **Specify** every format the brand will be produced in (table at the end).

## Category color map

| Category (atlas ID) | Crowded hues | Ways to differentiate |
| --- | --- | --- |
| Banking and fintech (`industry.fintech-banking`) | Navy, royal blue, green; neobank black with a vivid accent; the 2018-2022 purple-to-pink gradient | Deep teal, oxblood, warm coral, saffron, warm neutrals with one bold accent |
| B2B SaaS (`industry.saas-b2b`) | Blue, indigo, violet, gradient purple | Moss and olive, burnt orange, ink and paper with one signal color, deep ultramarine with warm neutrals |
| AI products (`industry.ai-products`) | Violet and indigo gradients, black with neon, "aurora" blurs | Warm off-white and terracotta, ink black and a single primary, paper textures, earth tones |
| Developer tools (`industry.developer-tools`) | Black and charcoal with neon green, purple or cyan | Off-white documentation-first palettes, amber terminals, saturated primaries on neutral |
| Healthcare (`industry.healthcare-provider`) | Blue, teal, green, white | Warm clay, deep plum, soft coral, sage with ink; avoid the red cross emblem |
| Digital health and wellness (`industry.digital-health-wellness`) | Pastel mint, lavender, peach | Saturated sunrise orange, deep green, confident ink with one bright accent |
| Food, beverage, CPG (`industry.food-beverage-cpg`) | Red, yellow, orange, kraft brown, organic green | Unexpected cool hues for a warm category, very dark packaging, two-color signature pairs |
| Luxury (`industry.luxury-goods`, `tier.luxury`) | Black, gold, ivory, deep green | One signature hue used consistently over decades; restraint and material over metallic effects |
| Kids and family (`industry.kids-family`) | Rainbow primaries | A limited 3-4 color set with one signature hue, softened but not pastel-only |
| Energy and climate (`industry.energy-climate`) | Green, leaf, blue sky | Warm sun yellows, deep earth, electric accents on dark neutrals |
| Government and civic (`industry.government-civic`) | Navy, flag colors | Usually stay conventional; differentiate by clarity, not hue |

Example ownable colors (computed, WCAG ratios against white and against #111111):

| Name | OKLCH | Hex | White text | Dark text |
| --- | --- | --- | --- | --- |
| Oxblood | 0.38 0.12 20 | #751E26 | 10.66:1 | 1.77:1 |
| Plum | 0.38 0.10 330 | #5F2C5B | 10.51:1 | 1.80:1 |
| Forest | 0.30 0.05 150 | #1A3520 | 13.34:1 | 1.42:1 |
| Slate blue | 0.45 0.06 250 | #3B5876 | 7.39:1 | 2.56:1 |
| Moss | 0.50 0.10 130 | #506E2C | 5.82:1 | 3.24:1 |
| Jade | 0.55 0.09 165 | #358264 | 4.64:1 | 4.07:1 |
| Signal orange | 0.62 0.19 45 | #D85A04 | 3.90:1 | 4.84:1 |
| Coral | 0.70 0.15 35 | #EC785B | 2.84:1 | 6.66:1 |
| Saffron | 0.80 0.16 80 | #F3B01D | 1.90:1 | 9.93:1 |
| Acid yellow | 0.88 0.17 105 | #E9DD3C | 1.41:1 | 13.37:1 |

Mid-lightness colors (signal orange, jade) pass neither white nor dark text comfortably; use them as large fills, illustration and logo colors, and derive darker ramp steps for text.

## Ownership by color: public anchors

Several brands are publicly identified with a color, and some have pursued trademark protection for it: Tiffany & Co. (robin's-egg blue), UPS (brown), Deutsche Telekom and T-Mobile (magenta), Christian Louboutin (red soles), John Deere (green with yellow). Color marks are possible in some jurisdictions when the color has acquired distinctiveness in a specific class of goods. Check that a chosen color does not collide with a protected color mark in the client's category; confirm with counsel for the specific product and jurisdiction.

## The generic purple and indigo default

The look most associated with AI-generated and template SaaS design is an indigo-to-violet-to-pink gradient on white or near-black. Reference values: Tailwind's indigo-500 #6366F1 (oklch 0.59 0.204 277), violet-500 #8B5CF6 (oklch 0.61 0.219 293), pink-500 #EC4899 (oklch 0.66 0.212 354). White text on #6366F1 is 4.47:1, just under AA for body text.

Purple is not banned; using it because it is the default is the problem. If the strategy points to purple:

- Make it deeper (plum, L 0.35-0.40) or dustier (chroma 0.06-0.10) instead of electric.
- Pair it unexpectedly (plum with mustard, violet with olive, lilac with oxblood).
- Drop the gradient; use flat fields and let type or imagery carry energy.
- Check the category map: in SaaS and AI it is the most crowded hue.

## Test a candidate before committing

- Logo at full size, favicon at 16px and app icon at 1024px; on white, on black, on a photo.
- A large field: does it vibrate, look cheap, or tire the eye? Saturated reds and blues vibrate when adjacent.
- Next to status colors: a red brand fights `--color-danger-*`; a green brand fights success. Shift the status hue or reserve the brand for non-interactive use.
- Grayscale: the brand color must hold its place in the value hierarchy.
- Print proof on coated and uncoated stock; screen on sRGB and P3 displays.
- Photography and illustration: does the color work with the art direction, or does it need a neutral buffer?
- Dark mode variant: lighter and lower chroma, same hue (see [dark mode](dark-mode.md)).

## Specifying color in brand guidelines

| Format | Where | How to get it right |
| --- | --- | --- |
| HEX and sRGB | Web, apps, office documents, video | The master screen value; record the OKLCH source too |
| OKLCH | Design tokens | Token `$description` holds the source coordinates |
| Display P3 (optional) | Modern screens | A more saturated variant behind `@media (color-gamut: p3)` |
| Pantone Coated (C) and Uncoated (U) | Spot-color print, packaging | Choose from a physical Pantone guide, not a screen; C and U chips of the same number look different, so specify both and approve on paper |
| CMYK | Process print | Convert from Pantone or RGB with the target profile and name the profile (for example FOGRA51 or FOGRA39 for coated stock in Europe, GRACoL 2013 / CRPC6 in the US, Japan Color 2011 in Japan); ask the printer for their standard |
| RAL or NCS | Paint, signage, architecture, vehicles | Match from physical fan decks under daylight |
| Textile references (for example Pantone TCX) | Apparel, merchandise | Approve lab dips on the actual fabric |
| Vinyl, thread, enamel | Signage film, embroidery, pins | Supplier-specific color charts; approve samples |

Production notes:

- Many vivid screen colors (bright greens, oranges, cyans, electric blues) are outside CMYK. Check the gamut warning; specify a Pantone spot color or accept a documented CMYK compromise.
- Rich black for large areas: a common build is C60 M40 Y40 K100; small text uses 100K only. Keep total ink within the printer's limit (often 300-320% on coated stock, lower on uncoated and newsprint).
- Pantone libraries in design tools now require a Pantone Connect subscription; physical guides remain the reference.
- Record every value in one table per color so suppliers never convert on their own:

```text
Meridian Teal (UI accent, teal 600)
  Screen   HEX #006C6C   sRGB 0 108 108   OKLCH 0.481 0.082 195
  Print    Pantone ____ C / ____ U (approved on stock, date)   CMYK __ __ __ __ (profile: FOGRA51)
  Other    RAL ____   Vinyl ____   Thread ____
  Usage    Primary buttons, links (teal 700), section fields. Text on it: white (6.25:1).
```

Leave the Pantone and CMYK fields blank until they are matched and proofed; never guess them from hex.
