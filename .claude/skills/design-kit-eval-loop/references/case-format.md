# Eval case format

Version-Timestamp: 2026-10-20 10:31:13 UTC

Format as read by `claude plugin eval` in Claude Code 2.1.304 (`claude plugin eval init --bare <name>` writes a blank case). Cases live in `plugins/visual-design-studio/evals/<case>/`.

## prompt.md

```markdown
---
max_turns: 20
timeout_seconds: 420
allowed_tools: [Read, Glob, Grep, Skill]
---

The user's request, written the way a client would say it.
```

- `allowed_tools`: `[Read, Glob, Grep, Skill]`. Add `Write` only when a grader checks a created file; the operator then passes `--allow-tools Write`. Never `Bash`: the harness refuses it without a sandbox backend.
- `timeout_seconds`: 420 for design cases that read skills and atlas entries; 180 for no-fire controls. Default is 300.
- `runs` defaults to 3; leave it unset.
- No absolute paths or `~/` in prompts or graders; cases run in a sandbox working directory.

## graders/<name>.md

| `type` | Frontmatter | Body |
| --- | --- | --- |
| `llm` | `weight`, optional `focus` (`last_message`, `trace`, `files`, or `{source: file, path}`) | Rubric of concrete checkable claims |
| `regex` | `flags` (JS flags, for example `"i"`), `match` (`contains`, `not_contains`, `count:N`), `weight`, optional `target` | The pattern |
| `tool_used` | `tool`, `input_match` (a regular expression over the tool input), `min`, `max`, `arm` (`with-only` or `both`) | Description |
| `file_exists` | `path` (glob), `exists` | Description |
| `tool_order` | `before`, `after` | Description |

- Skill indicator: `type: tool_used`, `tool: Skill`, `input_match: typography` (or `a|b` for alternatives), `arm: with-only`. Under ablation it shows whether the plugin fired but does not score.
- Should-not-fire: `tool: Skill`, `min: 0`, `max: 0`, `arm: both`. Omitting `min` leaves it at 1; omitting `arm` makes it display-only.
- `file_exists` sees only files created during the run.

## Rules for kit-specific graders

1. **Reward what only the kit knows.** Computed values (contrast ratios, barcode widths), named standards (Bill 96, 21 CFR 202.1, WCAG 2.2.2), atlas specifics (Pix copia e cola, tate-chu-yoko) and kit rules (3-of-6 distinctness, sensitivity check). A grader any competent answer passes measures nothing.
2. **Make the obvious answer wrong.** Put a constraint in the prompt that a generic answer misses: a request that breaks the law, a panel too small for the barcode, a palette that fails contrast, a brand that is locked.
3. **Every bullet is checkable.** "Gives a line-height of 1.6-1.9 for Arabic" is checkable; "good typography" is not. Name acceptable alternatives so the judge does not fail an equivalent answer.
4. **Pair an `llm` outcome grader with one or two `regex` checks** for strings that must appear. Keep patterns tolerant of spacing and case.
5. **State the fail condition** ("Fails if it delivers the layout with safety information only in the footer").
6. **Floors:** every case has an outcome grader; the suite keeps should-NOT-fire controls; default runs stay at 3.
7. Before adding a case, check what the kit says on the topic and cite the file in the [case map](case-map.md).
