# Working without the Figma connector

Version-Timestamp: 2026-10-20 10:35:33 UTC

When the Figma MCP server is not connected, failed to connect, or the user's plan blocks a step, do not stop and do not fake a Figma result. Produce files a person can import in a few minutes, give exact instructions, and say which steps were not run.

## First, say what is missing

- Tools absent from the session: tell the user the Figma connector is not available here and that it can be enabled in their connector settings; continue with the fallback.
- Server listed but failing to connect: report it as a connection failure to retry, not as missing access.
- Plan limit (Code Connect, mode counts, shared fonts): name the limit, mark it "verify on Figma's pricing page", and use the fallback for that step only.

## Fallback 1: token JSON and import script

1. Build the files:
   `cd plugins/visual-design-studio/library && python3 scripts/tokens.py build && python3 scripts/tokens.py lint`
2. Hand over these files:

| File | Use |
| --- | --- |
| `tokens/dist/figma-variables.json` | Collections, modes, values and aliases in the kit's Figma format |
| `tokens/src/*.tokens.json` | DTCG source, for Figma's native variable import or a DTCG import plugin where available (verify) |
| `tokens/dist/tokens.resolved.json` | Resolved values for shadows and other styles variables cannot hold |
| Output of `python3 scripts/tokens.py figma-script` | Complete import script (data plus `figma-import.js`) |

3. Instructions for the user to run the script as a private development plugin in the Figma desktop app (steps as of 2026; verify menu names in Figma's plugin quickstart):
   - Plugins > Development > New plugin, choose "Figma design" and an empty template; save it locally.
   - Set `manifest.json` to `"main": "code.js"` and `"documentAccess": "dynamic-page"`.
   - Replace `code.js` with the printed script wrapped so top-level `await` and `return` work in a plugin:

```js
// code.js: paste the full output of `tokens.py figma-script` where marked.
(async () => {
  const report = await (async () => {
    /* paste the figma-script output here (it starts with `const DATA =` and ends with `return report;`) */
  })();
  figma.notify(`Variables: ${report.created} created, ${report.updated} updated, ${report.skipped.length} skipped`);
  console.log(report);
  figma.closePlugin();
})().catch((error) => figma.closePlugin(String(error)));
```

   - Open the target design file, run Plugins > Development > the new plugin, and read the console report.
4. Then follow the checks and manual foundations in [tokens and components](tokens-and-components.md); they apply unchanged.

## Fallback 2: screens and components

- **Screens into Figma:** export screenshots with `node ../design-critique/scripts/render_review.mjs <page> --widths 390,768,1440 --full-page` and hand over the PNGs plus the page URL; the user can import with Figma's own HTML import or a capture plugin later. Say the frames are images, not editable layers.
- **Components:** hand over the build order and property map from [Code Connect map](code-connect-map.md) as the specification for whoever builds the library.
- **Code Connect:** write the `.figma.ts` templates anyway; they publish later with `npx figma connect publish` once the plan and token allow.

## Fallback 3: a Figma frame back to code

Without `get_design_context`, ask for: the frame exported as PNG at 1x per width, the Dev Mode variable names on key layers (or a screenshot of the Inspect panel), and any exported SVG assets. Build from those, map values to the nearest tokens, list every guessed value, and run `compare_build.mjs` against the PNG wrapped in HTML ([build fidelity](../../design-critique/references/build-fidelity.md)).

## Handoff package

Zip or commit one folder:

```text
figma-handoff/
  README.md               steps above, token version, what was not run
  tokens/                 figma-variables.json, DTCG sources, tokens.resolved.json
  figma-import-plugin/    manifest.json, code.js
  screens/                PNGs per screen, width and theme
  code-connect/           *.figma.ts templates
```

## Report honestly

End with: what was produced, what the user must run, and what was not verified (import not run in Figma, plan limits unconfirmed, fonts not checked in the target file). Never describe a Figma file as updated when no Figma tool ran.
