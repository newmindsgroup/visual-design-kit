# Cinematic landing addendum

Version-Timestamp: 2026-11-05 18:10:00 UTC

Adapted from MotionSites claude-skill (MIT), see NOTICE.md.

Use this with the [rubric](rubric.md), not instead of it, when reviewing a cinematic landing page, hero or single-file showpiece built with `web-design`'s [cinematic landing workflow](../../web-design/references/cinematic-landing.md). It adds blocking checks, three criteria the twelve do not isolate (signature, media integration, motion choreography) and the look-and-fix loop's own stop rule.

## Evidence for this loop

```sh
node ../scripts/render_review.mjs index.html --widths 390,1440 --early 350 --full-page --serve
node ../scripts/render_review.mjs index.html --widths 390,1440 --reduced-motion --out render-review/reduced
```

Look at `*-1440.png`, `*-390.png` and both `*-early.png` frames as images first, then read the report. Judge motion from the code plus the early and settled frames; when it matters, screen-record at 60 fps and step through. Playwright's bundled Chromium has no H.264 decoder: a video marked "format or codec not supported by this browser" is a test limit, not a defect.

## Blocking (fix before scoring)

Any of these fails the page whatever else is good:

- Console errors, failed requests (status 400 or more), broken images, or a video that should play but reports an error other than the codec limit above.
- Horizontal overflow at 390 px (`horizontalOverflow: true`).
- A white or blank first paint on a dark design (`paintedBackground` reports "none set", or the early PNG is white): set the background on `html` and `body` in the first CSS rule.
- Text you cannot read: over a busy part of an image or video, under 4.5:1 for body text (3:1 for large text), or clipped. The report marks text over media as unmeasured; check the busiest frame by eye.
- The display font not loaded, or the H1 falling back to a system font (check rendered fonts in the report).
- Broken layout at either width: unintended overlaps, a nav wrapping onto two lines, a desktop hero taller than the viewport that hides the CTA.
- Placeholder or filler copy ("Lorem", "Your tagline here", "Feature 1"), invented statistics or testimonials.
- Motion with no reduced-motion branch, or anything moving longer than 5 s with no pause control (WCAG 2.2.2).

## Mapping onto the rubric

Score the twelve rubric criteria as usual, plus the three addendum criteria, each 1-5 with the rubric's descriptors and caps. The source review's ten 1-10 criteria map as follows:

| Cinematic review criterion | Scored as |
| --- | --- |
| First glance (3-second test) | Rubric 3 Hierarchy (squint test) and 1 Brief fit |
| Signature | Addendum A1 Signature (and rubric 2 Distinctiveness) |
| Typography | Rubric 4 Typography |
| Composition and space | Rubric 6 Layout and spacing |
| Color and light | Rubric 5 Color and contrast |
| Media integration | Addendum A2 Media integration (and rubric 7 Imagery) |
| Motion | Addendum A3 Motion choreography (and rubric 9 Interaction states) |
| Mobile | Rubric 11 Responsiveness |
| Copy | Rubric 1 Brief fit and 12 Craft details |
| Polish | Rubric 8 Consistency, 9 Interaction states and 12 Craft details |

Rubric 10 Accessibility has no source equivalent; it is always scored.

## A1. Signature

Is there one memorable thing (the media, an interaction, a type moment) that someone would screenshot and share? Average pages have none.

- **5** One signature, executed so well it defines the page; everything else supports it. The name-swap test fails on the signature alone.
- **4** A clear signature with one supporting element competing for attention.
- **3** A recognizable technique used generically (a stock video loop with centred text).
- **2** Several effects of equal weight and no single idea, or a signature copied from a template.
- **1** No idea beyond layout.

## A2. Media integration

Does the image, video or 3D feel like part of the design, cropped, positioned and layered on purpose, rather than a rectangle dropped in?

- **5** The page background equals the media's edge color; the subject sits opposite the copy for the whole loop; mobile is re-cropped; poster and loop are seam-free.
- **4** Integrated on desktop; mobile crop or the poster is merely acceptable.
- **3** Media fills the hero but fights the copy on some frames, or needs a heavy flat overlay.
- **2** A rectangle of footage or stock with no relation to the layout.
- **1** Broken, watermarked, unlicensed or showing recognizable people or brands without rights.

## A3. Motion choreography

- **5** Entrance in reading order, staggered and done by 1.2 s, ease-out; interactions feel physical; ambient motion comes from the media only; reduced motion shows the final state; every loop sits under a pause control.
- **4** Choreographed with one timing miss (a stagger too slow, a hover too big).
- **3** Everything fades up the same way, or the entrance runs past 2 s.
- **2** Distracting loops, shimmer on headlines or competing animations.
- **1** Motion hides content (nothing visible without JavaScript) or flashes more than 3 times per second.

## Scores and the stop rule

For this loop only, convert to a 10-point scale by doubling each 1-5 score (half points allowed, so 3.5 becomes 7). Score the twelve rubric criteria plus A1-A3.

- **Look-and-fix stop rule:** stop iterating when the average is 8 or more and nothing is below 7, or after 3 rounds. Most first drafts land at 6-7; the fixes are what make it good.
- **Client delivery still follows the rubric:** 4 or more (8 here) on every applicable criterion, no averaging. A page that clears the loop with a 7 somewhere has met the loop's stop rule but still carries that criterion as an open defect; list it in "Fixes this round" or "Preferences offered".
- Blocking findings above cap the related criterion at 2 (4 on the 10-point scale) until fixed.

## Fix loop

1. Write down the three weakest scores and, for each, the specific change in values: "H1 from 64px to clamp(3.5rem, 2rem + 6vw, 7.5rem), tracking -0.04em"; "a 40 % black-to-transparent gradient over the bottom 35 % of the video"; "the stats row on one line with 1 px dividers".
2. Make those changes under [revision discipline](revision-discipline.md), re-render with identical settings into `render-review/round-N`, and look again.
3. Repeat until the stop rule is met or for 3 rounds. If something cannot be fixed (no suitable media), tell the client plainly what would lift it.

Common high-impact fixes:

- **Generic:** bigger type, fewer words, a stronger signature, one section or element removed.
- **Busy:** remove decoration, unify radii, add one spacing step, reduce color to canvas, ink, muted and accent.
- **Flat:** depth from a media layer, a gradient scrim, subtle grain, one glass material or light falloff.
- **Text fights the video:** move the text over the calm area, add a scrim, or choose a calmer clip.
- **Mobile broken:** re-crop media with `object-position`, scale display type with `clamp()`, move secondary nav behind a menu.

## Score sheet addition

Append to the rubric's score sheet:

| # | Criterion | Score (1-5) | x2 | Defect or note (where, evidence) | Fix this round |
| --- | --- | --- | --- | --- | --- |
| A1 | Signature | | | | |
| A2 | Media integration | | | | |
| A3 | Motion choreography | | | | |

Record the 10-point average, the minimum, the early-frame result and which renders the scores came from.
