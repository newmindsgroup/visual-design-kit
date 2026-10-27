---
name: bama-app-brief
description: One-page brief (docs/BRIEF.md) for a new macOS app, written before any code. Use when the user has an app idea, wants to replace an app they pay for, or the research and clone skills are done.
argument-hint: "[idea in a few words]"
---

<!-- Version-Timestamp: 2026-10-27 07:36:32 AST -->

## Adapted execution contract

This is the pinned, MIT-attributed BAMA capability adapted for the owned design kit. Read `ADAPTATION.md` at the BAMA package root before executing helpers. Project instructions, approved DESIGN.md and canonical tokens take precedence. Use supported Codex or Claude Code tools. Resolve this skill's sibling files relative to its installed SKILL.md; `skill_dir` is a task-local shell variable that you set to that resolved directory before running the examples in either host. Invoke a named `bama-*` skill through the host's supported skill mechanism.

Stage local builds by default. Installation, signing identity selection, launch, CLI linking, MCP registration, system setting changes and capture access are separate explicit operations. Existing task authorization applies; ask only for an action not already authorized. Stage or commit only when the current task or repository workflow authorizes it. Stage explicit paths and include required attribution. The helpers do not commit. Preserve the feature, story and testing workflow below using the hardened helpers. Legacy installed-app paths in examples must be replaced by the staged binary returned by `build.sh`.

Before a new scaffold exists, keep planning evidence under the selected `<AppName>-planning/docs/` sibling or an existing approved planning folder. Treat docs paths below as relative to that planning folder until the fresh app is scaffolded, then copy the planning docs explicitly without replacing existing files. For an existing app, keep its current project layout.

The upstream acceptance statements describe checks to perform, never completed results. Screenshots, runtime behavior, permissions and cross-host acceptance require actual evidence. Use synthetic data and owned temporary test roots. Do not run a hosted session over real app data without project authorization.



# App brief

Write `<parent>/<AppName>-planning/docs/BRIEF.md` in the selected planning folder while the app destination remains absent. Use an existing approved planning folder when one exists. Every later planning skill reads this work packet. After fresh scaffolding, copy these docs into `<parent>/<AppName>/docs/` without overwriting files. Keep the brief to one page.

## 1. Name and read what exists

Pick the name first: one UpperCamelCase word (`Tasks`, `DailyLog`), not the
name of an app already in `~/Applications`, and a bundle id
`com.<yourname>.<appname>` in lowercase. The folder, the research, and the
scaffold all use it.

If `docs/research/` or `docs/screens/INDEX.md` exist, read them first.
Skip every question they already answer.

If the user gives you a spec from BAMA's `specs/` folder (a file or a
link), it already holds the brief and the stories. Copy its **Brief** block
to `docs/BRIEF.md` and its **Stories** block to `docs/STORIES.md`. Keep the
rest of the spec as `docs/SPEC.md`, so later skills read its **How it
works** and **Gotchas**. Ask only what the user wants to change, then call
the host-supported skill mechanism for `bama-new-mac-app`.

## 2. Interview

Ask a few questions at a time. If the user asked you to decide everything,
answer each question yourself from the research, write the choice in the
brief, and note "decided by the agent" next to it.

1. What do you do today, and which app or habit does it replace?
2. What are the three things you do most often? These become the main pages.
3. What data does it hold? Name the nouns: tasks, notes, recipes, invoices.
4. Is there a reference app you like? Then the `bama-clone` skill comes next.
5. Where does it live: a window with a sidebar, a menu bar item, a
   quick-capture panel with a global shortcut, or a mix?
6. Does it need the internet? Default: no.
7. Which three things are out of scope for version one?
8. Should it look like a built-in Mac app, or have its own look? Note a
   brand or accent color, and any app they name ("like Things"): the
   `bama-design-from-app` skill rebuilds its look. No answer means native with
   the Mac's own accent color.

## 3. Cut scope

First record whether this is a personal utility, a business app, or a desktop companion to an existing platform. For a personal single-user utility, propose omitting accounts, sharing, teams, servers, billing and analytics when they serve no job. For a business app or companion, preserve existing identity, authorization, synchronization, billing and operational requirements. Choose local or synced storage from the approved brief. Never remove required services merely to fit this template.

Choose a bounded first milestone without promising a fixed build duration. A useful personal-utility starting scope is: one window, two to five main
pages, one data model with two to four types. Smart lists that filter one
model (Today, Upcoming, Someday) count as one page.

## 4. Write docs/BRIEF.md

```markdown
# <AppName>

One sentence: what it is and who it is for.

## Replaces
<app or habit>

## Main jobs
1. ...
2. ...
3. ...

## Data
- <Type>: <fields>

## Shape
<sidebar window / menu bar extra / quick panel>, macOS 26 or later.
<local or connected data, offline behavior, identity and sync requirements from the approved project brief>.

## System hooks
<global shortcut, menu bar, Share menu, Shortcuts, CLI, or "none">

## Reference
<app name, or "none">

## Look
<native with an accent color (name it, or "system"), own parts, or "like <app>", and why>

## Not in version one
- ...
```

## 5. Hand off

Invoke the host-supported skill `bama-user-stories`, or with `bama-new-mac-app` if the user
wants to see a window first.

Done when `docs/BRIEF.md` exists, fits on one page, and has every section.
