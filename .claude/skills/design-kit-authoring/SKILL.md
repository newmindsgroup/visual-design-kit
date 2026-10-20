---
name: design-kit-authoring
description: Maintainer workflow for adding or revising Visual Design Kit content - registered plugin skills, skill references, Design Space Atlas entries, design tokens, examples and eval cases. Use when editing anything under plugins/visual-design-studio, adding an atlas style, industry, market, audience, archetype, price tier or channel, changing tokens, or preparing a kit release.
metadata:
  version-timestamp: "2026-10-20 01:42:00 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 01:42:00 UTC"
---

# Design Kit authoring

This skill is for people (and agents) maintaining the kit. It is not loaded by projects that use the kit.

## What lives where

| Layer | Path (under `plugins/visual-design-studio/`) | Loaded by Claude |
| --- | --- | --- |
| Registered skills | `skills/<name>/SKILL.md` + `references/` + `scripts/` | Name and description always; body on use |
| Design Space Atlas | `library/atlas/<axis>/<slug>.md`, `registry.json`, `index.json` | Only the entries a brief selects |
| Tokens | `library/tokens/src/*.tokens.json` → `library/tokens/dist/` | On design-system and implementation work |
| Deep process library | `library/draft-skills/*`, templates, contracts | Linked from registered skills when needed |
| Examples | `library/examples/*` | Rendered and inspected, rarely read whole |
| Evals | `evals/<case>/prompt.md` + `graders/*.md` | `claude plugin eval` only |

## Rules

1. Follow [writing rules](references/writing-rules.md). The short version: concrete defaults with override conditions, no governance boilerplate, no invented facts.
2. Registered skills follow [skill format](references/skill-format.md). Keep the always-loaded description short; put depth in `references/`.
3. Atlas entries follow [atlas schema](references/atlas-schema.md). IDs come from `library/atlas/registry.json`; add a new ID there first.
4. Token names follow [token contract](references/token-contract.md). Never rename a published CSS variable without a deprecation alias.
5. Never put client assets, private references, credentials or copyrighted third-party artwork in this public repo. Link to public references; bundle only OFL or MIT-compatible fonts with their license file.

## Validate before committing

Run from the repository root:

```sh
python3 plugins/visual-design-studio/library/scripts/atlas.py validate --complete
python3 plugins/visual-design-studio/library/scripts/atlas.py build
python3 plugins/visual-design-studio/library/scripts/tokens.py build && python3 plugins/visual-design-studio/library/scripts/tokens.py lint
python3 tools/validate_plugin.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
(cd plugins/visual-design-studio/library && PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests)
claude plugin validate . && claude plugin validate plugins/visual-design-studio
```

## Release

1. Bump the version in both `plugins/visual-design-studio/.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`, and in `.claude-plugin/marketplace.json`.
2. Rebuild integrity metadata: `python3 tools/build_plugin.py --plugin-root plugins/visual-design-studio --source-root . --version X.Y.Z --timestamp "YYYY-MM-DD HH:MM:SS TZ" --apply`, then re-run with `--check`.
3. Record the new `PAYLOAD.sha256` digest in `docs/VERIFIED-PIN.md` as a candidate until a maintainer verifies it on a receiving machine.
4. Add release notes and the `Agent-Attribution` commit footer.
