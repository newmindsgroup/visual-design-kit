---
type: llm
weight: 1
---

Passes only if the response delivers semantic tokens (for example color.bg.canvas, color.bg.surface, color.fg.default, color.fg.muted, color.accent.default) in DTCG JSON ($value/$type) or CSS custom properties, with the dark values, organized so the same semantic names also carry the light theme (light values given, or a light mode block or reference stated).
Fails if it gives only a loose list of hex values without semantic names.
