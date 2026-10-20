# Tokens and components in Figma

Version-Timestamp: 2026-10-20 10:35:33 UTC

The procedure for getting the kit's tokens into a Figma file as variables and building components on top of them. Variable types, scopes, styles-versus-variables and property conventions are in [design-system's Figma reference](../../design-system/references/figma.md); read it once before the first import.

## What the export contains (2026-10-20 build)

| Collection | Modes | Variables | Contents |
| --- | --- | --- | --- |
| `Primitives` | Meridian, Ember (brands) | 191 | Color ramps (`color/slate/50` ...), `font/family/*`, `font/size/xs`-`5xl`, `font/weight/*`, `space/*`, `radius/*`, `size/icon/*`, `size/target/*`, `border-width/*`, `duration/*`, `ease/*`, `container/*` |
| `Semantic` | Light, Dark, High contrast | 32 | `color/bg/*`, `color/fg/*`, `color/border/*`, `color/accent/*`, status colors; every value is an alias into `Primitives` |

Counts change with the token source: read them from `library/tokens/dist/figma-variables.json`, not from this table. The file's `notExported` block lists what variables cannot hold (line height, letter spacing, measure, fluid gutters, z-index, breakpoints, shadows); those become styles or frame settings.

## Import

1. Rebuild and lint the tokens so the export is current:
   `cd plugins/visual-design-studio/library && python3 scripts/tokens.py build && python3 scripts/tokens.py lint`
2. Load `figma-use`. Print the script: `python3 scripts/tokens.py figma-script > /tmp/kit-variables.js` (about 100 KB: the JSON data followed by [figma-import.js](../../../library/tokens/figma-import.js)).
3. Call `use_figma` on the target file with the full script as the code. It returns `{ collections, created, updated, skipped }`.
4. Read `skipped`. Expected entries: motion variables (`duration/*`, `ease/*`) in files that do not support those variable types, and fonts not installed for the file (`font ... not available`; the value is still set). Anything else is a defect: fix the source and re-run.
5. Re-running is safe: collections, modes and variables are matched by name and updated in place, so existing bindings survive a token release.

## Check the import

Run a read-only `use_figma` check (with `figma-use` loaded) and compare against the export:

| Check | Pass |
| --- | --- |
| Variables per collection | Equal to the export's counts |
| Modes | `Primitives`: Meridian, Ember. `Semantic`: Light, Dark, High contrast |
| Semantic values | Every mode value is a `VARIABLE_ALIAS`, none a raw color |
| Scopes | Present on every variable the export scopes; color primitives hidden from publishing |
| Code syntax | WEB syntax `var(--...)` on every variable that has one in the export |
| Specimen | A frame per brand x mode showing `color/fg/default` on `color/bg/canvas` and each status pair; screenshot all six |

```js
// Illustrative read-back for use_figma (load figma-use first). Returns counts and any non-alias semantic values.
const cols = await figma.variables.getLocalVariableCollectionsAsync();
const vars = await figma.variables.getLocalVariablesAsync();
const out = cols.map((c) => ({ name: c.name, modes: c.modes.map((m) => m.name), count: vars.filter((v) => v.variableCollectionId === c.id).length }));
const semantic = cols.find((c) => c.name === 'Semantic');
const raw = vars.filter((v) => semantic && v.variableCollectionId === semantic.id)
  .filter((v) => Object.values(v.valuesByMode).some((val) => !(val && val.type === 'VARIABLE_ALIAS'))).map((v) => v.name);
return { out, raw };
```

## Foundations the script does not create

| Item | Build as | Values |
| --- | --- | --- |
| Text styles | Text styles with font family, size and weight bound to `font/*` variables | Line height 110% (display), 125% (headings), 150% (body), 165% (long-form); letter spacing -2%, 0%, 1%, 6% (caps labels) |
| Shadows | Effect styles `shadow/sm` to `shadow/xl` | From `tokens.resolved.json`; values differ per mode, so make one style set per theme or document the Dark values |
| Layout grids | Grid styles per breakpoint | 4 columns at 390, 8 at 768, 12 at 1440; gutters 16-32px |
| Frame widths | Frame presets | 390, 768, 1440 (add 320 for reflow checks) |
| Native code syntax | iOS and ANDROID syntax on semantic variables | Only when native apps ship; names from the native token output |

Name text styles by role and size, matching the type scale: `Display/5xl`, `Heading/2xl`, `Body/md`, `Label/sm`, `Code/sm`.

## Build components

Load `figma-generate-library` with `figma-use`, run `search_design_system` first, and build in dependency order so instances nest:

1. **Primitives of the UI:** icons (24px frame, 1.5-2px stroke, `Icon/<Name>`), `Spinner`, focus ring as an effect or stroke style.
2. **Atoms:** `Button`, `Badge`, `Checkbox`, `Switch`, `RadioGroup`, `Tooltip`.
3. **Fields:** `TextField`, `Select` (label, hint, error and adornment parts).
4. **Containers:** `Card`, `Alert` and `Banner`, `Tabs`, `EmptyState`, `Skeleton`.
5. **Overlays and data:** `Dialog`, `Toast`, `DataTable` rows and header cells.

For each component:

- Variant properties mirror the React props and values exactly (see [Code Connect map](code-connect-map.md)); booleans for optional parts; instance swap for icons.
- Every state the coded component renders: default, hover, focus-visible, pressed, disabled, loading, invalid, selected. The react-system specimen shows them all at once (`data-preview-state`); screenshot it as the reference.
- Auto layout on every frame. Padding and gap bound to `space/*`, radius to `radius/*`, fills to `color/bg/*` or `color/accent/*`, text to `color/fg/*`, strokes to `color/border/*`. No typed numbers, no hex.
- Minimum target 24x24 (44x44 on touch components through `size/target/*`); focus indicator at least 2px with 3:1 contrast.
- Description field: one line on usage plus the code import, so Dev Mode shows it.

## Binding audit

After each component set, read back with `use_figma` or `get_variable_defs` on the set:

- No fills, strokes, padding, gap or radius without a bound variable (exceptions: transparent fills, image fills).
- Every text node uses a text style.
- Switching the frame's `Semantic` mode to Dark and High contrast changes colors without manual edits; switching `Primitives` to Ember changes the accent and fonts.
- Screenshot the component set in Light, Dark and High contrast for both brands (six images) and inspect at 100%.

## Token releases

Re-run the import after every token change, then the check table above. When a variable is renamed in the source, the script creates the new name and leaves the old one: rebind instances with a `use_figma` script that swaps the old variable for the new, then delete the old variable, and note the rename in the library release notes ([governance and versioning](../../design-system/references/governance-and-versioning.md)).
