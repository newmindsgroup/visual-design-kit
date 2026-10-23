---
name: design-kit-eval-loop
description: >-
  Maintainer loop for measuring whether the Visual Design Studio plugin actually improves Claude's design output:
  run the claude plugin eval suite with and without the plugin, read the per-case deltas, triage each failure into a
  skill fix or a bad grader, change one skill at a time, re-run only the affected cases, control cost and record
  results. Use before a kit release, after editing any registered skill or its references, when adding or hardening
  eval cases, or when asked whether the kit helps.
license: MIT
metadata:
  version-timestamp: "2026-10-20 10:31:13 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 10:31:13 UTC"
---

# Design kit eval loop

The kit is worth shipping only where Claude with the plugin beats Claude without it. This loop measures that lift case by case, fixes the kit (or the grader) one skill at a time, and re-measures.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| When to run the full suite | Before every release, and after a wave of skill edits | Single-skill edit: run only its cases (table in [case map](references/case-map.md)) |
| Ablation | `--ablation with-without` (lift is the delta) | Format smoke test of a new case: `--ablation none --runs 1` |
| Runs per case | 3 | Smoke: 1. A decision that hinges on one case: 5 |
| Judge | Default (haiku) for iteration | Release numbers and disputed verdicts: `--judge-model sonnet` |
| Cost ceiling | Always pass `--max-cost-usd` | Never omit it |
| Changes per iteration | One skill (plus its references) | Never batch unrelated skill edits; the delta stops being attributable |
| Pass bar for "lift" | With-plugin score at least 0.67 and delta at least +0.33 | Regulated or high-stakes cases: require with = 1.00 in all runs |
| Regression | Any negative delta, or a no-fire control below 1.00 | Fix before anything else |

## Commands

Run from the repository root. Unset `CLAUDE_CONFIG_DIR` first so the eval harness uses its own isolated config. Each run is a full Claude session on your credential.

```sh
unset CLAUDE_CONFIG_DIR
OUT=/tmp/vdk-eval-$(date -u +%Y%m%dT%H%M%SZ).json

# Full suite (release measurement)
claude plugin eval plugins/visual-design-studio --runs 3 --ablation with-without \
  --max-cost-usd 15 --no-publish --allow-tools Write --trust-plugin --json "$OUT"

# One case (after a fix), or a glob of cases
claude plugin eval plugins/visual-design-studio --case brazil-pix-checkout --runs 3 \
  --ablation with-without --max-cost-usd 2 --no-publish --trust-plugin --json "$OUT"

# Format smoke test of a new case (cheap; checks that prompt and graders parse)
claude plugin eval plugins/visual-design-studio --case <new-case> --runs 1 --ablation none \
  --max-cost-usd 0.5 --no-publish --trust-plugin --json "$OUT"

# Read the result
python3 .agents/skills/design-kit-eval-loop/scripts/summarize_eval.py "$OUT" --failures
python3 .agents/skills/design-kit-eval-loop/scripts/summarize_eval.py BEFORE.json AFTER.json

# Clean up harness temp dirs (they are created read-only)
for d in /tmp/claude-eval-*; do [ -e "$d" ] && chmod -R u+rwX "$d" && rm -rf "$d"; done
```

Notes:
- `--case` takes one name or glob per invocation. To re-run several unrelated cases, loop over them and keep each JSON.
- `--allow-tools Write` is needed only for cases that list `Write` in `allowed_tools` (for example `arabic-rtl-hero`). Never grant `Bash`: the harness refuses it without a sandbox backend, and no case needs it.
- `--max-cost-usd` aborts with exit code 2 and partial results; the summary marks `partial True`. The ceiling is checked before each run, so overrun is bounded to the runs in flight.
- Results also land in `plugins/visual-design-studio/evals/results/<timestamp>/` (ignored by git and the payload build).

## Reading the deltas

The score per arm is the weighted share of scored graders that passed, averaged over runs. Graders marked `arm: with-only` (the `tool_used: Skill` indicators) do not count under ablation; they only tell you whether the plugin's skill fired.

| With | Without | Reading | Action |
| --- | --- | --- | --- |
| High | Low | Lift: the kit adds what the grader asks for | Keep; record it |
| High | High | No lift: Claude already knows this | Harden the case toward kit-specific content, or keep and label it a regression guard |
| Low | Low | The kit lacks the content, the skill did not fire, or the grader is wrong | Triage (below) |
| Lower than without | any | Regression: the plugin makes the answer worse (over-asking, wrong language, lost specifics) | Fix first |
| Split runs (1/3, 2/3) | any | Variance, not signal | Re-run with `--runs 5` before acting |

Treat a delta from one run per arm as a smoke signal only.

## Triage a failing case

Work through [triage](references/triage.md). In short:

1. **Did the skill fire?** Check the "Skill fired" column. If not, the fix is the skill's `description` (trigger phrases), and every no-fire control must be re-run afterwards.
2. **Is the missing content in the kit?** `grep -rn` the skill, its references and the atlas for what the grader wanted. Missing: add it to the right reference with a source. Present but not used: move it up into the skill's Defaults, Non-negotiables or Workflow, where it is always read.
3. **Is the grader wrong?** Read the judge evidence. If a careful human would pass the answer, the grader is at fault: split conjunctive bullets, loosen a regex that rejects equivalent formatting, remove a requirement the prompt never implied, or re-judge with `--judge-model sonnet`.
4. **Is the grader generic?** If both arms pass easily, rewrite it to reward what only the kit knows (computed values, named standards, atlas specifics) and harden the prompt so the obvious answer is wrong.

Never edit a grader to make a failing plugin answer pass unless step 3 shows the grader was wrong. Record every grader change with its reason in `evals/README.md`.

## One skill at a time

1. Pick the worst regression or the largest low/low case.
2. Change one registered skill (its `SKILL.md` and references only).
3. Re-run only the cases mapped to that skill in [case map](references/case-map.md), plus all `no-fire-*` controls if a `description` changed.
4. Compare with `summarize_eval.py BEFORE.json AFTER.json`. Keep the change only if the target case improved and no mapped case got worse.
5. Run the repository validators from `CLAUDE.md`. Evals and skills are payload, so the release integrity rebuild (`tools/build_plugin.py ... --apply`, then `--check`) is still required before release.

## Cost control

- Measured on Claude Code 2.1.304 (2026-10-20): a no-fire control costs about $0.05 per run; a design case about $0.08-0.20 per run per arm with the default judge. The full suite (32 cases, 3 runs, 2 arms, about 190 runs) is therefore roughly $20-35; a $15 ceiling covers about half of it.
- Budget path: run the full suite once with `--runs 1 --ablation with-without` (about $7-12), then `--runs 3` only on cases that are low, split or near the lift bar.
- Fix iterations use `--case` and `--max-cost-usd 2` per case.
- `-j 2` to `-j 4` shortens wall time but not cost; runs share one rate limit.
- Never publish reports from this repository's runs (`--no-publish`); they contain prompts and full answers.

## Recording results

- **`plugins/visual-design-studio/evals/README.md`**: add a dated results section (Claude Code version, runs, judge, ceiling, total cost) with one row per case: with, without, delta and a one-line finding. Paste the `summarize_eval.py` table and edit the Reading column into findings. Note every grader change and why.
- **`BACKLOG.md`**: tick the measurement item when a full `--runs 3` ablation completes; add one unchecked item per regression or low/low case ("Fix: <case> fails <criterion> because <cause>; owner skill <name>"), and close it with the before/after numbers.
- Release notes (`docs/RELEASE-<version>.md`): the headline lift (mean delta, cases with lift, regressions) and the cost.
- Keep the raw JSON outside the repository or in the ignored `evals/results/`.

## Writing or hardening a case

Follow [case format](references/case-format.md): one `prompt.md` (frontmatter `max_turns`, `timeout_seconds`, `allowed_tools`), one outcome `llm` grader of concrete checkable claims, optional `regex` graders for kit-specific strings, and a `tool_used: Skill` indicator with `arm: with-only`. Keep at least one should-NOT-fire control per kind of unrelated work, an outcome grader on every case, and default runs of 3.

## References

- [Triage](references/triage.md): decision tree with examples of skill fixes versus grader fixes.
- [Case map](references/case-map.md): which cases to re-run after editing each skill.
- [Case format](references/case-format.md): grader types, fields and rules for kit-specific graders.
- Authoring rules for skills and references: `../design-kit-authoring/SKILL.md`.
- Cases and results: `../../../plugins/visual-design-studio/evals/README.md`.
