---
name: reference-reconstruction
description: >-
  Reconstructs the observed interface and behavior of a supplied app, site or screenshot set using a screen index,
  measurements, state and command maps, reusable components and matched-condition comparisons. Use when asked to
  reverse engineer, clone, reproduce or match a reference product, then adapt it if requested.
license: MIT
metadata:
  version-timestamp: "2026-10-27 11:36:23 UTC"
  agent-attribution: "computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-27 11:36:23 UTC"
---

# Reference reconstruction

A reconstruction explains and reproduces the reference's observed structure, appearance and behavior. It preserves the chain from source evidence to specification, implementation and comparison, with unknown behavior left explicit.

## Defaults

| Decision | Starting point | Change when |
| --- | --- | --- |
| Goal | Reconstruct the complete observed target scope, including interactions | Adapt styling, platform or behavior when the user requests it |
| Scope record | Screen index, state map, command map and reusable part inventory | A supplied single screenshot supports only its visible state |
| Evidence labels | `observed`, `inferred`, `unknown`, `deliberate adaptation` | Never promote inference to observation without new evidence |
| Source identity | Product/version, URL or artifact hash, date and environment | Keep multiple versions separate instead of averaging them |
| Screenshot scale | Record pixels, viewport/window logical size, zoom and DPR separately | Unknown scale stays unknown; never assume every Retina image is 2x |
| Initial slice | One representative screen plus a meaningful transition | A small one-screen utility may fit the whole first slice |
| Measurement order | Window, panes, type, rows, spacing, color, icons, detail | A user-prioritized discrepancy can move first |
| Layout tolerance | Start with 1 logical unit for major aligned edges | Set another tolerance before comparison when rendering differs |
| Pixel threshold | Start at 2% changed pixels for same-renderer stable fixtures | Cross-renderer or native materials need regional metrics and visual judgment |
| Reusable values | Project-owned primitive, semantic and component layers | Existing accepted project tokens remain authoritative for adapted output |
| Comparison fixture | Same content, size, theme, scale, scroll, focus and state | Record every unavoidable mismatch beside the result |
| Completion | Declared comparable claims verified, unknowns listed | Never claim global product equivalence from a finite sample |

## Workflow

1. **Bind the target.** Record the exact source, requested fidelity, target stack, output location and authorized observation surface. A request to clone is not automatically a request to redesign.
2. **Inspect before choosing tools.** Use supplied screenshots, project source and normal browser or native UI tools first. Select REA when shipped-artifact, runtime or capture evidence actually requires it.
3. **Build the screen index.** Give every route, window, panel, menu, dialog and significant state a stable ID. Record entry action, available actions, result and evidence path.
4. **Walk the behavior.** Exercise the requested task paths, including cancel, back, retry, empty, invalid, selected and persisted states where observation is available. Record only actions actually performed.
5. **Measure the visual grammar.** Establish scale first, then pane bounds, margins, row pitch, typography, color roles, stroke weights and icon variants. Follow [observation to specification](references/observation-to-spec.md).
6. **Write the reconstruction contract.** Map every observed requirement to a screen/state/command ID, source evidence and a planned verification. Put inferred rules and unresolved behavior in separate fields.
7. **Build the parts.** Reuse a compatible project system or create a project-owned component gallery. Preserve semantic controls and complete states while matching measured appearance.
8. **Implement the slice.** Reproduce both the representative screen and its transition with matching fixture data. Use deterministic local substitutes for unavailable backends and label the substitution.
9. **Render and compare.** Match capture conditions, inspect side-by-side and diff images, then measure high-impact discrepancies. Web comparisons can use the existing `design-critique/scripts/compare_build.mjs`; native output needs native screenshots.
10. **Fix causes in order.** Correct containers and tokens before local offsets. Repeat the same capture and interaction checks after a change; do not lower thresholds to hide a defect.
11. **Expand to the declared scope.** Use the index as the coverage ledger. A visited page is not complete until its required states and transitions have evidence.
12. **Adapt deliberately.** If requested, retain the reconstructed baseline and record brand, platform, copy or behavior changes with their reason. Respect project SSOT and replace assets that cannot be redistributed.
13. **Deliver the source and evidence.** Include screen index, measured spec, parts gallery, implementation, comparison matrix, known differences and next action. Separate visual, behavioral and runtime acceptance.

## Decisions that change the answer

- **Screenshot only:** visible pixels can support geometry and visual hypotheses. They cannot prove click behavior, persistence, keyboard navigation, hidden menus or server rules.
- **Existing source:** inspect the relevant code directly. Reverse engineering a complete source repository through REA adds no authority to ordinary architecture analysis.
- **Native target:** record OS, toolkit and active-window state. Glass and desktop tint require controlled backgrounds or a declared regional comparison.
- **Cross-platform clone:** preserve the observed task model; list platform substitutions explicitly. A web screenshot matched in Chromium does not certify a SwiftUI or Android result.
- **Project brand:** an exact study candidate can retain measured tokens separately; an adapted deliverable uses accepted project identity, assets and tokens. Never silently merge the two.
- **Unavailable workflow:** record the blocked action and what it prevents knowing. Continue independent visible scope without inventing the missing feature.
- **Runtime evidence:** a tool result, recording or REA evidence bundle establishes its declared coverage only. Use stable evidence IDs and preserve producer limitations.

## Common failures

- A polished approximation replaces requested reconstruction: restore the full observed screen and behavior contract, then propose adaptation separately.
- An unobserved button is implemented with guessed persistence: mark the behavior unknown and use an explicitly labeled fixture until verified.
- Pixel dimensions are divided by two automatically: establish actual logical size or retain pixel-only measurements.
- The diff compares different fonts or data: fix fixture equivalence before interpreting the score.
- A whole-window percentage hides a wrong primary action: compare named regions and the action's behavior as separate checks.
- Pixel similarity is reported as accessibility acceptance: run keyboard, semantic and assistive-technology checks independently.
- An upstream capture or analysis command is assumed harmless: inspect its actual launch, attachment, write and data effects before use.

## References

- [Observation to specification](references/observation-to-spec.md): evidence model, measurements, coverage and verification sequence.
- [Design system](../design-system/SKILL.md) and [component gallery](../design-system/references/component-gallery.md): reusable measured parts and state coverage.
- [UX surface placement](../ux-design/references/surface-placement.md): classify observed surfaces and specify any requested adaptation.
- [Design critique](../design-critique/SKILL.md): existing web comparison helper and rendered review.
- [Website fidelity process](../../library/draft-skills/design-web-fidelity/SKILL.md): design/build version binding.
- [BAMA design-from-app](https://github.com/daveebbelaar/bama/tree/15356bd8ebff408222ad21395aea09bd74b15310/skills/design/design-from-app) and [REA](https://github.com/morluto/rea/tree/570abe95f2a35b5c580a5ec2fca90c33d4114bdc): pinned upstream measurement and evidence methods.

Catalog IDs covered: reference-reconstruction, reference-direction, ui, ux, web-fidelity
