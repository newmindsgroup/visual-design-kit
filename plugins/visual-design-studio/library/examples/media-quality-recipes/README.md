# Prepared media recipe exercises

Version-Timestamp: 2026-09-11T21:08:20-04:00

Parent: [media workflow](../../MEDIA-QUALITY-WORKFLOW.md). Use the [packet](../../templates/media-quality-packet.md) and [rubric](../../templates/media-quality-rubric.md).

These are prepared acceptance cases, not generated or tested recipes. Use fictional or authorized references and an explicitly bounded generation budget.

## Glass product, portrait still

Brief: fictional refillable bottle on a 1080 by 1920 screen. Preserve supplied bottle proportions and label. Generate an atmospheric background with left-side soft light and an uncluttered upper copy zone; composite the exact bottle and editable headline separately. Compare glass edges, reflections and grounding. Reject invented label text, distorted cap or background contrast that overwhelms the message. Deliver layered master, portrait export and contact sheet.

## Textile detail, narrow strip

Brief: 1920 by 360 content strip using an authorized textile detail. Contrast with the portrait case: use a horizontal detail composition and separate editable message zone, not a stretched bottle layout. Preserve weave scale and color; inspect aliasing and excessive sharpening at native size. No absent product claims may be invented. Deliver original crop, composition map and strip export.

## Quiet product motion

Brief: silent six-second 1920 by 1080 loop. Use an exact fictional packshot on an original background; test deterministic parallax before generative product motion. Keep product geometry and copy stable. Inspect complete playback and last-to-first join for flicker, morphing and jump. Six seconds is this fixture's requirement, not a universal dwell-time rule. Deliver timeline, rendered loop, playback evidence and unresolved device checks.

## Adversarial checks

An attractive candidate with altered packaging must fail. A provider that lacks the requested edit control must not receive invented flags. An uncertain job must not be blindly resubmitted. A score without viewed media stays unobserved. An executed portrait case alone cannot promote the strip or motion recipe to tested status.

## Display detail acceptance extensions

Version-Timestamp: 2026-09-11T21:22:42-04:00

The still case must include zone mapping and a second format with long copy. A layout that fits only by unreadably shrinking type fails; record a layout/copy exception instead.

The motion case must include a reviewed still fallback. Simulate a missing or corrupt clip and verify the chosen runtime displays the current fallback. Compare compressed and master output, then record real hardware playback as pending if unavailable.

### Touchscreen sequence

Use the fictional product to define attract, entry, product exploration, warning, extension, reset and fresh attract. First touch must produce immediate feedback with explicit dismiss-versus-select semantics. Verify repeat taps cannot create duplicate navigation, media failure does not block controls, a late media response does not replace active navigation, extension preserves choices, and reset clears them before a new session. A late old-session response must be ignored. This is a prepared scenario, not a functioning touchscreen application.

### Cross-channel review

Compare the still, loop, fallback and touchscreen together using a manifest of exact versions. Reject altered product appearance, competing headline hierarchy, outdated fallback offers and inconsistent type treatment. Keep evidence for each medium; one attractive still cannot certify the loop or interaction.

Use the [detail checklist](../../templates/display-production-details.md).

## Ordered stage routes

Version-Timestamp: 2026-09-11T21:30:44-04:00

[Route data](routes.json) supplies explicit stage selections for still, motion and touch exercises. ChatGPT Images is the selected example route; substitute the chosen authorized CLI for that stage only. Do not select all providers by default. Each stage uses catalog prerequisites as information requirements. Reuse accepted files when their hashes, scope and assumptions remain unchanged; loading prerequisite instructions does not require regenerating assets.

Run catalog planning separately for each stage. Flattening the entire route into one prerequisite list would lose the second quality review after finishing. The route data does not execute tools, make approvals or enforce a runtime gate. At each transition, record produced files and observed checks. Missing required evidence or failed product invariants prevents promotion. Generation and real hardware execution remain pending.

## Executed local session model

Version-Timestamp: 2026-09-11T21:36:56-04:00

[Pure session model](touch-session/session.mjs) and [six behavior tests](touch-session/session.test.mjs) implement the touchscreen scenario's bounded event semantics. Run `node --test examples/media-quality-recipes/touch-session/session.test.mjs`. First entry dismisses only; repeated entry does nothing. Session IDs reject old media responses. Timeout epochs reject a stale expiry after extension. Reset clears choices. Media failure selects a fallback state without blocking navigation.

All six tests pass. Initial missing-module failure is retained in private/touch-session/red.log, results in private/touch-session/results.log. This is executable logic evidence only: no UI, real timers, fallback image, device, transaction or media generation is implemented by this fixture. The model accepts internal application events; it is not an untrusted-input API. Actual request cancellation and same-session request ordering require the eventual adapter.

Version-Timestamp: 2026-09-11T21:41:30-04:00

The [visual prototype](touch-session/index.html) now connects the state model to DOM controls and demonstration timers. Serve this folder locally on port 17662. Run [browser checks](touch-session/browser-checks.mjs) with a dedicated unsigned-in debugging Chrome on port 17661 and EVIDENCE_DIR set to a private output folder. Sixteen assertions cover desktop/mobile state and overflow. The visible fallback is a schematic, with a simulated failure button; a real media/player adapter remains unimplemented.
