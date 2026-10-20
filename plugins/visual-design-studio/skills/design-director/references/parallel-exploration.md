# Parallel exploration with direction explorers

Version-Timestamp: 2026-10-20 10:28:22 UTC

One context that writes five directions in a row drifts toward its first idea: the second direction borrows the first one's grid, the third its palette temperature. Separate contexts, each committed to one position, produce real spread. In Claude Code and Cowork, dispatch one `direction-explorer` subagent per position, in parallel, and keep the brief, the lane plan, the distinctness test and the scoring in your own context. In claude.ai chat, and in any host that does not load plugin agents, run the same lanes one at a time with the single-context fallback below.

## When to dispatch

| Situation | Default | Change when |
| --- | --- | --- |
| Identity, flagship site or app, campaign platform (4-5 directions, rendered) | Dispatch one explorer per direction | The user asked for a quick text answer: stay single-context |
| Small job (3 directions) | Single context is fine; dispatch if you will render all three stylescapes | Time or token budget is tight: single context, hero-palette-type-voice fidelity |
| Revision or a client-mandated direction (2 executions) | Single context | Never dispatch for one direction |
| No file system (chat) | Single-context fallback | Always |

Each explorer reads the kit references and fills the ten-section stylescape template, so it costs a full working context. Dispatch only when the directions will be rendered or the brief deserves 4-5 genuinely different answers.

## Before dispatch: plan the lanes

Do intake, the atlas query and the category scan yourself (workflow steps 1-4 in the skill). Then write a lane plan: one row per direction with a planned value on each of the six distinctness axes from [divergence](divergence.md). Check the plan before anyone builds: every pair must already differ on at least 3 planned axes. A plan that fails on paper will fail in pixels.

```markdown
| Dir | Position | Atlas styles | Type | Palette | Layout | Imagery | Motion | Voice |
| A "Harbor" | category-expected | style.corporate-modern | humanist sans, low contrast | cool, mid-saturation, light | 12-col, calm, symmetric | art-directed photo | precise, 200ms | warm-formal |
| B "Ledger" | adjacent: financial editorial | style.editorial-magazine + style.swiss-international | serif display, high contrast | warm paper, low saturation, light | asymmetric, numerals as heroes | data and charts | still, count-up once | precise, explanatory |
| C "Block Party" | category-breaking | style.neo-brutalist | grotesque, extreme scale jumps | saturated primaries, dark | modular blocks, dense | type-only and flat shapes | springy, 320ms | casual, playful |
```

Pick style IDs that exist: `python3 ../../../library/scripts/atlas.py list --axis style`. Give every lane a different primary style ID; sharing a secondary is fine.

## What each explorer receives

Send one Agent call per lane, all in the same message so they run in parallel. Use the subagent type `visual-design-studio:direction-explorer` (some hosts list it without the plugin prefix). Each prompt contains:

| Field | Content |
| --- | --- |
| `KIT` | Absolute path of this plugin (two levels above this skill's directory) |
| Brief summary | Objective, deliverable, channel, market and language, audience, tier, constraints, success metric, with each item marked given or assumed |
| Locks | Approved logo, colors, type, voice and assets, and the permitted range |
| Position and letter | One position, the direction letter and its working name |
| Atlas IDs | The lane's style IDs plus the shared industry, market, audience, archetype, tier and channel IDs |
| Category scan | The competitor map and the white space, in 5-10 lines |
| Sibling lanes | Every other row of the lane plan, verbatim |
| Your lane's planned axes | Its row of the lane plan, as a starting point the explorer may move away from siblings but never toward them |
| Working folder | Absolute path to the project's `directions/` folder |
| Fidelity | Early (hero, palette, type, voice), standard (all ten sections) or final (plus a second application), from [stylescapes](stylescapes.md) |

Keep the brief summary identical across prompts; only position, letter, atlas styles and planned axes change. Never send one explorer's draft to another during the first round; independence is the point.

## When explorers return

Each returns a fixed block (see `agents/direction-explorer.md` in this plugin) with an `Axes:` line and a stylescape path. For each return:

1. **Check completeness.** Two named typefaces, 4-8 hex colors with roles and contrast ratios, layout, imagery, motion with a duration and easing, voice with two sample lines, a rendered stylescape (or a stated reason it is not rendered). A `BLOCKED` return means your prompt was missing something; fix the prompt and re-dispatch that lane.
2. **Open the screenshots yourself.** Do not trust the self-check. Look for unrequested AI tells, overflow and placeholder copy; run `node ../../design-critique/scripts/render_review.mjs` on any page that was not rendered.
3. **Run the distinctness test on the returns, not the plan.** Build the pair table from the returned `Axes:` lines and the screenshots. Mark an axis as different only when you can see it in the screenshots at thumbnail size.

| Pair | Type | Palette | Layout | Imagery | Motion | Voice | Differ | Pass |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-B | x | x | x | x | | x | 5 | yes |
| A-C | x | x | x | x | x | x | 6 | yes |
| B-C | | x | x | | | x | 3 | yes |

4. **Fix failing pairs.** Keep the stronger direction of the pair (higher Brief fit and Distinctiveness at a glance). Re-dispatch the weaker lane once with the stronger direction's returned block added to "Sibling lanes" and an instruction naming the axes to move ("differ on type classification and imagery medium; move further toward category-breaking"). If it still fails, move it to an unused position, or drop it and present one direction fewer. Never present a near-duplicate.
5. **Equalize fidelity.** All directions at the same fidelity and the same screenshot widths. Uneven polish biases the choice; bring the weaker one up or the stronger one's extras out of the comparison.
6. **Score in your own context.** Explorers never score. Use [scoring](scoring.md) and `python3 ../scripts/score_directions.py scores.json`, then build the `directions/index.html` comparison page.

## Failure handling

| Problem | Do |
| --- | --- |
| An explorer drifted into another lane's style | Re-dispatch with the sibling's block and the axes to move |
| All directions share one tell (same gradient, same three cards) | The brief summary or the scan pushed them there; fix the shared input and re-dispatch the affected lanes |
| A direction breaks a lock | Re-dispatch with the lock stated as a hard rule; do not repair it silently |
| Playwright or axe missing | Explorers return unrendered pages; install once in the project with the user's permission, then render all directions with identical settings |
| An explorer wrote inside the installed kit | Move the files to the project folder and tighten the working-folder line in the prompt |

## Single-context fallback (claude.ai chat and hosts without plugin agents)

Plugin agents do not run in claude.ai chat. The skills still give the same result if you separate the lanes deliberately:

1. Write the lane plan table first and check it on paper, exactly as above.
2. Build one direction at a time, finishing its recipe before starting the next. Before each new direction, reread only its lane row and the sibling rows, not the previous direction's prose.
3. After each recipe, write its `Axes:` line and compare it with every finished direction. If a pair differs on fewer than 3 axes, change the new direction now, before writing the next.
4. Build the most different direction (category-breaking) second, not last, so the middle direction does not average the other two.
5. In chat without file tools, describe each direction with its token table, typefaces, hex values and sample copy, and say it is unrendered. When Artifacts are available, render the comparison as one artifact page with the directions at equal fidelity.
6. Score and recommend exactly as in the parallel route.

The output format, the distinctness table and the score table are the same on every host, so the client sees the same presentation whether the directions came from five explorers or one context.
