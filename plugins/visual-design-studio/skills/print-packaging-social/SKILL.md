---
name: print-packaging-social
description: >-
  Produces print, packaging, social, out-of-home, presentation and email work to production spec: bleed, safe zones,
  300ppi, CMYK profiles and ink limits, PDF/X preflight, dielines, barcodes and shelf tests, dated social formats with
  9:16 safe areas, billboard letter heights and dwell times, 16:9 decks and bulletproof email. Use when making a flyer,
  brochure, business card, poster, package, label, social post, carousel, story or reel cover, billboard, digital
  signage loop, slide deck or email template.
license: MIT
metadata:
  version-timestamp: "2026-10-20 02:07:10 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 02:07:10 UTC"
---

# Print, packaging, social and campaign formats

Excellent channel work is designed for the moment it is seen (held at 40cm, spotted on a shelf at 2m, passed at 80km/h, thumbed past in half a second) and produced so the printer, converter, platform or inbox reproduces it exactly. The vendor's spec always beats this skill; get it first.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Vendor spec | Printer's spec sheet, converter's dieline, media owner's template or platform help page before layout starts | Never skip; record the source and date |
| Bleed | 3mm (0.125in) on every trimmed edge | Packaging, large format or die-cuts: 3-5mm or the vendor's figure |
| Safe zone | 3-5mm inside trim for text and logos; 6mm from folds, glue flaps and spines | Thick saddle-stitched booklets: more on the outer edge for creep |
| Image resolution | 300ppi effective at final size; line art 600-1200ppi | Large format viewed from 1m+: 100-150ppi at final size |
| Print color | CMYK to the printer's profile (PSO Coated v3 / FOGRA51 or FOGRA39 in Europe, GRACoL 2013 or SWOP in the US); RGB masters kept; convert last | Brand-critical or out-of-gamut colors: Pantone spot plus a CMYK build |
| Black | Text and fine lines 100K, overprinting; large areas rich black C60 M40 Y40 K100 (240%) | Uncoated or newsprint: lighter build; ask the printer |
| Total ink | Coated about 300-330%, uncoated about 260-300%, newsprint about 240% | The printer's number wins |
| Print file | PDF/X-4, fonts embedded, bleed and trim boxes set, marks outside the bleed | Legacy workflow: PDF/X-1a |
| Social canvas | 1080px wide: feed 1080x1350 (4:5), vertical 1080x1920 (9:16) with UI safe areas, link preview 1200x630 | Platform-specific placements: see [social formats](references/social-formats.md) |
| OOH legibility | Cap height 25mm per 3m (1in per 10ft) of viewing distance for impact; 7 words or fewer roadside; 7:1 contrast | Pedestrian and dwell screens: longer copy, sequenced |
| Presentation | 1920x1080 (16:9); presented body 24pt+ (48px), never below 18pt; one idea per slide | Reading decks sent as PDF: 12-16pt body, denser layouts |
| Email | 600px container, single column on mobile, 16px live text, bulletproof buttons 44-48px tall, HTML under about 100KB | Transactional email: even simpler, text-first |

## Workflow

1. **Get the spec.** Printer, converter, media owner, platform or email service; save it with the date. Note anything unverified.
2. **Read the channel overview** in the atlas (links below) for structure, hierarchy and QA, then the reference file here for production depth.
3. **Set up the file** at final size with bleed, safe zone, grid, color profile and named layers (art, dieline, varnish, foil, white).
4. **Design for the viewing moment:** distance, dwell time, motion, lighting, competing content. Set the hierarchy to the single thing the viewer must get first.
5. **Render and inspect in context.** Print at 100% on an office printer and hold it at reading distance; mock packaging on a real shelf photo with competitors; preview social in the app (or an overlay template) on a phone; view OOH as a thumbnail at the equivalent distance; send test emails to real clients with images off and in dark mode. Fix and repeat.
6. **Preflight and export** to the spec (PDF/X, MP4, PNG, HTML), then reopen the exported file and check it again.
7. **Hand off** with a spec sheet: sizes, colors (CMYK, Pantone, HEX), finishes, file names, proof status and approvals.

## Decisions that change the answer

- **Tier.** Value: coated stock, CMYK, bold color, large price and benefit. Premium and luxury: uncoated or textured heavy stock (350gsm+ cards), one or two spot colors, foil, emboss, letterpress, soft-touch, more empty space, smaller logo.
- **Market.** ISO A sizes vs US Letter; local packaging law and languages (bilingual Canada, EU multilingual packs); RTL markets flip reading order on packs, decks and social layouts; market-specific platforms (for example WeChat and Xiaohongshu in China, LINE in Japan, KakaoTalk in Korea) have their own formats.
- **Industry.** Food, cosmetics, pharma, alcohol and cannabis packaging are regulated; claims and mandatory panels come from the client's regulatory team. Finance and health emails and ads carry required disclosures.
- **Audience.** Older adults: print body 12pt+, matte stock to cut glare, high contrast. Children: sturdy formats, rounded die-cuts, safety rules on small parts.
- **Sustainability.** Mono-material packs, fewer laminations and metallized films, FSC-certified paper, right-sized boxes; environmental claims must be specific and substantiated.
- **Channel mix.** A campaign needs a key visual that survives the hardest format (a 1200x628 link preview or a 6:1 billboard) before it is adapted to the easy ones.

## Common failures

- Designing before the dieline or spec arrives → wait or label the layout as provisional.
- RGB images in a print PDF, or 72ppi web images placed at large size → convert to the printer profile; 300ppi effective.
- Small text in rich black or four-color → 100K only.
- Barcode placed over a fold, in red, or shrunk below 80% → flat panel, dark on light, 80-200% magnification, quiet zones kept.
- Key copy under the TikTok or Reels UI → safe-area overlay on every vertical frame.
- Billboards with a paragraph → one idea, 7 words or fewer, brand big.
- Decks with 12pt bullet walls → one idea per slide, notes carry the detail.
- Image-only emails → live text, alt text, bulletproof buttons.

## References

- [Print production](references/print-production.md): bleed, resolution, profiles, rich black, ink limits, overprint, spot colors, paper, finishes, PDF/X preflight, size tables.
- [Packaging](references/packaging.md): dieline workflow, panel hierarchy, regulatory panels, barcodes, shelf tests, sustainability, mockups.
- [Social formats](references/social-formats.md): dated platform table, 9:16 safe areas, first-frame hooks, captions, carousels.
- [OOH and signage](references/ooh-and-signage.md): viewing distance and letter height, word counts, contrast, digital signage loops and dwell time.
- [Presentations](references/presentations.md): 16:9 canvas, type minimums, slide grid, data slides, speaker notes.
- [Email](references/email.md): width, live text, dark mode, bulletproof buttons, alt text, Gmail clipping, accessibility.
- Atlas channel overviews: [print collateral](../../library/atlas/channels/print-collateral.md), [packaging](../../library/atlas/channels/packaging.md), [social media](../../library/atlas/channels/social-media.md), [OOH and signage](../../library/atlas/channels/ooh-signage.md), [environmental and wayfinding](../../library/atlas/channels/environmental-wayfinding.md), [presentation](../../library/atlas/channels/presentation.md), [email](../../library/atlas/channels/email.md), [video and motion](../../library/atlas/channels/video-motion.md).
- Atlas query, when style, industry, market or tier matters:
  - `python3 ../../library/scripts/atlas.py query "craft beer can label premium"`
  - `python3 ../../library/scripts/atlas.py show channel.packaging`
  - `python3 ../../library/scripts/atlas.py combine industry.food-beverage-cpg channel.packaging tier.premium`
- Deep process for displays and digital signage on client projects: [display discovery](../../library/draft-skills/design-display-discovery/SKILL.md), [display art direction](../../library/draft-skills/design-display-art-direction/SKILL.md), [display content](../../library/draft-skills/design-display-content/SKILL.md), [display campaigns](../../library/draft-skills/design-display-campaigns/SKILL.md), [display production](../../library/draft-skills/design-display-production/SKILL.md), [display evaluation](../../library/draft-skills/design-display-evaluation/SKILL.md), [extreme formats](../../library/draft-skills/design-screen-formats/SKILL.md), [loops](../../library/draft-skills/design-screen-loops/SKILL.md) and [attention sequencing](../../library/draft-skills/design-screen-attention/SKILL.md).

Catalog IDs covered: display-discovery, display-art-direction, display-content, display-campaigns, display-production, display-evaluation, screen-formats, screen-loops, screen-attention
