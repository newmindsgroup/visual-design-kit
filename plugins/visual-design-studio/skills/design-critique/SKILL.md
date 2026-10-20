---
name: design-critique
description: >-
  Renders a design at real sizes, screenshots it, scores it against a 12-criterion rubric, lists up to five prioritized fixes, then revises and re-renders until the target is met. Includes a catalog of generic-AI design tells, the name-swap and squint tests, and a 15-minute accessibility audit. Use when reviewing, critiquing, QA-ing or polishing any page, screen, deck, social post, stylescape or brand asset; when asked "is this good", "make it better" or "does this look AI-made"; or before delivering work to a client.
license: MIT
metadata:
  version-timestamp: "2026-10-20 02:32:54 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 02:32:54 UTC"
---

# Design critique

Good critique works from evidence. It judges rendered pixels at real sizes against the brief, names each defect with a location and a fix, keeps defects apart from taste, and proves every revision with a before and after.

## Defaults

| Setting | Default | Move off it when |
| --- | --- | --- |
| Evidence | Screenshots of the rendered artifact, never source code or a description | Only prose exists: label the critique "conceptual" and say what to render |
| Web and app widths | 390, 768, 1440 px, full page; add 320 for reflow | The brief names devices (kiosk 1080x1920, TV 1920x1080, a specific phone) |
| Other formats | Native size: social 1080x1350 or 1080x1920, slides 1920x1080, print as a PDF raster at 150 dpi of the final trim, video as key frames | Distance media (OOH, signage): also view at about 10% scale to simulate viewing distance |
| Rubric target | 4+ on every applicable criterion for client delivery; never average | Directions for selection: 4+ on Brief fit and Distinctiveness, 3+ elsewhere |
| Fixes per round | 5 at most, most impactful first, defects before preferences | Never more |
| Rounds | Up to 3 before showing a person | The user asked for autonomous iteration |
| Contrast | 4.5:1 body, 3:1 large text (24px+, or 18.66px+ bold) and UI | Older or low-vision audiences: aim for 7:1 body |
| AI tells | 0-1 unrequested tells | The brief asks for the style; record why |
| Stop | Target met, or only preferences remain | Two rounds without score movement: rethink the direction, do not keep polishing |

## Workflow

1. **Freeze the brief.** Audience, job, channel, mandatories, invariants and anything already approved. If something is missing, state the assumption in one line.
2. **Render the real thing.** For HTML, SVG or a URL: `node scripts/render_review.mjs <file-or-url> --full-page` (path relative to this skill; add `--serve` when the page uses `fetch` or ES modules, `--widths 1080x1350` for fixed formats). It writes one PNG per width plus `report.json`. For other formats export PNGs at native size first (Figma export, `pdftoppm -r 150 -png`, `ffmpeg -ss 3 -frames:v 1`).
3. **Look at every screenshot** before reading the report. Note the first thing you see, the second, and anything broken. Then read the report: horizontal overflow, clipped text, single-word last lines, contrast failures, unmeasured text over images, rendered fonts and fallbacks, axe violations, failed requests.
4. **Run the squint test.** Blur the screenshot by 6-8px (or squint). There should be one clear entry point per view, then a second and third level. An even gray field means flat hierarchy; three equal blobs mean template cards.
5. **Run the name-swap test.** Cover the logo and read a competitor's name into the design. If nothing else needs to change, it is not distinctive yet: find or create one ownable device (type, color pairing, graphic system, image approach, voice).
6. **Scan for tells** with [ai-tells.md](references/ai-tells.md) and log them by ID (AT-01 to AT-26). Compare against the matching pair in the [AI-tells gallery](../../library/examples/ai-tells/index.html).
7. **Audit accessibility** for anything interactive with the [15-minute audit](references/accessibility-audit.md).
8. **Score** all twelve criteria in the [rubric](references/rubric.md). Every score below 4 names a defect: what, where (width and region), evidence (screenshot, measured value) and fix. Apply the rubric's caps (false claim, AA failure, overflow, placeholder copy).
9. **List up to five fixes**, most impactful first. Format: `[Defect|Preference] criterion: problem (evidence) -> change -> expected effect`.
10. **Revise** under [revision discipline](references/revision-discipline.md): scoped edits, invariants frozen, tokens and components rather than one-offs, no "while I'm here" changes.
11. **Re-render with identical settings** into a new folder (`--out review/round-N`), compare before and after at every width, confirm invariants are untouched and no other score dropped, then re-score.
12. **Stop** when the target is met or only preferences remain. Report the final scores, before and after screenshot paths, open preferences as options with their trade-off, and anything you could not test.

## Critique output

Write the critique in this shape, in chat or in the project's review record:

```text
Round N, <artifact> @ <version>, widths 390/768/1440, screenshots: review/round-N/
First read (5 s): <what the eye lands on first, second, third>
Name-swap: <ownable: which device | swappable: what any rival could reuse>   Squint: <one entry point | competing: what>
Tells: <AT-IDs found, or none>
Scores: Brief 4 | Distinct 3 | Hierarchy 4 | Type 4 | Color 5 | Layout 4 | Imagery 3 | Consistency 4 | States 4 | A11y 4 | Responsive 3 | Craft 4  (min 3)
Fixes this round (max 5, most impactful first):
1. [Defect] Responsiveness: hero H1 overflows at 390 (390.png, #hero) -> clamp(36px, 9vw, 64px) -> no overflow
2. [Defect] Distinctiveness: interchangeable three-card row (1440.png) -> numbered process with real durations -> name-swap fails
Preferences offered: <option A vs B, trade-off>
Not tested: <screen reader on Windows, real devices, ...>
```

## Defects versus preferences

- **Defect:** breaks the brief, a stated requirement, a measurable threshold (contrast, target size, overflow, clipping) or a craft rule with a clear consequence (a runt in a headline, mixed icon families, an invented statistic). Fix it.
- **Preference:** a taste call where both options pass every measure (warmer gray, pill or square buttons, a two- or three-line headline). Offer it, label it "preference", let the client choose.
- A preference becomes a defect when it is the client's stated requirement or a locked brand rule. Never present taste as a rule.

## Decisions that change the answer

- **Stage.** Exploration critiques direction (Brief fit, Distinctiveness) and ignores polish; delivery critiques everything at the 4+ target.
- **Requested style.** Glass, gradients, neon or symmetry asked for by the brief are not tells; judge the execution. `python3 ../../library/scripts/atlas.py show style.<slug>` prints the style entry's path; read its "Clichés and AI tells" and "Accessibility notes" sections.
- **Channel.** Web and apps: three widths plus keyboard and screen reader. Social and OOH: legibility at thumbnail or distance and safe areas. Print: final trim, bleed, minimum type size (7-8pt for captions as a common floor). Motion: key frames, reading holds and a reduced-motion version.
- **Audience.** Older adults, children and low-literacy audiences raise the text size, contrast and target-size bar; expert users can take higher density. Query the audience entry: `python3 ../../library/scripts/atlas.py query "older adults"`.
- **Script and market.** The single-word-last-line check is whitespace-based; for Chinese, Japanese, Thai and other scripts without spaces, check line breaks by eye. Check RTL layouts mirror correctly.
- **Locked assets.** When the logo, palette or copy are fixed, critique the system around them and say which defects the locks cause.

## Common failures

- Critiquing from code or a description -> render first and look at the pixels.
- Checking only 1440 px -> most breaks happen at 390 and 768.
- Twenty fixes in one pass -> five, ranked; the rest go to the next round.
- Averaging scores -> the minimum governs delivery.
- "Clean" mistaken for finished -> run the name-swap test; clean and interchangeable scores 3.
- Fixing a runt with a non-breaking space at one width and causing overflow at another -> re-render every width after every change.
- Treating the report as the verdict -> it lists leads; the screenshots decide.
- Endless polishing -> obey the stop rule and show a person.
- Claiming approval -> say "ready for review"; only a named person approves.

## References

- [Rubric](references/rubric.md): twelve criteria with 1-5 descriptors, caps and a score sheet. Read before scoring.
- [AI tells](references/ai-tells.md): 26 named tells with what they look like, why they happen and the fix.
- [Accessibility audit](references/accessibility-audit.md): the 15-minute pass (axe, keyboard, focus, zoom and reflow, contrast, targets, motion, VoiceOver and NVDA).
- [Revision discipline](references/revision-discipline.md): scoped changes, invariants, before and after evidence, stop rules.
- [render_review.mjs](scripts/render_review.mjs): Node 18+, no bundled dependencies. Install Playwright and axe-core in the working project (`npm i -D playwright axe-core && npx playwright install chromium`) or point `PLAYWRIGHT_MODULE`, `PLAYWRIGHT_CHROMIUM` and `AXE_SCRIPT` at existing copies. `--exclude SELECTOR` skips deliberate controls or third-party embeds; `--strict` exits 2 on blocking findings for CI.
- [AI-tells gallery](../../library/examples/ai-tells/index.html) and its [README](../../library/examples/ai-tells/README.md): 18 tells rendered generic versus better across 18 industries and styles.
- [Quality benchmark](../../library/examples/quality-benchmark/README.md): FORM and TIDAL calibration briefs with generic and wrong controls. Compare before you score.
- [Stylescapes](../../library/examples/stylescapes/README.md): twelve excellent, distinct directions to calibrate what a 5 looks like outside one aesthetic.
- Deep process for client projects: [design taste](../../library/draft-skills/design-taste/SKILL.md), [website visual review](../../library/draft-skills/design-web-visual-review/SKILL.md), [website accessibility](../../library/draft-skills/design-web-accessibility/SKILL.md), [browser QA](../../library/draft-skills/design-web-browser-qa/SKILL.md), [media quality evaluation](../../library/draft-skills/design-media-quality-evaluation/SKILL.md), [delivery](../../library/draft-skills/design-quality-delivery/SKILL.md) and [stage handoff](../../library/draft-skills/design-stage-handoff/SKILL.md).

Catalog IDs covered: design-taste, web-visual-review, web-accessibility, web-browser-qa, media-quality-evaluation, delivery
