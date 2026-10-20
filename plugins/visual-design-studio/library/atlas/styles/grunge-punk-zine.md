---
id: style.grunge-punk-zine
axis: style
name: Grunge / Punk / DIY Zine
aliases: [punk, zine, diy, photocopy, xerox, ransom note, grunge, cut and paste, riot grrrl, underground press]
summary: Photocopied, cut-and-paste, hand-made graphics - ransom-note lettering, torn paper, tape, marker scrawl, black-and-white with fluorescent hits; urgency, authenticity and refusal of polish.
tags: [punk, zine, grunge, diy, collage, photocopy, raw, underground]
pairs_with: [industry.media-entertainment-streaming, industry.fashion-apparel, industry.creative-agencies-studios, industry.nonprofit-ngo, audience.teens-gen-z, archetype.outlaw, archetype.creator, channel.social-media, channel.print-collateral, channel.ooh-signage]
avoid_with: [industry.fintech-banking, industry.healthcare-provider, industry.insurance, tier.luxury, archetype.ruler, archetype.caregiver]
version_timestamp: 2026-10-20 01:51:22 UTC
---

# Grunge / Punk / DIY Zine

## Essence

Graphic design as a protest you can photocopy. It grew from the 1970s punk press (Mark Perry's *Sniffin' Glue*, London 1976; *Punk* magazine, New York 1976; Jamie Reid's ransom-note sleeves for the Sex Pistols, 1977; Raymond Pettibon's Black Flag bars, 1978) and the Riot Grrrl zines of the early 1990s, then collided with digital layout in the grunge era: Emigre (1984-2005), Barry Deck's Template Gothic (1990), Sub Pop in Seattle, and David Carson's *Ray Gun* (1992-1995). The rules are urgency, available materials and ownership: if it can be made with a photocopier, scissors, a marker and a glue stick, it belongs. Use it where a brand's credibility depends on seeming made by people, not by a department.

## Visual signature

- Ransom-note headlines: letters from different fonts and sizes cut out and pasted unevenly, sometimes on tape or colored paper.
- High-contrast black-and-white photocopy texture, halftone dots, toner streaks and edge noise.
- Torn paper, masking tape, staples, pins, stickers and hand-cut collage shapes.
- Handwritten annotations, arrows, underlines, circled words, marker strokes.
- Typewriter or condensed grotesque text blocks glued at angles; rubber-stamp and stencil lettering.
- Fluorescent spot color (pink, yellow, cyan) hitting a monochrome page; red as an alarm.
- Overlap, mess and crooked placement, yet strong focal moments.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Anton (OFL, condensed poster gothic); Special Elite (Google Fonts, typewriter); Permanent Marker (Google Fonts, marker); mix at least 3 voices in ransom headlines; commercial: Template Gothic (Barry Deck, Emigre 1990), Trixie (FontFont, 1991), Franklin Gothic Heavy |
| Body font | Courier Prime 400-700 (OFL) at 16-17px for typewriter text; commercial: Letter Gothic |
| Scrawl accent | Rock Salt (Google Fonts) or Reenie Beanie (OFL) for annotations, 20-28px |
| Type scale ratio | 1.5-1.618; irregular per word in ransom headlines (e.g., 48/72/40/96px) |
| Body size / line-height | 16-17px / 1.5; measure 40-60ch; body on a solid paper strip |
| Display letter-spacing | -0.02em to 0 for Anton; random variation allowed per cut-out |
| Caps / labels | 12-14px, uppercase, +0.06em, Courier Prime bold or stencil |
| Weights | 400 and 700 only; weight changes by font swap rather than axis |
| Palette | Black #0F0F0F (oklch 0.17 0 0); Paper #E9E5DA (oklch 0.92 0.015 90); Photocopy gray #B9B5AA (oklch 0.77 0.016 90); Alarm red #CC0817 (oklch 0.53 0.215 27); Fluoro pink #FF2D78 (oklch 0.66 0.241 7); Acid yellow #E6FF2B (oklch 0.95 0.210 117); Cyan #00D0E8 (oklch 0.79 0.136 209) |
| Verified pairs | Black on Paper 15.23:1; Black on Acid yellow 17.07:1; Black on Cyan 10.21:1; Black on Photocopy gray 9.36:1; Black on Fluoro pink 5.38:1; Fluoro pink on Black 5.38:1; white on Alarm red 5.81:1; Alarm red on Paper 4.62:1; Acid yellow on Paper only 1.12:1 and Fluoro pink on Paper 2.83:1 (fills, never text on light) |
| Accent proportion | 85-90% black, paper and gray; one fluorescent at 5-10% as strips, highlights, stickers |
| Radius | 0; irregular torn edges (clip-path polygon, SVG mask) and rotated rectangles |
| Borders | 2-4px rough black strokes (SVG `feTurbulence` displacement of 1-2px), dashed "cut here" lines, tape strips |
| Shadow / elevation | None; hard 3px black offset for stickers; misregistered second ink layer (Fluoro pink offset 2-4px) |
| Spacing density | Dense and overlapping: 4px base, 8-16px gaps, negative space only for emphasis; rotations of 1-6 degrees |
| Grid | No visible grid; underlying 6-column structure keeps reading order; strips and columns glued at angles; single column on mobile |
| Motion | Stepped 8-12 fps (`steps(1)`), 80-120ms per frame; jump cuts, jitter 1-2px, no easing |

## Composition and layout

- Build with layers on a flat Paper ground: photocopied photo, torn color strip, ransom-note headline, typewriter paragraph strip, tape and stickers, annotation arrows. Limit to 5-7 layers.
- Keep body text on its own clean strip (Courier Prime on Paper) and attach it to the collage with tape; reading comes first.
- Use rotation (1-6 degrees) on blocks and images, not on text lines longer than 6 words.
- Hierarchy by scale and color: one 96-200px ransom headline, one fluorescent strip, small typewriter copy. Show the "mistakes" (misalignment) on non-essential elements only.
- Make real zine objects when possible: A5 folded photocopied sheets, staples, risograph covers, stickers and posters pasted on walls (`channel.ooh-signage`).
- On the web, build the collage with CSS transforms and SVG masks; export raster textures at 1x for photocopy grain and keep payload under 1.5MB.

## Imagery and iconography

- Photography: harsh flash, high-contrast black-and-white, crowd and live shots, photocopied 2-3 times for grit; threshold or halftone conversion.
- Illustration: ink drawings, cut-out figures, skulls and hands (sparingly), hand-lettered slogans, arrows and speech bubbles.
- Icons: hand-drawn marker icons, stencil or stamp-style glyphs at 24-32px with thick 3px strokes.
- Ephemera: tickets, receipts, stamps, newspaper clippings (use original or fictional text to avoid copyright issues).

## Motion

Hand-cut and choppy. Elements jump between positions at 8-12 fps (`animation-timing-function: steps(1, end)`), jitter 1-2px, and cut in as strips. Avoid easing and smooth parallax. Photocopy "flicker" must remain below 3 flashes per second and never fill the screen. With `prefers-reduced-motion`, show a static collage and swap jump cuts for instant changes.

## Fits and risks

- **Where it works today:** music, labels, tours and zines (`industry.media-entertainment-streaming`), streetwear and skate fashion (`industry.fashion-apparel`), independent studios (`industry.creative-agencies-studios`), activist campaigns and community groups (`industry.nonprofit-ngo`), posters, stickers and street teams (`channel.ooh-signage`, `channel.print-collateral`, `channel.social-media`) aimed at `audience.teens-gen-z`. `archetype.outlaw` and `archetype.creator` are its natural voices.
- **Accessibility risk:** noise, rotation, mixed-font ransom text and low-contrast torn textures harm legibility, dyslexic reading and screen-reader order; fluorescents on light grounds fail contrast.
- **Brand and longevity risk:** corporate punk reads as inauthentic ("punk by committee") and can alienate the scene it borrows from. Some punk and grunge imagery (swastikas, violence, self-harm) is unacceptable; moderate the content. The style recurs every decade but the 1990s grunge-distress look can read dated.
- **Wrong for:** `industry.fintech-banking`, `industry.healthcare-provider` and `industry.insurance` (trust and clarity), `tier.luxury`, `archetype.ruler` and `archetype.caregiver`.

## Do and don't

- Do make real artifacts (scan a hand-made collage) rather than faking everything with Photoshop filters.
- Do put body text on clean strips and keep font sizes at 16px+.
- Do limit fluorescent color to one hue per piece and keep black dominant.
- Don't put distressed textures across paragraphs or rotate paragraphs.
- Don't add a "grunge" filter pack to a corporate layout and call it punk.
- Don't use punk shock imagery to sell products unrelated to the scene.

## Clichés and AI tells

- The lazy version: a "distressed" font in bright red on black, a barcode, a skull, torn paper PNGs and the word "REBEL".
- Generated zine pages with perfectly symmetrical torn edges, fake ransom letters from the same typeface and illegible text.
- Fix: collect real ephemera, cut and scan letters from different sources, vary scale and baseline irregularly but consistently, keep a legible clean text strip, and let the brand's actual point of view write the slogan.

## Accessibility notes

- Black on Paper is 15.23:1 and Black on fluorescent fills is 5.38:1 or higher; always put text in Black on fluorescents (Acid yellow 17.07:1, Cyan 10.21:1, Fluoro pink 5.38:1).
- Acid yellow on Paper is 1.12:1 and Fluoro pink on Paper 2.83:1: fills, stickers and highlights only; Alarm red on Black is 3.30:1, too low for body text.
- Ransom-note headlines must be real text (spans with different fonts) or an image with a full-text `alt`; do not break words across absolutely positioned letters that confuse screen readers.
- Photocopy textures must stay under 8% contrast behind text and be removable in a "plain view" for long reads.
- Mouse and touch targets in collage layouts need 44px minimum even when the visuals are tiny scraps.

## Reference anchors

- Mark Perry, *Sniffin' Glue* (1976) and *Punk* magazine (1976, John Holmstrom, Legs McNeil)
- Jamie Reid, Sex Pistols artwork (1977); Raymond Pettibon, Black Flag logo and flyers (1978-1980s); Winston Smith, Dead Kennedys collages
- Riot Grrrl zines such as *Bikini Kill* (1991)
- Emigre magazine (1984-2005); Barry Deck, Template Gothic (1990)
- David Carson, *Ray Gun* (1992-1995) and *The End of Print* (1995, with Lewis Blackwell)
- Sub Pop Records' 1990s graphic identity, Seattle
