# From product observation to a reconstruction specification

Version-Timestamp: 2026-10-27 11:36:23 UTC

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-27 11:36:23 UTC

## Establish the reconstruction boundary

Record the source product, exact version or artifact hash, platform, requested scope and target implementation.
Reconstruct the full observed behavior in that scope by default. A request to clone a workflow includes its transitions, not only its first screenshot.
Adapt style, platform conventions or business behavior when asked, and retain an explicit difference register.
Keep original-source observations separate from accepted target-project rules and intended adaptations.
A single screenshot can establish visible structure; it cannot establish a whole product's feature set.
Use ordinary source tools for a complete repository. Use REA only when shipped artifacts, captures or requested runtime observations add evidence that source inspection cannot provide.

## Build a source register

| Field | What to retain |
| --- | --- |
| `source_id` | Stable local ID linked to the exact file, artifact or recording |
| `identity` | Product/version, URL or SHA-256 and capture date |
| `environment` | OS, browser/toolkit, viewport or window bounds and appearance |
| `capture` | Pixel size, logical size, DPR, zoom, crop, scroll and active state |
| `authority` | Screenshot, observed UI action, supplied source, runtime record or static analysis |
| `coverage` | What was inspected, what was excluded and whether source material is partial |
| `limitations` | Missing scale, blocked actions, unavailable state, substituted data or renderer differences |

Keep original capture files unchanged. Put crops, annotations and normalized derivatives beside them with a source pointer.
Avoid collecting unrelated desktop content when a window-only capture answers the question.
Store project evidence in the adopting project, not in the shared kit.
Retain tool-produced evidence IDs and their producer limitations when REA is used.
A finite complete page of results does not prove the underlying source or program was completely discovered.

## Make a screen and state index

Give each route, window, tab, panel, dialog, menu and significant overlay an ID such as `S01`.
For each screen list entry action, visible sections, available commands, default state and related overlays.
Give important states IDs such as `S01.empty`, `S01.loading`, `S01.invalid` and `S01.selected`.
Record the trigger, precondition, visible change, focus result, data result and exit path for each transition.
Visit cancel, back, retry, selection, filtering, sort, persistence and error paths that the requested scope exposes.
Record keyboard and pointer paths separately when they differ.
For a blocked action, retain the exact blocker and the question it prevents answering.
An action labeled Delete does not establish whether it is reversible, synchronized or immediately persistent.

## Keep four claim classes

- `observed`: directly visible or exercised under a recorded condition.
- `inferred`: a proposed rule explaining observations, with supporting IDs and confidence rationale.
- `unknown`: the necessary evidence is missing, conflicting or inaccessible.
- `deliberate adaptation`: a requested target change, linked to its reason and acceptance criterion.

Example: a screenshot directly shows a 320-pixel sidebar. Its 160pt interpretation is unknown until the capture scale is established.
Example: three rows at a 40-unit pitch support an inferred reusable row token; they do not prove every list uses it.
Example: a local fixture returns canned search results. Search layout can be observed; production ranking and network behavior remain unknown.
Do not fill a missing state with invented source behavior. Specify the chosen target fallback as a target decision.

## Measure scale before geometry

Record pixel dimensions directly from the image and logical window or viewport dimensions from the capture environment when available.
Use DPR and browser zoom as separate fields. Browser zoom, image resizing and an exported crop can change their relationship.
When only pixel evidence exists, keep pixel measurements and mark logical dimensions unknown.
Use a known UI element only as an explicit calibration hypothesis, never as hidden proof of scale.
Measure window and pane boundaries, page insets, column edges, row pitch and control bounds before small decorative detail.
Measure font metrics with the same text content: family candidates, size, weight, line height, letter spacing and baseline.
Sample colors from flat interior regions, avoiding anti-aliased edges, translucent overlays and selected states.
Separate visible color values from semantic roles. Dark mode or selection evidence can change the role mapping.
Measure icons' live bounds, stroke family, optical offsets and selected variants.
Mark each measurement with source ID, region and units so another person can reproduce it.

## Translate observations into reusable parts

Build an inventory of chrome, navigation, toolbar, rows, buttons, fields, badges, menus and feedback surfaces.
For every part record anatomy, dimensions, tokens, content behavior, keyboard contract and state matrix.
Use project-owned primitive, semantic and optional component token layers.
Keep source-derived candidate tokens separate when the target project's accepted identity differs.
Implement a component gallery with forced visual states and separate interactive controls.
Keep system controls native unless custom behavior or a measured visual requirement justifies a replacement.
An exact visual reconstruction still needs real control semantics and a keyboard path.

## Verify comparable claims

Start with one representative screen and at least one meaningful transition.
Match content, source version, logical size, pixel scale, appearance, scroll, focus and active-window state.
Capture both sides, inspect side-by-side, then inspect diff regions and measured edges.
Fix in order: overall window, panes, type metrics, row geometry, color roles, icon geometry and fine decoration.
Begin same-renderer stable fixtures with a 1-logical-unit edge tolerance and 2% changed-pixel threshold, then document task-specific overrides before measuring.
Compare critical regions separately so a small broken primary control cannot hide in a low whole-window score.
Dynamic glass, font rasterization and cross-renderer differences may need separate masks, regional tolerances and judgment.
Declare masks before comparison and retain the unmasked images. Never mask the feature being verified.
Run behavior tests independently: trigger, result, focus, cancellation, failure, recovery and persistence where applicable.
Use native capture for native output. A browser mockup proves only its browser rendering.
A REA `verify_reconstruction` pass covers the finite typed claims supplied to that operation, not global equivalence.

## Deliver a coverage ledger

For each screen/state/command include source IDs, implementation path, verification evidence, result and residual unknowns.
Count required states, states observed, states implemented and states verified separately.
Do not count a screenshot, an implementation file and an interaction test as interchangeable proof.
Keep the reconstructed baseline when producing an adapted version, with a version-bound list of changes.
The final report names unobserved paths, substitutions and mismatched conditions, plus the next evidence needed.

## Sources

- [BAMA clone](https://github.com/daveebbelaar/bama/tree/15356bd8ebff408222ad21395aea09bd74b15310/skills/plan/clone) and [design-from-app](https://github.com/daveebbelaar/bama/tree/15356bd8ebff408222ad21395aea09bd74b15310/skills/design/design-from-app): screen inventory and measured visual reconstruction.
- [REA pinned source](https://github.com/morluto/rea/tree/570abe95f2a35b5c580a5ec2fca90c33d4114bdc): artifact, runtime and coverage-qualified reconstruction evidence.
