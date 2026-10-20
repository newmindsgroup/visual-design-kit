# Scoring and recommending

Version-Timestamp: 2026-10-20 02:05:00 UTC

Score directions against the brief, not against taste. The matrix makes the trade-offs visible and lets the client disagree with a weight instead of with you.

## Criteria (score each 1-5)

| Criterion | 5 means | 1 means |
| --- | --- | --- |
| Objective fit | Directly advances the stated business objective and CTA | Unrelated or works against it |
| Audience fit | Matches the audience's needs, expectations and defaults (size, density, tone) | Alienates or excludes the core audience |
| Differentiation | Clearly ownable in the category; passes the name-swap test | Interchangeable with competitors |
| Brand truth | Expresses the archetype, personality and locks credibly | Contradicts the brand or its approved assets |
| Accessibility and inclusion | Meets WCAG 2.2 AA easily with headroom; inclusive imagery and language | Needs compromises to reach AA |
| Feasibility | Buildable in the stack, budget and timeline with available assets | Needs assets, skills or time the project lacks |
| Scalability | Extends across all required channels and future needs | Works only for the hero moment |
| Longevity | Will still feel right in 3-5 years | Tied to a passing trend |
| Risk | Low regulatory, cultural and reputational risk | Likely to cause compliance or cultural problems |

Write one line of evidence per score. A score without a reason is taste.

## Weight presets (adjust to the brief; weights sum to 100)

| Criterion | Default | Launch / campaign | Regulated (health, finance, gov) | Rebrand of established brand | Product UI / design system |
| --- | --- | --- | --- | --- | --- |
| Objective fit | 20 | 20 | 15 | 15 | 15 |
| Audience fit | 15 | 15 | 15 | 15 | 20 |
| Differentiation | 15 | 25 | 10 | 15 | 5 |
| Brand truth | 10 | 10 | 10 | 20 | 5 |
| Accessibility | 10 | 5 | 20 | 10 | 20 |
| Feasibility | 10 | 10 | 10 | 5 | 15 |
| Scalability | 10 | 5 | 5 | 10 | 15 |
| Longevity | 5 | 5 | 5 | 10 | 5 |
| Risk | 5 | 5 | 10 | 0 | 0 |

Weighted score = sum(score x weight) / 100, reported to one decimal on a 1-5 scale.

## Sensitivity check

Shift each weight up and down by 10 points (renormalizing the rest). If the winner changes under a plausible shift, say which criterion decides it: "B wins unless differentiation matters less than accessibility; then A wins." That sentence is often the most useful thing in the presentation.

## Presentation format

```markdown
## Directions
[stylescape thumbnails or links: A "Harbor", B "Ledger", C "Block Party"]

## Distinctness
| Pair | Type | Palette | Layout | Imagery | Motion | Voice |
| A-B | x | x | | x | | x |
...

## Scores (weights: regulated preset)
| Criterion (weight) | A | B | C |
| Objective fit (15) | 4: ... | 5: ... | 3: ... |
...
| **Weighted** | 3.9 | **4.3** | 3.6 |

## Recommendation
**B "Ledger"**: one paragraph on why, tied to the objective and audience.
**Runner-up:** A, if ...
**Risks and mitigations:** ...
**What would change my mind:** ...
**Next step:** refine B into tokens and the first deliverable (see handoff).
```

## Ties and hybrids

- Within 0.2: present both as a genuine choice and name the deciding question.
- Hybrids ("A's palette with C's type") are fine after selection, but re-run the distinctness and accessibility checks on the hybrid; mixtures often lose the idea that made each direction work.
