---
type: llm
weight: 1
---

Passes only if the response fixes the black logo so it does not vanish on a dark background: a light-on-dark logo swap where `prefers-color-scheme` is supported, AND a fallback for clients that ignore it (a transparent PNG with a light outline or glow, or the logo inside a padded light container or contained shape).
Fails if it offers only the swap with no fallback for inverting clients, or only says "use a transparent PNG".
