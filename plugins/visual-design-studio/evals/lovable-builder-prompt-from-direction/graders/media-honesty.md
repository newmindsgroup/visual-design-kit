---
type: llm
weight: 2
---

Passes only if the response handles the missing media honestly:
- Does not invent image or video URLs and tells the builder not to use stock or placeholder photos.
- Specifies a type-led hero (for example a large Fraunces headline, grain, a static light falloff or an inline SVG mark) or clearly declared stand-in slots that the client will replace with real, rights-cleared photography.
- Mentions that real food or venue photography needs to come from the client (or a commissioned shoot), with rights.

Fails if the prompt includes made-up asset URLs or asks the builder to "add beautiful food photos".
