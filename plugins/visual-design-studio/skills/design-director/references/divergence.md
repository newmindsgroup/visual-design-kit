# Divergence: building directions that are actually different

Version-Timestamp: 2026-10-20 02:05:00 UTC

The value of exploring is the spread. Three directions that share a type classification, palette temperature and layout pattern give the client one choice in three costumes. Build directions from deliberate positions, then prove they differ.

## Direction positions

Pick 3-5 positions. Always include the first three for identity and flagship work.

| Position | Question it answers | Typical source |
| --- | --- | --- |
| **Category-expected** | What if we meet expectations and win on craft? | Industry entry *Recommended directions: Category-expected*; the crowded corner of the scan, executed better |
| **Adjacent** | What if we borrow credibility from a neighboring category? | Industry entry *Adjacent*; e.g., a bank borrowing from editorial publishing, a clinic from hospitality |
| **Category-breaking** | What if we deliberately stand apart? | Industry entry *Category-breaking*; the open space in the scan |
| Competitor-contrast | What is the opposite of the leader? | Invert the leader's coded axes where the audience allows |
| Audience-led | What would the audience design for itself? | Audience entry *Visual tone*; culture the audience participates in |
| Heritage or place | What does the origin or locale offer? | Market entry; founder story; materials and craft of the place |

## Recipe for one direction

```markdown
### Direction B: "Ledger" (adjacent: financial editorial)
- Atlas: style.editorial-magazine + style.swiss-international, archetype.sage, tier.premium, channel.native-app
- Insight: our users read the FT and Morning Brew; they trust analysis more than reassurance.
- Type: Newsreader display (serif, optical sizes) + Inter Tight UI; scale 1.333; tabular numerals everywhere.
- Color: warm paper #F4F1EA, ink #1A1A1A, signal green #0B7A4B (accent ~8%), alert vermilion #C2410C.
- Layout: 12-col asymmetric grid; big numerals as heroes; hairline rules; no cards.
- Imagery: data illustrations and charts; no stock people.
- Motion: 200ms standard ease; numbers count up once; no parallax.
- Voice: precise, unhurried, explanatory ("Here is what changed this week").
- Risk: may feel dense to casual users; mitigate with progressive disclosure.
```

Fill a recipe from the atlas entries' *Token recipe* tables, then adjust to the brief. Name each direction with a short evocative word so people can discuss it ("Ledger", "Block Party", "Tide").

## Distinctness test

Compare every pair of directions on six axes. Each pair must differ clearly on **at least three**:

1. Type classification and scale contrast
2. Palette temperature, saturation and light/dark
3. Layout logic (grid, density, symmetry)
4. Imagery medium (photo, illustration, type-only, 3D, data)
5. Motion personality (still, precise, springy, cinematic)
6. Voice (formal-casual, serious-playful)

If a pair fails, move the weaker direction to an unused position or swap its style ID. Record the test as a small table in the presentation; it shows the client the exploration was real.

## Combining atlas entries

- Run `python3 ../../../library/scripts/atlas.py combine <style> <industry> <audience> <archetype> <tier> <channel>`.
- **Conflicts** (an entry's `avoid_with` lists another) are not vetoes; they are risks to resolve on purpose. Example: `style.neo-brutalist` with `audience.older-adults` can work if contrast, size and targets follow the audience defaults while keeping the bold shapes.
- **Audience and accessibility defaults beat style defaults.** When a style says 14px body and the audience entry says 18px, use 18px and adapt the style.
- **Market rules beat style rules.** RTL, script line-heights and local formats are not stylistic choices.

## Guardrails

- Every direction must be something you would be proud to deliver; "the safe one" is still excellent.
- No direction may rely on the generic AI look (see the `design-critique` skill's `references/ai-tells.md`) unless the brief explicitly calls for it.
- Do not make one direction deliberately weak to steer the client. If you have a favorite, say so in the recommendation.
