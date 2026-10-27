---
name: bama-agent-cli
description: Optional command line and MCP server for a macOS app, so Claude Code, Codex, and scripts can drive it (list, add, change, search, act) through the running app. Use when the user wants agents to work with their app or its data, asks for a CLI, an MCP server, or automation for the app, or says "Claude should be able to use my app".
argument-hint: "<cli-name, like tasks or mail>"
---

<!-- Version-Timestamp: 2026-10-27 07:36:32 AST -->

## Adapted execution contract

This is the pinned, MIT-attributed BAMA capability adapted for the owned design kit. Read `ADAPTATION.md` at the BAMA package root before executing helpers. Project instructions, approved DESIGN.md and canonical tokens take precedence. Use supported Codex or Claude Code tools. Resolve this skill's sibling files relative to its installed SKILL.md; `skill_dir` is a task-local shell variable that you set to that resolved directory before running the examples in either host. Invoke a named `bama-*` skill through the host's supported skill mechanism.

Stage local builds by default. Installation, signing identity selection, launch, CLI linking, MCP registration, system setting changes and capture access are separate explicit operations. Existing task authorization applies; ask only for an action not already authorized. Stage or commit only when the current task or repository workflow authorizes it. Stage explicit paths and include required attribution. The helpers do not commit. Preserve the feature, story and testing workflow below using the hardened helpers. Legacy installed-app paths in examples must be replaced by the staged binary returned by `build.sh`.

Before a new scaffold exists, keep planning evidence under the selected `<AppName>-planning/docs/` sibling or an existing approved planning folder. Treat docs paths below as relative to that planning folder until the fresh app is scaffolded, then copy the planning docs explicitly without replacing existing files. For an existing app, keep its current project layout.

The upstream acceptance statements describe checks to perform, never completed results. Screenshots, runtime behavior, permissions and cross-host acceptance require actual evidence. Use synthetic data and owned temporary test roots. Do not run a hosted session over real app data without project authorization.



# Agent CLI

Give the app a command line, so an agent can do everything a person can
do in the window: `tasks items add --title "Call the dentist"`. The app
binary is the CLI. Each command goes to the running app over a private
socket, runs there like a button press, and the window updates live.

```text
Claude Code --bash--> tasks items add ...  --socket--> Tasks.app (runs the command, saves, redraws)
Claude Desktop --MCP--> tasks mcp           --socket--> same commands, same app
```

## CLI, MCP, or App Intents

| Way in | Who uses it | Ship it |
| --- | --- | --- |
| CLI | Claude Code, Codex, scripts, people in Terminal | Always. Agents learn it from `--help`, and it costs no context until used |
| MCP (`tasks mcp`) | Claude Desktop and other clients with no shell | Optional. The same commands, one tool each. One line to register |
| App Intents | Siri, Spotlight, Shortcuts | Separate work. Agents cannot call them |

The CLI talks to the running app, never to the database file. Then there is
one writer, the app's checks and side effects run, and the window shows the
change at once. If the app is closed, the CLI opens it in the background.
Rules and reasons: [rules.md](rules.md).

## 1. List the commands

Read the user stories (`docs/stories/`). Write each thing a person does as
a command, `<noun> <verb>`, and mark it:

- **read**: `items list`, `items show`, `status`. Read-only within the selected app; opening a closed app remains an explicit lifecycle effect.
- **write**: `items add`, `items update`, `open`. Changes data, can be undone.
- **destructive**: `items delete`, `mail send`. Only reports what it would
  do until `--yes` is given.

Add `status` (is it running, what is open, counts) and `open <page>` (show
a page in the window), so an agent can see and steer the app.

Check: every M1 story has its commands, and each command is marked.

## 2. Add the files

```bash
"${skill_dir}/scripts/add-agent-cli.sh" <app-folder> <cli-name>
```

It copies `Sources/<App>/Agent/` (core, socket, CLI, MCP, example
commands) and `Main.swift`, moves `@main` to `Main.swift`, starts the socket
in the main view's `.task` only for an opted-in app session. It does not change `build.sh`, link PATH or register MCP. Apps not made from the template need the same app-local integration by hand, following the script.

Check: the script printed "added the agent CLI", and `swift build` passes.

## 3. Write the commands

Replace the examples in `Agent/AgentCommands.swift`. Each command has a
name, a one-line summary, its params, a full example, its mark
(`readOnly` or `destructive`), and a `run` that uses the same model code
as the window's buttons. Never copy logic: call the function the button
calls.

- Every model an agent touches gets `var uuid: UUID = UUID()`. Commands
  show the first 8 characters as `id`, and accept any unique start of it.
- Results are small JSON objects: the fields an agent needs, not the
  whole model. Lists take `--limit` and `--offset`, and return `total`
  and `nextOffset`.
- Errors throw `AgentError` with a message that says how to fix it:
  "no item with id 3f2a. Run `tasks items list`".

All the rules: [rules.md](rules.md).

Check: `<cli-name> help` lists every command from step 1, and
`<cli-name> help <command>` shows its params and example.

## 4. Build and choose the local binary

Run `./build.sh` with icon tooling, or `./build.sh --no-icon` for code-only staging. Read STAGED_BINARY from its output and use that absolute path for help and every command. The build never adds a PATH symlink. A global CLI alias or symlink is a separate authorized setup choice. Use `--sign-identity`, `--install` and `--open` only when the current task authorizes each requested operation.

Check: the explicit staged binary's `help` and `--version` output match this app.

## 5. Test the isolated contract

Run this skill's `scripts/check-agent-cli.sh /explicit/staged/binary`. It creates a private marked test root, starts its own app process with APP_AGENT_ENABLED=1, checks help, JSON/errors, read commands, default write denial and MCP coverage, then stops only that process. It retains logs.

For an authorized synthetic write test, use the same marked test-root contract from the wrapper and explicitly start that app session with APP_AGENT_WRITES=1. The same app database and window reflect the change. Never substitute an arbitrary APP_STORE path or real database.

Check: isolated CLI/MCP checks pass, write denial is observed by default, and each newly implemented write has its own test and visible result.

## 6. Teach both hosts

Create the app-local command guide from [teach-agents.md](teach-agents.md). Use the owning project's shared skills/export layout for both Codex and Claude Code. Include the actual binary location or an explicitly configured CLI alias, the allowed commands and task/data boundaries. Register global skills or permissions only through the existing approved host workflow.

A fresh hosted-agent test uses synthetic data and separately approved provider/context. Do not run a new Claude session against real records merely to satisfy this checklist. Native host inspection of help plus the isolated CLI contract is the first verification step.

Check: both host guides describe the same command contract, their actual discovery is verified when available, and any untested host is recorded.

## 7. MCP, when the user wants it

For Claude Desktop, or to get one approval prompt per tool:

```bash
claude mcp add --scope user <cli-name> -- ~/Applications/<App>.app/Contents/MacOS/<App> mcp
codex mcp add <cli-name> -- ~/Applications/<App>.app/Contents/MacOS/<App> mcp
```

Claude Desktop: add it to `~/Library/Application Support/Claude/claude_desktop_config.json`
under `mcpServers`, with the full path and `"args": ["mcp"]`. More in
[teach-agents.md](teach-agents.md).

Check: the selected host lists the explicitly registered server and an isolated read tool succeeds. Registration output alone is not runtime acceptance.

Done when each command has passed its isolated behavior checks, default writes are denied, the app-local guides are in parity, and actual host/tool acceptance or its remaining prerequisite is recorded. A native app build failure holds runtime claims.
