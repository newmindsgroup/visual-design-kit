# Logo design and construction

Version-Timestamp: 2026-10-20 02:07:10 UTC

A strong logo is one idea, drawn with control, that is recognizable as a silhouette, legible at 16px and still interesting at 10m. This file covers choosing the logo type, exploring territories, constructing and optically correcting the drawing, testing it, and delivering the files.

## Logo types

| Type | Public examples | Use when | Watch for |
| --- | --- | --- | --- |
| Wordmark (logotype) | FedEx, Google, Coca-Cola | Name is short to medium, distinctive and the main asset; media budget is modest | Needs a compact form (initial or monogram) for avatars and favicons |
| Lettermark or monogram | IBM, HBO, Louis Vuitton LV | Long name, heritage or luxury, app icons | Initials alone carry no meaning until famous |
| Pictorial symbol | Apple, Twitter's former bird, Shell | A concrete object owns a link to the name or story | Literal objects become clichés in crowded categories |
| Abstract symbol | Nike, Mastercard, Chase | Global brand, many products, strong media budget | Meaning must be built through exposure; many look alike |
| Emblem or badge | Starbucks (earlier rings), Harley-Davidson, sports crests | Heritage, institutions, merchandise, craft | Fine detail fails small; needs a simplified secondary mark |
| Combination mark | Adidas, Airbnb, Spotify | Default for new brands: symbol for small spaces, wordmark for clarity | Lockup proportions must be designed, not just placed side by side |
| Mascot or character | Michelin Bibendum, Duolingo owl | Consumer, kids, community, social-first brands | Needs a character system (poses, expressions), not one drawing |
| Dynamic or generative | MIT Media Lab (2011), City of Melbourne (2009) | Cultural, tech or multi-program brands with motion and code capability | Requires fixed constants and governance; see [identity system](identity-system.md) |

Rule of thumb: a new brand with an app or social presence needs a symbol or monogram as well as the wordmark.

## Concept exploration to three territories

1. **Word list.** 30-50 words from the platform: attributes, product nouns, process verbs, places, metaphors, the name's letters and meaning.
2. **Thumbnails.** 50-100 sketches at thumbnail size (about 2-3 cm, or 64px in vector), five minutes each at most. Small size forces silhouette thinking.
3. **Idea sources.** Push across at least five: the name (letterforms, meaning, sound), the product or process, place or heritage, a metaphor from the positioning, a gesture or behavior, a typographic detail, a system device (frame, crop, pattern).
4. **Cluster** the sketches into ideas. Discard the first obvious idea in each cluster only if a reverse image search shows it is common in the category.
5. **Pick 3 territories** that differ in idea and in at least two of: logo type, shape language (geometric, organic, angular, calligraphic), type genre (grotesque, geometric sans, serif, slab, script, custom).
6. **Develop each** to one hero mark and two alternates, plus a wordmark lockup and three applications (app icon, business card or letterhead, one channel from the brief).
7. **Swap test.** If two territories' rationales still make sense after swapping their marks, they are not distinct. Redo one.

Present each territory on the same template: name, one-line idea, mark in black on white at the same optical size, reversed version, lockup with the real name, three applications, what it signals, risks. Mark unselected options clearly as rejected after the decision.

## Construction

Build on a unit system so every decision is repeatable.

- **Base unit.** Set the main stroke weight to 1u. Express radii, gaps, counters and terminal lengths as multiples or simple fractions of it (0.25u, 0.5u, 1u, 2u). A common grid: cap height 10u for a wordmark, or a 24u or 48u square for a symbol.
- **Primitive geometry.** Start from circles, squares and straight lines when the brand is precise; switch to hand drawing over the geometry when it should feel human. Use one radius family: for example inner corner radius = outer radius − stroke.
- **Bezier hygiene.** Put on-curve points at extrema (where the tangent is horizontal or vertical), keep handles horizontal or vertical at those points, use as few points as possible, and avoid kinks where a curve meets a straight. A circle quadrant uses handles about 0.552 of the radius; superellipse or "squircle" corners use longer handles (roughly 0.6-0.75) for a softer join.
- **Continuity.** Where a curve meets a straight, aim for curvature continuity (G2) rather than just tangent continuity (G1). G1-only joins show a visible "bump" in large signage and reflections.
- **Golden ratio and grids.** Use proportional systems only if they produce a better drawing. Never retrofit circles over a finished mark to justify it. Publish a construction drawing only for relationships that drove decisions.
- **Custom lettering.** Start from a typeface whose license permits modified logo artwork: the OFL does; many commercial EULAs do, but some restrict modification or require an extended license, so read it. Then redraw: adjust spacing, weight, terminals, apertures and one or two signature letters. Outline the final, keep a live-text working file, and record the source font and license.

## Optical corrections

Mathematically equal shapes do not look equal. Typical values (a common starting point; judge at the final sizes):

| Correction | Typical value | Why |
| --- | --- | --- |
| Round overshoot (O, C, S, bowls, circles) | 1-3% of cap or x-height beyond baseline and cap line | Curves touch the line at a single point and look smaller |
| Pointed overshoot (A apex, V and W vertices, triangles) | 2-5% beyond the line; more as the angle gets sharper | Points thin to nothing and look short |
| Circle next to a square of equal perceived size | Circle diameter about 10-12% larger than the square side | Same logic as icon keylines (circle 20px vs square 18px on a 24px grid) |
| Horizontal vs vertical strokes | Horizontals 5-12% thinner than verticals for a monoline look | The eye reads horizontal strokes as heavier |
| Diagonal strokes | 3-8% thinner than verticals, thinned further where they meet | Diagonals and joins accumulate visual weight |
| Junction thinning | Thin strokes 10-25% where they meet at acute angles (v, w, k, n shoulders) | Prevents dark spots and closed counters |
| Ink traps | Notch 5-15% of stroke width for small or print use; 15-30% for very small sizes or porous paper | Ink spread and screen blur fill acute joins (Matthew Carter's Bell Centennial is the classic example) |
| Visual center | Place the mark 2-5% above geometric center in frames, tiles and badges | Objects centered mathematically look low |
| Directional shapes | Shift a play-style triangle toward its point by about 5-10% of its width | Full centroid centering (about 17%) overshoots; bounding-box centering looks off-center |
| Reversed (light on dark) | Reduce stroke weight 2-5% or draw a reversed master | Light shapes on dark grounds look bolder (irradiation) |
| Small-size master | Open counters and apertures, heavier hairlines, +2-5% letter spacing, fewer details | Detail merges below about 24px or 8mm |
| Spacing | Space by area between letters: straight-straight loosest, straight-round tighter, round-round tightest | Equal metric gaps look uneven |

Test every correction at the smallest and largest real size; corrections that are invisible at 1000px often make or break 32px.

## Scalability and reproduction tests

| Test | Pass condition |
| --- | --- |
| 16x16 and 32x32 px favicon, 1x pixel preview | Symbol or monogram recognizable; key edges snapped to whole pixels at 16 and 32 |
| 24-48px UI and avatar (circle crop) | Readable inside a circle with the mark in the central 70-80% |
| Wordmark at 80-100px wide on screen | Every letter distinct, no filled counters |
| 1-color black, 1-color white on black | No reliance on color or gradient to separate parts |
| On a busy photo and on the brand's mid-tone color | Holds with a defined container or clear-space rule |
| Grayscale and color-blindness simulation | Parts still separate (deuteranopia and protanopia at minimum) |
| Blur test (Gaussian 4-8px at 200px wide) or view at 10% scale | Silhouette still recognizable |
| Competitor lineup | Distinct among 8-12 category logos in grayscale at equal height |
| Print small (8-10mm) on uncoated stock | No fill-in; ink traps working |
| Embroidery, emboss, laser etch | Lines under about 1mm and text under about 5mm cap height usually fail; confirm with the vendor |
| Large format (2m+ sign, building) | Inspect curves at 800-1600% zoom for kinks and uneven curvature |
| Motion | The mark can be built, revealed or animated without breaking its geometry |

## Clear space and minimum size

- **Clear space** is defined by a measurable part of the mark so it scales with it: "x = cap height of the wordmark" or "x = width of the symbol". 1x on all sides is a common starting point; 0.5x for tight UI contexts as a documented exception; 1.5-2x for luxury and editorial use.
- **Minimum size** comes from tests of the actual mark. Starting points:

| Version | Screen minimum | Print minimum |
| --- | --- | --- |
| Wordmark | 80-100px wide | 20-25mm wide |
| Horizontal combination mark | 100-120px wide | 25-30mm wide |
| Stacked combination mark | 60-80px wide | 15-20mm wide |
| Symbol or monogram alone | 16px (favicon master), 24px elsewhere | 6-8mm |
| Lockup with tagline | 150px wide; tagline cap height at least 8-10px | 35mm wide; tagline at least 6pt |

Below the tagline minimum, drop the tagline. Below the wordmark minimum, switch to the symbol.

## Color versions and lockups

**Color versions:** full color positive, full color reversed, 1-color black, 1-color white, 1-color brand color, and a spot-color version where Pantone is used. Specify each color as HEX (sRGB), RGB, CMYK for coated and uncoated (separate builds, not one conversion), Pantone C and U, and RAL or NCS for paint and signage. Logos are exempt from the WCAG text contrast requirement, but aim for at least 3:1 between the mark and its background so it stays recognizable; compute it rather than guessing.

**Lockups** (design each one; never just place two files side by side):

| Lockup | Typical rule |
| --- | --- |
| Horizontal | Symbol height = cap height × 1.3-1.6, gap = 0.5-1x symbol width |
| Stacked | Symbol centered over the wordmark; gap = 0.5-1x cap height |
| Symbol only, wordmark only | For small or repeated placements |
| With tagline or descriptor | Tagline at 25-40% of wordmark cap height, aligned to a wordmark edge |
| Sub-brand or endorsed | Masterbrand name at 30-50% of the sub-brand's cap height ("by Brand") |
| Co-brand or partner | Equal optical weight, a vertical rule or "x" between, gap = clear space on both sides |
| Multiscript (Arabic, Hebrew, CJK, Devanagari) | Native lettering matched in weight and optical size; RTL lockups mirror order; align by visual center, not baseline alone |
| Responsive set | Full lockup → horizontal → wordmark → symbol, switching at measured widths |

## Deliverable file set

| File | Spec | Use |
| --- | --- | --- |
| Native master | Illustrator, Figma or Affinity source with live type and construction layers | Editing; never sent to vendors |
| SVG | Outlined text, `viewBox` set, no embedded raster, no editor metadata, `<title>` with the brand name; monochrome version uses `fill="currentColor"` | Web and apps |
| PDF | Vector, fonts outlined; PDF/X-4 for print vendors | Print, Office, partners |
| EPS | Only when a legacy vendor (signage, embroidery, promotional products) requests it | Legacy workflows |
| PNG | Transparent; @1x/@2x/@3x, or 500, 1000 and 2000px wide | Office, social, quick use |
| Favicon set | `favicon.ico` (16, 32, 48), `icon.svg` (can switch colors with a `prefers-color-scheme` media query), `apple-touch-icon.png` 180x180, manifest icons 192 and 512, plus a 512 maskable icon with the mark inside the central circle of radius 40% | Websites and PWAs |
| iOS app icon | 1024x1024 square master, no transparency, no pre-rounded corners (the system masks it); dark and tinted variants (iOS 18+) and layered sources for the current icon tooling | App Store and devices |
| Android adaptive icon | Foreground and background layers on a 108x108dp canvas, 72dp visible, key artwork within the central 66dp; monochrome layer for themed icons; 512x512 Play Store icon | Android launchers |
| Social avatar | 400x400 minimum (800x800 better), mark inside the central 70-80% for circle crops | Profiles |
| Color specs sheet | All values per version and color space | Vendors and guidelines |

**File naming:** `brand-logo-[lockup]-[color]-[space].[ext]`, for example `ledgerly-logo-horizontal-fullcolor-rgb.svg`, `ledgerly-symbol-white-cmyk.pdf`. Add a version folder (`v1.0`) and a readme listing fonts, licenses and contacts.

Before delivery: reopen every file in a different app than the one that exported it, check bounding boxes and artboards, confirm no stray points or hidden layers, and compare exports against the master at matched size.

## AI tools in logo work

- Use image generators for mood and rough sketch prompts only. Treat their output as reference, never as the master.
- Redraw the chosen idea in vector by hand. In the US, the Copyright Office requires human authorship for protection, so purely generated marks may be unprotectable under copyright; trademark rights depend on use and distinctiveness. Record what was generated and what was drawn.
- Run a reverse image search on every finalist; generators reproduce common shapes.

## Common failures

- Detail that only works at 1000px → design at 32px first, then add detail for large sizes.
- Construction grid presented as proof of quality → judge the rendered mark, not the overlay.
- One master stretched across every size → a small-size master and a reversed master where tests show the need.
- Lockups improvised by each vendor → ship every lockup as a file with its spacing rule.
- Missing one-color version → required for stamps, etching, embroidery, fax-style documents and partner materials.
- Delivering only PNGs → vector masters plus the favicon and app icon sets.

See the deep process skills for client approvals: [logo refinement](../../../library/draft-skills/design-logo-refinement/SKILL.md) (with [lettering and optics](../../../library/draft-skills/design-logo-refinement/references/lettering-and-optics.md)), [logo variants](../../../library/draft-skills/design-logo-variants/SKILL.md) and [logo evaluation](../../../library/draft-skills/design-logo-evaluation/SKILL.md).
