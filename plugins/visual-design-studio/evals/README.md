# Evals

Version-Timestamp: 2026-10-20 02:05:00 UTC

Behavioral evals for the Visual Design Studio plugin, in the `claude plugin eval` format: each case is a folder with `prompt.md` (the user request and run limits) and `graders/*.md` (LLM rubric, file checks and skill-firing indicators).

Run from the repository root (each run is a full Claude session on your own credential; set a cost ceiling):

```sh
claude plugin eval plugins/visual-design-studio --runs 3 --max-cost-usd 10 --no-publish
claude plugin eval plugins/visual-design-studio --case direction-genz-neobank-brazil --runs 1 --ablation none --no-publish
```

The default ablation runs each case with and without the plugin and reports the score delta, which is the real measure of whether the kit improves Claude's design output. `no-fire-git-undo` checks that design skills stay out of unrelated work. Results are written to `evals/results/` (ignored by the payload build).

Add a case whenever a real project exposes a failure: describe the request in `prompt.md`, write what a passing answer must contain in an `llm` grader, and keep at least one outcome grader per case.
