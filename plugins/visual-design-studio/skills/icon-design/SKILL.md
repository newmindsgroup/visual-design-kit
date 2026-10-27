---
name: icon-design
description: >-
  Designs coherent UI icon families and original application icons, from concept and vector geometry to semantic
  registries, optical sizes, accessible controls and platform exports. Use when creating, extending, reconstructing
  or auditing icons, a pictogram set, an app icon, a Dock icon or Icon Composer artwork.
license: MIT
metadata:
  version-timestamp: "2026-10-27 11:36:23 UTC"
  agent-attribution: "computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-27 11:36:23 UTC"
---

# Icon design

An icon family shares a visual grammar and makes actions easier to recognize. An application icon communicates one product idea at a glance, including at its smallest rendered size.

## Defaults

| Decision | Starting point | Change when |
| --- | --- | --- |
| Authority | Accepted project DESIGN.md, tokens and icon registry | A requested reconstruction keeps measured reference geometry in a separate candidate |
| UI canvas | 24x24 viewBox, 2-unit nominal stroke, 2-unit safe inset | Extend the existing family's grid and stroke first |
| Optical sizes | Review 16, 20, 24 and 32 CSS px or native pt | Deliver only actual product sizes; draw a small variant when detail collapses |
| Geometry | Consistent caps, joins, corner family and apparent weight | A recognizable object needs an intentional documented exception |
| Family selection | One licensed system or one original family | Mix only with a measured visual correction and named replacement plan |
| Naming | Semantic registry keys such as `addItem`, `archive`, `syncError` | Preserve published keys; deprecate instead of silently renaming |
| Color | Semantic foreground token, usually one color | State meaning adds text or shape; never color alone |
| UI state | Rest, hover, pressed, selected, focused, disabled, busy where applicable | Platform components own states they already implement |
| Icon-only action | Native Button or semantic HTML button with an accessible action name | Decorative icons are hidden from accessibility APIs |
| Web target | 24x24 CSS px minimum hit region; 44x44 preferred for touch | Larger audience or device requirements override |
| App icon | Three different object/silhouette concepts, one clear idea each | A locked accepted concept needs refinement rather than new concepts |
| App source | Editable vector or layered platform source plus export receipt | Existing licensed bitmap masters can remain authoritative |
| Iteration | Change one cause per round; inspect at actual sizes | A concept failure warrants a new silhouette rather than detail polishing |

## Workflow

1. **Identify the job.** UI glyph family, custom illustration pictograms, application icon, or all three. Record target platforms, sizes, appearances, current assets and allowed change.
2. **Read the project authority.** Inspect its icon registry, tokens, approved marks and licensing. Reuse accepted geometry before proposing another family.
3. **Inventory meaning.** List each semantic key, action or concept, visible label, context, directional behavior, and required state variants. Separate the same drawing used for different meanings.
4. **Set the grammar.** Specify canvas, live area, stroke, caps, joins, corner rules, optical correction, fill policy and baseline. Follow [UI and app icons](references/ui-app-icons.md).
5. **Explore the hard cases first.** Draw one simple, one dense and one asymmetric glyph; for app icons compare three silhouettes at 16, 32 and 128 units before adding materials.
6. **Build editable assets.** Use named vector geometry and a semantic registry. Views request a semantic key, never a vendor symbol name scattered through the app.
7. **Design the optical variants.** Simplify interior gaps, open counters and adjust apparent weight at 16. Treat 24-to-16 scaling as a candidate that must survive inspection.
8. **Implement real controls.** Keep hit area separate from artwork bounds. Add accessible labels, tooltip and keyboard route when relevant, and selected/busy semantics on the owning control.
9. **Render a contact sheet.** Show the whole family on light, dark, selected, high-contrast and content-backed surfaces, at actual target sizes and at enlarged geometry scale.
10. **Inspect in context.** Place the icons in representative toolbar, navigation, table and error states. Compare weight beside text and alignment against neighboring controls.
11. **Export for the target.** Keep SVG source for web; use licensed platform assets or original native shapes for native UI. App icons follow the actual platform pipeline.
12. **Verify the delivery.** Record source hash, export dimensions, registry coverage, appearance matrix, visual findings and runtime checks. A contact sheet alone does not prove keyboard or screen-reader behavior.

## Decisions that change the answer

- **Reference reconstruction:** measure the source family's geometry and complete observed states first. Preserve exact observed behavior; list intentional adaptations separately when requested.
- **Brand:** the approved project system overrides kit geometry and material defaults. An app icon may carry brand character more strongly than utility glyphs.
- **Native platform:** use the platform's symbols inside apps when suitable and permitted. Do not assume platform-symbol licenses allow logos, merchandise or application icons.
- **Density:** dense desktop tools may use 16pt artwork inside native controls; touch interfaces need larger hit regions without automatically enlarging the glyph.
- **Writing direction:** mirror direction-dependent actions such as forward/back where the platform does; preserve symbols whose meaning is fixed, and test the actual RTL layout.
- **Complexity:** a small icon cannot explain a detailed workflow. Pair unfamiliar symbols with visible text instead of inventing more detail.
- **macOS Icon Composer:** a compiled layered icon requires available `actool` and Icon Composer's `ictool`. Source drawings and flat previews remain useful when those tools are missing; compilation and native appearance acceptance remain pending.

## Common failures

- A mixed 1.5-unit and 2-unit stroke family: normalize apparent weight, then inspect circles, diagonals and dense forms together.
- A glyph looks centered numerically but leans visually: apply a documented optical offset and compare at actual size.
- A shape with a click handler replaces a button: restore the native control and style its contents.
- Tooltip is the only accessible name: provide an action label on the control, then add the tooltip as supplementary help.
- A static icon implies selected or busy without state semantics: bind the owning control's state and test its announcement.
- An app icon is a miniature screen or wordmark: reduce to one original silhouette and test it at 16.
- A vendor symbol is repurposed into an application icon without checking its license: replace it with an original design or a permitted asset.
- The export looks correct only when enlarged: fix the smallest optical variant before adding detail.

## References

- [UI and application icons](references/ui-app-icons.md): geometry, registry, optical variants, interaction and platform export checks.
- [Design system](../design-system/SKILL.md): project tokens, component APIs and versioned adoption.
- [Native app design](../native-app-design/SKILL.md) and [macOS](../native-app-design/references/macos.md): native controls and the layered Mac icon toolchain.
- [Reference reconstruction](../reference-reconstruction/SKILL.md): observed icon measurements and source-bound fidelity.
- [UI system process](../../library/draft-skills/design-ui-system/SKILL.md): component and state records for client projects.
- [BAMA app-icon source](https://github.com/daveebbelaar/bama/tree/15356bd8ebff408222ad21395aea09bd74b15310/skills/design/app-icon): pinned upstream method behind the platform specialization.

Catalog IDs covered: icon-design, ui, identity, production
