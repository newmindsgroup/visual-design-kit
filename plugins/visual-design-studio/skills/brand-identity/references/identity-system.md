# Identity system

Version-Timestamp: 2026-10-20 02:07:10 UTC

People recognize brands by a handful of consistently used assets, and the logo is often not the strongest of them. Design the system that makes a piece recognizable with the logo covered: color, type, a graphic device, imagery, motion, sound and voice, each with rules tight enough to be consistent and loose enough to make new work.

## Elements beyond the logo

| Element | Define | Starting defaults |
| --- | --- | --- |
| Color | Roles, proportions, tints, accessible pairs, dark mode, print builds | 1-2 brand colors, 2 neutrals, 1 accent; proportion about 60% neutral, 30% brand, 10% accent; every text pair computed for 4.5:1 |
| Typography | Display, text and mono families; weights; scale; licensing for web, app, print and broadcast | 1 display + 1 text family (or 1 superfamily); 2-3 weights each; system fallbacks for Office (for example Arial and Georgia) |
| Graphic device | One ownable shape, line, frame, crop, pattern or texture derived from the logo or the idea | Rules for scale, crop, color, density and where it may not appear |
| Layout principles | Grid, margins, logo placement, typographic hierarchy | Logo in a fixed corner per format; margins as a % of the short edge (5-8%) |
| Photography | Subject, light, framing, grade, casting | See the imagery skill's photography reference |
| Illustration and icons | Style system, icon grid and stroke | One icon family; illustration palette drawn from brand colors |
| Data visualization | Categorical and sequential palettes, chart style | 6-8 categorical colors checked for color-vision deficiency |
| Motion | Logo animation, transitions, easing, durations | Logo sting 1-3 s; UI transitions 120-320 ms; one signature easing curve |
| Sound | Sonic logo, UI sounds, music direction | Sonic logo 1-3 s; must work on phone speakers |
| Voice and tone | Principles, vocabulary, tone shifts by context | 3-4 principles with do/don't examples |
| Templates | Social, deck, document, email, signage | Locked layouts with editable text and image slots |
| Tokens | Color, type, space, radius, motion as design tokens | DTCG source with brand overrides (for example `brands/<brand>.tokens.json` mapping to `--color-accent-default` and `--font-family-display`) |

## Distinctive assets first

Following Jenni Romaniuk's *Building Distinctive Brand Assets* (2018), plan which 2-3 assets the brand will own and use relentlessly: typically one color, one shape or device, and one more (a character, a typeface, a sound or a pack structure). An asset becomes distinctive only when it is both widely linked to the brand (fame) and not linked to competitors (uniqueness). Avoid assets that competitors already use; check them against the competitor audit.

## Building a graphic device

1. Derive it from the logo's geometry, the name, the product or the core idea, so it reinforces rather than competes with the mark.
2. Define the rules: allowed scales (for example 3 sizes), crops (bleeds off one or two edges only), rotation (0 or 90 degrees only), colors (which combinations), density (maximum one device per layout), and keep-out zones (never behind body text).
3. Stress-test it on six applications at real size: business card, social post 1080x1350, website hero, deck title slide, signage or vehicle, packaging or app screen.
4. Cover the logo on each application. If the piece is still recognizable, the system works.

## Fixed, flexible and dynamic identities

| Model | What changes | Public examples | Fits |
| --- | --- | --- | --- |
| Fixed | Nothing; one mark, strict rules | Most corporate identities | Regulated industries, small teams, low production capacity |
| Flexible | A container, color, image or pattern changes around fixed constants | AOL (2009, logo over changing images), Casa da Música (2007, form colored by its content) | Brands with many programs, seasons or campaigns |
| Responsive | The mark simplifies by size and context | Most modern logo sets (full lockup → symbol) | Every brand that lives on screens |
| Dynamic or generative | Rules or code produce many marks, sometimes driven by data | MIT Media Lab (2011), City of Melbourne (2009), Whitney Museum's "responsive W" (2013) | Cultural, tech and multi-program organizations with code and motion skills |

Rules for any non-fixed system:

- Hold at least two constants among shape, type, color and position, so variety still reads as one brand.
- Define the variable's range numerically (angles, scale steps, palette subset, data mapping) and curate an approved library of outputs. A generator without a library becomes chaos.
- Build the generator where the team works: a Figma component with variants, a variable font, an After Effects rig with expressions, or a small p5.js or JavaScript tool. Document inputs, outputs and export settings.
- Keep a fixed fallback version for contexts that cannot vary (legal documents, favicons, partner lockups).
- Assign an owner who approves new variations.

## Responsive logo breakpoints

| Context width | Version |
| --- | --- |
| 240px or more | Full horizontal lockup, with tagline if 300px+ |
| 120-240px | Horizontal lockup without tagline |
| 48-120px | Wordmark only or stacked lockup |
| Under 48px | Symbol or monogram, small-size master under 24px |

Measure the switch points on the real mark; these are starting values.

## Brand architecture models

David Aaker and Erich Joachimsthaler's brand relationship spectrum (*Brand Leadership*, 2000) is the standard frame.

| Model | Description | Public examples | Visual implications |
| --- | --- | --- | --- |
| Branded house | One masterbrand, products use descriptors | FedEx (Express, Ground, Freight), Google Workspace products | Shared logo, type and color; products differ by descriptor and maybe a color code |
| Sub-brands | Masterbrand plus a distinct product name | Apple iPhone, Microsoft Teams | Product names in the masterbrand's type; optional product icons from one family |
| Endorsed brands | Distinct brands with a visible endorser | Courtyard by Marriott, Nestlé KitKat | Each brand has its own mark; endorsement line at 30-50% of the brand's cap height in a fixed position |
| House of brands | Independent brands, parent mostly invisible to consumers | Procter & Gamble, Unilever portfolios | No shared visual language required; corporate identity only on corporate touchpoints |
| Hybrid | A mix, usually after acquisitions | Most large groups | Document which model each brand follows and why |

Choose by answering:

1. Do the offerings share an audience and a promise? Yes → branded house or sub-brands.
2. Could one offering's failure damage the others, or do they target conflicting segments or price tiers? Yes → endorsed or house of brands.
3. Is there budget to build several brands? No → branded house.
4. Are acquisitions or divestments likely? Yes → endorsed or house of brands keeps options open.

Sub-brand design rules:

- Name pattern decided once (descriptive "Brand Pay", coined "Brand + coined name", alphanumeric) and applied to every new product.
- Color coding by product works up to about 6-8 hues before codes stop being learnable; beyond that, code by family.
- Product icons from one shared grid and construction; see the imagery skill's iconography reference.
- Lockup grammar documented: masterbrand + descriptor spacing, size ratio and alignment.

## System testing and handoff

- Build a "system board": the six applications side by side, plus a covered-logo version of each.
- Test the palette on real content: data charts, error and success states, dark mode. Compute contrast for every text and UI pair.
- Turn decisions into tokens and templates before writing guidelines; guidelines should describe files that already exist.
- Hand off to the design-system skill for token architecture, and to the motion skill for logo animation.

## Common failures

- Logo plus a color and nothing else → add a graphic device and photography rules; run the covered-logo test.
- Every application improvises a new device → one device, three scales, documented crops.
- Flexible identity with no constants → fix two of shape, type, color, position.
- Sub-brands drawn as unrelated logos inside a branded house → shared construction and type.
- Ten product colors nobody can remember → family coding, or let names do the work.
