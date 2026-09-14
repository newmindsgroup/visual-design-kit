# Reusable motion and asset recipes

Version-Timestamp: 2026-09-10 20:14:15 AST

Agent-Attribution: computer=NMG-MBP-M5.local; tool=codex-cli; version=0.149.1; timestamp=2026-09-08 15:19:16 AST

Original conditional extension of [production](draft-skills/design-production-interface/SKILL.md). These are authored methods, not verified automated media-editing features. Use only the selected mode inside the existing design-work record; do not create a new client database or default provider.

## Recipe record

Record recipe ID/version, purpose and audience, allowed uses, source IDs/timecodes, approved reference decision and asset rights. Include aspect ratio, resolution, frame rate/timebase, duration, typography and icon-family IDs, palette roles, composition/focal point, motion timing/easing, color treatment, audio needs, loop endpoints, fallback and output/native formats. State which values are fixed and which are variables. Include the actual tool/model/version, operation allowance and cost result when executed; unknown cost remains unknown.

Reuse a verified recipe and permitted assets before generating again. Tie the recipe to its checked example, input hashes and test evidence. A successful single demonstration is provisional; test another representative input before claiming general reuse. Scope asset search to authorized folders and preserve canonical paths/hashes. Semantic indexing of an entire computer is a separate feature with a separate data boundary, not permission granted by a video.

## Transcript to visual plan

Use actual timed speech and relevant frames. For each proposed insert, record source clip, in/out time, exact statement, communication purpose, proposed graphic, supporting evidence, asset/recipe IDs and acceptance check. Prefer a useful explanation of the statement over decoration. Mark added research as an addition rather than making it appear to have been said in the source.

Verify external numbers against their original dataset, date, population and units. Keep example numbers visibly synthetic. Preserve scales, labels and meaning during chart transitions and make the final values readable without animation. Never use unrelated benchmark values as evidence for model comparisons. If exact word timing matters, obtain and verify word-aligned output from a capable tool. A caption segment or a file described as RTF does not establish word timing.

Have the plan reviewed within the task's approval scope before expensive production. Return proposed inserts or clips when authorized; inserting them into the source video is a distinct edit with source/version and recovery requirements.

## Color treatment and transitions

For a grade, inspect the actual footage and its source color space/transfer function, exposure, skin/product color and intended output. Preserve the source, compare before/after, and distinguish technical normalization from a creative look. Record LUT provenance/expected input, intensity and output settings. A list of sampled colors is not proof of a correct grade. Validate on representative frames and playback; check clipping, banding and unintended identity/product changes.

For transitions, record candidate cut points, incoming/outgoing clip handles, duration, compositing/alpha behavior, audio continuity and the selected asset's permitted use. Scene-detection output is a proposal. Inspect it and render the join before acceptance. Prefer licensed supplied transitions or a simple cut when an invented effect fails; do not add a custom editor merely to imitate the creator's dashboard.

A common grade or motion rhythm can support coherence, but rapid frame changes and film burns are not universal defaults. Check flash exposure and readability. [W3C's flash criterion](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html) applies separately from reduced-motion support. [FFmpeg's filter documentation](https://ffmpeg.org/ffmpeg-filters.html) is an implementation reference when that tool is actually selected, not a claim that a local editing path was tested.

## Icons, Lottie and generated media

Select a coherent icon family with the needed states, sizes, stroke weights and licensing. Separate the animation file from its renderer. Check the actual target's supported Lottie features, external image/font dependencies, performance, reduced/static fallback and export behavior. An animation gallery or a free download does not prove unrestricted redistribution. The [LottieFiles public-file license](https://lottiefiles.com/page/license) and [Lordicon](https://lordicon.com/) are distinct sources; check the exact asset and use.

For image-to-video, keep the approved still, subject geometry, camera intent, aspect ratio, loop start/end and truthful representation explicit. Inspect generated footage for invented features and crop failures. A rotating video does not become an interactive 3D model. Static alternatives remain valid when motion adds no value or generation lacks an authorized route.

For subscription asset libraries, catalog candidates by link and verify the actual project, asset terms and download permissions before use. Keep dated provider observations in the adopting project source register; do not infer bulk-download or redistribution rights from a subscription.

## Acceptance

Use the existing work record, manifest, native reopen/export and delivery checks. Record playback, loop/transition seams, speech synchronization, data integrity, readability, accessibility and rights separately. Test required aspect ratios and actual target consumption; a web preview does not establish a social-platform export or physical-display acceptance. Store a reusable recipe only with its stated evidence level and remaining limitations.


## UI, scroll and expressive effects

For effect selection, choreography and reusable behavior specifications, use the [motion skill](draft-skills/design-motion-effects/SKILL.md) and its 20 authored recipes. This file retains ownership of media inserts, grading, clip transitions and asset reuse. Neither set implies tested runtime support.


Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.149.1; timestamp=2026-09-08 20:43:08 AST

## Continuous media and bounded website embeds

For a continuous journey, specify the intended camera direction, subject geometry, lighting and destination of each move. Choose duration and clip count from the communication need, authorized cost and target playback budget. A single generated take still needs inspection for internal cuts or deformation.

When joining generated clips, inspect both the join and motion throughout each clip. If the selected provider supports endpoint references, test the preceding rendered final frame as the next start reference under the authorized upload scope. Verify the destination account and upload scope explicitly instead of trusting tool defaults. Before the first join, decide how to retain completed clips, account for spent credits and reconcile partial-chain jobs when a later join fails. Inspect the first proposed join before committing the remaining chain budget. Matching input images and similarity scores are clues, not proof that rendered continuity passed. Accept the continuous treatment only when full playback and targeted frame inspection show the planned direction, lighting and subject geometry without unintended cuts, freezes or deformation. Change the shot plan or select a simpler approved treatment when the test fails. Follow the existing [generation contract](MEDIA-GENERATION.md) for job reconciliation and retry limits.

For an existing website, agree the placement and purpose before generating media. Preserve its approved content, tokens and asset rights; limit changes to the agreed placement and record affected files and recovery. Use the [motion skill](draft-skills/design-motion-effects/SKILL.md), an authored draft requiring implementation evidence, for scroll or playback behavior. Check the chosen desktop and mobile crops, text contrast across representative frames, loading and memory budgets, and static/reduced-motion fallback on the actual target. Use the existing [quality checks](QUALITY.md) and [rights contract](REFERENCE-CONTRACT.md). Measure foreground contrast at the least favorable frames against the project accessibility target, and verify the operating-system reduced-motion preference produces the specified fallback. No fixed frame count, clip duration or renderer is a universal acceptance rule.

Source provenance belongs to the source version pinned in the manifest. Endpoint behavior depends on the provider and version and must be verified on the destination.


## Controlled motion acceptance

Inspect both clip joins and within-clip motion. A smooth join can conceal an internal jump. Use a representative successful case and a deliberately faulty join or internal-motion case when verifying an implementation. Record actual playback/frame evidence; no source demonstration or membership entitlement is inherited.
