---
id: channel.print-collateral
axis: channel
name: Print Collateral
aliases: [print design, brochure, flyer, business card, poster, catalog, annual report, stationery, leaflet, book]
summary: Printed pieces built for prepress from the start (bleed, CMYK, resolution, paper and finishing) where color and craft are judged in the hand at actual size.
tags: [print, brochure, flyer, business card, poster, catalog, prepress, cmyk, bleed, finishing]
pairs_with: [style.editorial-magazine, style.swiss-international, style.classic-luxury-serif, style.risograph-print-texture, style.fashion-editorial-didone, industry.luxury-goods, industry.events-conferences, industry.nonprofit-ngo, tier.premium, archetype.ruler]
avoid_with: [style.glass-spatial, style.soft-ui-neumorphic]
version_timestamp: 2026-10-20 02:01:01 UTC
---

# Print Collateral

## Formats and specs

Always get the printer's specification sheet and template first; it overrides this table. Profiles and paper standards vary by region.

| Item | Spec | Notes |
| --- | --- | --- |
| Bleed | 3 mm (0.125 in) on all trimmed edges; 5 mm for large or die-cut pieces if the printer asks | Extend backgrounds and images, not just color boxes |
| Safe margin | 3-5 mm (0.125-0.2 in) inside trim for text and logos; 5-6 mm near folds and for perfect-bound spines | Stitched booklets: add inside margin for gutter |
| Image resolution | 300 ppi at final size for photos; 600-1200 ppi for line art and bitmap logos; vector for logos and type | Large format viewed beyond 1 m: 100-150 ppi at final size |
| Color mode | CMYK to the printer's profile (FOGRA39 or FOGRA51 coated in Europe, GRACoL 2013 coated or SWOP in the US, Japan Color in Japan); convert at the end, keep RGB masters | Spot colors (Pantone) for brand-critical colors, with CMYK build for digital |
| Ink coverage | Total area coverage typically 300-330% coated and 260-300% uncoated, set by the press condition's ICC profile (for example 300% in PSO Uncoated v3 / FOGRA52); confirm the exact limit with the printer | Rich black for large areas: C60 M40 Y40 K100; text stays 100K only |
| File format | PDF/X-4 (or PDF/X-1a:2001 for older workflows) with fonts embedded or outlined, crop marks and bleed | Name separations, die lines and varnish layers clearly |
| Minimum sizes | Type 6 pt (8-9 pt for body), reversed-out type 8 pt and sans, hairlines 0.25 pt (0.5 pt reversed) | Smaller on uncoated, textured stock |
| Common sizes | A4 210x297 mm; A5 148x210; A3 297x420; DL 99x210; US Letter 8.5x11 in; Tabloid 11x17; business card 85x55 mm (EU) or 3.5x2 in (US) | Confirm trim size with the printer; A and B series vs US |
| Paper weights | Text 90-150 gsm; covers and cards 250-400 gsm; bound books use 80-120 gsm text | Coated, silk, uncoated and recycled change color and dot gain |
| Binding | Saddle stitch up to about 64 pages (multiples of 4); perfect bound from about 48 pages; wire-o; case bound | Spine width = sheets x paper caliper; verify with a dummy |
| Finishes | Spot UV, foil, emboss/deboss, die cut, soft-touch lamination, edge painting | Each is a separate, named layer; allow 0.5 mm trapping tolerance |

## Structure and hierarchy

- **Format follows use:** pieces that are handed over (cards, leaflets) need one message and one action; pieces that are kept (catalogs, reports) need navigation: contents, running heads, folios, indexes.
- **Grid:** choose columns from the trim size (A4: 4-6 columns, 12-15 mm margins; 5 mm baseline units); keep margins larger at the spine and bottom (optical margins).
- **Hierarchy:** three type levels per spread (headline, subhead, text) plus captions; use scale contrast of at least 1.5x between levels and a consistent baseline.
- **Cover and first spread:** one idea, one image, strong title; the back cover carries contact and action. For brochures, design the front panel to work alone on a rack.
- **Folds:** tri-fold panels need a narrower inner panel (about 1-2 mm); put critical copy away from folds; define reading order across panels.
- **Variable data and versions:** reserve fixed areas and character limits.

### Layout settings by piece

| Piece | Trim | Margins and type |
| --- | --- | --- |
| Business card | 85x55 mm (EU) or 3.5x2 in (US) | 4-5 mm safe; name 9-10 pt, details 7-8 pt; 350-400 gsm |
| Flyer (A5 / A6) | 148x210 / 105x148 mm | 8-10 mm margins; headline 28-48 pt, body 9-10 pt |
| Brochure (A4 tri-fold, DL panels) | 297x210 mm folded to 99x210 mm | 8-10 mm margins; inner panel 1-2 mm narrower; body 9-10 pt |
| Poster (A3 / A2 / A1) | 297x420 / 420x594 / 594x841 mm | 10-20 mm margins; headline 60+ pt; read at 1-3 m |
| Report or book (A4 / A5) | 210x297 / 148x210 mm | Inner margin 20 mm, outer 15 mm, top 15 mm, bottom 20 mm; body 9.5-10.5 pt |
| Letterhead and stationery | A4 210x297 mm | 20-25 mm left margin; letter text 10-11 pt; keep the logo block under 40 mm tall |

## Craft defaults

- Typography: text 8.5-10.5 pt (serif) or 8-9.5 pt (sans) with 120-140% leading and 45-75 characters per line; justified text requires hyphenation control; avoid rivers.
- Color: design with the paper in mind. Uncoated stock dulls color and increases dot gain, so lift darks and reduce saturation expectations; proof on the actual stock.
- Images: sharpen for print, soft-proof in the output profile, avoid heavy shadows that plug in uncoated stock.
- Rules and tints: tints under 10% may disappear; hairlines below 0.25 pt break up; large solid fills show banding or streaks, so add a subtle texture or use a spot color.
- Black: pure K for body text; rich black for large fields and reversals only; keep registration color (all inks) out of artwork.
- Finishing: use one or two finishes with intent (foil on the logo, spot UV on the title); never on body text.
- Sustainability: FSC or PEFC-certified stock, soy or vegetable-based inks, fewer coatings to ease recycling.

## Production and handoff

- Workflow: layout in InDesign, Illustrator or Affinity Publisher; link images; preflight (Adobe Acrobat or InDesign preflight, PitStop); package fonts and links.
- Proofs: contract proof (Fogra-certified or digital proof) for color-critical work, press check for large runs; for packaging-like work request a dummy.
- Send: the PDF/X file, a low-resolution reference PDF, a spec sheet (quantity, size, paper, finish, delivery), and Pantone references. The `print-packaging-social` skill holds a deeper prepress and finishing guide.
- Lead times: allow 3-10 working days for digital, 2-4 weeks for offset with finishing, plus shipping; keep a 5-10% overage for waste.
- Accessibility and inclusion: type 12 pt or larger for general audiences (14 pt for older readers), 4.5:1 contrast for text on tinted fields, large-print versions on request, Braille or tactile options for key documents.
- Regulatory: disclosures with minimum sizes (financial, health, alcohol, tobacco) vary by jurisdiction; confirm with counsel.

## QA checklist

- [ ] Trim size, bleed (3 mm / 0.125 in), crop marks and safe margin verified against the template.
- [ ] All images 300 ppi at final size; no RGB or unintended spot colors in the final PDF.
- [ ] Fonts embedded or outlined; no missing links; PDF/X preflight passes.
- [ ] Black text is 100K only; rich black only in large areas; total ink within limit.
- [ ] Folds, die lines, varnish and foil layers are named and set to overprint correctly.
- [ ] Proof checked for color, type legibility, spelling, contact details and legal copy.
- [ ] Pagination, folios, imposition and spine width confirmed with the printer.
- [ ] Accessible alternative (PDF with tags, large print) planned where required.

## Reference anchors

- Robert Bringhurst, *The Elements of Typographic Style*; Josef Müller-Brockmann, *Grid Systems in Graphic Design*
- Ellen Lupton, *Thinking with Type*; Jan Tschichold, *The Form of the Book*
- Adobe InDesign and Acrobat preflight documentation; ISO 15930 (PDF/X) and ISO 12647 (process control in print)
- Fogra (fogra.org) and GRACoL/IDEAlliance for color standards
- Pentagram, Experimental Jetset and Studio Dumbar printed work as craft benchmarks for finishes and typography
