---
name: bama-research
description: Online research for a macOS app before building it, run as parallel researcher subagents, saved to docs/research/. Use when the user asks what to build, which features matter, how the best apps in a category work, how a macOS API or integration works, or wants a feature comparison.
argument-hint: "<app category or question>"
---

<!-- Version-Timestamp: 2026-10-27 07:36:32 AST -->

## Adapted execution contract

This is the pinned, MIT-attributed BAMA capability adapted for the owned design kit. Read `ADAPTATION.md` at the BAMA package root before executing helpers. Project instructions, approved DESIGN.md and canonical tokens take precedence. Use supported Codex or Claude Code tools. Resolve this skill's sibling files relative to its installed SKILL.md; `skill_dir` is a task-local shell variable that you set to that resolved directory before running the examples in either host. Invoke a named `bama-*` skill through the host's supported skill mechanism.

Stage local builds by default. Installation, signing identity selection, launch, CLI linking, MCP registration, system setting changes and capture access are separate explicit operations. Existing task authorization applies; ask only for an action not already authorized. Stage or commit only when the current task or repository workflow authorizes it. Stage explicit paths and include required attribution. The helpers do not commit. Preserve the feature, story and testing workflow below using the hardened helpers. Legacy installed-app paths in examples must be replaced by the staged binary returned by `build.sh`.

Before a new scaffold exists, keep planning evidence under the selected `<AppName>-planning/docs/` sibling or an existing approved planning folder. Treat docs paths below as relative to that planning folder until the fresh app is scaffolded, then copy the planning docs explicitly without replacing existing files. For an existing app, keep its current project layout.

The upstream acceptance statements describe checks to perform, never completed results. Screenshots, runtime behavior, permissions and cross-host acceptance require actual evidence. Use synthetic data and owned temporary test roots. Do not run a hosted session over real app data without project authorization.



# Research

Research answers three questions before code exists: what the best apps in
the category do, what users love and hate about them, and how macOS lets
you build it. The output feeds `bama-app-brief` and `bama-user-stories`.

## Working folder

For a new app, record the chosen parent/name and work in its `<AppName>-planning` sibling or the existing approved planning folder. Save research under that folder's `docs/research/`. Leave the intended app destination absent for the scaffold. Existing apps keep their current repository paths.

## 1. Frame

Write the question in one line, and the decision it informs ("which
features go in version one", "Carbon hotkeys or an event tap"). If the user
gave only a category, the question is "what makes the best <category> app
on the Mac".

## 2. Fan out

Start one subagent per track, in parallel, with the brief below. Pick the
tracks that fit. Four is typical. Market and Reviews always run. Reviews
covers many apps: give each subagent 3 or 4 apps, or the 600 words run out.

| Track | Finds |
| --- | --- |
| Market | The 5 to 8 best apps in the category, their price, platform, and headline features |
| Reviews | Per app: what people like and what they dislike, from App Store and Mac App Store reviews, Reddit, Hacker News, forums, and "switched from X" posts |
| Features | The full feature list of the 2 or 3 leaders, from docs, changelogs, and help pages |
| Design | Screens, interaction details, and keyboard shortcuts of the leaders |
| Platform | The macOS APIs, permissions, and limits each feature needs, and what other apps on this Mac already use (global shortcuts, URL schemes, bundle ids) |

Subagent brief (fill in the brackets):

```text
Research [track] for a native macOS app that [one-line idea].
Question: [the question]. Decision it informs: [decision].
Search the web. Prefer primary sources: official docs, changelogs, Apple
developer docs, WWDC sessions, the app's own help pages. Use reviews and
forums for opinions only. If a source is blocked, say so and use another
(Hacker News, App Store reviews, Mac forums). Do not write any files.
Tag every claim: [V] verified in a source (give the URL), [K] from your
own knowledge, [U] unverified, must be tested.
Return at most 600 words: a findings list, a table where it helps, and
the 3 things that matter most for the decision. No intro, no summary.
```

## 3. Merge

Write one file per question: `docs/research/<topic>.md`.

```markdown
# <Topic>

Research for <AppName>. Done <YYYY-MM-DD>.
[V] verified in a source, [K] from knowledge, [U] unverified, test first.

## Findings
- ... [V](https://example.com)

## Likes and dislikes
| App | People like | People dislike | Sources |
| --- | --- | --- | --- |
| App A | <3 to 5 points, most mentioned first> | <3 to 5 points> | <urls> |

Patterns: <likes that repeat across apps (must have), dislikes that repeat
(our chance to do better)>

## Feature matrix
| Feature | App A | App B | App C | Version one? |

## Decisions
1. <decision>, because <finding>. Planned test: <test, for a [U] finding>.

## Open questions
- <[U] claim and how to test it>
```

Keep the feature matrix: `bama-user-stories` turns its "Version one?" column
into stories. Every "People like" point maps to a decision or to an
"accepted gap" line in the brief, so nothing loved is dropped by accident.
Check whether a system store (EventKit for reminders and calendars,
CloudKit) gives sync and phone capture for free. Turn each `[U]` that a decision depends on into a test before
you trust it (a probe script, a self-test step, or a preview field in the
reference app).

## 4. Hand off

Invoke the host-supported skill `bama-clone` if one app stands out as the reference
and you can open it. If it is not installed, or computer use and a browser
are not available, link its public help pages and screenshots in the
research file instead. Then invoke the host-supported skill `bama-app-brief`.

Done when every track returned, the file has a likes and dislikes table
for every app in the market list, a feature matrix, and a decision list,
and every decision cites a `[V]` or a planned test.
