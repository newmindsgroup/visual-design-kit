---
name: bama-router
description: Build any Mac app. Start here to pick the next skill for a native macOS app.
disable-model-invocation: true
---

<!-- Version-Timestamp: 2026-10-27 07:36:32 AST -->

## Adapted execution contract

This is the pinned, MIT-attributed BAMA capability adapted for the owned design kit. Read `ADAPTATION.md` at the BAMA package root before executing helpers. Project instructions, approved DESIGN.md and canonical tokens take precedence. Use supported Codex or Claude Code tools. Resolve this skill's sibling files relative to its installed SKILL.md; `skill_dir` is a task-local shell variable that you set to that resolved directory before running the examples in either host. Invoke a named `bama-*` skill through the host's supported skill mechanism.

Stage local builds by default. Installation, signing identity selection, launch, CLI linking, MCP registration, system setting changes and capture access are separate explicit operations. Existing task authorization applies; ask only for an action not already authorized. Stage or commit only when the current task or repository workflow authorizes it. Stage explicit paths and include required attribution. The helpers do not commit. Preserve the feature, story and testing workflow below using the hardened helpers. Legacy installed-app paths in examples must be replaced by the staged binary returned by `build.sh`.

Before a new scaffold exists, keep planning evidence under the selected `<AppName>-planning/docs/` sibling or an existing approved planning folder. Treat docs paths below as relative to that planning folder until the fresh app is scaffolded, then copy the planning docs explicitly without replacing existing files. For an existing app, keep its current project layout.

The upstream acceptance statements describe checks to perform, never completed results. Screenshots, runtime behavior, permissions and cross-host acceptance require actual evidence. Use synthetic data and owned temporary test roots. Do not run a hosted session over real app data without project authorization.



# Build any Mac app

Find where the user is on the path below, then invoke the host-supported skill mechanism for that step. One skill per call.

```text
idea -> research -> clone (optional) -> app-brief -> user-stories -> new-mac-app
     -> mac-design + design-system + app-icon -> improve-loop (ux, code, design, verify, commit) -> repeat
```

Pick the name first (app-brief, step 1). Keep research, screenshots, brief and stories in `<parent>/<AppName>-planning/docs/`, or the approved existing planning folder. Leave `<parent>/<AppName>` absent until the scaffold helper creates it. Then copy the planning docs explicitly into the new app without overwriting an existing file, and switch the work packet to that app root. Existing apps keep their current repository layout. Design follows the scaffold, using project tokens from the first view. Icon design can proceed as source work; actual native icon rendering requires its toolchain.

## Plan

| The user has | Skill |
| --- | --- |
| A vague idea, or asks "what should I build" | `bama-research`, then `bama-app-brief` |
| An app they want to replace or rebuild | `bama-clone` |
| A brief or a screen index, no backlog | `bama-user-stories` |
| A spec from BAMA's `specs/` folder | `bama-app-brief` (it copies the spec) |

## Build

| The user wants to | Skill |
| --- | --- |
| Start a new project | `bama-new-mac-app` |
| Write or fix Swift and SwiftUI code | `bama-swift-swiftui` |
| Hook into macOS: hotkeys, menu bar, windows, screen capture, Shortcuts | `bama-os-integrations` |
| Make it fast: hangs, stutter, GPU, video, memory | `bama-performance` |
| Let Claude Code, Codex, or scripts drive the app: a CLI, an MCP server | `bama-agent-cli` |
| Refactor, clean up, or check the code as it grows | `bama-improve-architecture` |

## Design

| The user wants to | Skill |
| --- | --- |
| Decide how a feature works and what it says: names, flow, modals, accessibility | `bama-ux-design` |
| Make it look and feel like a Mac app | `bama-mac-design` |
| An accent or brand color, a color picker, tokens | `bama-design-system` |
| Their own parts and feel, not Apple's: buttons, rows, sidebar, icons | `bama-design-kit` |
| The look of an app they name, or screenshots of one | `bama-design-from-app` |
| One set of colors, radii, motion, and controls for the whole app | `bama-design-system` |
| Fix spacing and alignment, or check the layout on the grid | `bama-layout-grid` |
| An app icon | `bama-app-icon` |

## Ship

| The user wants to | Skill |
| --- | --- |
| Build it and look at every page | `bama-build-and-verify` |
| Tests, a self-test, or an agent that drives the running app | `bama-test-mac-app` |
| Work through the backlog on its own | `bama-improve-loop` |

## Done when

You named the step, called its skill, and told the user which skill comes
after it.
