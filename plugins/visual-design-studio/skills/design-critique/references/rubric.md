# Critique rubric

Version-Timestamp: 2026-10-20 02:29:27 UTC

Twelve criteria, each scored 1-5 from rendered screenshots at real sizes, never from source code or a description. Calibrate before scoring by looking at the [FORM/TIDAL benchmark](../../../library/examples/quality-benchmark/README.md) (what 4-5 looks like for two very different briefs) and the [AI-tells gallery](../../../library/examples/ai-tells/index.html) (what 2-3 looks like and how it moves to 5).

## Scoring rules

- **Target for client delivery: 4 or higher on every applicable criterion.** Do not average. One 2 blocks delivery even if everything else is 5.
- **Directions shown for selection** (stylescapes, first concepts): 4+ on Brief fit and Distinctiveness, 3+ elsewhere. Polish comes after the client picks.
- **Internal work in progress:** any score is fine; the list of defects is what matters.
- **Gates that cap a score regardless of how it looks:** a false or unsupported claim caps Brief fit at 1; any WCAG 2.2 AA failure on core content or a core task caps Accessibility at 2; horizontal overflow or clipped text at a target width caps Responsiveness at 2; placeholder copy (lorem, "Your headline here") caps Craft at 2.
- **Every score below 4 names a defect**: what, where (width, section, selector or crop), evidence (screenshot path, measured value) and the fix.
- **N/A is allowed** with a reason (Interaction states for a printed poster; Responsiveness becomes format adaptation for fixed-size work).
- **Tells lower Distinctiveness:** count catalog tells from [ai-tells.md](ai-tells.md) that the brief did not ask for. 0-1: no cap. 2-3: cap at 3. 4 or more: cap at 2.

## 1. Brief fit

Does it serve the stated audience, job, channel and constraints, and keep every mandatory and invariant?

- **5** Every element traces to the brief. A stranger could reconstruct audience, offer and tone from the design alone. Mandatories, legal lines and locked assets are present and correct.
- **4** Right audience and job; one secondary element is generic or slightly off-tone.
- **3** Right category, wrong emphasis: sells features when the brief asked for reassurance, or tone drifts between sections.
- **2** Generic for the category; the key message or a mandatory is missing; tone conflicts with the audience (jokey copy in a debt or grief flow).
- **1** Wrong audience, contradicts a locked brand rule, or makes a claim nobody supplied.

## 2. Distinctiveness (name-swap test)

Cover the logo and swap in a competitor's name. If nothing else has to change, the design is not distinctive.

- **5** The swap fails: the type, color pairing, graphic device, image approach or voice is ownable and used consistently. People could name the brand from a crop.
- **4** One clear ownable device; the rest is competent and appropriate to the category.
- **3** Competent but interchangeable. The swap works with minor copy edits.
- **2** Template look with two or three unrequested tells.
- **1** Indistinguishable from a starter template; four or more tells.

## 3. Hierarchy (squint test)

Blur your eyes, or apply a 6-8px Gaussian blur to the screenshot. What do you see first, second, third?

- **5** One entry point, then a clear second and third level. Reading order matches business priority. One primary action per view.
- **4** Clear entry point; two second-level elements compete mildly.
- **3** Two elements fight for first place, or the primary action looks like the secondary.
- **2** Flat: headline, body and buttons at similar size and weight; the blurred image is an even gray field.
- **1** No order. The key message or action takes more than 5 seconds to find.

## 4. Typography

- **5** Families chosen for the brand with a stated reason; a held scale (ratio such as 1.25 or 1.333; display can jump steps); body 16-18px, line-height 1.4-1.6, measure 45-75ch; display tracking tightened (-0.01 to -0.04em at 48px+); no single-word last lines in headings; tabular figures where numbers align; webfonts load with no fallback glyphs.
- **4** Sound scale and readable text; one or two setting misses (a heading runt, loose display tracking, a widow in a pull quote).
- **3** Readable but default: one system sans for every role, ratio unclear, measure over 85ch or under 35ch somewhere.
- **2** Hierarchy relies on color or caps alone; body under 15px or line-height under 1.3; several heading runts; visible fallback font.
- **1** Illegible, clipped or overlapping text; faux bold or italic; families mixed with no logic.

## 5. Color and contrast

- **5** Palette has named roles (canvas, surface, text, muted text, accent, status) and proportions (accent on roughly 5-15% of the surface). All text meets 4.5:1 (3:1 at 24px+ or 18.66px+ bold); UI boundaries and focus rings meet 3:1; status is never color alone; dark mode, if shipped, is designed rather than inverted.
- **4** Roles clear and AA met everywhere; the accent is slightly overused or one surface is muddy.
- **3** Default or borrowed palette with little link to the brand; AA met but muted text hovers at 4.5-5:1 across large areas.
- **2** One or more text or UI contrast failures; accent on everything.
- **1** Body text fails AA, or color is the only carrier of meaning (errors, status, required fields).

## 6. Layout and spacing

- **5** An explicit grid (columns, margins, gutters) that holds across sections; spacing from a scale (4 or 8px base) with proximity that groups related items; deliberate asymmetry or tension; few, obvious alignment axes.
- **4** Grid holds; a few off-scale values or uneven gaps between equivalent items.
- **3** Everything centered or stacked in identical sections; spacing is even but does not group.
- **2** Misalignments visible at a glance; cramped or floating elements; gutters change between sections.
- **1** Overlaps, collisions or a broken layout.

## 7. Imagery and iconography

- **5** Imagery is specific to this brand and subject: art-directed photography, a custom illustration system, true product renders or real data. One icon family, one stroke weight, one grid. Every image earns its space.
- **4** Specific imagery with one inconsistency (an icon from another set, an off-brand crop).
- **3** Relevant but generic stock or illustration; icons mix weights or styles.
- **2** Decorative filler: orbs, blobs, blob people, stock smiles, emoji as icons, a fake dashboard.
- **1** Misleading, low-resolution, watermarked or unlicensed images; AI artifacts (garbled text, extra fingers) left in.

## 8. Consistency

- **5** The same component looks and behaves the same everywhere; tokens are used throughout; radius, elevation, spacing and voice are uniform across pages, screens or frames.
- **4** One or two one-off values.
- **3** Several drifts: three button styles, two card radii, mixed date formats.
- **2** Inconsistencies a user would notice: different navigation per page, different names for the same thing.
- **1** Looks like several products stitched together.

## 9. Interaction states

N/A for static print and stills. For motion-only pieces, score the motion system instead.

- **5** Every control has default, hover, focus-visible, active, disabled and loading states; forms have empty, error, success and help states; motion is 120-320ms for UI with a reduced-motion alternative.
- **4** All core states; one edge state missing (loading on a secondary action, empty state for a rare list).
- **3** Hover only; focus left to the browser default; one generic error message for everything.
- **2** No visible focus or no error states; states indistinguishable from each other.
- **1** Interactive elements cannot be identified as interactive.

## 10. Accessibility

Run the [15-minute audit](accessibility-audit.md) before scoring.

- **5** axe clean; keyboard-only pass completes every task with visible focus and no traps; 200% zoom and 320px reflow lose nothing; targets 24px minimum (44px for primary touch); headings, landmarks, labels and alt text correct; reduced motion honored; screen-reader smoke test passes.
- **4** Measured checks pass; minor issues (a redundant alt, a missing landmark, verbose link text).
- **3** One or two non-blocking failures with known fixes (decorative image announced, skip link missing on a short page).
- **2** Any AA failure on core content or a core task: contrast, keyboard trap, unlabeled field, focus hidden by a sticky header.
- **1** A core task is impossible by keyboard or screen reader.

## 11. Responsiveness

For web and apps check 390, 768 and 1440px (add 320px for reflow). For fixed formats score format adaptation: each size composed for itself (1080x1350 is not a cropped 1920x1080).

- **5** Designed at each width, not squeezed: layout recomposes, type scales fluidly, images are cropped per width, touch targets grow on mobile, no horizontal overflow.
- **4** Works at every width; one breakpoint is merely stacked.
- **3** Desktop shrunk to mobile: everything stacks, the hero is oversized, spacing never changes.
- **2** Overflow, clipped text or overlap at one target width.
- **1** Unusable at a target width.

## 12. Craft details

- **5** Optical alignment of icons and type; kerning on display sizes; correct quotes, apostrophes, dashes, units and number formats for the locale; real copy; consistent icon optical sizes; compressed images; nothing to fix at 200% zoom.
- **4** One or two small misses.
- **3** Several small misses: straight quotes, inconsistent number formats, icons sitting off the text baseline.
- **2** Placeholder copy, misspellings, or pixel misalignment visible at 100%.
- **1** Broken images, lorem ipsum, obvious errors.

## Score sheet

Copy into the project's review record for each round.

| # | Criterion | Score | Defect or note (where, evidence) | Fix this round |
| --- | --- | --- | --- | --- |
| 1 | Brief fit | | | |
| 2 | Distinctiveness | | | |
| 3 | Hierarchy | | | |
| 4 | Typography | | | |
| 5 | Color and contrast | | | |
| 6 | Layout and spacing | | | |
| 7 | Imagery and iconography | | | |
| 8 | Consistency | | | |
| 9 | Interaction states | | | |
| 10 | Accessibility | | | |
| 11 | Responsiveness | | | |
| 12 | Craft details | | | |

Record the minimum score, the count of criteria below target, the tells found (by ID) and the screenshot set the scores came from. A score without a screenshot set is not evidence.
