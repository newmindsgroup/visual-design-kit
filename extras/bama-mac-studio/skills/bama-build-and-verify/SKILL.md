---
name: bama-build-and-verify
description: Build a SwiftUI macOS app from the command line, install it, and check light and dark window snapshots of every page before calling a change done. Use after any UI code change, when a build fails, or when the user asks to run, screenshot, or check the app.
---

<!-- Version-Timestamp: 2026-10-27 07:36:32 AST -->

## Adapted execution contract

This is the pinned, MIT-attributed BAMA capability adapted for the owned design kit. Read `ADAPTATION.md` at the BAMA package root before executing helpers. Project instructions, approved DESIGN.md and canonical tokens take precedence. Use supported Codex or Claude Code tools. Resolve this skill's sibling files relative to its installed SKILL.md; `skill_dir` is a task-local shell variable that you set to that resolved directory before running the examples in either host. Invoke a named `bama-*` skill through the host's supported skill mechanism.

Stage local builds by default. Installation, signing identity selection, launch, CLI linking, MCP registration, system setting changes and capture access are separate explicit operations. Existing task authorization applies; ask only for an action not already authorized. Stage or commit only when the current task or repository workflow authorizes it. Stage explicit paths and include required attribution. The helpers do not commit. Preserve the feature, story and testing workflow below using the hardened helpers. Legacy installed-app paths in examples must be replaced by the staged binary returned by `build.sh`.

Before a new scaffold exists, keep planning evidence under the selected `<AppName>-planning/docs/` sibling or an existing approved planning folder. Treat docs paths below as relative to that planning folder until the fresh app is scaffolded, then copy the planning docs explicitly without replacing existing files. For an existing app, keep its current project layout.

The upstream acceptance statements describe checks to perform, never completed results. Screenshots, runtime behavior, permissions and cross-host acceptance require actual evidence. Use synthetic data and owned temporary test roots. Do not run a hosted session over real app data without project authorization.



# Build and verify

A change is done when four things are true:

1. `./build.sh` finishes with no errors.
2. You looked at the light and dark snapshots of every page you touched.
3. The snapshots match what the user story or reference screenshot asks for.
4. The grid checks pass (`bama-layout-grid` skill).

App not made from the `bama-new-mac-app` template (Xcode, XcodeGen, a menu bar
utility, Swift 5)? Map the commands below with
[existing-app.md](existing-app.md) first.

Do not report a UI change as done from the code alone. SwiftUI code that
compiles can still render an empty sidebar, clipped text, or unreadable dark
mode.

## 1. Build

```bash
./build.sh              # stage release output with icon tooling
./build.sh --no-icon    # stage code-only output when icon tooling is unavailable
./build.sh --debug      # stage a debug build while iterating
# --sign-identity, --install and --open are separate explicitly authorized operations
```

Read the errors, fix them, and build again. Fix the first error first: later
errors often come from it. If a new file is "not in scope" right after you
created it, run `swift package clean --scratch-path ~/Library/Developer/<AppName>/build`.

## 2. Snapshot

Run the snapshot wrapper with the explicit staged binary. It creates a fresh marked private test root and database. The app opens, walks through every sidebar page and every Settings
tab in light and dark mode, saves one PNG per page and mode, and quits.

```bash
tools/snap.sh /explicit/staged/binary
# BAMA_TEST_ROOT=<new private temporary root>
# SNAPSHOT <root>/shots/all-light.png
```

`tools/snap.sh` creates a new isolated store and output directory each time, preserving any previous evidence. It never deletes real Saved Application State. Keep restoration problems isolated to the test process. The wrapper fails when no PNG output exists; inspect every image before treating the capture as accepted.

Use `APP_SNAPSHOT_PAGES=today,inbox` to limit the pages. Add `settings` to
include the Settings tabs.

In every image, look for three bugs agents often miss: a focus ring or
selected text that nobody asked for, a scroll bar with nothing to scroll,
and an empty band under short content. The fixes are in `bama-mac-design`,
"Windows open calm".

To see scroll bars as people with a mouse see them, add
`-AppleShowScrollBars Always` after the binary path. It changes only this
run.

Always use the wrapper's marked APP_TEST_ROOT and APP_STORE. An arbitrary /tmp path alone is insufficient. Never capture against the real database.

### Seed data

Empty pages only show empty states. The template's
`Sources/<AppName>/SeedData.swift` fills an empty test store when
`APP_SEED=1` is set. Grow it with the app: 10 to 20 items with long and
short titles, dates in the past and future, every priority and status, and
only what a person can create in the app.

### Screen Recording permission

Snapshots use `screencapture -l <window>`, which shows glass, sidebars, and
materials exactly as on screen. It needs Screen Recording permission for the
app that runs the command (Terminal, Ghostty, or Claude). If a snapshot line
ends with `(fallback: ...)`, the permission is missing and sidebars and glass
render blank. Ask the user to allow it in System Settings > Privacy &
Security > Screen & System Audio Recording, then restart the terminal.

### Missing snapshots

If every snapshot fails, or `screencapture` says "could not create image
from window", the display is probably asleep: an unattended Mac turns it
off. The template's snapshot mode wakes the display itself. For captures
from outside the app (like `window-shot.sh`), run `caffeinate -u -t 2` first.

If some states print "no window" while others work, another app hid yours
during the run. Computer use does this to apps it does not control, and so
does Hide Others. The template's snapshot mode un-hides the app and brings
the window forward before each capture. Run it again, and avoid using
computer use in another session at the same time.

## 3. Check the grid

```bash
tools/grid-lint.sh
swift tools/check-layout.swift /tmp/<AppName>-shots/*-layout.json
```

Both print PASS. On a FAIL, invoke the host-supported skill `bama-layout-grid`: it has
the rules, the overlay, and a table of fixes.

## 4. Look

Open every PNG with the Read tool and check, in this order:

- Nothing is blank, clipped, or overlapping. Text fits. Sidebars show their items.
- Dark mode is readable. No fixed white or black surfaces.
- The page matches the story or the reference screenshot (layout, labels, order).
- The `bama-mac-design` rules hold: glass only on controls, one accent,
  SF Symbols, system text styles, empty states that invite the first action.

Describe what you see in one or two sentences per page in your report, and
name the PNG paths so the user can open them.

## 5. Interaction checks

Snapshots show state, not behavior. Run `tools/selftest.sh` (exit 0 when
every check passes) and add a check for each new action. The
`bama-test-mac-app` skill covers unit tests, the self-test, key events, the
menu check from outside, and a debug bridge.

### Inactive windows

Gray traffic lights mean the window was not key when it was captured:
sidebar text, selection, and toggles look dimmer than in use. A snapshot of
an inactive window does not count as reviewed. Run the snapshots again
while nobody else uses the screen, and do not "fix" dim text you only see
there.

### Debug output and private screens

A GUI app started with its output going to a file buffers `print`, and the
lines are lost when the process is killed. Write debug lines to stderr
(`FileHandle.standardError.write`) behind an environment flag.

Do not take full-screen captures to check your app: they show the user's
other windows. Capture your own window, or add a mode to the app that
renders the state you want to see (prefilled text, an open sheet).

## 6. Commit

When the build is clean and the snapshots look right, commit with a message
that says what the user can now do: "Add tasks from the quick-add panel",
not "Update views".

Done when the four conditions at the top hold and the change is committed.
