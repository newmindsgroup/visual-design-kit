# Review panel

Version-Timestamp: 2026-10-20 10:28:22 UTC

One reviewer reading for everything misses things: the eye that judges hierarchy skims the error messages, the eye that checks contrast ignores the logo's clear space. In Claude Code and Cowork, convene a panel of read-only specialist subagents, each with one mandate and its own checklist, then merge their scores into the [rubric](rubric.md) yourself. In claude.ai chat, and in any host that does not load plugin agents, run the same five lenses in sequence with the fallback below. You still own the critique: the panel supplies evidence, you look at the screenshots and decide.

## The panel

| Agent | Mandate | Feeds rubric criteria |
| --- | --- | --- |
| `art-director` | Distinctiveness, hierarchy, typography, layout, imagery, craft, AI tells | 2, 3, 4, 6, 7, 12 |
| `accessibility-auditor` | WCAG 2.2 AA via the [15-minute audit](accessibility-audit.md) and axe | 10 (owner), 5, 9 |
| `copy-editor` | Voice, plain language, microcopy, claims, filler and copy tells, locale mechanics, localization | 1, 12 |
| `brand-guardian` | Fidelity to the chosen direction, tokens and locked assets | 1, 5, 8 (owner) |
| `frontend-engineer` | Buildability, token use, responsiveness, states, component API, performance budgets | 9 (owner), 11 (owner), 8 |

Subagent types carry the plugin prefix, for example `visual-design-studio:art-director` (some hosts list them without it). Agent definitions live in this plugin's `agents/` folder.

## When to convene

| Situation | Panel | Change when |
| --- | --- | --- |
| Client delivery of a page, screen flow or app build | All five | Static print or social: drop `frontend-engineer` |
| Directions shown for selection (stylescapes) | `art-director`, `copy-editor`; `accessibility-auditor` for contrast only | Regulated or older-adult audience: full accessibility audit |
| Brand asset, deck, social set, packaging, print | `art-director`, `copy-editor`, `brand-guardian` | Interactive PDF or email: add `accessibility-auditor` |
| Component library or design-system release | `frontend-engineer`, `accessibility-auditor`, `brand-guardian` | Marketing docs site included: add `art-director` |
| Two rounds without score movement | Full panel once, to find what a single reviewer keeps missing | Scores move: return to single-reviewer rounds |
| Quick internal check, work in progress | No panel; run the skill's workflow yourself | Never convene for a one-line fix |

Each panel member costs a full context. Convene for delivery gates and stalls, not every round.

## Convene

1. **Freeze the brief** and the version under review (workflow step 1 in the skill).
2. **Render once yourself** with `node ../scripts/render_review.mjs <file-or-url> --full-page --widths 320,390,768,1440 --out review/round-N`, so every member reads identical pixels. Members re-render only for checks you did not run (reduced motion, dark scheme, extra formats), into their own subfolder.
3. **Dispatch all members in one message** so they run in parallel. Each prompt contains: `KIT` (absolute path of this plugin), the artifact path or URL and version, the screenshot folder, the frozen brief, the stage (exploration or delivery), core tasks, and the sources of truth the member needs (direction recipe, token build, guidelines and locks for `brand-guardian`; stack and budgets for `frontend-engineer`; voice chart and supplied claims for `copy-editor`).
4. **Wait for every return.** A `BLOCKED` line means a missing input; supply it and re-dispatch that member only.

## Merge scores into the rubric

1. **Look first.** Open the screenshots yourself before reading any return, and write your own first read and squint result.
2. **Map each panel score to its rubric criterion** using the table above. Copy-editor scores: Voice and Clarity feed Brief fit (1); Microcopy and Truthfulness feed Craft details (12). Brand-guardian: Fidelity and Locks feed Brief fit (1); Tokens and Consistency feed Consistency (8). Frontend-engineer: Responsive feeds 11, States feeds 9, Tokens feeds 8; Buildability and Performance go in the notes column as delivery risks.
3. **Take the lowest evidenced score per criterion.** A lower score counts only if it names a defect with location and evidence. A lower score that rests on a preference does not move the criterion; record the preference instead.
4. **Carry every cap.** AA failure on core content: Accessibility 2. Overflow or clipped text: Responsiveness 2. Placeholder copy: Craft 2. False or invented claim, missing mandatory or misused logo: Brief fit 1. Unrequested tells: Distinctiveness capped per the rubric.
5. **Fill the score sheet** in the rubric. In the notes column, name the member whose evidence set each score below 4.
6. **The minimum governs.** Delivery needs 4+ on every applicable criterion; never average across members.

## Merge fixes

Members return up to five fixes each, so a full panel can return 25. Ship five per round.

1. Remove duplicates (contrast found by both `art-director` and `accessibility-auditor` is one fix; keep the measured version).
2. Sort by the conflict ladder below, then by impact on the lowest-scoring criterion.
3. Keep five. Park the rest in the review record for the next round.
4. Write each in the skill's format: `[Defect|Preference] criterion: problem (evidence) -> change -> expected effect`, crediting the member.

## Conflict resolution

When two members ask for opposite changes, the higher rung wins. Record the losing request and why.

| Rung | Wins | Example |
| --- | --- | --- |
| 1 | Accessibility (WCAG 2.2 AA) and legal or regulatory requirements | The direction's muted gray body text fails 4.5:1: darken the ramp step, even though the art director prefers the softer gray |
| 2 | The brief's mandatories and locked brand assets | The copy editor's sharper headline drops a mandated product name: keep the name, tighten the rest |
| 3 | Fidelity to the chosen direction | The frontend engineer suggests a stock card component that turns the asymmetric grid into centered stacks: build the grid with CSS Grid instead |
| 4 | Buildability and performance budgets | A full-bleed video hero blows the LCP budget: poster frame plus click-to-play, keeping the art direction |
| 5 | Craft and taste preferences | Pill versus square buttons: offer both to the client as a labeled preference |

A higher rung beats a lower one only on the conflicting point. Look for the fix that satisfies both before ruling: a darker ramp step keeps the art director's palette temperature; an underline plus color keeps the brand's link color and passes 1.4.1. Locks bend only through the brand owner: when a locked color fails AA as text, use it for non-text elements at 3:1 and propose an accessible text variant to the owner; do not change the lock yourself.

## Report

```text
Panel round N, <artifact> @ <version>, members: <list>, screenshots: review/round-N/
First read (mine): <first > second > third>
Scores: Brief 4 | Distinct 3 (art-director) | Hierarchy 4 | Type 4 | Color 4 | Layout 4 | Imagery 3 (art-director) | Consistency 4 | States 3 (frontend) | A11y 2 (a11y: 1.4.3 #pricing) | Responsive 4 | Craft 4  (min 2)
Fixes this round (5):
1. [Defect] Accessibility (a11y): ...
Conflicts ruled: <request vs request -> rung, outcome>
Parked for next round: <count, where recorded>
Not tested: <union of members' lists>
```

## Single-context fallback (claude.ai chat and hosts without plugin agents)

Plugin agents do not run in claude.ai chat. Keep the lenses separate in one context:

1. Render or obtain screenshots as the skill's workflow describes; in chat without tools, ask for screenshots or label the critique "conceptual".
2. Run one lens at a time in this order: accessibility, brand fidelity, copy, build, art direction. Use each agent file's checklist (`agents/<name>.md` in this plugin) as the lens. Write that lens's score line and fixes before starting the next.
3. Merge with the same rules: lowest evidenced score per criterion, caps carried, five fixes, conflict ladder.
4. Say which lenses you could not run (no DOM access for the build lens, no axe in chat).

Art direction goes last on purpose: once the measured lenses have spoken, taste cannot quietly overrule them.
