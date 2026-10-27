# Lottie and Rive

Version-Timestamp: 2026-10-23 20:12:12 UTC

Lottie plays designer-authored vector animation exported from After Effects (or authored in Lottie-native tools). Rive is its own editor and runtime for interactive, state-driven vector animation. Both beat video for UI-scale illustration and lose to code for anything that must behave like a real control. Feature support differs by player and version; test the exact runtime you will ship.

## Choose the medium

| Need | Choose | Why |
| --- | --- | --- |
| State changes on real controls (buttons, menus, toggles, form feedback) | CSS or code | Semantic, accessible, token-driven, tiny |
| Linear illustrative animation: success checks, empty states, onboarding spots, animated icons, loaders | Lottie | After Effects workflow, huge ecosystem, simple play, segment and loop control |
| Interactive or stateful character and illustration: hover, press and drag reactions, blended states, data-driven visuals, game-like UI | Rive | State machines and data binding built into the file, compact binary, runtime control |
| Photographic, 3D-rendered, particle-heavy or long-form content | Video | Lottie and Rive are vector; heavy effects do not survive export |
| A designer must change it without a developer | Lottie (swap the file) or Rive (republish the `.riv`) | Keep a stable file name, artboard names and inputs |

A Lottie or Rive file is not a control. Wrap it in a real `<button>` or other element with an accessible name; the animation only decorates the state.

Without After Effects, build token-driven portable Lottie (logo reveal, loader, icon morph, underline sweep) with `lottie_build.py` and check any Lottie with its `validate` command; see the [production pipeline](production-pipeline.md).

## Lottie: authoring in After Effects

- Export with the Bodymovin extension (the original exporter by Hernan Torrisi) or the LottieFiles After Effects plugin, which also exports dotLottie.
- Build with shape layers. Convert Illustrator layers with "Create Shapes from Vector Layer", then delete the source layer.
- Use parenting, nulls and precomps freely; they export. Keep layer counts low, because each layer costs at runtime.
- Name layers and markers clearly. Markers export and players can play named segments (for example `intro`, `loop`, `outro`).
- Text: convert to shapes for fixed text. Live text needs glyphs or fonts available to the player and is limited on mobile players.
- Keep the composition at the delivery frame rate (30 or 60fps for UI). File size comes mostly from keyframe and path data, not the frame rate.
- Do not bake expressions to keyframes on every frame, and do not embed raster images unless you must. Both inflate the file.

## Lottie: what survives export

Summarized from the Lottie supported-features matrix (airbnb.io/lottie) and LottieFiles' After Effects support guide; re-check them for the player version you ship.

| Feature | Android | iOS | Web (lottie-web) |
| --- | --- | --- | --- |
| Shape layers, fills, strokes, gradients | Yes | Yes | Yes |
| Trim paths | Yes | Yes (one combination differs between the Core Animation and Main Thread renderers) | Yes |
| Masks: add, subtract, intersect | Yes | Yes | Add and subtract; intersect not supported |
| Alpha mattes / luma mattes | Yes / No | Yes / No | Yes / unclear |
| Repeaters | Yes | Core Animation renderer only | Yes |
| Merge paths | Yes | No | No |
| Time remap, parenting, precomps | Yes | Yes | Yes |
| Expressions | No | No | Partial |
| Layer effects (fill, stroke, tint, tritone) | No | No | Yes |
| Drop shadow, Gaussian blur | Drop shadow and blur on recent versions | Drop shadow | Unclear |

Plan on these not surviving: 3D layers and cameras, adjustment layers, most blur, distortion and particle effects, third-party plugins, motion blur and complex expressions. Fake depth with scale and parallax; fake blur with feathered shapes or opacity.

## dotLottie and players

- **dotLottie (`.lottie`)** is a zipped container: one or more animations, their assets, themes (color sets you switch at runtime) and state machines (click, hover and scroll interactions defined in the file). LottieFiles claims large size reductions over raw JSON; measure your own files.
- The Lottie format specification is maintained by the Lottie Animation Community, which publishes the format spec independently of any one player.
- **Players:** `lottie-web` (SVG, canvas and HTML renderers; the light build drops expressions and keeps only SVG), `@lottiefiles/dotlottie-web` (a WebAssembly player built on the ThorVG engine, rendering to canvas), `lottie-ios`, `lottie-android`, `lottie-react-native`, and the pure-Dart `lottie` package for Flutter.
- Load players lazily. Do not ship a player on pages that show no animation.

File-size budgets (a common starting point; measure the transferred bytes after compression):

| Use | Target |
| --- | --- |
| Icon or micro-interaction | 10-30KB |
| Spot illustration, empty state, success | 30-100KB |
| Onboarding or hero illustration | 100-250KB |
| Anything larger | Reconsider: video, a still image or Rive |

Runtime rules: pause offscreen, stop after a fixed number of loops for decorative pieces, show a static frame under reduced motion (`goToAndStop` on the final or most meaningful frame), and set `aria-hidden="true"` on decorative players. Informative animations need a text alternative.

## Rive: concepts

- **Editor:** design and animate modes in one tool; the output is a compact binary `.riv` file containing artboards, timelines and state machines.
- **State machines:** layers of states (timelines or blend states) connected by transitions with conditions. One state machine can run several layers at once, for example a body layer and an eyes layer.
- **Inputs (legacy):** boolean, number and trigger values that the runtime sets to drive transitions. Rive now documents inputs as legacy.
- **Data binding (current):** view models with typed properties that you bind to almost any editor property and read or write from code. Rive recommends it for new work over inputs and runtime event listeners, and the editor can convert inputs to view models.
- **Listeners and events:** listeners handle pointer interaction inside the file (hover, press, drag on hit areas); events report moments back to the host app (for example "celebration finished").
- **Text, layouts and audio:** runtime-editable text runs with embedded fonts, responsive layouts, and audio events. Check each runtime's support table.
- **Runtimes:** web (`@rive-app/canvas` and `@rive-app/webgl2`), React (`@rive-app/react-canvas`), React Native, iOS and macOS, Android, Flutter, C++, Unity and Unreal. The Unreal runtime was paused for a rewrite as of 2026. The runtimes are open source; the editor is a paid product with a free tier. Verify plans and runtime licenses at rive.app.

Web example using the current data-binding approach (property names come from the `.riv` file):

```js
import { Rive } from '@rive-app/canvas';

const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const rive = new Rive({
  src: '/motion/mascot.riv',
  canvas: document.querySelector('#mascot'),
  stateMachines: 'Main',
  autoplay: !reduce,
  autoBind: true,
  onLoad: () => {
    rive.resizeDrawingSurfaceToCanvas();
    const happy = rive.viewModelInstance?.boolean('isHappy');
    if (happy) happy.value = true;
  },
});
```

Check the runtime's current API for data binding before copying this; method names have changed across releases.

## Lottie or Rive

| Question | Lottie | Rive |
| --- | --- | --- |
| The team already animates in After Effects | Strong fit | Learning curve |
| Needs states, blending or real-time reactions | dotLottie state machines cover simple cases | Strong fit |
| Driven by app data (progress, score, user name) | Limited | Data binding |
| Shared with marketing video | The same After Effects source | Separate source |
| File size for an interactive character | Grows with every state | Usually smaller |
| Ecosystem of ready-made assets | Very large (check each asset's license) | Smaller community library |

## Handoff checklists

Designer to developer (Lottie):

- [ ] Exported with the plugin version noted; tested in the target player, not only the LottieFiles preview
- [ ] Composition size, frame rate, duration and markers or segments listed
- [ ] No unsupported features (check the table above); no embedded rasters unless agreed
- [ ] Transferred size within budget
- [ ] Loop behavior (count, segment) and the static frame for reduced motion named
- [ ] Colors mapped to tokens, or a dotLottie theme provided for dark mode
- [ ] Rights recorded for every third-party asset (the LottieFiles public license and Lordicon terms differ; see [motion recipes](../../../library/MOTION-RECIPES.md))

Designer to developer (Rive):

- [ ] Artboard, state machine and view-model or input names documented exactly as spelled in the file
- [ ] The state diagram: each state, its trigger and its exit condition
- [ ] Events the app must handle, and their payloads
- [ ] Fit and alignment rules for resizing; minimum and maximum display sizes
- [ ] Reduced-motion behavior: a still state or a paused first frame
- [ ] Runtime and version tested on each target platform

Developer acceptance (both): the wrapping control is keyboard operable with an accessible name; the animation pauses offscreen; there is no layout shift while it loads (reserve the box with `aspect-ratio`); the player is lazy-loaded; and frame timing has been measured on a mid-range phone.
