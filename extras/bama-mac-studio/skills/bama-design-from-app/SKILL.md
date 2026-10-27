---
name: bama-design-from-app
description: Rebuild the look of an app the user likes as a native SwiftUI design kit, by measuring its screenshots (sizes, spacing, type, colors, icons), building its parts, and comparing pixel by pixel until they match. Use when the user names an app whose look they want, shares screenshots of one, or says "make it look like X".
argument-hint: "<app name or screenshot paths>"
---

<!-- Version-Timestamp: 2026-10-27 07:36:32 AST -->

## Adapted execution contract

This is the pinned, MIT-attributed BAMA capability adapted for the owned design kit. Read `ADAPTATION.md` at the BAMA package root before executing helpers. Project instructions, approved DESIGN.md and canonical tokens take precedence. Use supported Codex or Claude Code tools. Resolve this skill's sibling files relative to its installed SKILL.md; `skill_dir` is a task-local shell variable that you set to that resolved directory before running the examples in either host. Invoke a named `bama-*` skill through the host's supported skill mechanism.

Stage local builds by default. Installation, signing identity selection, launch, CLI linking, MCP registration, system setting changes and capture access are separate explicit operations. Existing task authorization applies; ask only for an action not already authorized. Stage or commit only when the current task or repository workflow authorizes it. Stage explicit paths and include required attribution. The helpers do not commit. Preserve the feature, story and testing workflow below using the hardened helpers. Legacy installed-app paths in examples must be replaced by the staged binary returned by `build.sh`.

Before a new scaffold exists, keep planning evidence under the selected `<AppName>-planning/docs/` sibling or an existing approved planning folder. Treat docs paths below as relative to that planning folder until the fresh app is scaffolded, then copy the planning docs explicitly without replacing existing files. For an existing app, keep its current project layout.

The upstream acceptance statements describe checks to perform, never completed results. Screenshots, runtime behavior, permissions and cross-host acceptance require actual evidence. Use synthetic data and owned temporary test roots. Do not run a hosted session over real app data without project authorization.



# Design from app

Look at an app, measure it, and rebuild its design system in SwiftUI. The
result is a design kit (`bama-design-kit` skill) with the reference app's
numbers, and one reference screen that matches the screenshot.

Guessing gets close. Measuring gets it right. Two scripts do the
measuring, next to this skill:

- `scripts/measure.swift`: sizes, positions, text heights, and colors from
  a screenshot.
- `scripts/compare.swift`: a side-by-side, a diff, and the share of pixels
  that differ.

Run them with `swift "${skill_dir}/scripts/measure.swift" ...`.
Record the capture scale explicitly. Pass `--scale 1` for a 1x screenshot or `--scale 2` for a verified Retina capture when measuring. Full-image comparison uses pixel dimensions directly. Region comparison requires `--scale N`, the measured pixels per logical point. Never infer the scale merely from the browser or host.

## 1. Get the screenshots

Ask for screenshots, or take them with the `bama-clone` skill. You need:

- The window only, at 2x, no desktop. Save them in `design/reference/`.
- One screen with the most parts on it (a sidebar, a list, a toolbar),
  plus close-ups of menus, dialogs, and dark mode if they matter.
- The window size: `measure.swift info shot.png`.

Check: `info` prints the window size in points, and every screenshot uses
the same scale.

## 2. List the parts

Look at each screenshot and name every distinct part: window chrome,
sidebar row, section header, primary action, list row, checkbox, date
chip, icon button, divider. Start `design/KIT.md` from the `bama-design-kit`
skill's kit-spec.md with one section per part.

Check: every visible element on the main screenshot belongs to a part.

## 3. Measure

Fill `design/KIT.md` with numbers, not estimates. The recipes and the
traps are in [measuring.md](measuring.md). In short:

| To find | Command |
| --- | --- |
| Sidebar width, panes | `hline shot.png <y in an empty area>` |
| Row positions and pitch | `rows shot.png <x0> <x1> [y0 y1]` |
| Left edges, gaps | `cols shot.png <y0> <y1> [x0 x1]` |
| Selection pill, dividers | `vline` and `hline` through it, `--tolerance 4` |
| Text and icon colors | `ink shot.png x y w h` |
| Surface colors | `palette shot.png x y w h` |
| A close look | `crop shot.png x y w h out.png 4` |

Check: every token and every part size in `design/KIT.md` has a number
from a command.

## 4. Find the font and the icons

- Most apps on the Mac use the system font, even web apps. Start there.
  When the letters differ (a, g, t, digits), name the font and pick it or
  an open alternative with a license that allows bundling.
- Text sizes come from step 6: build, measure the same word in both
  images, scale.
- Icons: note the size, stroke weight, corners, and whether selected rows
  switch to a filled form. Match with SF Symbols at a light weight first;
  draw the ones that do not match as shapes (`bama-design-kit` parts.md, Icons).

Check: `design/KIT.md` names the font, the icon source, and the icon size
and weight.

## 5. Build the kit and one screen

Invoke the host-supported skill `bama-design-kit` and build the tokens, the parts, the
window chrome, and the gallery from `design/KIT.md`. Then build the main
screenshot's screen from kit parts only, with the same data and the same
window size.

Check: a snapshot of that screen has the same size in pixels as the
reference.

## 6. Compare until it matches

```bash
swift "${skill_dir}/scripts/compare.swift" design/reference/main.png /tmp/<App>-shots/<page>-light.png /tmp/<App>-compare
swift "${skill_dir}/scripts/compare.swift" ... /tmp/<App>-compare-sidebar 0 0 220 300 --scale 2  # only for a verified 2x capture
```

Open `side-by-side.png` and `diff.png` with the Read tool. Then measure
the same rows, edges, and words in both images, and fix the tokens, not
the views. Order: window size, text sizes, columns and left edges, row
heights, colors, icons.

Check: under 2% of pixels differ on the whole window, and every row and
left edge is within 1.5 pt of the reference.

## 7. Make it yours

Before the app ships to anyone else, replace what belongs to the other
company: its name, logo, illustrations, and any font or icon it owns.
Keep the structure, the spacing, and the feel. Write the replacements in
`design/KIT.md`.

Done when `design/KIT.md` has a measured number for every token and part,
the kit's gallery shows every part, the reference screen passes step 6,
and step 7 lists what was replaced.
