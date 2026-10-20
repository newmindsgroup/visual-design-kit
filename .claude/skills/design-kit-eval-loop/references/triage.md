# Triage a failing eval case

Version-Timestamp: 2026-10-20 10:31:13 UTC

Start from `summarize_eval.py <result.json> --failures`, which lists each failing grader with the judge's explanation. The full answer is in the JSON under `cases[].arms.with[].graders[].evidence`; the session trace path is in `tracePath` while the harness temp directory still exists.

## Decision tree

1. **The run errored or timed out** (`error` set, score 0 with no evidence). Raise `timeout_seconds` or `max_turns` in `prompt.md`; an under-set timeout reads as a 0, not as a kit failure. Re-run before judging the kit.
2. **The skill indicator failed** (the plugin skill never loaded). Fix the owning skill's `description`: add the user's words from the prompt as trigger phrases, keep it under 600 characters. Then re-run the case and all `no-fire-*` controls; a wider description can start firing on SQL or git questions.
3. **The skill loaded but the answer lacks what the grader asks for.**
   - `grep -rn "<key term>" plugins/visual-design-studio/skills plugins/visual-design-studio/library/atlas` for the missing content.
   - Not in the kit: add it to the reference the [case map](case-map.md) names, with the source and a "verify" hedge for volatile facts. This is a content fix.
   - In a reference or atlas entry the run never read (check the trace for `Read` calls): move the rule into the skill's Defaults, Non-negotiables or Common failures, or add a Workflow step that reads that file for this kind of brief. This is a routing fix.
   - In the skill body but ignored: make it a non-negotiable, shorten the surrounding prose, or add the failure to Common failures with its fix.
4. **The answer has it but the grader failed it.** This is a grader fix, not a kit fix. Signs:
   - Judge votes are split (for example PASS FAIL PASS): the rubric is ambiguous. Rewrite the bullet as one checkable claim.
   - One long bullet joins three requirements with "and": split it, or accept "at least two of".
   - A regex rejects equivalent text (`2.54 : 1` against `2.5:1`, `11 X` against `11X`, typographic quotes): widen the pattern or move the check into the `llm` grader.
   - The rubric demands something the prompt never implied: remove it, or put the requirement in the prompt.
   - The default haiku judge missed nuance a human sees: re-judge with `--judge-model sonnet` before changing anything.
5. **Both arms pass.** The case measures general knowledge. Harden it: make the obvious answer wrong (a constraint that breaks the default, like a 25mm barcode panel or nine chart categories), and grade the kit-specific move (a computed value, a named standard, an atlas rule).
6. **With is lower than without.** The plugin hurts. Common causes: over-asking (qualifying questions on a complete brief), replying in the market's language, process prose crowding out specifics, or a skill pulling the answer to the wrong channel. Read both answers side by side and fix the instruction that caused the difference.

## Examples from this kit

| Symptom | Diagnosis | Fix type |
| --- | --- | --- |
| `direction-genz-neobank-brazil` answered an English brief in Portuguese and dropped typefaces and scores when asked to be concise (2026-10-20) | Skill instruction gap | Skill: design-director "Non-negotiables" (reply language; specifics survive concision) |
| `typography-longform-defaults` scored 1.00 with and without the plugin | Grader rewards general knowledge | Case replaced by `typography-bilingual-annual-report` |
| A regex for a contrast ratio fails on "2.54 to 1" | Regex too strict | Grader: accept the variant or fold it into the `llm` rubric |

## Rules

- One skill per iteration; re-run only the mapped cases.
- A grader change needs a written reason in `evals/README.md`. Never loosen a grader only because the plugin failed it.
- Keep failing evidence (the JSON) until the fix is confirmed, so the before/after comparison is possible.
