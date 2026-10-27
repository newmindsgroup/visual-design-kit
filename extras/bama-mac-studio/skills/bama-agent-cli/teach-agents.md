# Teach agents to drive the app

Agents learn a CLI from three places: a short skill that says when and how
to use it, `<cli> help`, and the errors. Write the skill; the CLI does the
rest.

## Contents

- The app's agent skill
- Where to put it
- Permissions
- MCP registration

## The app's agent skill

Save as `.claude/skills/<cli>/SKILL.md` in the app's repo. Replace the
angle brackets. Keep it under 60 lines: list the five commands used most,
and point at `help` for the rest.

```markdown
---
name: <cli>
description: Drive the <App> app on this Mac from the shell with the `<cli>` command: <the main jobs, like "list, add, complete, and search tasks">. Use when the user asks about their <things> or wants to change them, or names <App>.
---

# <App>

`<cli>` runs commands in the <App> app. Changes show in its window at once.
If the app is closed, the command opens it in the background.

## Rules

- Always add `--json` and read the JSON. Exit 0 is ok; otherwise read
  `error.code` and `error.message`, and do what the message says.
- Find ids with `<cli> <noun> list` or `--search`. An id is 8 characters.
- Destructive commands (<delete, send>) only report what they would do.
  Show the user that report and ask before you run it again with `--yes`.
- To test without real data, use the marked private APP_TEST_ROOT created by the isolated helper. Enable APP_AGENT_ENABLED=1 for that app session. Writes additionally require APP_AGENT_WRITES=1 and task authorization. An arbitrary APP_STORE path alone is not test isolation.

## Main commands

| Command | Does |
| --- | --- |
| `<cli> status --json` | Is the app running, what is open, counts |
| `<cli> <noun> list [--search T] [--limit N] --json` | Find things |
| `<cli> <noun> add --title T --json` | Add one |
| `<cli> <noun> update <id> [--field value] --json` | Change one |
| `<cli> open <page>` | Show a page in the window |

Everything else: `<cli> help`, and `<cli> help <command>` for its options.
```

## Where to put it

| Place | Who sees it |
| --- | --- |
| `.claude/skills/<cli>/SKILL.md` in the app's repo | Agents working on the app's code |
| `~/.claude/skills/<cli>/SKILL.md` | Claude Code in any folder: "add milk to my tasks" works everywhere |
| `~/.codex/skills/<cli>/SKILL.md` (or `AGENTS.md`) | Codex |

Copy the same file to each place the user wants. Update all of them when a
command changes.

## Permissions

Host approval behavior depends on its actual policy. If the user explicitly requests a permission configuration, propose the narrow read-command allowlist in the host's supported format and apply it only through that authorized setup. This Claude Code example does not establish Codex syntax or permission:

```json
{ "permissions": { "allow": ["Bash(<cli> status:*)", "Bash(<cli> help:*)", "Bash(<cli> <noun> list:*)", "Bash(<cli> <noun> show:*)"] } }
```

Leave write and destructive commands out, so the user approves each one.
Ask the user before changing their settings.

## MCP registration

Only when the user wants MCP (Claude Desktop, or one prompt per tool).
Use the verified full path to the staged or explicitly installed binary. Do not infer that a host reads shell PATH or that registration grants app-side write authority. Enable the app-local listener explicitly for the authorized app session; it remains read-only unless writes were enabled separately.

```bash
claude mcp add --scope user <cli> -- ~/Applications/<App>.app/Contents/MacOS/<App> mcp
claude mcp list            # shows <cli> as connected
codex mcp add <cli> -- ~/Applications/<App>.app/Contents/MacOS/<App> mcp
```

Claude Desktop, in `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{ "mcpServers": { "<cli>": { "command": "/absolute/path/to/staged/<App>.app/Contents/MacOS/<App>", "args": ["mcp"] } } }
```

Restart Claude Desktop after editing. Its logs are in
`~/Library/Logs/Claude/mcp-server-<cli>.log`.

Tools are named like the commands with `_` for spaces (`items_add`), carry
`readOnlyHint` and `destructiveHint`, and take the same options as the CLI.
