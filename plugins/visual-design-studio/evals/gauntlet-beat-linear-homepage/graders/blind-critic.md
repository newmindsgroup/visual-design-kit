---
type: llm
weight: 3
---

Passes only if the critic is separate from the builder and the comparison is blind and binary:
- A separate critic (a subagent such as the kit's `art-director`, a fresh session or a person) with fresh context judges each round; the builder never judges its own work. In a single context, the critic pass is written as a separate role without access to the builder's reasoning, and the response admits this is weaker than a truly separate critic.
- Blind: logos, wordmarks and product names stripped from both captures, same crop and viewport, A/B order randomized each round, and the critic is not told which is ours.
- Binary: the critic says which is better, A or B, and names the single biggest gap; no scores out of 10.
- Each round's pick and gap are recorded in a log.

Fails if the same agent builds and scores, or if the critic gives numeric scores instead of a pick.
