---
name: design-motion-effects
description: Select and specify display motion graphics, kinetic typography, UI animation and scroll effects by purpose, with choreography, accessible alternatives, interruption behavior and target-specific verification.
---

# Motion and effect design

Version-Timestamp: 2026-09-16T18:27:08.062526-04:00

Status: authored instructions; effect recipes are unverified until implemented and tested.

Read [decision ownership](../../DESIGN-CRAFT.md), then only relevant [effect recipes](references/effects.md). Existing [media recipes](../../MOTION-RECIPES.md) remain the owner for transcript inserts, color grading, clip transitions and generated media provenance. Reuse them rather than duplicating those workflows.

## Establish the job of movement

Inputs: work record and audience context, approved composition/assets, purpose, target medium/runtime, control method, required timing/audio and baseline. Choose functional feedback/orientation, narrative explanation or expressive brand atmosphere. An optional effect must justify its attention and implementation cost. Static is a valid deliberate choice. Do not automatically attach the same entrance animation to every section.

Use timing/spacing and easing to shape speed; staging to establish focus; anticipation to prepare a meaningful change; continuity and follow-through to connect related states; rhythm and stagger to establish sequence. Arcs, squash/stretch, exaggeration, secondary action and appealing silhouettes can support expressive animation but are not mandatory UI behaviors. Preserve exact logos/product geometry unless distortion is authorized. Immediate feedback and task completion take priority over theatrical delays. Vendor motion principles are examples of brand-specific decisions, not universal easing values.

Distinguish scroll-triggered playback (crossing a threshold starts a time-based animation) from scroll-driven progress (the scroll position controls the animation). Choose native CSS transitions/keyframes, browser scroll/view timelines, Web Animations API or an existing vetted library based on required control and actual target support. Use a native editing/timeline tool for rendered motion graphics where an editable timeline is required. A video or Lottie file is not a DOM interaction or editable timeline.

## Specify before implementation

Fill the [motion specification](../../templates/motion-spec.md) with named start/end states, trigger or timeline range, animated properties, duration/curve or progress mapping, repeat/reverse/interrupt rules, related elements, audio and ownership. Choose values from the actual scene and audience; do not copy a vendor's timings wholesale. Add a reduced/static version conveying the same facts. Specify no-JS, unsupported API, slow-loading and failed-media behavior for web where relevant. Progressive enhancement must leave essential content available even if animation initialization never runs.

Define resize/orientation, route change, rapid repeat, back navigation, keyboard focus, touch and offscreen/tab-hidden behavior. Pinning must not trap scrolling or hide focused content. Text splitting must preserve one coherent accessible reading sequence and selection/copy behavior. Motion cannot be the only source of a factual result. A decorative pointer effect must not remove the normal cursor or imply unusable controls.

## Acceptance

Implement only through an available authorized route. Inspect normal/reduced motion, static fallback, appropriate desktop/mobile and actual input methods. For web, record the target browser/device and measure frame timing/dropped frames, interaction latency, main-thread work, layout shift and asset bytes against project-set budgets. Do not assume compositor-friendly properties guarantee smoothness. Check teardown/reinitialization and whether animations resume incorrectly after navigation.

WCAG interaction-animation disablement is Level AAA; pause/stop/hide for qualifying automatically moving content is a separate Level A requirement. Flash limits are separate again. Use the research capability to verify the applicable official WCAG criteria and platform motion guidance for the selected target, and record source URLs, versions, exceptions and test evidence. Hold compliance claims when that evidence is missing; reduced motion does not alone establish compliance. Never make long auto-motion compulsory merely because it is decorative.

For rendered media, inspect full playback, loop seams, pacing, text-reading time, audio/caption synchronization and output codec/frame rate on the intended player. Route native source and export verification to production/delivery. Update recipe status only with the exact tested version, evidence and coverage; one browser render is not universal support.


Version-Timestamp: 2026-09-11T23:21:42-04:00

## Display specialist extension

Version-Timestamp: 2026-09-11T09:45:01-04:00

For retail displays, billboards and touchscreen attraction, use the [display workflow](../../DISPLAY-WORKFLOW.md) and operator restrictions. Define a motion identity: rhythm, easing, entry/exit, scale, transitions, logo invariants and approved variations. Reuse brand rules; infer only provisionally when absent.

Sequence concept, storyboard and style frames, timed animatic, editable production, export and actual playback. Each scene records message, source assets, start/hold/end timing and transition; test reading time rather than copy a fixed duration. Compare still and moving variants. Kinetic type must preserve readable holds and balanced lines; do not animate every word simply to add activity.

Choose applicable 2D/3D, masking, compositing, product-image movement, character rigs, lighting and material techniques from the actual brief. Preserve product/character geometry, source provenance and rights. A generated clip does not establish an editable rig or factual product demonstration. Specify camera/parallax depth and focal hierarchy without changing approved product attributes.

For loops allow entry midway, maintain message anchors and inspect seam continuity, repeated exposure and silent comprehension. Separate sound design from essential meaning, provide captions where needed, and verify venue audio restrictions and rights. Coordinate multiscreen timelines, seam-safe elements and loss-of-sync fallbacks. Touch attraction yields immediately to active interaction. Export static/reduced alternatives when appropriate, and hand assets and specification to display production for actual player checks; evaluation consolidates readiness.

For every rendered display loop, including passive video and LED walls, specify and evaluate flash frequency, affected area, luminance change and saturated-red transitions using an applicable recognized flash-analysis method. Record method, thresholds, tested file and results; do not infer safety from frame rate or a casual preview. Unchecked flashes or strobes hold playback acceptance; prefer a nonflashing alternative. Motion owns specification and animation assets; production owns technical exports/player checks and evaluation owns acceptance.

## Rendered calibration

Version-Timestamp: 2026-09-16T18:06:33.096655-04:00

Use the [shared fictional collection](../../examples/quality-benchmark/README.md) for comparative quality, rendered typography, precise revision and motion evidence. Inspect its recorded limits; do not inherit its fonts, style or agent review as approval for another brand.
