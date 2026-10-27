# Motion production pipeline

Version-Timestamp: 2026-10-23 20:12:12 UTC

How to take an approved motion spec to finished, token-driven files: pick the engine, map the tokens, render and encode, check accessibility, and record licenses and provenance. Working code is in the [Remotion and Lottie example](../../../library/examples/motion-remotion/README.md) and the stdlib [Lottie builder](../../../library/scripts/lottie_build.py). Tool versions and license terms below were checked on 2026-10-23; re-check them before a release.

## Choose the engine

| Deliverable | Default engine | Why | Move off it when |
| --- | --- | --- | --- |
| UI state changes, hover, page transitions, scroll reveals | CSS, WAAPI, View Transitions; GSAP or Motion for timelines | Semantic, token-driven, tiny, respects `prefers-reduced-motion` live | Never render UI motion to video or Lottie |
| Icons, loaders, success checks, logo stings for app and web | Portable Lottie from `lottie_build.py`, or After Effects plus Bodymovin | Vector, small (10-30KB for icons), plays on web, iOS, Android and in Remotion | Needs states or data binding: Rive. Needs photos, particles or blur: video |
| Video from data or templates: personalized clips, localized variants, changelog and stats videos, many sizes from one design | Remotion (React, rendered per frame) | Props, code review, batch rendering, tokens straight from `tokens.resolved.json` | Check the license first (below). One-off hand-animated piece: After Effects |
| Idents, explainers, broadcast spots with hand-tuned timing, character animation, compositing over footage | After Effects (or another NLE or compositor) built from a written spec | Animator control, plugins, editorial workflow | The client needs 50 variants: template it in Remotion or as a MOGRT |
| Social cutdowns from an existing edit | The editor (Premiere Pro, DaVinci Resolve) with the kit's safe-area overlay | Reframing and captions belong in the edit | Text and brand cards built per variant: Remotion |

Rules that hold across engines: one token file drives every engine; every moving deliverable has a static poster; nothing ships without a flash check, caption check and a watched full playback.

## Map tokens to each engine

The token build (`library/tokens/dist/`) is the source. Never retype values.

| Token | CSS and GSAP | Remotion | Lottie (`lottie_build.py`) | After Effects spec |
| --- | --- | --- | --- | --- |
| `duration.*` (120, 200, 320, 480ms) | `var(--duration-slow)` | `msToFrames(ms, fps)`, round half up: 320ms is 10 frames at 30fps, 19 at 60fps | Same rounding into keyframe times | Write frames at the comp rate next to the ms value |
| `ease.*` cubic-bezier | `var(--ease-standard)`, GSAP `CustomEase` | `Easing.bezier(x1, y1, x2, y2)` in `interpolate()` | Out tangent `o = {x: x1, y: y1}` on the start key, in tangent `i = {x: x2, y: y2}` | Influence and speed from the curve; or the Flow plugin with the exact bezier |
| `color.*` hex | `var(--color-accent-default)` | Theme from `selectTheme(tokens, brand, mode)` | `[r, g, b, a]` in 0-1, 4 decimals (`#006c6c` is `[0, 0.4235, 0.4235, 1]`) | Hex in the spec; a color control on the master comp |
| `font.family.*` | `font-family` stack | `@remotion/fonts` `loadFont` from `public/fonts` (OFL files with their license) | Convert text to shapes; Lottie text layers are not portable | Same family; collect fonts with their licenses |
| Brand and mode | `data-brand`, `data-mode` | Props `brand`, `mode` | Rebuild with `--brand`, `--mode`, or ship dotLottie themes | One render per brand and mode |

Keep the token name next to the value in layer names or comments (`Ring (color.accent.default)`), so a reviewer can trace every color and curve.

## Remotion

- **Pin exactly:** `remotion`, `@remotion/cli`, `@remotion/lottie`, `@remotion/fonts` all at the same version (4.0.538 on 2026-10-23). Remotion warns about mismatched versions and they can break rendering.
- **Node:** 22 or later. Remotion 4 runs on Node 16+, Remotion 5 will need 22.
- **Deterministic frames:** derive everything from `useCurrentFrame()`; use `random(seed)`, never `Math.random()` or wall-clock time. Hold the render with `delayRender()` until fonts and data load.
- **Compositions:** one per deliverable size, each with `brand`, `mode` and `reducedMotion` props, and default props that pass the hold and caption checks.
- **Headless Linux:** Remotion downloads Chrome Headless Shell into `node_modules` (`npx remotion browser ensure`). Install the shared libraries listed in the example README; glibc 2.35 or later; no Alpine. FFmpeg (7.1 line) is bundled and encodes H.264, H.265, VP8, VP9 and ProRes only.
- **CI:** run `npx remotion browser ensure` and the apt list, cache `node_modules`, and treat each CI render as a metered render under the v5 terms.

## Portable Lottie

`lottie_build.py` writes the subset of Lottie Animation Format v1.0 that plays the same in lottie-web, dotlottie-web, lottie-ios, lottie-android and `@remotion/lottie`:

- Allowed: shape, null, solid and precomp layers; groups, rectangles, ellipses, polystars, paths, fills, strokes, gradients, trim paths, rounded corners; masks in add, subtract or none mode; alpha mattes; markers for named segments.
- Not allowed: expressions, text layers, image, audio and camera layers, layer effects, 3D, merge paths, repeaters, embedded rasters.
- `validate` checks those rules plus required keys, frame rate (24, 25, 30, 50 or 60; 1-120 allowed), in and out points, keyframe order and tangents, color ranges, precomp references and cycles, and a size budget (default 100KB).
- Masks carry an expansion property `x` (`{"a": 0, "k": 0}`). lottie-web reads it and draws nothing without it; an `x` that is a string is an expression and fails validation.
- After Effects exports: run `validate` on the Bodymovin output before handoff; fix every error in the comp, not in the JSON.

```sh
python3 ../../../library/scripts/lottie_build.py presets
python3 ../../../library/scripts/lottie_build.py build spec.json -o mark.json --brand ember --mode dark
python3 ../../../library/scripts/lottie_build.py validate mark.json --max-kb 30
```

Remotion cannot export Lottie; it only plays it. python-lottie is AGPL and Glaxnimate is GPL: use them as separate tools if at all, never as dependencies of the kit.

## After Effects specs

When an animator builds it, hand over a spec they can key from without guessing:

- Comp size, frame rate, duration in frames, and the delivery list (master, cutdowns, poster frames).
- Per moment: trigger, start frame, duration in frames with the token name, the exact bezier, properties, and the reduced-motion alternative.
- Colors as hex with token names; fonts with license files; the safe-area overlay for each format.
- Lottie targets: the portable subset above, the size budget, markers (`intro`, `loop`, `outro`), and `validate` passing.
- Use the [motion specification template](../../../library/templates/motion-spec.md).

## Render and encode

| Deliverable | Encode | Notes |
| --- | --- | --- |
| Master | ProRes 422 HQ `.mov` (`--codec=prores --prores-profile=hq`) | Archive and hand off; never re-encode from the H.264 |
| Overlay with alpha | ProRes 4444, PNG frames, `yuva444p10le` | Lower thirds and idents for an editor |
| YouTube and general 1080p | H.264 MP4, 8 Mbps at 24-30fps, 12 Mbps at 48-60fps, AAC 48kHz | YouTube's SDR recommendation; verify |
| Vertical social, 1080x1920 | H.264 MP4, 10-20 Mbps | Platforms re-encode; verify each platform's current spec |
| Web hero loop | H.264 MP4 plus VP9 WebM, 1-3 Mbps, 6-15s, no audio | Poster frame and a pause control; AV1 needs a separate FFmpeg |

Posters: render the most meaningful frame as a PNG (`npx remotion still ... --frame=-1` for the last frame) for `<video poster>`, the reduced-motion fallback and the social cover. Then watch every file in full on the target player, check loop seams three times, and meter loudness (about -14 LUFS for streaming and social; see [video and motion graphics](video-and-motion-graphics.md)).

## Accessibility gates

| Check | Rule | How |
| --- | --- | --- |
| Reduced motion (web) | Swap video and Lottie for the poster or the final frame under `prefers-reduced-motion: reduce`; UI motion becomes a fade of 200ms or less | `goToAndStop` on the last frame; poster image; CSS media query |
| Reduced motion (video) | Video files cannot read the setting: provide a pause control, a reduced variant (`reducedMotion: true`) where the player can choose, and keep autoplaying loops to 5s or give them pause, stop or hide (WCAG 2.2 SC 2.2.2) | Render the variant; check the player UI |
| Flashing | No more than 3 flashes in any one-second period (WCAG 2.2 SC 2.3.1, Level A); beat-synced cuts and strobing text are the usual causes | Count flash frames per second window (`maxFlashesPerSecond` in the example); for broadcast and large screens run PEAT or Harding FPA and record the result |
| Captions | Open captions for social autoplay; SRT or WebVTT sidecar everywhere else (SC 1.2.2). 2 lines, 42 characters per line landscape, 32 vertical, 5/6s to 7s per cue, 20 characters per second or less | `checkCue` in the example; watch with sound off |
| Contrast | Text and captions 4.5:1 on the least favorable frame (SC 1.4.3) | Token pairs tested per brand and mode in the example; scrim or box over footage |
| Hold | Each line holds 1s + words / 3 once legible, at least 1.5s, +50% for numbers | `holdSeconds` and the schedule checks |
| Safe areas | 16:9 title-safe 90%; 9:16 text inside about 880x1280 at (60, 220) organic or 855x980 at (65, 269) paid | Review with the overlay on; never deliver with it |

## Licenses and provenance

- **Remotion is not MIT.** It is source-available under the Remotion License (https://github.com/remotion-dev/remotion/blob/main/LICENSE.md). Organizations with 4 or more people, counting contractors on the project, need a Remotion Company License (https://www.remotion.dev/docs/license). Rendering with `npx remotion render`/`renderMedia()` is metered as Automators use under the v5 terms. Users of this kit are responsible for their own license. Agencies: whose headcount counts depends on who owns the project; ask Remotion and keep the answer on file.
- **Players:** lottie-web 5.13.0 and dotlottie-web are MIT. GSAP has its own no-charge license ([web implementation](web-implementation.md)).
- **Fonts:** OFL families only, with `OFL.txt` beside the files. Rendering a font into video is fine under the OFL; selling the font files alone is not.
- **Audio and stock:** Freesound CC0 only or Pixabay; keep source URL, license, retrieval date and a saved copy of the license for every file. CC0 does not clear trademarks or likeness.
- **FFmpeg:** Remotion's bundled build is GPL-2.0+. Run it; do not redistribute the binary inside a deliverable or product.
- **Provenance:** keep the spec, token build hash, tool versions and render command with each master. For C2PA content credentials use `c2patool` (MIT or Apache-2.0, pre-1.0) as an optional final step; signing needs a real certificate. Generated Lottie records its generator and the tokens used in `meta`.
