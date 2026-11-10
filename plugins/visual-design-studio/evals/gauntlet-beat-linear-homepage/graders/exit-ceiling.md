---
type: llm
weight: 2
---

Passes only if the exit rule is a blind win or a cost or time ceiling:
- Exits per piece when the blind critic picks ours (optionally confirmed by a second round or the name-swap test).
- Because this is paid client work, sets a spend or time ceiling: asks for one once, or states a concrete default it will use (for example 60 minutes) despite the user's "don't stop to ask"; at the ceiling it stops and reports where each piece stands rather than looping silently.
- Does not use a fixed number of rounds as the exit.
- After the loop, re-scores the page against the normal critique rubric or delivery checks before calling it done. This point is a plus, not required.

Fails if it promises to loop indefinitely with no ceiling, or stops after a set number of rounds.
