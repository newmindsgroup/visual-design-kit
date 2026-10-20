# Visual Design Kit: maintainer instructions

Version-Timestamp: 2026-10-20 11:00:00 UTC

This repository is a public, MIT-licensed Claude plugin marketplace (`.claude-plugin/marketplace.json`) that also ships a Codex plugin. The main plugin is `plugins/visual-design-studio/`. These instructions are for working **on** the kit. Projects that **use** the kit install the plugin; they never edit this repo.

## Layout

- `plugins/visual-design-studio/skills/`: registered skills (always-listed descriptions, bodies loaded on use). `design-director` is the front door; `design-project-start` owns client-project continuity.
- `plugins/visual-design-studio/library/atlas/`: Design Space Atlas (125 entries, `registry.json`, generated `index.json`).
- `plugins/visual-design-studio/library/tokens/`: DTCG token source (`src/`) and generated output (`dist/`).
- `plugins/visual-design-studio/library/draft-skills/`, `templates/`, `knowledge/`: deep process library (unregistered; linked from skills).
- `plugins/visual-design-studio/library/examples/`: calibration sets (stylescapes, ai-tells, quality-benchmark) and reference code (astro-motion, react-system).
- `plugins/visual-design-studio/agents/`: specialist subagents (direction-explorer and the review panel). Claude Code and Cowork load them; every skill keeps a single-context fallback.
- `plugins/visual-design-studio/evals/`: `claude plugin eval` cases. Improve skills with `.claude/skills/design-kit-eval-loop/`.
- `tools/spec_radar.py`: lists volatile "verify" claims for the monthly review in `docs/SPEC-RADAR.md`.
- `tools/`: packaging build and validation. `tests/`: repository tests.

## Before every commit

```sh
python3 tools/validate_plugin.py
python3 plugins/visual-design-studio/library/scripts/atlas.py validate --complete
python3 plugins/visual-design-studio/library/scripts/atlas.py build      # if any atlas entry changed
(cd plugins/visual-design-studio/library && python3 scripts/tokens.py build && python3 scripts/tokens.py lint)
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
(cd plugins/visual-design-studio/library && PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests)
claude plugin validate . && claude plugin validate plugins/visual-design-studio
```

Any change inside `plugins/visual-design-studio/` changes the payload. Rebuild integrity metadata with `tools/build_plugin.py ... --apply` (see `.claude/skills/design-kit-authoring/SKILL.md`), then run it again with `--check`.

## Rules

- Content rules live in `.claude/skills/design-kit-authoring/` (writing rules, skill format, atlas schema, token contract). Follow them; the validators enforce most of them.
- Give concrete defaults with override conditions. Do not reintroduce "no universal numbers" language.
- Never commit client work, private references, credentials, or third-party artwork, logos, fonts or code without a compatible license. Bundle only OFL/MIT-compatible fonts with their license file.
- Python helpers are standard-library only and must support Python 3.9.
- Do not add a top-level `bin/` directory to a plugin; claude.ai and Cowork refuse those plugins.
- Keep versions identical in `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json` and the root marketplace.
- Versioned files carry a `Version-Timestamp` (skills in frontmatter `metadata`). Commits end with an `Agent-Attribution: computer=<host>; tool=<tool>; version=<version>; timestamp=<YYYY-MM-DD HH:mm:ss TZ>` footer using real values.
- Regulatory and platform statements must be verifiable; hedge and point to the source when unsure.
