# Evals

Version-Timestamp: 2026-10-23 11:31:41 UTC

Behavioral evals for the Visual Design Studio plugin, in the `claude plugin eval` format: each case is a folder with `prompt.md` (the user request and run limits) and `graders/*.md` (LLM rubric, file checks and skill-firing indicators).

Run from the repository root (each run is a full Claude session on your own credential; set a cost ceiling):

```sh
claude plugin eval plugins/visual-design-studio --runs 3 --ablation with-without --max-cost-usd 15 --no-publish --allow-tools Write --trust-plugin --json <out>
claude plugin eval plugins/visual-design-studio --case direction-genz-neobank-brazil --runs 1 --ablation none --no-publish
```

The default ablation runs each case with and without the plugin and reports the score delta, which is the real measure of whether the kit improves Claude's design output. Three `no-fire-*` controls check that design skills stay out of unrelated work. The maintainer loop for measuring, fixing and re-measuring is `.claude/skills/design-kit-eval-loop/` at the repository root. Results are written to `evals/results/` (ignored by the payload build).

Add a case whenever a real project exposes a failure: describe the request in `prompt.md`, write what a passing answer must contain in an `llm` grader, and keep at least one outcome grader per case.

## Cases (32)

| Case | What it tests |
| --- | --- |
| `android-m3-nav-six-sections` | Six sections vs the 3-5 destination M3 bar; window size classes, rail, `NavigationSuiteScaffold` |
| `arabic-rtl-hero` | Writes an RTL Arabic hero file (needs Write) |
| `brazil-pix-checkout` | Pix QR + copia e cola, installments, CPF mask, R$ format |
| `critique-ai-tells` | Names AI tells in a code snippet with concrete fixes |
| `critique-described-pricing` | Labels a prose-only critique conceptual, computes #9CA3AF failure, rubric gates |
| `dataviz-nine-categories` | Pushes back on nine hues; Okabe-Ito, grouping, small multiples, dark values |
| `direction-genz-neobank-brazil` | Distinct, specific, scored directions for a Brazilian market |
| `director-distinct-scored` | 3-of-6 distinctness table, weighted matrix, sensitivity check |
| `email-dark-mode` | Client dark-mode behaviors, `color-scheme`, `[data-ogsc]`, logo swap |
| `healthcare-portal-compliance` | HIPAA, accessibility and plain-language design implications |
| `ios-tab-bar-seven-sections` | Five-tab limit and 44pt targets |
| `japan-vertical-editorial` | Tategaki CSS: vertical-rl, tate-chu-yoko, kinsoku, Mincho, ruby |
| `kids-coppa-onboarding` | Rejects child PII; parental gate and consent, store kids programs |
| `locked-brand-careers-site` | Stays inside locked colors/type; orange-on-white 3.0:1 caveat |
| `low-literacy-benefits-form` | Grade 5-6 copy, one question per screen, plain-language standards |
| `motion-bottom-sheet` | Timing, easing and reduced motion for a sheet |
| `motion-reduced-motion-spec` | Per-effect reduced-motion replacements, WCAG 2.2.2 video pause |
| `neurodivergent-focus-app` | No pressure patterns, sensory control, predictability, COGA |
| `no-fire-git-undo` | Control: no skill loads |
| `no-fire-spreadsheet-formula` | Control: no skill loads for a Sheets formula |
| `no-fire-sql-query` | Control: no skill loads for SQL behind a dashboard |
| `older-adults-medication-app` | Large type, targets and contrast for 70+ |
| `packaging-barcode-quiet-zone` | EAN-13 at 80% (29.8mm) does not fit 25mm; GS1 quiet zones |
| `packaging-luxury-vs-value` | Atlas tier tokens: luxury vs value pack, concrete type/hex/materials |
| `pharma-promo-fair-balance` | Refuses footer-only ISI; fair balance, PI/Med Guide, MLR review |
| `print-business-card-us` | US card trim, bleed, safe area, PDF/X |
| `qualifying-questions-vague-logo` | 2-4 focused questions for a vague brief |
| `qualifying-restraint-full-brief` | Asks 0-1 questions when the brief is complete |
| `quebec-french-launch` | Bill 96, native fr-CA, French typography, Law 25, QST |
| `tokens-dark-mode-contrast` | Computes failing pairs; near-black canvas, elevation, lighter accent |
| `tokens-light-dark` | Primitive/semantic tokens for light and dark |
| `typography-bilingual-annual-report` | Arabic/English spec: per-script size and line-height, numerals, tabular figures (replaces typography-longform-defaults) |

## Running notes

- Cases use read-only tools (`Read`, `Glob`, `Grep`, `Skill`) and set `timeout_seconds`; `arabic-rtl-hero` also needs `Write`, which the operator grants with `--allow-tools Write`. Shell access is deliberately not requested: the harness refuses to run `Bash` without a sandbox backend (bubblewrap and socat on Linux), and every case can be answered by reading skill and atlas files.
- `--case` takes one name or glob per run.
- Results land in `evals/results/`, which git and the payload build ignore.

## First results (2026-10-20, Claude Code 2.1.304, one run per arm)

| Case | With plugin | Without | Finding |
| --- | --- | --- | --- |
| `no-fire-git-undo` | 1.00 | n/a | Design skills stayed out of a git question. |
| `typography-longform-defaults` | 1.00 | 1.00 | Claude already knows these defaults when asked directly; kept as a regression guard, not as evidence of lift. |
| `direction-genz-neobank-brazil` | 0.00, then 1.00 after a fix | 0.00 | The first run exposed two design-director defects: it answered an English brief in Portuguese and dropped typefaces, colors and scores when asked to be concise. Adding the skill's "Non-negotiables" fixed both. |

Total spend for these runs: about $0.30. One run per arm is a smoke test; use `--runs 3` or more before drawing conclusions.


`typography-longform-defaults` was removed on 2026-10-20 because it passed without the plugin; `typography-bilingual-annual-report` replaces it. Pilot format checks of the new suite (`--runs 1 --ablation none`): `no-fire-sql-query` 1.00 ($0.04), `japan-vertical-editorial` 1.00 ($0.18).

## 0.6.0 results (2026-10-20, Claude Code 2.1.304, judge haiku)

**Full suite, one run per arm, before fixes** ($4.24, 32 cases): overall 0.64 with the plugin. Clear lift on `japan-vertical-editorial` (+0.80), `arabic-rtl-hero` (+0.75), `brazil-pix-checkout` (+0.60) and `typography-bilingual-annual-report` (+0.25). The main defect: the expected skill loaded in only 8 of the 21 with-plugin runs that track skill firing, so many cases measured Claude without the kit. Two regressions traced to the kit: a thin logo brief drew 7 questions, and `director-distinct-scored` had no sensitivity check.

**Fixes:** eight skill descriptions now open with when to load them ("Load before answering any ... question, even a quick one"). `design-director` has non-negotiables for at most 4 questions, a pairwise distinctness line and a sensitivity line. `brand-identity` caps thin-brief questions at 4. The `grade` regex now accepts "5th-6th grade".

**Re-run of the 15 affected cases, with plugin only** ($1.34): the skill loaded in 14 of 15. Moved to 1.00: `critique-ai-tells`, `direction-genz-neobank-brazil`, `kids-coppa-onboarding`, `locked-brand-careers-site`, `neurodivergent-focus-app` and `qualifying-questions-vague-logo` (the regression is fixed). Still below the bar: `critique-described-pricing`, `dataviz-nine-categories`, `director-distinct-scored`, `email-dark-mode`, `low-literacy-benefits-form`, `packaging-luxury-vs-value`, `quebec-french-launch` and `tokens-dark-mode-contrast`. A read of these responses shows mostly strong answers failing one clause of an all-of rubric, so the next loop is grader hardening (split rubrics into weighted graders) plus `--runs 3`, then skill fixes where a clause is a real gap. `pharma-promo-fair-balance` passes its graders but did not load a skill.

Total eval spend for 0.6.0: about $5.70, under the $15 cap.


## 0.7.1 hardening (2026-10-23, Claude Code 2.1.309, judge haiku)

**Grader changes.** The single all-of `llm` rubric in eight cases is now 3-4 weighted `llm` graders, one clause or a closely related pair each, so partial credit is visible. The clauses still require kit-specific content (computed ratios, named standards, atlas typefaces and hex values); regex and `tool_used` graders are unchanged. Wording changes beyond the split, with reasons:

- `critique-described-pricing/pricing-fixes`: "at least two of" the three pricing fixes. The old bullet listed them with commas, and the judge read it as all-of; the clause is generic, so it carries weight 1 of 4.
- `dataviz-nine-categories/palette-dark` (changed after the first measurement): also accepts "the light values already clear 3:1 on the named dark canvas, with black swapped for a light value". That is what the kit's `data-palettes.md` prescribes, so the old wording failed kit-correct answers (judge evidence, all three with-plugin runs).
- `tokens-dark-mode-contrast/diagnosis`: the blue's ratio is required on at least one of the two dark surfaces (both were required before); the muted-gray ratio is still required.
- `tokens-dark-mode-contrast/tokens`: light values may be given or referenced through the same semantic names. The prompt asks only for a dark-theme fix.
- `email-dark-mode/palette-cta`: "avoid pure black and white" now applies to background and body text, not to an inverted white button fill.

**Measurement** (`--runs 3 --ablation with-without`, scores are the weighted share of scored graders; the skill indicator does not count):

| Case | With | Without | Delta | Skill fired | Cost USD | Finding |
| --- | --- | --- | --- | --- | --- | --- |
| `pharma-promo-fair-balance` | 1.00 | 1.00 | 0.00 | 3/3 | 0.40 | Skill now loads (0/1 in 0.6.0) after the web-design description change; no lift, so Claude already knows fair balance. Keep as a regulated-content guard. |
| `critique-described-pricing` | 0.80 | 0.73 | +0.07 | 3/3 | 0.41 | Every with-plugin run failed `scoring-gates`: a conceptual critique dropped the rubric scores and caps. Skill fix below. |
| `dataviz-nine-categories` | 0.50 | 0.17 | +0.33 | 3/3 | 0.58 | `palette-dark` failed kit-correct answers (grader fix above); one run gave only one alternative. |
| `director-distinct-scored` | 0.80 | 0.07 | +0.73 | 3/3 | 0.43 | Clear lift. Every with-plugin run failed `matrix`: there was no accessibility criterion and no reason per score. Skill fix below. |
| `email-dark-mode` | 1.00 | 0.83 | +0.17 | 3/3 | 0.51 | Passes; without the plugin, the per-client behaviors and the images-off check go missing. |
| `low-literacy-benefits-form` | 0.33 | 0.27 | +0.07 | 3/3 | 0.39 | The skill fired, but the answers never set a numeric reading level, step count, standard, icon rule or 16px floor. The atlas audience entry was reachable only through `atlas.py`, which needs a shell. Skill fix below. |
| `packaging-luxury-vs-value` | 0.00 | 0.00 | 0.00 | 3/3 | 0.39 | No answer named typefaces or hex values. The tier token recipes were reachable only through `atlas.py`. Skill fix below. |
| `quebec-french-launch` | 0.73 | 0.67 | +0.07 | 3/3 | 0.48 | `typography` (expansion, no-break spaces, accents on capitals) and `fr-ca` (a vocabulary example) fail in most runs of both arms. Open: route web-design to `atlas/markets/canada.md` in a later iteration. |
| `tokens-dark-mode-contrast` | 0.83 | 0.75 | +0.08 | 3/3 | 0.47 | Only `tokens` fails, because the answers give no light values. Not a plain kit gap: the dark-mode reference tabulates dark values only. |

Mean with 0.67, without 0.50, mean delta +0.17 over nine cases. The skill fired in 27 of 27 with-plugin runs.

**Skill fixes (one per gap)** and their single re-run (`--runs 1 --ablation none`; the score here includes the skill indicator):

| Skill | Change | Case | Before (with, 3 runs) | After (1 run) |
| --- | --- | --- | --- | --- |
| `web-design` | Description names above-the-fold layouts and regulated industries (prescription drug, health, finance); the industry decision links the pharma-biotech atlas entry | `pharma-promo-fair-balance` | skill fired 0/1 (0.6.0) | fired 3/3, 1.00 |
| `print-packaging-social` | The tier decision links the five tier token recipes directly (named faces, hex, checked pairs) | `packaging-luxury-vs-value` | 0.00 | 1.00 |
| `design-director` | Non-negotiable: criteria come from `scoring.md`, always including accessibility, with one reason per criterion | `director-distinct-scored` | 0.80 | 1.00 |
| `design-critique` | Conceptual critiques still give provisional rubric scores with the caps that apply | `critique-described-pricing` | 0.80 | 0.83 (`scoring-gates` passes; `tells` failed this run) |
| `ux-design` | The audience decision links the low-literacy, older-adults, neurodivergent and children entries directly | `low-literacy-benefits-form` | 0.33 | 0.50 (`first-screen` passes; level, structure and help still fail) |
| (grader) | `palette-dark` rewording | `dataviz-nine-categories` | 0.50 | 0.80 (`palette-dark` vote split PASS FAIL FAIL) |

The `web-design` description changed, so the controls were re-run once: `no-fire-git-undo`, `no-fire-spreadsheet-formula` and `no-fire-sql-query` all scored 1.00 with no skill loaded.

**Still failing.** `low-literacy-benefits-form`: the answer cites the guidance but drops its numbers. Next step: make the grade 5-6 target and the step-count rule a ux-design non-negotiable. `quebec-french-launch`: French typography and fr-CA vocabulary are missing. `tokens-dark-mode-contrast`: decide whether light values belong in the prompt or in the color skill. The fix re-runs are one run each; confirm them with `--runs 3 --ablation with-without` before the next release.

Spend: $4.05 for the measurement and $0.67 for the re-runs and controls, $4.72 in total (agent plus judge cost) against an $8.00 cap.
