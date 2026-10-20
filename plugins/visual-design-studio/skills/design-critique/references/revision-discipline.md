# Revision discipline

Version-Timestamp: 2026-10-20 02:29:27 UTC

How to revise a design without breaking what already works or what the client already approved, and how to prove each round made it better. The critique finds problems; this file governs the edit.

For client projects with formal records, the deep process lives in [design stage handoff](../../../library/draft-skills/design-stage-handoff/SKILL.md) (baselines, approval references, invariants, resumable handoffs) and [design taste](../../../library/draft-skills/design-taste/SKILL.md) (brief-specific critique and equal-content comparison). Use them when the project keeps a version index; the rules below apply to every revision either way.

## Rules

1. **Five changes per round, at most.** Ranked by impact on the lowest rubric scores. More than five at once makes it impossible to tell which change helped or hurt.
2. **One change, one hypothesis.** Write each as: problem, evidence, change, expected effect. "Hero headline and subhead compete in the squint test (screenshot 1440 #hero): raise H1 from 40 to 64px, drop subhead to 18px regular; expect a single entry point."
3. **Defects first, preferences last.** A defect breaks a rule, the brief or a measurable threshold. A preference is a taste call with no failing measure. Fix all defects before spending a round on preferences, and label preferences as such to the client.
4. **Freeze the invariants.** Before editing, list what must not change: approved copy, logo and lockups, locked colors and fonts, approved sections and components, legal lines, image subjects. Check them again after the edit.
5. **Change the system, not the instance.** Fix a token, a component or a layout rule rather than one-off overrides, unless the defect is genuinely local. A one-off fix that drifts from the system creates a Consistency defect next round.
6. **No "while I'm here" edits.** Anything outside the change list goes onto the next round's list.
7. **Stop and ask** when a fix requires touching an approved element. Show the conflict (the defect, the approved element, two options) instead of deciding alone.

## Defects versus preferences

| Defect (fix) | Preference (offer, label, let the client decide) |
| --- | --- |
| Body text at 3.8:1 contrast | Warmer or cooler gray for body text, both above 7:1 |
| Headline ends on a single word at 390px | Two-line versus three-line headline at 1440px |
| Primary and secondary buttons look identical | Pill versus square buttons in a brand that allows both |
| Horizontal scroll at 390px | Tighter or looser section spacing within the scale |
| Claim not supplied by the client ("10x faster") | A punchier rewrite of approved, true copy |
| Two icon families mixed | Outline versus filled icons when either fits the brand |
| Brief asks for reassurance; design sells speed | Serif versus grotesk when both fit the brief |

A preference becomes a defect when it is the client's stated requirement or a locked brand rule.

## The round

1. **Baseline.** Render the current version before touching anything: `node ../scripts/render_review.mjs <target> --out review/round-0 --full-page`. Keep the screenshots and `report.json`; they are the "before".
2. **Score.** Fill the [rubric](rubric.md) score sheet from those screenshots. Note tells by ID from [ai-tells.md](ai-tells.md).
3. **List.** Write up to five changes, most impactful first, each tied to a criterion and a screenshot.
4. **Edit.** Make only those changes. Prefer token and component edits.
5. **Re-render.** Same target, same widths, same content, same flags: `--out review/round-1`. Different content or widths make the comparison meaningless.
6. **Compare.** Put before and after side by side at each width. For pixel-level checks, `compare -metric AE review/round-0/x-390.png review/round-1/x-390.png diff.png` (ImageMagick) highlights every changed pixel; the diff should be confined to the regions you meant to change.
7. **Verify invariants.** Approved copy, assets and locked regions unchanged (text diff for copy, the pixel diff for regions).
8. **Re-score.** Only the criteria the changes targeted should move, and no other criterion may drop. If one drops, revert that change or fix the regression before anything else.

## Before and after evidence

Record each round in the project's review record (or in the handoff when there is no project record):

| Change | Criterion | Before | After | Evidence | Invariants |
| --- | --- | --- | --- | --- | --- |
| H1 64px, subhead 18px regular | Hierarchy | 3 | 4 | review/round-0/home-1440.png, review/round-1/home-1440.png | Copy, logo, hero image unchanged (diff confined to #hero text) |
| Muted text #8A8A8A to #5E5A52 | Color and contrast | 2 | 4 | report.json: 0 contrast failures (was 14) | Palette roles unchanged except muted |

Keep the "before" files. Never overwrite a baseline with its revision; give every round its own folder.

## When to stop

- **Target met:** every applicable rubric criterion at 4 or higher for delivery (see the rubric for exploration targets).
- **Only preferences remain:** present them as options with their trade-off, then stop.
- **No movement:** two rounds without a score improvement means the direction, not the polish, is the problem. Go back to the brief or the direction choice rather than adding a third round of tweaks.
- **Three rounds by default** before showing a person, unless the user asked for autonomous iteration. Show the current best with its open defects rather than polishing in silence.

## Turning feedback into changes

| Feedback | Ask or translate | Testable change |
| --- | --- | --- |
| "Make it pop" | Which element should be noticed first? | Increase contrast and scale of that element; reduce competing ones |
| "It feels cold" | Is it the color, the type or the copy? | Warm the neutral ramp 10-20 degrees of hue, or swap the display face, or rewrite the headline; one at a time |
| "Too busy" | Which section? | Remove or merge elements until the squint test shows one entry point per view |
| "Looks like everyone else" | Which competitor? | Run the name-swap test against that competitor; introduce one ownable device |
| "Can the logo be bigger?" | Where is it read: nav, hero, social avatar? | Size the logo for its context; show both sizes at real scale |

Ask one focused question when feedback could mean two different changes; otherwise translate it, make the change, and show the before and after.

## Approval language

Never mark work "approved". Use "ready for review", "revised for the stated scope" or "accepted by <name> on <date> for <scope>" only when that person said so. A clean report, a high rubric score or a passing test is evidence for a reviewer, not an approval.
