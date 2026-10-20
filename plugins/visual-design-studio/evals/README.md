# Evals

Version-Timestamp: 2026-10-20 02:05:00 UTC

Behavioral evals for the Visual Design Studio plugin, in the `claude plugin eval` format: each case is a folder with `prompt.md` (the user request and run limits) and `graders/*.md` (LLM rubric, file checks and skill-firing indicators).

Run from the repository root (each run is a full Claude session on your own credential; set a cost ceiling):

```sh
claude plugin eval plugins/visual-design-studio --runs 3 --max-cost-usd 10 --no-publish --allow-tools Write
claude plugin eval plugins/visual-design-studio --case direction-genz-neobank-brazil --runs 1 --ablation none --no-publish
```

The default ablation runs each case with and without the plugin and reports the score delta, which is the real measure of whether the kit improves Claude's design output. `no-fire-git-undo` checks that design skills stay out of unrelated work. Results are written to `evals/results/` (ignored by the payload build).

Add a case whenever a real project exposes a failure: describe the request in `prompt.md`, write what a passing answer must contain in an `llm` grader, and keep at least one outcome grader per case.

## Running notes

- Cases use read-only tools (`Read`, `Glob`, `Grep`, `Skill`); `arabic-rtl-hero` also needs `Write`, which the operator grants with `--allow-tools Write`. Shell access is deliberately not requested: the harness refuses to run `Bash` without a sandbox backend (bubblewrap and socat on Linux), and every case can be answered by reading skill and atlas files.
- `--case` takes one name or glob per run.
- Results land in `evals/results/`, which git and the payload build ignore.

## First results (2026-10-20, Claude Code 2.1.304, one run per arm)

| Case | With plugin | Without | Finding |
| --- | --- | --- | --- |
| `no-fire-git-undo` | 1.00 | n/a | Design skills stayed out of a git question. |
| `typography-longform-defaults` | 1.00 | 1.00 | Claude already knows these defaults when asked directly; kept as a regression guard, not as evidence of lift. |
| `direction-genz-neobank-brazil` | 0.00, then 1.00 after a fix | 0.00 | The first run exposed two design-director defects: it answered an English brief in Portuguese and dropped typefaces, colors and scores when asked to be concise. Adding the skill's "Non-negotiables" fixed both. |

Total spend for these runs: about $0.30. One run per arm is a smoke test; use `--runs 3` or more before drawing conclusions.

