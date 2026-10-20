---
id: style.eco-natural-sustainable
axis: style
name: Eco / Natural / Sustainable
aliases: [eco design, natural branding, sustainable brand, earthy organic, green brand, botanical, low-impact design, regenerative]
summary: Earth-tone palettes, warm serifs, organic shapes and honest material and process imagery that signal care for people and planet, backed by specific proof rather than green decoration.
tags: [eco, natural, sustainable, earthy, organic, botanical, green, kraft, regenerative, calm]
pairs_with: [industry.energy-climate, industry.nonprofit-ngo, industry.food-beverage-cpg, industry.beauty-cosmetics, industry.hotels-travel, archetype.caregiver, archetype.explorer, archetype.innocent, tier.premium, channel.packaging]
avoid_with: [archetype.outlaw, industry.crypto-web3, industry.gaming-esports, tier.value]
version_timestamp: 2026-10-20 01:57:45 UTC
---

# Eco / Natural / Sustainable

## Essence

Look as if the product grew rather than was manufactured, and back it with proof. The style borrows from soil, bark, clay, linen and uncoated paper: warm neutrals, muted greens and earths, organic curves, tactile textures and natural light. It signals care, calm and transparency. Its main enemy is greenwashing: a leaf icon without evidence is worse than no leaf. The best eco design is specific (materials, origins, numbers, certifications) and light on resources itself.

## Visual signature

- Earth palette: bone and sand grounds, forest and moss greens, clay and ochre accents, deep ink-green text.
- Warm serif display with humanist or quirky sans text; generous line height, left-aligned.
- Organic shapes: arches, pebbles, leaf silhouettes, hand-torn edges, irregular masks (kept restrained).
- Paper, kraft, linen and stone textures at low opacity (3-8%), grain on photography.
- Honest photography: hands, raw materials, soil, workshops, process, natural light, matte color grade.
- Evidence modules: origin maps, material breakdowns, impact figures with sources, certification badges that are genuinely held.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Young Serif (OFL); Red Hat Display (OFL) for a modern, earthy sans; commercial: Reckless, Tiempos Headline, Canela Text |
| Body font | Karla (OFL); Work Sans (OFL); commercial: Freight Text, Sofia Pro |
| Mono (data, SKUs) | DM Mono (OFL) |
| Type scale ratio | 1.250 (major third); calm steps, display 44-72px |
| Body size / line-height | 17-18px / 1.6-1.65; measure 55-65ch |
| Display letter-spacing | -0.01em to -0.02em; line-height 1.1-1.15 |
| Caps / labels | 12-13px uppercase, +0.1em, weight 600, in moss deep for category tags |
| Weights | Display 400 (Young Serif is single-weight) or 600-700 for Red Hat Display; body 400, UI 600 |
| Palette | Bone #F8F4EA (oklch 0.97 0.014 89); Sand #EFE7D6 (oklch 0.93 0.024 86); Forest #1F3D2B (oklch 0.33 0.049 156); Moss deep #4A6A2E (oklch 0.48 0.095 132); Clay deep #9A4F37 (oklch 0.51 0.107 38); Sun #E0B341 (oklch 0.79 0.138 87); Ink #1B2A21 (oklch 0.27 0.026 158); Soft ink #4F5E54 (oklch 0.47 0.024 156) |
| Graphic-only hues | River #3E7C86 (oklch 0.55 0.066 209) for charts and large fills; lighter moss #5F7F3E (oklch 0.56 0.099 131) and clay #B5654A (oklch 0.59 0.111 39) for illustration, not text |
| Accent proportion | Bone/sand 60-70%, forest or ink 20-25%, moss/clay/sun accents 5-10%; avoid pure grass green (#4CAF50-like) as the dominant color |
| Radius | 12-24px for cards; arch masks (top radius 9999px) for hero images; 8px for buttons or pills |
| Borders | 1px forest at 20-30% opacity or a sand tone; dashed or hand-drawn rules for texture |
| Shadow / elevation | Very soft or none: `0 6px 20px rgb(31 61 43 / 0.08)`; prefer flat color separation |
| Spacing density | Calm: 8px base, section spacing 96-144px, wide margins; one idea per viewport |
| Grid | 12 columns; asymmetrical text/image pairs; organic overlaps allowed |
| Motion | 400-700ms ease-out cubic-bezier(0.22, 1, 0.36, 1); gentle fade-up of 12-16px; slow ambient sway for botanical art (6-10s) |

## Composition and layout

- Lead with the human or material story, then the product, then the proof. For example: farm or workshop photo, product, "Made from 100% recycled ocean plastic, third-party verified" with a link to the report.
- Alternate bone and sand bands with a single forest-colored band for the mission statement; keep text on flat colors.
- Add proof modules near claims: a "What it's made of" table (material, origin, percentage), a lifecycle graphic, certificate IDs, links to methodology.
- Design product pages around transparency: ingredients and materials in plain language, repair/reuse/refill options, end-of-life instructions.
- Keep the page light: system-friendly image formats (AVIF/WebP), lazy loading, limited video, small JavaScript. Show a performance or hosting statement only if true.

## Imagery and iconography

- Photography: natural light, matte tones, real people and real places, close-ups of texture; avoid hands cupping seedlings, globes, and glossy "eco" stock.
- Illustration: botanical line drawings or paper-cut shapes in the palette; seasonal or regional species for authenticity.
- Icons: 1.5-2px rounded line icons in forest; material and certification icons only where verified.
- Packaging cues: uncoated stock, one to two spot inks, blind deboss, kraft; the digital design should echo these constraints.
- Data: simple bars and dot maps in moss and clay, direct labels, sources and dates on every chart.

## Motion

Slow, grounded and optional. Fade up elements 12-16px over 500-700ms, let botanical art sway or grow once when entering view, and use scroll-linked reveals sparingly. Avoid autoplaying full-screen video and heavy WebGL; they raise energy use and data cost. Respect `prefers-reduced-motion` and `prefers-reduced-data` (a proposed media feature with little browser support, so also use the Save-Data hint) by serving still images.

## Fits and risks

- **Fits:** climate and clean energy (`industry.energy-climate`), nonprofits and conservation, organic food and refill brands, natural beauty, eco-hotels and travel, outdoor gear, B Corps, wellness. Matches `archetype.caregiver`, `archetype.explorer`, `archetype.innocent`.
- **Risks:** greenwashing and vague claims. Regulators treat unsubstantiated environmental claims as misleading: US FTC Green Guides, the UK CMA Green Claims Code, and the EU's rules on environmental claims (Directive (EU) 2024/825 restricts generic claims such as "eco-friendly" without proof; verify application dates and national rules). Confirm claims and badges with counsel. The look is also common to every "natural" shelf brand; differentiate through specifics and a distinctive hue (indigo, ochre, rust) rather than more beige.
- **Wrong for:** high-tech, hard-edged, nightlife and aggressive performance brands; low-price promotional retail where "premium natural" cues contradict the offer.
- **Why these pair:** `industry.nonprofit-ngo`, `industry.food-beverage-cpg`, `industry.beauty-cosmetics` and `industry.hotels-travel` sell provenance and care; `tier.premium` can justify materials and process; `channel.packaging` is where uncoated stock and honest materials become real.
- **Why these clash:** `archetype.outlaw` and `industry.gaming-esports` contradict calm, earth-bound tone; `industry.crypto-web3` carries an energy-use narrative that clashes with eco claims; `tier.value` rarely supports the cost of verified sustainable materials.

## Do and don't

- Do back every environmental claim with a number, a scope, a date and a source or certificate, and design the proof into the layout.
- Do use moss deep #4A6A2E and clay deep #9A4F37 for text accents; the lighter versions are for illustration.
- Do consider digital footprint: compress images, minimize scripts, avoid autoplay.
- Don't use a leaf, globe or recycling arrows as decoration; don't fake certifications.
- Don't make every surface kraft-textured; texture belongs behind headings or in small zones.
- Don't rely on green alone: pair color with labels (and avoid red-green pairs for impact charts).

## Clichés and AI tells

- Lazy version: a lime-to-teal gradient, a leaf in the logo, "Together for a greener future", stock hands holding a sprout, a world map of dots, rounded white cards with soft shadows, and Inter or Montserrat.
- Fix: use specific, sourced language (illustrative format: "Refill pouches use X% less plastic per wash than our 2023 bottle; method and dataset linked", with X filled from a real, verifiable measurement), commission or capture real process photography, choose a regionally specific palette (for example indigo, clay and linen, not just green), set headings in a warm serif, and design the proof section as the centerpiece.

## Accessibility notes

- Forest #1F3D2B on bone is 10.86:1; ink #1B2A21 on bone is 13.66:1; soft ink #4F5E54 on bone is 6.25:1; moss deep #4A6A2E on bone is 5.64:1 and clay deep #9A4F37 is 5.39:1.
- The lighter palette steps fail as text on bone: moss #5F7F3E is 4.16:1, River #3E7C86 is 4.31:1 and clay #B5654A is 3.88:1; use them only for graphics, large type or fills with dark text on top (ink on sun #E0B341 is 7.64:1; ink on sand is 12.20:1).
- White on lighter clay #B5654A is 4.26:1 and fails for small button text; use bone text on clay deep (5.39:1).
- Texture overlays must stay under about 8% so they do not reduce text contrast; keep all text on flat fills.
- Provide text equivalents for origin maps and impact charts, and avoid color-only legends.

## Reference anchors

- Patagonia and Aesop as examples of material honesty and restrained earth palettes (study, do not copy)
- Kinfolk and Cereal magazines for calm natural editorial layout
- FTC Green Guides (16 CFR Part 260), UK CMA Green Claims Code, EU Directive 2024/825
- Sustainable Web Design guidance and the Green Web Foundation for digital footprint practice
- B Corp and FSC certification marks, usable only by certified holders
- Google Fonts specimens: Young Serif, Red Hat Display, Karla
