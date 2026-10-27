# Visual Design Kit: maintainer instructions

Version-Timestamp: 2026-10-27 07:51:01 AST

This repository is a public, MIT-licensed design plugin marketplace for **Claude** (`.claude-plugin/marketplace.json`) and **Codex** (`.agents/plugins/marketplace.json`). The main plugin is `plugins/visual-design-studio/`. These instructions are for working **on** the kit, in either tool. Projects that **use** the kit install the plugin; they never edit this repo.

This file is the single source of instructions. Codex reads it directly. Claude Code reads `CLAUDE.md`, whose first line imports this file. Edit only this file; never add rules to `CLAUDE.md`.

## Scope: any brand, any business

The kit is brand-agnostic and business-agnostic. It must work for any company, industry, market or vertical. Company-specific brand packs, client assets, briefs and deliverables live in each adopting project, never here.

## Layout

- `plugins/visual-design-studio/skills/`: registered skills (always-listed descriptions, bodies loaded on use). `design-director` is the front door; `design-project-start` owns client-project continuity.
- `plugins/visual-design-studio/library/atlas/`: Design Space Atlas (125 entries, `registry.json`, generated `index.json`).
- `plugins/visual-design-studio/library/tokens/`: DTCG token source (`src/`) and generated output (`dist/`).
- `plugins/visual-design-studio/library/draft-skills/`, `templates/`, `knowledge/`: deep process library (unregistered; linked from skills). New capabilities go in `library/capabilities.json`.
- `plugins/visual-design-studio/library/examples/`: calibration sets (stylescapes, ai-tells, quality-benchmark), reference code (astro-motion, react-system) and production templates (collateral, deck-pptx, motion-remotion). Remotion is source-available, not MIT: see `library/knowledge/ASSETS-LICENSES.md`.
- `plugins/visual-design-studio/agents/`: specialist subagents (direction-explorer and the review panel). Claude Code and Cowork load them; every skill keeps a single-context fallback, which is how Codex runs them.
- `plugins/visual-design-studio/evals/`: `claude plugin eval` cases. Improve skills with `.agents/skills/design-kit-eval-loop/`.
- `.agents/skills/`: maintainer skills (authoring rules, eval loop). Canonical copy; Codex discovers it here. `.claude/skills/` is a generated mirror for Claude Code.
- `tools/spec_radar.py` and `tools/spec_radar_scope.json`: list the volatile "verify" claims in our markets and platforms for the monthly review in `docs/SPEC-RADAR.md`.
- `tools/`: packaging build, validation and the skill mirror. `tests/`: repository tests. `docs/research/`: historical research records (not instructions).
- `project-starter/`: the entry block an adopting project copies into its own `AGENTS.md`, plus a `CLAUDE.md` that imports it.

## Working in this repo with Claude and Codex

Both tools work in the same local clone. Keep one source of truth and no drift:

1. **Start every session with `git pull`** on the branch you are on. GitHub `main` is the source of truth.
2. **Work on a branch, never directly on `main`.** Name it for the change (`feat/...`, `fix/...`). Merge through a pull request after CI passes.
3. **One writer per checkout.** If Claude and Codex need to work at the same time, give the second one its own `git worktree` on its own branch.
4. **End every session by committing and pushing**, even work in progress, so the other tool and other machines see it. Uncommitted work is invisible to everyone else.
5. **Never edit generated files by hand:** `PAYLOAD.sha256`, `library/CHECKSUMS.sha256`, `library/PACKAGE-MANIFEST.json`, `atlas/index.json`, `tokens/dist/`, `.claude/skills/`. Regenerate them with the tools below.
6. **Do not keep a second copy of this repo** (a research folder, a Drive folder, an exported package) as a working source. Packages and backups are derivatives.

## Before every commit

```sh
python3 tools/validate_plugin.py
python3 tools/build_toolkits.py --check                                  # optional BAMA and REA integrity/host parity
python3 plugins/visual-design-studio/library/scripts/atlas.py validate --complete
python3 plugins/visual-design-studio/library/scripts/atlas.py build      # if any atlas entry changed
(cd plugins/visual-design-studio/library && python3 scripts/tokens.py build && python3 scripts/tokens.py lint)
python3 tools/sync_agent_skills.py --apply                                # if .agents/skills changed
python3 tools/check_codex_parity.py                                       # Codex manifest, versions, skills, agent fallback, mirror
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
(cd plugins/visual-design-studio/library && PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests)
claude plugin validate . && claude plugin validate plugins/visual-design-studio   # needs the Claude Code CLI; CI also runs it
```

Any change inside `plugins/visual-design-studio/` changes the payload. Rebuild integrity metadata with `tools/build_plugin.py ... --apply` (see `.agents/skills/design-kit-authoring/SKILL.md`), then run it again with `--check`.

## Rules

- Content rules live in `.agents/skills/design-kit-authoring/` (writing rules, skill format, atlas schema, token contract). Follow them; the validators enforce most of them.
- Give concrete defaults with override conditions. Do not reintroduce "no universal numbers" language.
- Never commit client work, company-specific brand data, private references, credentials, local machine paths, or third-party artwork, logos, fonts or code without a compatible license. Bundle only OFL/MIT-compatible fonts with their license file.
- Python helpers are standard-library only and must support Python 3.9.
- Do not add a top-level `bin/` directory to a plugin; claude.ai and Cowork refuse those plugins.
- Keep versions identical in `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json` and the root marketplace.
- Versioned files carry a `Version-Timestamp` (skills in frontmatter `metadata`). Commits end with an `Agent-Attribution: computer=<host>; tool=<tool>; version=<version>; timestamp=<YYYY-MM-DD HH:mm:ss TZ>` footer using real values.
- Regulatory and platform statements must be verifiable; hedge and point to the source when unsure.
