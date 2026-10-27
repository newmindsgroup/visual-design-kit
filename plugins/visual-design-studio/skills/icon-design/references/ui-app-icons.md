# UI glyphs and application icons

Version-Timestamp: 2026-10-27 11:36:23 UTC

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-27 11:36:23 UTC

## Choose the asset contract

Separate interface glyphs, explanatory pictograms and application identity. A small toolbar action needs reliable meaning; a Dock icon needs recognition and distinction.
Read accepted project DESIGN.md, token sources and existing icon assets first. Their rules override the starting geometry here.
For a reference reconstruction, keep measured source values in its candidate spec and label any deliberate deviation.
Do not recolor or redraw approved marks merely to fit a new icon family.

| Asset | Source master | Required usage record |
| --- | --- | --- |
| Interface glyph | Named SVG paths, original native shapes or licensed symbol reference | Semantic key, sizes, states and accessible use |
| Pictogram | Editable vector with named groups | Context, accompanying text and minimum size |
| Application icon | Original vector or platform layered source | Concept, platform, appearances and export versions |
| Reconstructed reference | Source evidence plus measured geometry | Observed values, unknowns and replacement rights |

## Define the geometry sheet

Start a new UI family on a 24x24 coordinate canvas with a 20x20 live area and a 2-unit nominal stroke.
Use the existing family's canvas when extending it; a second grid creates inconsistent weight and alignment.
Choose round or square caps and joins once. Document corner radii for structural corners and internal cutouts separately.
Keep circles, squares, diagonals and dense forms in one test row. Equal numerical bounds rarely produce equal apparent weight.
Allow modest optical corrections for circles and diagonals, then name the exception rather than hiding it in arbitrary transforms.
Align at the final rendered scale. A mathematically half-unit coordinate is not inherently sharp at every DPR.
Check open counters and adjacent strokes at actual size; start with at least one visible device pixel of separation at the smallest supported rendering.
Use filled variants for selected state only when the selected meaning remains clear alongside its text and control semantics.
Keep a geometry annotation layer outside exported artwork.

## Create optical sizes

Render the same candidate at 16, 20, 24 and 32 CSS px for web or pt for native UI.
Inspect at 100% first, then enlarge to diagnose the cause of a defect.
At 16, remove secondary marks, open tight gaps and slightly strengthen thin features when needed.
At 32, preserve the family character; do not automatically scale up every correction made for the 16 variant.
Use one asset when it survives the full range. Add separate optical variants only where a measured problem requires them.
Name variants by intended size or role, not by export sequence such as `final2`.
For raster exports record source canvas, output pixels and intended display scale independently.
Never infer a screenshot's point size from its pixel dimensions alone.

## Build a semantic registry

Views ask for meaning such as `addItem`, `openInspector`, `archive`, `retrySync` and `warning`.
The registry maps each key to a drawing or permitted platform symbol, optical variants and directional behavior.
Keep the accessible action wording on the owning control because the same drawing can serve different actions.
Store source, license, asset version and known restrictions with the registry record.
Avoid automatic fallback from an unknown key to an unrelated glyph. Show a development error or a declared neutral fallback.
Publish key changes with deprecations so a new family does not break consumers.
Audit product code for direct vendor names outside the adapter layer; allow intentional platform exceptions explicitly.

## Make the control usable

Wrap artwork in a real HTML button, link or native control appropriate to its action.
For an icon-only action, name the action: "Archive project", rather than "box icon".
Hide a purely decorative icon from the accessibility tree when adjacent text already conveys its meaning.
Expose toggle state, selection, busy state and errors through the owning control's semantics.
Keep visible focus around the hit region, not clipped to the glyph's internal path.
Use a 24x24 CSS px minimum target on web and 44x44 or larger for touch comfort; retain native platform control sizing on desktop.
Provide hover help for an unfamiliar desktop control, with its shortcut where useful. Do not rely on hover for essential instructions.
Keep equivalent commands available through keyboard and menus when the host platform expects them.
Pair status color with shape or wording and check meaningful icon contrast at 3:1 against adjacent colors.
Test labels and focus in the actual implementation. SVG source inspection does not establish announcements.

## Design the application icon

Sketch three different product metaphors as black silhouettes before adding color or depth.
Choose one recognizably different silhouette that communicates the app's purpose at 16 and 32 units.
Start with one dominant object and up to two supporting layers; reduce detail before making the object smaller.
Treat the often useful 45% to 55% canvas-width glyph as a composition starting point, not a platform requirement.
Use an original drawing or an asset whose license permits application identity use. Check platform-symbol restrictions directly.
Avoid miniature UI, tiny text and unrelated decorative badges unless the approved identity specifically requires them.
Keep source geometry and export settings separate so platform effects are not baked into every asset.
For macOS layered icons, use the actual Icon Composer source format and verify the current Apple toolchain.
Do not add an extra rounded-square mask, glare or shadow when the selected platform renderer supplies it.
A flat approximation remains a flat preview until the compiled result is inspected.

## Review and export

Make one contact sheet with all UI glyphs at actual sizes, plus application-icon silhouettes and appearances.
Review on light, dark, selected, high-contrast and busy/content-backed surfaces relevant to the product.
Check weight beside real text, baseline, apparent center, direction, selected form and color-token mapping.
Render toolbar, navigation and error examples. Similar-looking assets can still communicate different meanings poorly.
For macOS compilation verify `xcrun --find actool` and locate Icon Composer's `ictool` in the selected Xcode installation.
Do not substitute `xcrun ictool` without checking which utility it resolves. Record exact tool paths and versions.
Compile in a new output directory, check command status and expected outputs, then inspect the generated appearances and small sizes.
Missing tools hold compilation and native appearance acceptance; they do not prevent vector design or a clearly labeled flat contact sheet.
Keep installation, Dock refresh and distribution separate from asset generation. Do not restart Dock as a routine icon-design step.
Deliver editable source, semantic registry, export manifest and the actual review findings.

## Sources

- [BAMA app icon](https://github.com/daveebbelaar/bama/tree/15356bd8ebff408222ad21395aea09bd74b15310/skills/design/app-icon) and [custom design kit](https://github.com/daveebbelaar/bama/tree/15356bd8ebff408222ad21395aea09bd74b15310/skills/design/design-kit): pinned method sources.
- [Apple app icons](https://developer.apple.com/design/human-interface-guidelines/app-icons) and [SF Symbols](https://developer.apple.com/sf-symbols/): verify current formats and usage terms before production.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): web contrast, target and accessible-name requirements.
