# Evals

Version-Timestamp: 2026-10-20 10:31:13 UTC

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


`typography-longform-defaults` was removed on 2026-10-20 because it passed without the plugin; `typography-bilingual-annual-report` replaces it. Pilot format checks of the new suite (`--runs 1 --ablation none`): `no-fire-sql-query` 1.00 ($0.04), `japan-vertical-editorial` 1.00 ($0.18). The full ablation run is pending.
