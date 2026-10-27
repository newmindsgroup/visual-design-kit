---
name: bama-improve-loop
description: Autonomous loop that works through docs/STORIES.md one story at a time for a macOS app, building, snapshotting, comparing against reference screenshots, fixing, and committing, until a milestone is done. Use when the user says "keep going", "work through the backlog", "make it match the reference", or wants an unattended improvement loop.
argument-hint: "[milestone, e.g. M1]"
---

<!-- Version-Timestamp: 2026-10-27 07:36:32 AST -->

## Adapted execution contract

This is the pinned, MIT-attributed BAMA capability adapted for the owned design kit. Read `ADAPTATION.md` at the BAMA package root before executing helpers. Project instructions, approved DESIGN.md and canonical tokens take precedence. Use supported Codex or Claude Code tools. Resolve this skill's sibling files relative to its installed SKILL.md; `skill_dir` is a task-local shell variable that you set to that resolved directory before running the examples in either host. Invoke a named `bama-*` skill through the host's supported skill mechanism.

Stage local builds by default. Installation, signing identity selection, launch, CLI linking, MCP registration, system setting changes and capture access are separate explicit operations. Existing task authorization applies; ask only for an action not already authorized. Stage or commit only when the current task or repository workflow authorizes it. Stage explicit paths and include required attribution. The helpers do not commit. Preserve the feature, story and testing workflow below using the hardened helpers. Legacy installed-app paths in examples must be replaced by the staged binary returned by `build.sh`.

Before a new scaffold exists, keep planning evidence under the selected `<AppName>-planning/docs/` sibling or an existing approved planning folder. Treat docs paths below as relative to that planning folder until the fresh app is scaffolded, then copy the planning docs explicitly without replacing existing files. For an existing app, keep its current project layout.

The upstream acceptance statements describe checks to perform, never completed results. Screenshots, runtime behavior, permissions and cross-host acceptance require actual evidence. Use synthetic data and owned temporary test roots. Do not run a hosted session over real app data without project authorization.



# Improve loop

One pass through the loop takes one story from `todo` to `done`:

```text
pick story -> plan -> code -> ./build.sh -> snapshot -> compare -> fix -> commit -> update STORIES.md
```

Stop after the milestone the user named, or after the current milestone if
they named none. Then report.

## 1. Pick

Open `docs/STORIES.md`. Take the first `todo` story in the current
milestone whose dependencies are `done`. Set it to `doing`.

## 2. Plan

If the story adds a screen, an action, or words and has no `UX:` block
yet, invoke the host-supported skill `bama-ux-design` first.

Write two to five lines in your head or in the commit body: which files
change, which model fields are new, which menu command and shortcut it adds,
which snapshot page shows it. If the story needs a new SwiftData field, give
it a default value so existing databases keep loading.

## 3. Code

Follow the `bama-swift-swiftui` and `bama-mac-design` skills, the story's `UX:`
block, and `design/DESIGN-SYSTEM.md` if the app has one. System hooks follow
`bama-os-integrations`. Keep each view file under about 300 lines.
Put new pages in the `SidebarItem` enum so snapshot mode visits them.

## 4. Build and snapshot

Follow the `bama-build-and-verify` skill. If the story has logic, add a test
or a self-test step (`bama-test-mac-app` skill). Use seed data (`APP_SEED=1`) so pages
show real content.

## 5. Compare

Open your snapshot and the story's reference screenshot side by side with
the Read tool. Write down the differences that matter, in this order:

1. Missing or wrong behavior from the acceptance criteria.
2. Words and flow: names, surface, and states that differ from the `UX:`
   block or `docs/GLOSSARY.md`.
3. Layout: wrong column, wrong order, missing element, and every FAIL from
   the grid checks.
4. Hierarchy: what is biggest, boldest, first.
5. Spacing and alignment.
6. Color and details.

Follow the selected reconstruction contract. For a faithful reconstruction, preserve observed structure, behavior and visual treatment, using semantic native controls styled to match where possible. Replacing the reference with platform defaults is a deliberate adaptation, not an automatic improvement. Record an unavoidable platform difference, its evidence and the accepted target decision. An explicitly adapted native version can use native conventions while retaining the observed task model.

No reference screenshot (no app was cloned)? Compare against the story's
acceptance lines and the `bama-mac-design` rules instead.

Snapshot only the pages a story touches (`APP_SNAPSHOT_PAGES`), and the
full set at the end of each milestone.

Fix, rebuild, and compare again. Three rounds per story at most. If it still
does not match, set the story to `todo` again with a note that says what is
blocking, and move on.

## 6. Commit and record

```bash
git diff --check  # review scoped changes; do not stage automatically
# Commit only under the project workflow with required attribution.
```

Set the story to `done` in `docs/STORIES.md` and commit that with the code.
One story per commit, so any story can be reverted on its own. M1 may
land as one commit when its stories share one skeleton (model, pages,
list, persistence); from M2 on, one story per reviewed change.

## 7. Report

At the end of the loop, report to the user:

- Stories done, with one line each and the snapshot paths that show them.
- Stories blocked, and why.
- Anything the user should try by hand (shortcuts, drag and drop).
- The next story in line.

Then `./build.sh --open` so the user can try the new build.

## Milestone check-in

When the last story of a milestone is `done`, invoke the host-supported skill
`bama-improve-architecture` before you start the next milestone. Unattended, do
its top recommendation only if it is `Strong`, and leave the rest in the
review file for the user.

When a story fixes a bug, add an entry to `docs/FIXLOG.md`: symptom,
cause, fix, and a last line `Rule: <what to always or never do>`. The fix
log outlives squashed history, and the check-in reads it.

## Running it unattended

The loop works with no one watching, because every step checks itself:
the build, the snapshots, the acceptance criteria. To let it run longer,
start it with a clear limit ("finish M2, then stop"), make sure the tree is
committed before you start, and never let it touch the user's real database.
Each story is a separate commit, so the user can review the history in the
morning and revert anything they do not like.

Done when every story in the milestone is `done` or named in the report as
blocked with a reason, each done story has its own commit, and the user
has the report.
