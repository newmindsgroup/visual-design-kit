---
id: style.risograph-print-texture
axis: style
name: Risograph / Print Texture
aliases: [risograph, riso print, screenprint look, two-color print, grain texture, overprint, indie print aesthetic, duplicator print]
summary: Limited fluorescent and spot inks overprinted on uncoated paper with grain, halftone and slight misregistration; a tactile, indie-print look that works best when built from real ink separations.
tags: [risograph, riso, print, grain, halftone, overprint, texture, spot-color, zine, limited-palette]
pairs_with: [industry.creative-agencies-studios, industry.events-conferences, industry.food-beverage-cpg, industry.nonprofit-ngo, archetype.creator, archetype.outlaw, audience.teens-gen-z, channel.print-collateral, channel.packaging, channel.social-media]
avoid_with: [industry.fintech-banking, industry.insurance, industry.pharma-biotech, tier.luxury, audience.low-bandwidth-entry-devices]
version_timestamp: 2026-10-20 01:57:45 UTC
---

# Risograph / Print Texture

## Essence

Let the printing process show. A risograph is a Japanese stencil duplicator that prints one ink color per pass, using soy-based inks on uncoated paper; designers separate artwork into layers, one per ink, and the inks overlap to make new colors. The results have flat saturated fields, grain, dot patterns and slight misregistration that read as human, affordable and local. The digital version of the style is convincing only when it obeys the constraints: two or three inks, multiply overprints, uncoated paper and imperfect alignment.

## Visual signature

- Two to three spot inks (fluorescent pink, blue, yellow, teal, orange) on warm uncoated paper; black for text.
- Overprints where shapes overlap, creating a third and fourth color by multiplication.
- Grain-touch and halftone textures: speckled solids, coarse dot gradients instead of smooth blends.
- Slight misregistration: ink layers offset by a pixel or two (or up to about 1mm in print), with visible white gaps and overlaps.
- Bold simple shapes, hand-drawn linework, cut-out figures and chunky lettering.
- Matte, slightly mottled surfaces; no gloss, no drop shadows, no gradients.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Bricolage Grotesque (OFL, optical size and width axes); Anybody (OFL, width 50-150); commercial: ABC Favorit, GT America Expanded |
| Body font | Space Mono (OFL) for captions and short copy; Newsreader (OFL) for longer text; commercial: Maison Neue, Untitled Sans |
| Type scale ratio | 1.414 (augmented fourth) for poster-like contrast; body 15-17px, display 56-160px |
| Body size / line-height | 15-17px / 1.5 (mono) or 1.55 (serif); measure 45-60ch |
| Display letter-spacing | -0.02em to -0.04em for heavy widths; 0 for mono |
| Caps / labels | Space Mono 11-12px uppercase, +0.04em |
| Weights | Display 700-800; body 400; mono 400-700 |
| Palette (screen approximations) | Paper #F4F0E6 (oklch 0.96 0.014 89); Black #1A1A1A (oklch 0.22 0 0); Fluorescent pink #FF48B0 (oklch 0.69 0.236 350); Blue #0078BF (oklch 0.55 0.141 245); Yellow #FFE800 (oklch 0.92 0.193 102); Teal #00838A (oklch 0.56 0.094 201); Orange #FF6C2F (oklch 0.71 0.193 41); Green #00A95C (oklch 0.64 0.164 154) |
| Overprint results | Pink x yellow = #FF4200 (oklch 0.66 0.231 35); blue x yellow = #006D00 (oklch 0.46 0.158 142); blue x pink = #002284 (oklch 0.32 0.166 263); computed by multiplying channels |
| Accent proportion | Choose 2 inks plus black per piece; ink coverage 20-60% per layer; paper stays visible as the lightest tone |
| Radius | 0-4px; blobs and organic shapes are allowed; cut-out feel over rounded UI |
| Borders | 2-3px solid black or ink outlines, often slightly offset from the fill |
| Shadow / elevation | None; use overlap, offset duplicates and halftone shadows (dot gradient) instead |
| Spacing density | Medium to loose: 8px base, 24-48px margins; large shapes can bleed or crop |
| Grid | Loose 6 or 12-column grid; items snap but overlap; print layouts keep a non-printing border (commonly 3-6mm; confirm with your printer) |
| Motion | Stepped and mechanical: 2-4 frame jitter at 8-12 fps, 150-300ms snap-ins, layer offsets that wobble 1-2px; no smooth blur |

## Composition and layout

- Design in separations. Make one layer per ink (pink, blue, black) in grayscale, then assign colors and set each layer to multiply. Check how the inks overlap before finalizing.
- Let shapes be big and simple: circles, arches, stripes and hand-cut figures. Use overlaps as the color palette.
- Compose like a poster: one dominant shape or picture, big type in black or one ink, small mono details. Keep generous paper-color margins so the texture feels printed.
- On the web, keep content on flat paper areas; use ink shapes behind and beside text. Avoid placing mono text on halftone zones.
- For packaging and print, specify paper (uncoated 90-160gsm, recycled or cream), ink list, and trim size. Standard riso machines handle up to A3; plan bleed alternatives with the printer.
- Build a limited ink library (6-8 inks) and choose 2-3 per project so every piece has a recognizable restraint.

## Imagery and iconography

- Photographs become 1-2 ink halftones or threshold images; use coarse dots (6-10px at screen size) at a 45 degree angle, or grain-touch style stochastic noise.
- Illustration: bold fills with imperfect edges, hand-drawn outlines, simple characters and patterns.
- Icons: thick outline or silhouette icons in a single ink, 2-3px, slightly offset from a fill block.
- Texture assets: scanned paper (3-4 variants) and ink grain tiles of 512px at 6-12% opacity; keep each under 100KB; prefer SVG filters (feTurbulence) only for small areas because they cost render time.
- CSS building blocks: `mix-blend-mode: multiply` for ink layers, `radial-gradient` dots with `background-size: 8px 8px` for halftone, and `filter: contrast(1.1)` on scans.

## Motion

Keep it analog. Shapes slide into place in 150-250ms with a 1-2px overshoot, ink layers lag each other by one frame to mimic misregistration, and hover reveals an offset duplicate. Stop-motion cut-outs at 8-12 fps echo the printing process. Avoid smooth glides, blurs, glows and parallax depth. Pause jitter on focus and honor `prefers-reduced-motion` by showing a static, aligned composition.

## Fits and risks

- **Fits:** event posters, zines and album art, indie food and drink, craft packaging (`channel.packaging`), cultural and educational nonprofits, youth-facing brands, creative studios, merchandise. Fits `archetype.creator` and `archetype.outlaw` voices.
- **Risks:** fashionable but easily faked; the "riso filter" look on every asset becomes shallow. Fluorescent inks exceed sRGB, so screens understate them and prints differ run to run. Texture and blend effects are costly on low-end devices and ruin accessibility when text sits on halftone.
- **Wrong for:** banking, insurance, pharma and any context where precision and sterility are the brand; high-luxury tiers; very low-bandwidth contexts.

## Do and don't

- Do limit each piece to two inks plus black, plan the overprint colors, and proof with a printed swatch sheet from your print shop.
- Do keep body text in black (15.29:1 on paper) and use inks for shapes, headings and accents.
- Do add imperfection with rules: consistent 1-3px offsets and consistent grain, not random noise.
- Don't apply a "riso effect" filter to full-color photos and call it risograph.
- Don't use more than three inks plus black, or smooth gradients; the process cannot print them.
- Don't set text in fluorescent pink, yellow or orange on paper.

## Clichés and AI tells

- Lazy version: pastel gradients with a grain overlay, a generic misregistration filter on stock photos, six inks overprinted at random, rounded UI cards with a noise PNG, and Space Grotesk headlines.
- Fix: constrain to two or three named inks, design real separations, show overprints deliberately (pink over yellow gives a red-orange), choose a paper tone, add halftone to photos at a consistent angle and size, and keep UI elements plain, with texture reserved for art zones.

## Accessibility notes

- Black #1A1A1A on paper #F4F0E6 is 15.29:1. Inks as text on paper fail: pink 2.71:1, yellow 1.10:1, orange 2.48:1, green 2.70:1, teal 4.00:1 and blue 4.16:1. Only purple #765BA7 reaches 4.82:1.
- Black on ink fills: black on pink 5.64:1, yellow 13.92:1, green 5.66:1, orange 6.16:1. White on blue #0078BF is 4.73:1 (paper on blue 4.16:1, large text only).
- Halftone and grain behind text lower effective contrast; reserve flat paper or a solid ink block under any paragraph.
- Fluorescent colors cannot be matched in sRGB; if the brand depends on them, supply a Display P3 version (`color(display-p3 ...)`) and confirm print swatches.
- Offset layers should not create double vision for text: keep text on a single unshifted layer; keep jitter amplitude below 2px and provide reduced-motion states.

## Reference anchors

- Riso Kagaku (Japan) as the manufacturer of the risograph and its ink color charts; check the current swatches
- Print Club London and other independent riso studios and zine fairs for process references
- Josef Albers, *Interaction of Color*, for overprint and transparency studies
- Silkscreen poster traditions: the Polish poster school, Cuban OSPAAAL posters and Pop-era gig posters
- Google Fonts specimens: Bricolage Grotesque, Anybody, Space Mono, Newsreader
