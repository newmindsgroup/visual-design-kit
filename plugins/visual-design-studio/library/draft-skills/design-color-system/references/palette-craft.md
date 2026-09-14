# Palette construction and interaction

Version-Timestamp: 2026-09-11T19:32:14-04:00

Start with approved colors or an explicitly provisional exploration. Present identical composition, imagery and copy across options. Compare hue, perceptual lightness and chroma separately; neutrals and large surfaces often determine the overall impression more than accent swatches. Test color adjacency, transparency and image backgrounds in actual composition. Do not infer a universal color meaning from a hue name.

For perceptual scales use an appropriate perceptual space such as OKLCH when the implementation supports it; choose lightness/chroma progression by intended role, inspect gamut mapping and verify exported sRGB values. Even perceptual-space intervals need visual review. Record source-space coordinates, mapped values and acceptable use; do not silently replace approved brand primitives.

Map primitives into role/theme/state tokens. Extend functional success/error/focus colors separately from the brand palette when needed. Inspect links, selected states, charts, gradients and photography. Test categorical distinguishability and ordered-data lightness without relying only on hue. Forced-color and non-color cues remain separate checks.

The offline checker handles opaque sRGB arithmetic only. Alpha, video, gradients, wide gamut and printed output require their own compositing/proof method. A changed token invalidates every dependent pair and visual artifact; changed font size/weight can invalidate a contrast target even when colors are unchanged. Keep token authority and evidence version binding explicit.

Use the [craft laboratory](../../../CRAFT-LAB.md) for bounded comparison tools and evidence limits.
