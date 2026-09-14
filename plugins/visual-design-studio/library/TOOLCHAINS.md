# Medium-specific production interfaces

Version-Timestamp: 2026-09-10 19:58:10 AST

These are authored interface contracts. No renderer, paid service, framework or hardware is selected. Tools must be discovered and authorized per project. The manifest validator checks local files, hashes and recorded use permissions; it does not launch tools.

| Medium | Required specification | Native/runtime acceptance evidence |
| --- | --- | --- |
| Web | Routes, state IDs, viewports, browser support, fonts/assets, build/runtime/dependency versions | Actual build and browser interaction checks at desktop/mobile, keyboard and changed error/loading states |
| App | Target OS/version, screen states, navigation, offline/error behavior, data boundaries, packaging | Native build, simulator/device interactions, permission/recovery behavior and package opening |
| Static | Width/height/units, resolution, color space/profile, bleed/safe area where applicable, formats | Viewer-open/export inspection, measured dimensions, typography and legibility at intended viewing conditions |
| Motion | Canvas, duration, frame rate, codec/container, audio policy, timing, safe areas, loop behavior | Actual playback, first/last-frame and loop checks, text exposure time, audio checks and native source reopen |
| Touch | Display/context, reachable targets, input method, idle/reset/privacy behavior, connectivity/recovery | Physical interaction and reach tests on intended device/context, reset/recovery and shared-session privacy |
| Fixture | Units, geometry, materials, tolerances, attachment/load assumptions, drawing/render formats | CAD/native reopen and dimensional checks; qualified engineering/manufacturing review for fabrication and safety |

For each production run record tool/version, source format, export parameters, environment, dependency/license references and whether execution/reopen was observed. A renderer value of `unselected` with `status: unverified` is honest and permitted for planning. `verified` requires a local hashed reopen-evidence file, whose truth still needs review.

The manifest field `verified` is a structural evidence-reference status, not a production-route verdict. Use `route-verified` only for an app route with actual native save/reopen, editable-structure and export/viewer evidence. Do not promote a route from the manifest status alone.

Local file reopening here means opening bytes to recompute SHA-256. Native application reopening, rebuild reproducibility, visual comparison and destination behavior remain distinct tests. Preserve an immutable baseline copy, compare structured geometry/text/token data with the CLI where available, and inspect actual rendered changes separately. JSON lists compare atomically; empty or dotted object keys are unsupported in the comparison command.

## Select existing software when it serves the output

The [software production workflow](SOFTWARE-PRODUCTION.md) extends these medium contracts with native/collaborative application selection and verification. Read only the selected app workflow. The [destination readiness record](SOFTWARE-READINESS.md) distinguishes installed tools, exposed integrations, tested operations and accepted outputs for this project. No app, connector or export format alone proves a production deliverable.
