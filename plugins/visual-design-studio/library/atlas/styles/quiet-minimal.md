---
id: style.quiet-minimal
axis: style
name: Quiet Minimal / Japandi
aliases: [japandi, wabi-sabi, muji style, zen minimalism, soft minimalism, calm minimal, ma, japanese minimalism]
summary: Calm, warm minimalism - low-chroma paper and stone tones, soft mincho or gentle sans type, vast negative space and near-still motion; emptiness is the feature, not the absence of one.
tags: [minimal, japandi, wabi-sabi, calm, neutral, whitespace, warm, japanese]
pairs_with: [industry.digital-health-wellness, industry.beauty-cosmetics, industry.hotels-travel, industry.ecommerce-dtc, market.japan, archetype.sage, archetype.innocent, tier.premium, channel.native-app, channel.ecommerce-store]
avoid_with: [industry.gaming-esports, archetype.jester, audience.older-adults, audience.low-literacy-plain-language]
version_timestamp: 2026-10-20 01:51:22 UTC
---

# Quiet Minimal / Japandi

## Essence

Space as a material. The style combines Japanese ideas (ma, the meaningful interval; wabi-sabi, beauty in the imperfect and impermanent; Kenya Hara's "emptiness" as a container for the viewer's imagination) with Scandinavian warmth and functionality, hence "Japandi". Muji (Mujirushi Ryohin, founded 1980; Hara its art director since 2002) is the global reference: no logo on the product, neutral materials, calm words. Use it when the brand sells calm, care, clarity or craft, and when the customer is tired of noise.

## Visual signature

- Large, calm negative space; very few elements per view, each given room to be noticed.
- Low-chroma, warm neutrals: rice paper, washi, stone, sumi ink, moss gray, with at most one earthy accent used sparingly.
- Light-to-regular type, soft mincho serif or gentle sans, generous leading and slightly open tracking.
- Natural, tactile material in photography: linen, ceramic, wood grain, paper, water, soft daylight.
- Asymmetric but still compositions; thin, low-contrast dividers; shapes with small radii and no ornament.
- Restraint in motion and sound; interactions feel like touch on paper.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Shippori Mincho 400-500 (OFL, Japanese and Latin); Zen Old Mincho (OFL); Cormorant Infant (OFL) for Latin-only editorial; commercial: Tiempos Headline (Klim), Yu Mincho (system on macOS/Windows) |
| Body font | Zen Kaku Gothic New 400 (OFL, Japanese and Latin); Hanken Grotesk 400 (OFL); commercial: Söhne (Klim), Hiragino Sans (macOS) |
| Type scale ratio | 1.2 (minor third) for body hierarchy; one calm display jump (1.5) on heroes |
| Body size / line-height | 16-17px / 1.7-1.8 Latin; 15-16px / 1.9-2.0 Japanese; measure 40-55ch Latin, 30-38 full-width characters Japanese |
| Display letter-spacing | +0.02em to +0.06em; line-height 1.3-1.4 at 40px+ |
| Caps / labels | 11-12px, uppercase or small, +0.14em, weight 400-500 |
| Weights | 300-400 for display, 400 body, 500 for emphasis; no bold above 600 |
| Palette | Rice #F5F2EA (oklch 0.96 0.011 90); Washi #E7E1D4 (oklch 0.91 0.019 86); Stone #B9B0A2 (oklch 0.76 0.022 79); Line #8A8479 (oklch 0.62 0.018 83); Moss gray #6B6F60 (oklch 0.53 0.023 119); Sumi #2C2A27 (oklch 0.29 0.006 78); Kaki #8F4A2F (oklch 0.49 0.102 42) |
| Verified pairs | Sumi on Rice 12.79:1; Sumi on Washi 10.98:1; Kaki on Rice 5.89:1; Rice on Kaki 5.89:1; Moss gray on Rice 4.61:1; Line on Rice 3.32:1 (UI borders, input outlines); Moss gray on Washi only 3.96:1; Stone on Rice 1.92:1 is decoration only |
| Accent proportion | Kaki under 3% (one link color, one button, one seal); the rest neutral |
| Radius | 2-6px; images square or with 2px radius; pill buttons optional at 999px for mobile |
| Borders | 1px Line (#8A8479) on inputs and key dividers; 1px Washi for decorative section rules |
| Shadow / elevation | None, or 0 1px 2px rgba(44, 42, 39, 0.06) on floating sheets |
| Spacing density | Very generous: 8px base, 120-240px between sections, 24-40px between related items |
| Grid | 12 columns with only 4-6 used per view; wide margins (8-12vw); single column mobile with 24px gutters |
| Motion | 500-900ms, cubic-bezier(0.45, 0, 0.15, 1); opacity and 8px translate only |

## Composition and layout

- Pick one focal element per view (an image, a sentence, a product) and give it at least 60% of the surrounding area as empty space.
- Use an off-center placement and a quiet secondary text block aligned to a common baseline; avoid symmetrical heroes.
- Show the product or service in context: a single ceramic, a room corner, a hand at work. Crop to a still frame.
- Navigation is minimal: logo, 3-5 text links, one account or cart icon; no mega menus. Hide secondary links in the footer.
- Use vertical rhythm: 8px base, text blocks sit on a 4px baseline; spacing between sections is a design decision, never padding left over.
- For apps, show one task per screen with large touch targets, a single primary action and ample list row height (64-72px).

## Imagery and iconography

- Photography: natural light, desaturated warm grade, shallow depth of field, matte textures; avoid people looking at the camera.
- Illustration: sparse line drawings or ink wash (sumi-e) shapes, one-color; stamp-like seals (hanko) as brand marks.
- Icons: 1.25-1.5px monoline at 24px, rounded or butt ends, gentle radii; always paired with text labels in key flows.
- Texture: paper fibre, linen weave or stone at 3-5% contrast on large fields; never behind text.

## Motion

Barely there. Elements fade in 500-900ms with an 8px rise, and transitions between pages cross-dissolve. Hover changes an underline or color over 300ms. Use cubic-bezier(0.45, 0, 0.15, 1) and a single motion property per element. No parallax, marquees, bouncing or confetti. With `prefers-reduced-motion`, switch to instant state changes with opacity only.

## Fits and risks

- **Fits:** wellness, meditation and sleep apps (`industry.digital-health-wellness`, `channel.native-app`), skincare and fragrance (`industry.beauty-cosmetics`), ryokan-style hotels and retreats (`industry.hotels-travel`), home goods and fashion basics (`industry.ecommerce-dtc`, `channel.ecommerce-store`), Japanese-market products (`market.japan`), and premium services (`tier.premium`). `archetype.sage` and `archetype.innocent` match its calm clarity.
- **Risks:** so common in 2020s DTC and wellness branding that sameness is the main danger; low-contrast greys and tiny type are a frequent accessibility failure. Without a material or photographic point of view the result reads empty.
- **Wrong for:** `industry.gaming-esports` and `archetype.jester` (energy mismatch), `audience.older-adults` (needs larger, higher-contrast text and explicit labels), and `audience.low-literacy-plain-language` (sparse text and icon-only cues).

## Do and don't

- Do remove until one more removal would hurt; then stop.
- Do use contrast of scale and position, not boxes, to show hierarchy.
- Do verify that border and placeholder colors meet 3:1 (inputs) and 4.5:1 (text).
- Don't equate minimal with light gray text on white; "quiet" must still be legible.
- Don't add faux wabi-sabi (random cracks, fake rust) or Zen clichés (stacked stones, bamboo, lotus).
- Don't crowd the page with consent banners, chat widgets and promotional bars; they undo the premise.

## Clichés and AI tells

- The lazy version: beige background, thin gray sans, a lone eucalyptus branch, a stack of smooth stones and the word "Mindful" on everything.
- Generated imagery of arranged pebbles, steam, candles and linen with soft focus and no specific object or place.
- Fix: photograph the actual product and its maker, use a mincho or humanist text face with real contrast, give each page one specific idea, and spend the "emptiness" on content that deserves attention.

## Accessibility notes

- Sumi #2C2A27 on Rice is 12.79:1 for body; secondary text in Moss gray #6B6F60 passes on Rice (4.61:1) but fails on Washi (3.96:1); use Sumi on tinted panels.
- Placeholder and border color Line #8A8479 reaches 3.32:1 on Rice, meeting the 3:1 non-text threshold; the lighter Stone #B9B0A2 (1.92:1) does not and must stay decorative.
- Light type weights (300) are only safe at 24px+; body stays at 400.
- Keep generous space but also visible focus: a 2px Sumi outline with 3px offset is consistent with the aesthetic and passes.
- For Japanese text keep the font size at 15px+ and line-height 1.9+; avoid italics and avoid vertical writing for essential UI.

## Reference anchors

- Muji / Ryohin Keikaku (1980), with Kenya Hara's art direction and his books *Designing Design* (2007) and *White*
- Naoto Fukasawa and Jasper Morrison, *Super Normal* (2006 exhibition and 2007 book)
- John Pawson, *Minimum* (1996); Tadao Ando, Church of the Light (1989)
- Leonard Koren, *Wabi-Sabi for Artists, Designers, Poets and Philosophers* (1994)
- Dieter Rams, "Less, but better" and the ten principles of good design (Braun)
- Aesop retail and print identity, Hay and Kinfolk for the Nordic-Japanese crossover
