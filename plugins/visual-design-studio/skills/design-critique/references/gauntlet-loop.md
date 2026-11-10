# Gauntlet loop

Version-Timestamp: 2026-11-10 03:20:00 UTC

Adapted from RoboNuggets' gauntlet-loop skill (Jay E, CC BY 4.0, https://github.com/robonuggets/gauntlet-loop, commit 9b1975a); technique by Matt Shumer (https://github.com/mshumer/Claude-of-Duty). See NOTICE.md. Sections marked *(adapted)* restate the upstream method in the kit's words; sections marked *(kit)* are additions. Changes: design-specific bars and capture, gates before comparison, copy guard, cost ceiling, agent mapping, single-context fallback and the hand-back to the rubric.

The rubric loop asks "is this good enough to ship?" The gauntlet asks "does this beat a named, real piece of work, judged blind?" Use the rubric as the floor and the gauntlet to push past it.

## When to use it *(kit)*

| Situation | Use | Why |
| --- | --- | --- |
| Client delivery, any artifact | Rubric loop (SKILL.md workflow) | 4+ on every criterion is the delivery floor; the gauntlet never replaces it |
| The user names a bar: "until it beats Linear's homepage", "as good as Stripe's pricing page" | Gauntlet, after the rubric target is met | The ask is relative to a real thing, not to a score |
| Cinematic page that has met the 8+ average, none below 7 stop rule | Optional gauntlet on the hero and signature | The stop rule ends polishing; the gauntlet is how to go further on purpose |
| The user asks for autonomous iteration past "good enough" with a time or spend budget | Gauntlet | A binary pick against a bar does not drift upward the way self-scores do |
| Exploration: directions still being chosen | Rubric and [scoring](../../design-director/references/scoring.md) only | One bar pulls every direction toward it and kills divergence |
| Quick fix, internal draft, no fetchable bar | Rubric loop | A gauntlet without a real bar invents its comparison |

Run the gauntlet only when all hard gates already pass and the rubric minimum is at or near target. Polishing toward a bar while an accessibility defect is open is wasted rounds.

## Choose the bar *(adapted, design specifics are kit)*

A bar passes three tests:

- **Named:** one specific thing. "Linear's homepage" works; "best SaaS sites" does not.
- **Fetchable:** you can capture it now. A live URL rendered with `render_review.mjs`, a deck you hold as PDF, a screen in the client's licensed reference library. If you cannot capture it, the critic will imagine it.
- **Comparable:** same format and job. A landing page against a landing page, a pricing table against a pricing table, a 12-slide pitch section against a 12-slide pitch section.

Prefer the hardest bar you can actually reach; an easy bar exits in round one. Add a measurable half when one exists (LCP, CLS, JS weight, axe violations, word count of the hero): taste plus a number beats taste alone.

| Deliverable | Bar that works | Capture |
| --- | --- | --- |
| Landing page, marketing site | A specific live page from a best-in-class product in the same or an adjacent category | `node ../scripts/render_review.mjs <bar-url> --full-page --widths 390,1440 --out review/gauntlet/bar` and the same command on ours into `review/gauntlet/ours-rN` |
| App screen or flow | The same task in a shipped product (from the [reference-first](../../design-director/references/reference-first.md) table) | Same widths or the device size; one screen per state |
| Deck | A real deck from a firm known for it, same section and slide count | PDF to PNG at 1920x1080: `pdftoppm -r 150 -png` |
| Social, OOH, print | A named campaign piece in the same format | Native size (1080x1350, 1080x1920, final trim at 150 dpi) |
| No external bar allowed (confidential client, offline host, rights unclear) | A kit calibration piece: a [stylescape](../../../library/examples/stylescapes/README.md) in a different direction from ours, or the [quality benchmark](../../../library/examples/quality-benchmark/README.md) correct variant | Render the local HTML at the same widths |

Rules for the capture:

1. **Same settings for both:** widths, viewport height, device pixel ratio, color scheme, `--reduced-motion` state and wait time. A 1440 bar against a 1280 ours is not a comparison.
2. **Capture the bar once per session** and reuse it, so the bar does not move between rounds. Re-capture only if the live page changed and say so in the log.
3. **Keep bar captures in the client project's working folder** for internal analysis only, as the [category scan](../../design-director/references/category-scan.md#ethics-and-limits) requires. Never commit them to a shared template, ship them or publish them.
4. **One bar per piece.** Two bars let the critic pick whichever ours beats.

## Split into judgeable pieces *(adapted)*

Compare small pieces, not whole pages. A whole-page pick hides which part lost.

| Artifact | Pieces (default) | Crop |
| --- | --- | --- |
| Landing page | Hero (first viewport), type system, color and contrast, imagery, motion (key frames at 0, 300 and 1200 ms, plus reduced motion), interaction (hover, focus, open states), mobile (390 first two screens) | Same region and height on both captures |
| Product screen | Primary task view, empty state, error state, dense data view, mobile | One state per pair |
| Deck | Title and opening, the argument section, the data slides, the close | Same slide count per pair |
| Brand asset set | Logo lockup at size, a social post, a sell sheet | Native size each |

Drop pieces the bar does not have (no motion on the bar means no motion piece). Run pieces independently; a piece that wins is frozen as an invariant under [revision discipline](revision-discipline.md) while the others continue.

## Builder and critic on the kit's agents *(kit)*

| Role | Who | Sees | Does not see |
| --- | --- | --- | --- |
| Lead | You (the session running `design-critique`) | Everything; owns the log, the A/B mapping and the ceiling | Nothing hidden; never acts as critic |
| Builder | You, or `direction-explorer` when the piece is a stylescape or direction asset (it has Write and Edit; the panel reviewers are read-only) | The brief, tokens, the piece, the critic's single gap | The critic's reasoning beyond the gap |
| Hard gates | `accessibility-auditor` (WCAG 2.2 AA), `brand-guardian` (tokens, locked assets, direction fidelity); `frontend-engineer` for buildability and budgets on web pieces; `copy-editor` when the piece carries copy claims | Our capture and the sources of truth they need | The bar |
| Blind critic | `art-director`, fresh dispatch every round | Two images labeled A and B, the piece's job in one line, no brand names | Which image is ours, the builder's notes, earlier rounds, the score history |

Dispatch the critic with a new subagent each round so it carries no memory of how hard the builder tried. The critic prompt is fixed:

```text
Two crops, A and B, of the same piece: <job in one line, for example "the first viewport of a B2B product landing page at 1440 and 390">.
Judge craft only: hierarchy, typography, color, layout, imagery, polish, specificity. Be harsh; praise is not useful.
Answer in this order: 1. Pick: A or B. 2. Single biggest gap in the image you did not pick, with location and evidence. 3. Single biggest gap in the image you picked.
No scores.
```

Ask for the gap in both images: the loser's gap is the builder's next change; the winner's gap tells the lead whether a win is narrow.

## Blind comparison mechanics *(adapted, mechanics are kit)*

1. **Strip identity.** Cover logos, wordmarks, product names and favicons on both crops with a flat neutral box (any image editor, or `magick in.png -fill "#808080" -draw "rectangle X0,Y0 X1,Y1" out.png`). Replace visible brand names in headlines with the same neutral word on both, or crop below them. A critic that recognizes the bar is not blind.
2. **Same crop.** Same region, width and height on both. Pad the shorter one with its own background color, never scale one to fit.
3. **Randomize order** every round: `python3 -c "import random; print(random.choice(['ours=A', 'ours=B']))"`. Write the result to the log before dispatching; never tell the critic.
4. **One pair per dispatch per width,** or one image per width side by side with the same layout for both.
5. **Record** the round in the log (below) the moment the pick returns, then unmask.

## Copy guard and rights *(kit)*

The goal is to beat the bar, not to resemble it.

- **The critic judges craft, never resemblance.** If ours wins because it now looks like the bar, it has not won.
- **Name-swap test on every win:** put the bar's name on ours. If it reads as theirs (their palette and accent, their type pairing, their signature layout or illustration), it is a copy: the win is void and the piece goes back with the gap "reads as <bar>".
- **Study, never copy.** Take structure and principles (hierarchy, density, rhythm, how the proof is staged). Never take the bar's assets, illustrations, copy, icons, distinctive layouts or code. The atlas [limits](../../../library/atlas/README.md#limits) and [reference-first rights](../../design-director/references/reference-first.md#rights-and-limits) apply in full.
- **Faithful reproduction is a different task.** If the client actually wants a supplied product rebuilt, use `reference-reconstruction`, which has its own rights checks.

## Hard gates before every comparison *(kit)*

Run the gates on our capture each round before blinding. A failed gate goes straight back to the builder; no comparison is run that round.

| Gate | Pass condition | Checked by |
| --- | --- | --- |
| Accessibility | WCAG 2.2 AA: text 4.5:1 (3:1 at 24px+ or 18.66px+ bold), non-text 3:1, targets 24x24 CSS px, visible focus, reduced-motion state, no serious or critical axe findings | `accessibility-auditor`, `render_review.mjs` report |
| Brand | Tokens used, locked assets intact (logo clear space and minimum size, palette, type), no drift from the chosen direction | `brand-guardian` |
| Licensing | Every font, image, icon, clip and component has a recorded license per [asset licenses](../../../library/knowledge/ASSETS-LICENSES.md); nothing taken from the bar | Lead, `brand-guardian` |
| Accuracy | No invented claims, stats, logos or testimonials; placeholder copy marked | `copy-editor`, lead |
| Budget (web) | The measurable half, when named, and the kit's [performance](../../web-design/references/performance.md) budgets | `frontend-engineer`, report |

A blind win never overrides a failed gate. The gates come first because a critic choosing on craft will happily pick the prettier, inaccessible version.

## Exit and cost ceiling *(adapted; ceiling default is kit)*

- **Exit on a blind win,** per piece, confirmed by the name-swap test. A narrow win (the critic's gap in ours is a defect, not a preference) gets one confirming round with a fresh order before freezing.
- **Or exit at the ceiling.** For client or paid work, ask once for a spend or time ceiling before round 1. If the user gives none, use 60 minutes of wall-clock time for the whole gauntlet, a common starting point, and say so. Personal or internal work may run without a ceiling if the user says so.
- **Never exit on a round count,** and never on "it feels done". Rounds are logged, not targeted.
- **At the ceiling, stop and report.** Do not loop silently, raise the ceiling yourself or lower the bar. Report each piece: won (round), losing (latest gap), not started.
- **Stalls:** the same gap three rounds running means the builder's approach is wrong, not the details. Change the approach (layout logic, image approach, type pairing) before the next round; tell the user if the fix needs something you cannot supply (real photography, licensed media, copy).

## The round log *(kit)*

Keep `review/gauntlet/log.md` in the project. It is the progress page; update it every round so the user can watch.

```text
Bar: <name, URL, captured YYYY-MM-DD HH:MM, widths 390/1440>   Ceiling: 60 min (default, user not asked twice)   Started: HH:MM
| Piece | Round | Gates | Order | Pick | Gap (loser) | Gap (winner) | Change made | Elapsed |
| Hero | 1 | pass | ours=B | A (bar) | ours: H1 and subhead compete, no single entry point at 390 | bar: CTA low on 390 | H1 to clamp(2.5rem, 1.5rem + 4vw, 4.5rem), subhead to 18px muted | 9 min |
| Hero | 2 | fail: a11y 1.4.3 subhead 3.9:1 | - | - | - | - | subhead to neutral-700 | 13 min |
| Hero | 3 | pass | ours=A | A (ours) | bar: ... | ours: proof row reads small | name-swap: ownable (signature diagram) -> confirm round | 21 min |
```

## Single-context fallback *(kit)*

Codex, claude.ai chat and hosts without plugin agents run the same steps in sequence:

1. Build the piece; write the builder notes under a heading "Builder, round N".
2. Run each gate lens using its agent file's checklist (`agents/<name>.md` in this plugin) and log pass or fail.
3. Blind the pair with a script that writes the order to the log, then start a heading "Critic, round N". In that section read only the two images and the job line; do not reread the builder notes; state the pick first, then the two gaps, in the critic prompt's order.
4. Log, unmask, return to step 1.

Say plainly in the report that a single-context critic is not truly blind: it may recognize its own work. Label those wins "single-context". For the final round, prefer a fresh session or a person as the critic.

## Hand back to the rubric *(kit)*

1. After every piece has won or the ceiling is reached, re-render every width with identical settings into `review/round-N` and run the full SKILL.md workflow: squint, name-swap, tells, accessibility, all twelve criteria.
2. The rubric minimum still governs delivery. A gauntlet win is evidence for Distinctiveness, Hierarchy and Craft; it does not raise a score that a measured defect or a cap holds down.
3. If a criterion dropped while chasing the bar (motion broke reduced motion, imagery outgrew the LCP budget, a token was hard-coded), fix it under revision discipline and re-confirm the piece's win once.
4. Report in the critique output: `Gauntlet: bar <name> captured <date>; hero won blind round 3; type won round 2; mobile losing at ceiling, gap "<gap>"; single-context: no`.

## Generating a paste-ready prompt

To hand the gauntlet to another agent or a fresh session, use the `prompt-engineering-expert` plugin's gauntlet-loop template (`skills/prompt-engineering-expert/references/templates/gauntlet-loop.md`, 1.4.0 and later). Fill it with the bar and capture command above, the gate list and the ceiling. Add multi-agent orchestration keywords only when the user has opted into that scale; it can spawn many agents and cost a lot.
