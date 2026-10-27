# Visual Design Studio in Codex

Version-Timestamp: 2026-10-23 18:00:00 UTC

Agent-Attribution: computer=vm; tool=Claude Code; version=2.1.309; timestamp=2026-10-23 18:00:00 UTC

This page says what works in Codex today, what does not, and how to check it on a real install. The sources are the 0.8.0 production-layer research (Codex section, 2026-10-23). Most Codex documentation hosts were not reachable from the research sandbox, so claims marked **[search summary]** come from a search-engine summary of the official page and claims marked **verify** are not confirmed. Re-check them on a real Codex install before you rely on them.

## What Codex loads

| Surface | In Claude Code and Cowork | In Codex today | Source |
| --- | --- | --- | --- |
| Plugin skills | `skills/` through `.claude-plugin/plugin.json` | `skills/` through `"skills": "./skills/"` in `plugins/visual-design-studio/.codex-plugin/plugin.json`; each skill folder has a `SKILL.md` | [search summary] https://developers.openai.com/plugins/quickstart; OpenAI's own Remotion plugin uses the same key: https://raw.githubusercontent.com/openai/plugins/main/plugins/remotion/.codex-plugin/plugin.json |
| Maintainer skills | `.claude/skills/` (generated mirror) | `.agents/skills/` (canonical), discovered from the working directory up to the repo root, plus `$HOME/.agents/skills` and `/etc/codex/skills` | [search summary] https://developers.openai.com/codex/skills; repo stub https://raw.githubusercontent.com/openai/codex/main/docs/skills.md |
| Plugin agents (`agents/*.md`: direction-explorer and the review panel) | Loaded as subagents | **Not loaded.** Claude-format agent files are not Codex agents. Skills run their single-context fallback instead | Research section 7 |
| Codex custom agents | n/a | Standalone TOML files in `~/.codex/agents/` or `.codex/agents/`, each with `name`, `description` and `developer_instructions`. Built-in agents: `default`, `worker`, `explorer`. Codex spawns subagents only when asked | [search summary] https://developers.openai.com/codex/subagents |
| Plugin-bundled agents in Codex | n/a | The openai/plugins README lists plugin-level `agents/` and `commands/` as optional surfaces; whether Codex loads them is **verify** | https://github.com/openai/plugins |
| Custom prompts and slash commands | n/a | Custom prompts are **deprecated** in favor of skills. They were local Markdown files under `~/.codex`, not shared through a repo. The kit ships none | [search summary] https://developers.openai.com/codex/custom-prompts; built-in commands: https://developers.openai.com/codex/cli/slash-commands |
| Manifest layout | `.claude-plugin/plugin.json` | `.codex-plugin/plugin.json` is supported. A newer portable root `plugin.json` with `extensions.com.openai` also exists; the two files are **not merged** | [search summary] https://developers.openai.com/codex/plugins/build |

The kit keeps `.codex-plugin/plugin.json` and does not add a root `plugin.json`. `tools/check_codex_parity.py` warns if one appears, because Codex would read one file and ignore the other.

## Single-context fallback

Codex does not see the Claude agents, so every skill that dispatches one also says how to do the same work in one context:

- `design-director` dispatches one `direction-explorer` per direction. Its fallback is in `skills/design-director/references/parallel-exploration.md` ("Single-context fallback").
- `design-critique` convenes the review panel. Its fallback is in `skills/design-critique/references/review-panel.md` ("Single-context fallback").

Expect the fallback to be weaker on distinctness: one context writing several directions drifts toward its first idea. Run the distinctness check in the director skill on every set of directions. Generating `.codex/agents/*.toml` equivalents is deferred until plugin-bundled agents are confirmed (research section 7).

## Install

From a clone of the repository root (commands from [INSTALLATION.md](../INSTALLATION.md#codex), available in Codex CLI 0.154.0):

```sh
codex plugin marketplace add .
codex plugin add visual-design-studio@visual-design-team --json
codex plugin list --marketplace visual-design-team --json
```

The Codex marketplace is `.agents/plugins/marketplace.json`; it points to `./plugins/visual-design-studio`. Open a fresh task after installing: the task that installed a plugin may not have reloaded its skills, and an earlier authoring session saw automatic discovery drop the entry because of the host's skills context budget. For pinned client projects use the project entry in `project-starter/` (see [INSTALLATION.md](../INSTALLATION.md)).

## Parity check (run before every commit)

```sh
python3 tools/check_codex_parity.py          # human-readable
python3 tools/check_codex_parity.py --json   # machine-readable
```

Exit codes: 0 all checks pass, 1 a check failed, 2 the layout cannot be checked. It checks:

1. **manifest**: `.codex-plugin/plugin.json` exists, has the same `name` as `.claude-plugin/plugin.json`, and `"skills"` resolves to a folder inside the plugin.
2. **versions**: `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, the root `.claude-plugin/marketplace.json` (`metadata.version` and the plugin entry) agree; `.agents/plugins/marketplace.json` lists the plugin with a source path that exists.
3. **skills**: every registered skill folder has a `SKILL.md` with `name` equal to the folder and a `description`.
4. **fallback**: every Markdown file in a skill that names a plugin agent (the file names in `agents/*.md`, matched as whole hyphenated words) either has a fallback marker or links to a Markdown file that has one. A marker is a heading containing "fallback" (the kit uses `## Single-context fallback (claude.ai chat and hosts without plugin agents)`), or a line that starts with "Without subagents" or "Single-context fallback" (list markers and bold allowed).
5. **mirror**: `.claude/skills/` is an exact copy of `.agents/skills/` (same comparison as `tools/sync_agent_skills.py`).

When you add a skill that names an agent, add a `## Single-context fallback` section to it or link the name to a file that has one.

## Verification checklist on a real Codex install

Record the Codex CLI version, the date and the result of each line in the release notes. Do not mark a line verified from documentation alone.

- [ ] `codex plugin marketplace add .` succeeds from the repo root and `codex plugin list --marketplace visual-design-team --json` shows `visual-design-studio` at the version in `.codex-plugin/plugin.json`.
- [ ] In a fresh task, the plugin's skills are listed (count matches `python3 tools/check_codex_parity.py --json`, field `skills`). Note any skill dropped by the skills context budget.
- [ ] Ask for a brand direction: `design-director` loads and runs the single-context fallback (no attempt to dispatch `direction-explorer`), and the answer still has named typefaces, hex values and scores.
- [ ] Ask for a design critique: `design-critique` loads and uses the single-context review, labeling a prose-only critique "conceptual".
- [ ] Skill links resolve: the skill reads a reference file and an atlas entry through relative paths from the installed plugin cache.
- [ ] In this repo, `.agents/skills/design-kit-authoring` and `design-kit-eval-loop` are discovered as repository skills.
- [ ] Check whether a plugin-level `agents/` folder is loaded by Codex (it should not be for Claude-format `.md` files). Record the result here and in research before writing `.codex/agents/*.toml` equivalents.
- [ ] Confirm whether Codex prefers a root `plugin.json` over `.codex-plugin/plugin.json` on this version, and that the kit has only the latter.
- [ ] Bundled helpers run under the Codex sandbox with Python 3.9 or later (for example `python3 library/scripts/atlas.py list` from the plugin folder); note any that need network or write approval.
- [ ] Upgrade test: install the previous edition, then this one; confirm the cache holds the new version and the project pin still points at its preserved checkout.
