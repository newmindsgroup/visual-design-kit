---
id: style.collage-mixed-media
axis: style
name: Collage / Mixed Media
aliases: [collage, cut and paste, mixed media, paper cut-out, scrapbook design, photomontage, torn paper, analog collage, digital collage]
summary: Layered cut-out photography, paper scraps, tape, halftone and mixed type arranged with deliberate tension; handmade, surprising and culturally literate, but easy to turn into scrapbook noise.
tags: [collage, mixed-media, cut-out, paper, halftone, layered, surreal, handmade, photomontage, texture]
pairs_with: [industry.creative-agencies-studios, industry.media-entertainment-streaming, industry.events-conferences, industry.fashion-apparel, archetype.creator, archetype.outlaw, archetype.jester, audience.teens-gen-z, channel.social-media, channel.print-collateral]
avoid_with: [industry.fintech-banking, industry.healthcare-provider, industry.government-civic, industry.insurance, tier.ultra-luxury, audience.expert-power-users]
version_timestamp: 2026-10-20 01:57:45 UTC
---

# Collage / Mixed Media

## Essence

Make meaning from juxtaposition. Collage cuts images out of their original context and recombines them: a statue's head on a skateboard, a hand holding a planet, a typewritten caption under a neon sticker. The lineage runs from Cubist papier collé and the Dada photomontages of Hannah Höch and Kurt Schwitters, through Pop art, to modern music posters and festival identities. The fascination is visible hands-on construction and the shock of scale and context. The discipline is deciding what is foreground, what is texture and where the eye rests.

## Visual signature

- Cut-out subjects with crisp scissor edges (often a thin white border) layered over paper, halftone and color blocks.
- Torn paper, tape strips, staples, stickers, stamps and handwritten marks as connective tissue.
- Scale and context collisions: giant heads, tiny figures, architecture mixed with botanicals.
- Mixed typography: a refined serif italic, a loud grotesque, a typewriter caption and a marker scribble, never more than 3-4 voices.
- Halftone dots, photocopy contrast, limited spot colors over off-white or newsprint grounds.
- Rotations of -6 to +6 degrees, overlaps and deliberate misregistration.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Instrument Serif (OFL, regular and italic); Syne (OFL, weights 400-800); commercial: GT Sectra, Editorial New, Pitch |
| Body font | DM Sans (OFL); commercial: Neue Haas Grotesk Text, Graphik |
| Accent / caption faces | Courier Prime (OFL) for typewriter captions and labels; Permanent Marker (OFL) for handwritten annotations, used sparingly |
| Type scale ratio | 1.414 (augmented fourth) for strong contrast; display 64-200px against 14-16px captions |
| Body size / line-height | 16-17px / 1.5; captions 13-14px / 1.4; measure 50-62ch on flat text blocks |
| Display letter-spacing | -0.02em on serif italics; 0 on Syne; typewriter +0.02em |
| Caps / labels | Courier Prime 12-13px uppercase, +0.06em, on tape or label stickers |
| Weights | Instrument Serif 400 (and italic), Syne 700-800, DM Sans 400-600 |
| Palette | Old paper #EFE6D2 (oklch 0.93 0.028 87); Newsprint #D9D2C0 (oklch 0.86 0.026 89); Ink #151515 (oklch 0.20 0 0); Soft ink #5C5446 (oklch 0.45 0.024 82); Tape yellow #F5D547 (oklch 0.88 0.157 96); Stamp red #D1342A (oklch 0.57 0.195 29); Cut-out blue #2B4FD8 (oklch 0.49 0.213 267); Magenta #E8479B (oklch 0.65 0.211 353) |
| Extra spot color | Leaf green #3F8F5B (oklch 0.59 0.112 153), used only as one of the three campaign spots |
| Accent proportion | Paper/newsprint 50-60%, ink and photography 25-35%, spot colors 10-15% (choose 2-3 of yellow, red, blue, magenta, green per piece) |
| Radius | 0 for paper scraps and photos; irregular polygon clips for cut-outs; 2-3px on UI buttons |
| Borders | 3-6px white cut-out border via stacked `drop-shadow` filters; 1.5px ink outlines on stickers and tape labels |
| Shadow / elevation | Lifted paper: `2px 3px 6px rgb(21 21 21 / 0.25)`; layers use different offsets by depth (small = closer to the base); no glows |
| Spacing density | Intentionally uneven but anchored: an 8px base, 24-48px safe margins around text blocks, 3-4 visual depth levels maximum |
| Grid | A loose 12-column grid under the chaos: text, nav and CTAs align to it; images and ornaments break it by 10-30% |
| Motion | Stop-motion feel: `steps()` timing at 8-12 fps for jitter, 120-300ms snap-ins; hover parallax by layer depth (4-12px); no smooth glides on cut-outs |

## Composition and layout

- Pick a hero cut-out and build around it. Rule of thumb: one dominant element (40-60% of the area), a supporting set of 3-5 pieces, and small marginalia.
- Keep reading surfaces flat. Place paragraphs on straight, unrotated scraps of paper or on plain ground; only headlines and decorations rotate.
- Control depth with order and shadow: base paper, texture layer, large cut-out, mid-size objects, tape and stickers on top. Limit to 4 levels.
- Use scale shocks: a gigantic hand against a small headline, a tiny person on a huge slab of color.
- Structure web pages as strips: each section is a mini collage composed on a clean 12-column frame, with navigation and calls to action kept consistent and plain.
- Create a reusable kit (20-40 cut-outs, 6-8 papers, 5 tape/staple/stamp elements, 3 halftone treatments) so campaigns stay coherent.

## Imagery and iconography

- Sources: your own photography and scans, commissioned shoots, and public-domain or openly licensed archives such as the Rijksmuseum, The Met Open Access, Biodiversity Heritage Library, Library of Congress and Wikimedia Commons (check each item's license). Scanning magazines or stock you do not hold rights to is infringement in commercial work.
- Unify disparate sources: convert to grayscale or duotone, add halftone or grain at 6-12% multiply, match contrast, then add spot color.
- Cut-outs: export WebP or AVIF with alpha at 2x; keep each under 150KB; use SVG for tape, stamps and torn edges (feTurbulence plus feDisplacementMap at scale 6-12).
- Icons: hand-cut or rubber-stamp feel: 2px irregular outlines, filled with a spot color slightly offset.
- Handwriting and marks should come from the designer's hand or a license-cleared font, not from generic "scribble packs".

## Motion

Imitate stop-motion. Elements snap into place in 120-200ms, hold, and occasionally jitter by one degree at 8-12 fps; scrolling shifts layers at different speeds (the nearer the paper, the faster the movement, 4-12px range); hover tilts a sticker 2-3 degrees. Video collage uses cut-out loops of 1-3 seconds layered over still texture. Avoid smooth cinematic easing on cut-outs, which breaks the handmade illusion. Provide a pause control for looping jitter and honor `prefers-reduced-motion` by freezing layers in their final composition.

## Fits and risks

- **Fits:** music, festivals and events (`industry.events-conferences`), culture and media (`industry.media-entertainment-streaming`), creative studios, youth and streetwear, publishing, campaigns that need a human, subversive voice. Works for `archetype.creator`, `archetype.outlaw` and `archetype.jester` brands.
- **Risks:** noise and weak hierarchy; heavy image weight; unclear CTAs; copyright and likeness issues in found imagery; a "Canva scrapbook" sameness when stock sticker packs are used. Accessibility suffers when text rides on busy layers.
- **Wrong for:** regulated or trust-first sectors (banking, health, insurance, government), data-dense tools, and ultra-luxury brands needing serene polish.

## Do and don't

- Do limit the system: 3-4 type voices, 2-3 spot colors, one halftone treatment, one tape style, one shadow recipe.
- Do build kits from owned or cleared assets and record licenses in the asset library.
- Do test legibility by squinting at the layout and by running it through grayscale; the hierarchy must survive.
- Don't rotate or distort body text, navigation or form fields.
- Don't layer more than four depth levels or add decorative elements after the composition already works.
- Don't mix clashing photo grades; unify with duotone or grain.

## Clichés and AI tells

- Lazy version: a generic "Y2K scrapbook" with the same torn-paper PNG pack, rainbow stickers, random tape, a Midjourney surreal flower-eye image, 6 fonts, drop shadows on everything and text rotated at 15 degrees.
- Fix: write a collage brief (themes, source archive, palette, depth levels), curate source images with a shared treatment, create one repeatable edge style (scissor or torn, not both), keep text on flat scraps, and add one idea per composition (a pun, a scale shock, a cultural reference) so the juxtaposition says something.

## Accessibility notes

- Ink #151515 on old paper #EFE6D2 is 14.71:1, on newsprint #D9D2C0 12.11:1 and on tape yellow #F5D547 12.60:1; soft ink #5C5446 on paper is 6.02:1.
- Spot colors: stamp red #D1342A on paper is only 3.99:1 (large text or graphics), but white on red is 4.96:1; white on blue #2B4FD8 is 6.54:1 and blue on paper is 5.27:1. White on magenta #E8479B is 3.62:1 and white on leaf green #3F8F5B is 3.97:1 (both fail); use ink on them (5.05:1 and 4.60:1).
- Text over images needs a flat backing (a paper scrap or tape label at 90%+ opacity) rather than relying on the picture.
- Provide alt text that describes the meaningful composition (not each fragment) and mark decorative layers as `alt=""` or CSS backgrounds; reduce DOM weight by flattening non-interactive layers into a single image.
- Avoid flicker (jitter at 8-12 fps is safe, but never flash high-contrast areas more than 3 times per second); keep tap targets 44px even when stickers are the buttons.

## Reference anchors

- Hannah Höch and Kurt Schwitters (Dada photomontage and Merz collage)
- Richard Hamilton and Eduardo Paolozzi (British Pop collage)
- Barbara Kruger and Jamie Reid for text-and-cutout graphic collage
- *Raygun*, *Emigre* and *i-D* magazine layouts of the 1990s
- Contemporary music poster and festival identities that use cut-out and halftone systems
- Open Access archives: The Met, Rijksmuseum, Biodiversity Heritage Library (check each license)
