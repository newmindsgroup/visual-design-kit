---
name: design-media-image-repair
description: Controlled image repair for original visual media, controlled revisions and reusable campaign production.
---

# Controlled image repair

Version-Timestamp: 2026-09-12T11:33:18-04:00

## Inputs and workflow

Read the [media workflow](../../MEDIA-QUALITY-WORKFLOW.md) and reuse accepted upstream inputs. Use the [production packet](../../templates/media-quality-packet.md) for concrete inputs and outputs. Missing evidence stays explicit; tool availability is not production acceptance.

Use screen-compositing only when the repair is part of a screen composition. General image repair uses the supplied asset brief and baseline directly. This optional handoff does not recursively restart either capability.

Classify the defect before editing: source error, mask edge, lighting mismatch, geometry drift, unwanted object, insufficient canvas or export artifact. Choose deterministic retouching for exact product/label changes; use generation for suitable contextual repairs. Preserve the original, a mask/change map and the editable repair layers when the tool supports them.

For outpainting, establish the final canvas and protect subject scale, perspective and copy zones. For selective edits, specify changed region and invariants, then compare the full output against the baseline. Inspect edges at 100 percent, the whole composition at target size and neighboring areas for unintended changes. Do not repeatedly regenerate a degraded derivative: return to the best approved source when detail drifts. Upscaling cannot certify recovered factual detail. Return before/after, allowed differences, unresolved defects and revised asset hash.

## Handoff and acceptance

Return artifact locations, exact baseline, candidate status, observed checks, remaining defects and next owner through the existing [handoff](../design-stage-handoff/SKILL.md). Apply the [rubric](../../templates/media-quality-rubric.md). Preserve original assets and follow the [media execution contract](../../MEDIA-GENERATION.md). Stop at the agreed revision/budget limit and report an unresolved result rather than silently changing the brief.
