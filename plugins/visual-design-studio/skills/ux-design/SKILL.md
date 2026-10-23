---
name: ux-design
description: >-
  Load before designing or reviewing any flow, form, onboarding, navigation or content for real users, especially
  low-literacy, older, neurodivergent, child or other specific audiences. Covers research and usability tests,
  heuristic reviews, personas and jobs to be done, journeys and service blueprints, information architecture, UX laws,
  SUS, SEQ and HEART metrics, plain language and reading level, and microcopy and error messages.
license: MIT
metadata:
  version-timestamp: "2026-10-23 11:25:07 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-23 11:25:07 UTC"
---

# UX design

Excellent UX work starts from a decision that evidence can change, uses the cheapest method that answers it, and ends in structures, flows and words that people complete without help. Every claim is labeled observed, inferred or assumed; nothing is invented to look complete.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Qualitative usability round | 5 participants per distinct user group, then fix and retest (NN/g) | 2+ distinct groups: 3-5 each; rare-but-severe tasks: add participants |
| Quantitative usability benchmark | About 40 participants per group (NN/g) | You need a tighter interval: size from the target margin of error |
| Interviews | 5-8 per segment; stop at saturation, often near 12 in total | Very heterogeneous segments or markets: more per segment |
| Card sort / tree test | Open sort 15-20 people; tree test about 50 per tree variant (30 minimum) | Several audiences with different mental models: per audience |
| Survey | About 385 completes for +/-5% at 95% confidence; about 100 for +/-10% | Comparing segments: that n per segment |
| Expert review | 3-5 evaluators, Nielsen's 10 heuristics, severity 0-4 | Solo or AI review: label it "expert inspection", never user evidence |
| Satisfaction | SEQ after each task, SUS at session end (68 = average) | Very short intercept: UMUX-Lite |
| Response time | 0.1 s feels instant, 1 s keeps flow, 10 s holds attention; feedback within 400 ms | Long jobs: progress, cancel and background completion |
| Hierarchy | Broad and shallow: 5-9 top-level groups, 3 levels or fewer for most sites | Large catalogs: faceted navigation plus search |
| Reading level | Grade 6-8 for consumers; GOV.UK writes for a reading age of 9 | Experts: keep precise terms, define each once |
| Sentences | Average 15-20 words; split anything over 25 | Legal text that must be verbatim: add a plain summary above it |
| Personas | 3-5 behavioral personas; proto-personas labeled HYPOTHESIS | One clear audience: one persona plus JTBD statements |
| Flow coverage | Every flow: entries, happy path, alternatives, errors, empty, cancel, recovery, exit | Never relax |

## Workflow

Paths in commands are relative to this skill's directory; resolve them to absolute paths before running.

1. **Frame the decision.** Write what will change depending on the answer, then 3-5 research questions. A question no answer could change is cut.
2. **Use existing evidence first.** Analytics, search logs, support tickets, reviews, sales notes, prior studies, competitor flows. Record each source with an ID and date.
3. **Pick the method and size the sample** with the matrix in [research methods](references/research-methods.md). Write the plan: questions, method, participants and screener, consent, tasks or guide, analysis, timeline.
4. **Run it honestly.** With no participants available, deliver the protocol plus a heuristic review labeled as expert inspection. Never fabricate participants, quotes, counts or emotions; synthetic users may draft hypotheses only.
5. **Synthesize.** Observation, then insight, then recommendation, each with participant counts ("4 of 5") and severity per [heuristics and laws](references/heuristics-and-laws.md).
6. **Model.** Personas or JTBD ([personas](references/personas.md)), journey map or service blueprint and user flows ([journeys and flows](references/journeys-and-flows.md)), sitemap, taxonomy and labels ([information architecture](references/information-architecture.md)).
7. **Write the words** with [content design](references/content-design.md): labels, errors, empty states, confirmations. Real content goes into wireframes; no lorem ipsum.
8. **Prototype at the lowest fidelity that answers the question**, test it, and measure with [measurement](references/measurement.md): task success, time, errors, SEQ, SUS.
9. **Render and inspect.** Draw flows and wireflows (Mermaid or FigJam), screenshot prototypes at phone and desktop widths, and review them with the `design-critique` skill before sharing.
10. **Hand off** numbered requirements, flows with state IDs and IA to `ui-design`, `web-design` or `native-app-design`, each traced to a finding or a labeled hypothesis.

## Decisions that change the answer

- **Research stage.** Discovery (generative: interviews, field study, diary), design (evaluative: usability tests, tree tests), launch (summative: benchmarks, A/B tests). Do not run an A/B test to answer a "why" question.
- **Audience.** Read the audience entry before designing (without a shell, open it directly): [low literacy](../../library/atlas/audiences/low-literacy-plain-language.md) (grade 5-6 target, one question per screen, icons with words, 18px body, plain-language translations, ISO 24495-1), [older adults](../../library/atlas/audiences/older-adults.md), [neurodivergent](../../library/atlas/audiences/neurodivergent.md), [children under 13](../../library/atlas/audiences/children-under-13.md); others via `python3 ../../library/scripts/atlas.py query "<audience in plain words>"`. Older adults: longer sessions, larger text in stimuli, more recruiting lead time. Children under 13: parental consent plus child assent, short sessions. Low literacy: oral tasks, reading age 9 or lower. Expert power users: realistic data volumes and keyboard paths.
- **Industry.** Health, finance and government add consent, data handling and recruiting constraints (special-category data under GDPR, HIPAA in US healthcare). Query `industry.*` entries for trust signals and regulation.
- **Market.** Moderate in the participant's language; scale responses vary by culture (some markets rate higher or lower overall), so compare within a market, not across. Localize stimuli before testing.
- **Channel.** Websites: tree tests and first-click tests are cheap and decisive. Native apps: test on real devices. Public kiosks and touchscreens: field observation at the site. Multi-touchpoint services: service blueprint.
- **B2B buying committee.** Research buyers, admins and end users separately; their jobs and success criteria differ.
- **Traffic.** Run the power calculation first (baseline 5%, +10% relative lift needs about 31,000 visitors per variant). If the site cannot reach that in 4-6 weeks, use qualitative testing and before/after benchmarks instead of an A/B test.

## Common failures

- Asking people what they want or would do. Fix: ask about the last time they did it, and observe behavior.
- Leading or hypothetical questions ("Would you use a feature that..."). Fix: neutral, past-tense, open questions from the guide template.
- Reporting "80% succeeded" from 5 users. Fix: report "4 of 5" and the adjusted-Wald interval (36-98%) if a number is demanded.
- Personas made of demographics and stock photos. Fix: behavioral variables, goals and evidence links; no portraits that imply traits.
- Journey maps with invented emotions. Fix: plot only evidenced emotions with source IDs; mark gaps as unknown.
- Navigation that mirrors the org chart. Fix: top-tasks research, open card sort, then tree-test two candidate hierarchies.
- NPS used as a usability metric. Fix: SUS, SEQ and task success for usability; NPS only as a relationship metric with its caveats.
- "Submit", "OK" and "Invalid input". Fix: verb-plus-object buttons and errors that say what happened and how to fix it.
- Testing with colleagues or the client team. Fix: recruit real target users with a behavior-based screener.

## References

- [Research methods](references/research-methods.md): method matrix, interview guide, usability testing, card sorting and tree testing, surveys, diary studies, analytics and A/B tests, recruiting, consent, synthesis.
- [Heuristics and laws](references/heuristics-and-laws.md): Nielsen's 10 heuristics with checks, severity 0-4, UX laws with caveats, cognitive load.
- [Measurement](references/measurement.md): SUS scoring and grades, SEQ, UMUX-Lite, task metrics, NPS caveats, Google HEART.
- [Information architecture](references/information-architecture.md): inventories, organization schemes, breadth versus depth, labeling, taxonomy, validation.
- [Journeys and flows](references/journeys-and-flows.md): JTBD, journey maps, service blueprints, user flows, wireflows, state inventories.
- [Content design](references/content-design.md): plain language, voice and tone, microcopy, error messages, readability, localization.
- [Personas](references/personas.md): proto-personas versus research personas, building from behavioral variables, inclusive personas.
- Atlas: `python3 ../../library/scripts/atlas.py query "older adults healthcare portal in the UK"` when audience, industry or market changes the plan; `show <id>` to read one entry.
- Deep process for client projects: [UX architecture](../../library/draft-skills/design-ux-architecture/SKILL.md), [persona build (118-field schema)](../../library/draft-skills/design-persona-build/SKILL.md), [prototype evaluation](../../library/draft-skills/design-prototype-evaluation/SKILL.md), [evidence research](../../library/draft-skills/design-evidence-research/SKILL.md), [content writing](../../library/draft-skills/design-content-writing/SKILL.md), [UX deliverable contracts](../../library/UX-DELIVERABLES.md) and the [UX and content decision card](../../library/knowledge/ux-and-content.md).
- Related skills: `ui-design` for components and states, `web-design` for sites, `design-critique` for the render-and-review loop.

Catalog IDs covered: ux, persona, prototype, research, content
