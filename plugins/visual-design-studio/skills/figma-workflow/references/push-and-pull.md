# Push screens into Figma and pull frames back to code

Version-Timestamp: 2026-10-20 10:35:33 UTC

Two directions, one rule: the result must be built from the shared tokens and components, and a screenshot comparison must prove it matches its source. Tool names below are those of the official Figma MCP server and its skills as read on 2026-10-20; servers update often, so use the names your server lists. Commands run from the `figma-workflow` skill folder.

## Push: a chosen stylescape into Figma

Stylescapes in `library/examples/stylescapes/<brand>/index.html` are self-contained static HTML (CSS, inline SVG, self-hosted fonts) with fixed section ids: `direction`, `hero`, `palette`, `type`, and so on. Push one when the client wants to review or extend the chosen direction in Figma.

1. **Pick the output.** Editable design layers for review and extension (default); a runnable Code Layer only when the client asks to click through it. Ask if the brief does not say; `figma-code-workflows` requires that choice before importing.
2. **Get a file.** Use the link the user gives, or load `figma-create-new-file` and call `create_new_file`.
3. **Capture a reference.** Static HTML to editable layers: `html_to_figma` with the stylescape file (load `figma-code-workflows`). The result is a faithful but flat layer tree.
4. **Decide whether to rebuild.** A stylescape is a mood and system board, not product UI; a clean capture is often enough for review. Rebuild with library instances only for sections that will become real screens (the hero, app screens, components section).
5. **Rebuild sections** with `figma-generate-design` and `figma-use`: `search_design_system` for components and variables, then assemble section by section with `use_figma`, binding fills, type and spacing to variables.
6. **Name** frames `<Brand> / Stylescape / 1440`, sections by their HTML ids (`hero`, `palette`), layers by role.
7. **Check.** `get_screenshot` of the frame next to `node ../design-critique/scripts/render_review.mjs <stylescape> --widths 1440 --full-page`. Fonts are the usual gap: the stylescape's self-hosted OFL fonts must be available to the Figma file (installed locally, or uploaded as shared fonts, which Figma offers on Organization and Enterprise plans; verify), otherwise Figma substitutes and every heading drifts.

## Push: a React screen into Figma

For screens built from `library/examples/react-system/` (the specimen at `/` and the billing screen at `/billing.html`) or a client app:

1. **Run the app.** `npm ci && npm run dev` in a working copy (never inside the installed plugin), or serve `dist/` after `npm run build`. Use URL parameters to fix the state: `?theme=dark&brand=ember&dir=rtl`.
2. **Load** `figma-generate-design` and `figma-use`. Import tokens and components first ([tokens and components](tokens-and-components.md)); a screen pushed before its library exists ends up as detached frames.
3. **Capture and build in parallel**, as `figma-generate-design` describes: `generate_figma_design` captures the running page into the target file (required when the screen has photos, avatars or logos, because `use_figma` cannot fetch image URLs), while `use_figma` builds the screen from library instances.
4. **Match, then delete the capture.** Adjust the instance-built screen to the capture's spacing and sizes, copy image fills from the capture, delete the capture.
5. **One frame per width and theme:** `Billing / 390 / Light`, `Billing / 1440 / Dark`. Breakpoints are separate frames, not separate components.
6. **Prove it:** export the frame at 1x and compare with the running page using `compare_build.mjs` (below). Thin text-edge differences are expected; whole-region differences are rebuild defects.

## Pull: a Figma frame back to code

1. **Load** `figma-design-to-code`; it is mandatory before `get_design_context`.
2. **Parse the link** into `fileKey` and `nodeId` (`node-id=12-345` becomes `12:345`).
3. **Call `get_design_context`** for the frame and request the screenshot with it; if no screenshot comes back, call `get_screenshot`. When the response is sparse, request the visible child nodes in one parallel batch.
4. **Map before writing:**

| Figma evidence | Map to | Never |
| --- | --- | --- |
| Code Connect snippet on an instance | That component, configured as the snippet shows | Re-create it in raw markup |
| Instance of a library component without Code Connect | The matching react-system component (`Button`, `TextField`, `Card` ...) | Copy generated CSS |
| Variable on a fill, gap or radius (`color/bg/surface-raised`, `space/4`) | The token: `bg-(--color-bg-surface-raised)` in Tailwind 4 syntax or `var(--color-bg-surface-raised)` | A hex or px literal |
| Raw value with no variable | The nearest token, logged as a design defect for the Figma owner | Silently invent a new value |
| Absolute positioning in the generated code | Flex or grid with the same gaps | Ship absolute layout |
| Image or SVG asset | The downloaded asset at its exact slot | Temporary Figma asset URLs |

5. **Build** inside the project's structure, with semantic HTML, real interaction states and keyboard behavior the frame cannot show (read the Dev Mode annotations).
6. **Verify visually**, then numerically:

```sh
# Export the frame PNG at 1x (Figma export or get_screenshot), wrap it in an HTML page with the image at full width,
# then compare it with the build at the frame's width.
node ../design-critique/scripts/compare_build.mjs frame-1440.html http://127.0.0.1:5173/billing.html \
  --widths 1440 --threshold 8% --mask "[data-dynamic]" --out review/figma-pull-1440
```

Calibrate the threshold on a frame you know matches first; cross-renderer text noise varies with the amount of text. Read the regions: a region the size of a component is a defect; outlines around text are rasterizer noise. Thresholds, masks and acceptable drift: [build fidelity](../../design-critique/references/build-fidelity.md).

7. **Critique** the built page with the design-critique workflow; fidelity to a weak frame is not quality.

## Dev Mode handoff

Before marking a frame Ready for dev:

- [ ] Every component is a library instance; nothing detached.
- [ ] Every fill, stroke, gap, padding, radius and text style is bound; Dev Mode shows variable names with WEB code syntax, not hex.
- [ ] Code Connect snippets appear on mapped components ([Code Connect map](code-connect-map.md)).
- [ ] Frames exist at 390, 768 and 1440 (or the brief's sizes), in Light and Dark, plus High contrast for key screens.
- [ ] States are shown: hover, focus, disabled, loading, error, empty, long content and truncation.
- [ ] Annotations carry keyboard order, ARIA roles and live regions, motion durations by token (`duration/fast`), analytics events and content rules.
- [ ] The frame names the token version it was built against.
- [ ] Measurements developers will read are on the 4px space scale.

After build, run `compare_build.mjs` frame against build and attach the report to the handoff record.

## Failure modes

- Capture left in the file next to the rebuilt screen -> delete it once matched; two versions confuse Dev Mode.
- Stylescape fonts substituted in Figma -> install or share the OFL fonts before capture; re-capture.
- Pulled code that duplicates a component the project already has -> search the codebase first; reuse and extend.
- Screens pushed at one width only -> push every agreed width; responsive behavior is part of the design.
- A Figma frame that disagrees with tokens -> the tokens win; log the drift for the Figma owner instead of coding the off-token value.
