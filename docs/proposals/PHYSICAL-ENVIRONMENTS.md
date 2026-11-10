# Proposal: physical environment and fixture visualization

Version-Timestamp: 2026-10-23 13:50:00 AST
Status: **proposed** (not adopted). Follows decision D2 in [the decision register](../research/DECISIONS.md): explore and test before choosing architecture.

## Why

The kit covers identity, web, apps, screens, touchscreens, print and media. It has almost nothing for **physical retail environments and the objects in them**: store fixtures, point-of-purchase displays, millwork and casework, wire and metal racks, shelving, and the renderings that sell them. A search of the library for millwork, casework, veneer, pegboard and engineering-drawing-to-render finds no coverage.

Many businesses that design physical things need this: fixture makers, store planners, exhibition and trade-show builders, furniture and interior brands, packaging and merchandising teams.

## Evidence: one retail fixture render project (June 2026)

A team edited a photoreal render of a branded retail fixture (wood veneer, pegboard, acrylic shelves, glass, applied graphics) under deadline with chat-based image tools. Observed failures:

| # | Failure | Likely cause |
|---|---|---|
| F1 | Fine detail (pegboard holes, shelf knobs) disappeared over iterations | Each edit started from a re-compressed output of the previous one |
| F2 | Edits changed surroundings, not just the target | Whole-image regeneration instead of a defined edit region |
| F3 | Warm lighting kept returning when a cool look was required | Lighting was never stated as its own step; the model preserved it by default |
| F4 | One lighting-only prompt fixed in one pass what many mixed iterations could not | Single attribute with explicit "change this, keep everything else" boundaries |
| F5 | Shelves removed, fixture squashed | Several changes requested in one generation, no locked baseline to compare against |
| F6 | Results drifted in long chats | Earlier conversation context leaked into new steps |
| F7 | Applied advertising stretched, pulled and left gaps | A generative model asked to do exact geometric placement |
| F8 | Prompts were refined but never confirmed with the person | No validation step before execution |

Starting a fresh session per attribute, a fully specified prompt with boundaries, and working from the best available base image were what worked.

These are observations from one project. Two of them, lighting-first ordering and high-resolution baselines, are recorded as open hypotheses (O1 in the decision register) until tested.

## Proposed capabilities

Library draft skills, following the existing capability pattern. Reuse before adding: `design-media-image-repair`, `design-media-reference-control`, `design-screen-compositing`, `design-screen-product-fidelity`, `design-media-quality-evaluation`, `REALISM-REASSESSMENT.md` and the Photoshop route already cover parts of this.

| Proposed | Purpose | Closes |
|---|---|---|
| `design-environment-discovery` | Intake for physical work: input type (photo, render, CAD or engineering drawing, sketch), real dimensions, materials, viewing context, deliverable spec | F8 |
| `design-attribute-edit-protocol` | One attribute per step: region, target, do-not-change list, locked numbered baseline, change audit against the previous baseline. Generalizes the screen-only revision rules to any photoreal asset | F2, F4, F5, F6 |
| `design-environment-lighting` | Ambient, key, back, edge, practical and self-illuminated display light; color temperature; consistency across a set | F3 |
| `design-materials-finishes` | Wood veneer, laminate, metal, powder coat, acrylic, glass: references, defects to reject, how each reads under light | F1 |
| `design-surface-graphic-application` | Place real artwork onto fixture faces, headers and screens with exact geometry (perspective transform, smart object or 3D surface), then blend light only | F7 |
| `design-drawing-to-render` | Engineering drawing or CAD to photoreal render, including when a 3D model beats generation for geometric accuracy | new |
| Atlas entries | Industries and channels for retail fixtures, POP, exhibitions and store environments | new |

## Controlled test (resolves O1)

One fictional, rights-cleared fixture scene. Same target changes, three runs, every output kept:

| Run | Ordering | Baselines |
|---|---|---|
| A | All changes in one request | Chat output to chat output |
| B | One attribute per step, lighting first | Chat output to chat output |
| C | One attribute per step, lighting first | Full-resolution master, region edits, locked numbered baselines |

Measure: unrequested changes per step (change audit), detail retention at native-resolution crops, steps to an accepted result, and a blind preference review. Repeat with lighting last to separate ordering from isolation. Adopt a rule only if the evidence supports it.

## Decisions needed

1. Accept this capability list as the direction, or narrow it.
2. Which image tools are approved for the test, and with what data terms.
3. Who supplies domain review for fixtures and millwork (craft standards cannot come from the model alone).

## Not in scope here

Company-specific brand packs, client renders and fixture designs. Those belong in each adopting project, never in this repository.
