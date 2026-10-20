---
name: design-director
description: >-
  Turn any design brief into the best design solution. Extracts every variable (industry, market, audience, archetype,
  price tier, channel, constraints), asks only the questions that change the answer, queries the Design Space Atlas,
  generates 3-5 deliberately different directions, renders them as stylescapes, scores them with a weighted matrix and
  recommends one with reasoning. Use at the start of any brand, website, app, campaign, packaging, motion or design-system
  work, when choosing a visual direction or style, or when asked "what should this look like?"
license: MIT
metadata:
  version-timestamp: "2026-10-20 02:05:00 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 02:05:00 UTC"
---

# Design director

Great design is the right answer to a specific brief, chosen from real alternatives. This skill makes the alternatives explicit, makes them visibly different, and makes the choice defensible. It works for any style, industry, market, audience and channel because it draws on the Design Space Atlas instead of a house style.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Qualifying questions | 2-4, each with options and a recommendation | Brief already answers them, or the task is a small revision (ask 0-1) |
| Directions explored | 3 for small jobs, 4-5 for identity or flagship work | Client mandated a direction: explore 2 executions of it instead |
| Direction spread | Category-expected, adjacent, category-breaking (+ competitor-contrast, audience-led) | Regulated or conservative brief: keep the breaking one but say what it risks |
| Distinctness | Each pair differs on at least 3 of 6 axes (type, palette, layout logic, imagery, motion, voice) | Never relax; near-duplicates waste the client's attention |
| Rendering | One stylescape per direction from `../../library/examples/stylescapes/_template/stylescape.html` | Text-only context: describe with token tables, and say it is unrendered |
| Scoring | Weighted matrix, 1-5 per criterion, weights from the brief, with a sensitivity check | Client supplies their own criteria: use theirs, keep yours as a second view |
| Recommendation | One winner, one runner-up, what would flip the decision | Scores within 0.2: present both as a deliberate choice for the client |

## Non-negotiables

- **Reply in the user's language.** The market decides the language of sample brand copy (headlines, CTAs), not of your answer. Gloss foreign-language samples in the user's language.
- **Every direction carries specifics, even in a short answer:** two named typefaces (display and text), 3-5 colors as hex with roles, one layout idea, one imagery idea and one line of sample copy. Cut prose before you cut specifics; an adjective-only direction is not a direction.
- **Always show the score table and a recommendation** (winner, runner-up, what would flip it). In a short answer, keep the table to the criteria and totals.

## Workflow

Paths in commands are relative to this skill's directory; resolve them to absolute paths before running.

1. **Intake.** Extract the variables in [intake](references/intake.md): objective, deliverable, channel, industry, market and language, audience, archetype, price tier, existing brand assets and locks, competitors, constraints (accessibility, regulation, budget, stack, timeline), success metric. Mark each as given, inferred or unknown.
2. **Ask only what changes the answer.** For each unknown, ask yourself: would two plausible answers lead to different designs? If yes, ask (2-4 questions max, offer options, recommend one). If no, state your assumption and move on.
3. **Query the atlas.** Run `python3 ../../library/scripts/atlas.py query "<brief in plain words>"` and read the top industry, market, audience, archetype, tier and channel entries. Read each industry entry's *Recommended directions* and *Category clichés* before inventing your own.
4. **Scan the category.** Follow [category scan](references/category-scan.md): map 6-12 competitors on type, color, imagery, layout and voice; find the white space. Skip only if you have no web access, and say so.
5. **Diverge on purpose.** Build 3-5 direction recipes using [divergence](references/divergence.md). Each recipe = 1-2 style IDs + archetype + tier signals + channel constraints, then concrete tokens. Check combinations with `python3 ../../library/scripts/atlas.py combine <ids...>` and resolve every listed conflict deliberately.
6. **Render, don't describe.** In Claude Code and Cowork, dispatch one `direction-explorer` subagent per direction in parallel ([parallel exploration](references/parallel-exploration.md)); in chat, build them in turn. Make a stylescape per direction ([stylescapes](references/stylescapes.md)). Then screenshot and inspect them with the `design-critique` skill's `scripts/render_review.mjs`. Fix generic-AI tells before anyone sees them.
7. **Score.** Use the weighted matrix in [scoring](references/scoring.md) and compute it with `python3 scripts/score_directions.py scores.json` (presets: default, launch, regulated, rebrand, product-ui). It prints the table and the sensitivity check: if a plausible weight change flips the winner, say so.
8. **Recommend.** Present: the directions side by side, the score table, the recommendation, the runner-up, risks, and what would change your mind. Keep it to one screen of text plus the visuals.
9. **Converge and hand off.** After a choice, turn the direction into tokens and route to the discipline skills per [handoff](references/handoff.md). For client projects with records and approvals, also use `design-project-start`.

## Decisions that change the answer

- **Industry** sets trust signals, conventions and regulation. Break conventions only where the brief rewards distinctiveness.
- **Market** changes script, type families, color meaning, formats, payments and law. Never transplant a US default into another market unexamined.
- **Audience** changes the numbers: older adults, children, low literacy and expert users each have their own defaults table in the atlas.
- **Price tier** changes density, whitespace, type contrast, imagery and motion pace. Mismatched tier signals are the most common positioning failure.
- **Channel** sets hard specs (sizes, safe areas, color space, performance budgets) that constrain every direction.
- **Existing brand** locks: preserve approved logo, colors, type and voice; explore within the permitted range only.

## Common failures

- Three directions that are the same idea in three colors. Fix: enforce the 3-of-6 distinctness rule.
- A "breaking" direction that is merely trendy (glass, gradients, brutalism) with no reason from the brief. Fix: tie every direction to an insight about the audience or the category.
- Asking ten questions up front. Fix: ask the 2-4 that change the answer; assume and state the rest.
- Recommending by taste. Fix: score against the brief's weighted criteria and show the math.
- Describing a direction in adjectives. Fix: tokens, specimens and a rendered hero, or it is not a direction.

## References

- [Intake and qualifying questions](references/intake.md): the variable checklist, question bank and brief template.
- [Category scan](references/category-scan.md): competitor mapping and white space.
- [Divergence](references/divergence.md): direction positions, recipes and the distinctness test.
- [Stylescapes](references/stylescapes.md): rendering and presenting directions.
- [Scoring](references/scoring.md): weighted matrix, weight presets by brief type, sensitivity check, recommendation format.
- [Handoff](references/handoff.md): from chosen direction to tokens and discipline skills.
- [Worked example](references/worked-example.md): a full run from brief to recommendation.
- [Parallel exploration](references/parallel-exploration.md): one direction-explorer subagent per position in Claude Code and Cowork, the distinctness test on returns, single-context fallback for chat.
- Atlas index and schema: `../../library/atlas/README.md`.
- Calibration set of distinct directions: `../../library/examples/stylescapes/README.md`.
- Discipline skills: `brand-identity`, `typography`, `color`, `layout`, `imagery`, `motion`, `ux-design`, `ui-design`, `web-design`, `native-app-design`, `design-system`, `data-visualization`, `print-packaging-social`, `design-critique`.

Catalog IDs covered: research, reference-direction, brand-strategy, design-taste, web-discovery, display-discovery, display-art-direction, web-art-direction, media-art-direction
