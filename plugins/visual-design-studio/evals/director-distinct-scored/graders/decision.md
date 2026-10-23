---
type: llm
weight: 1
---

Passes only if the response does both:
- Includes a sensitivity check: says whether a plausible change in a weight would flip the winner, naming the criterion (for example "B wins unless differentiation matters less than accessibility", or "B wins if audience fit rises to 35%").
- Recommends one winner, names a runner-up, and says what would change the decision.
Fails if there is no sensitivity statement tied to a named criterion or weight.
