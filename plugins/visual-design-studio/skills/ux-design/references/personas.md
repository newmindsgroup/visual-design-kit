# Personas

Version-Timestamp: 2026-10-20 02:04:32 UTC

A persona is a decision tool: it should make a team choose differently. Build personas from behavior and goals, label how much evidence stands behind each one, and never invent a person to make a deck look researched.

## Proto-persona versus research persona

| | Proto-persona | Research persona |
| --- | --- | --- |
| Source | Team knowledge, stakeholder interviews, existing data | Interviews, field studies, surveys with real participants |
| Label | "HYPOTHESIS: not validated" at the top | "Research-based: [study IDs, dates, n]" |
| Time to build | 1-3 hours workshop (Jeff Gothelf, *Lean UX*) | 2-6 weeks including research |
| Good for | Aligning a team, choosing whom to recruit, early concepts | Prioritization, design decisions, recruiting quotas, messaging |
| Not good for | Claims about real users, final prioritization | Questions it was not researched for |
| Validation plan | Required: which research will confirm or kill each assumption | Refresh trigger: major market or product change, or 12-18 months (convention) |

Treat every unvalidated field as a hypothesis with a test attached. A proto-persona that is never tested becomes a stereotype with a name.

## Proto-persona canvas

```text
HYPOTHESIS: not validated. Owner: <name>. Created: <date>. Validate by: <study, date>.

Role-based name:       "Operations lead at a 20-person agency" (not a stock photo and a first name)
Context:               Where, when, devices, constraints, accessibility needs if known
Behaviors:             What they do today (tools, frequency, workarounds)
Goals and jobs:        Functional, emotional, social
Pain points:           Observed or assumed (mark which)
What would change our design: The 2-3 decisions this persona should inform
Assumptions to test:   A1 ..., A2 ..., A3 ...
```

## Building research personas from behavioral variables

Alan Cooper's method (*About Face*) still works best:

1. **List behavioral variables** that differ across participants: frequency of the task, expertise, motivation, attitude to risk, team size, budget authority, channel preference, accessibility needs.
2. **Place each participant** on each variable's spectrum (P01 to P12 along "plans weekly ... reacts daily").
3. **Find clusters**: participants who sit together on 5 or more variables form a pattern.
4. **Describe goals** for each pattern: end goals (what they want to achieve), experience goals (how they want to feel), life goals (longer-term aspirations, only when they affect design).
5. **Choose types**: one primary persona per interface (if satisfied, others are not dissatisfied), secondary personas with additional needs, and a negative persona (who the product is deliberately not for).
6. **Add narrative last**, only from evidence. Quotes must be real and attributed to a participant ID.

Aim for 3-5 personas. More than 6 usually means the segments are demographic, not behavioral.

## Fields for screen and product work

| Field | Contents | Evidence status |
| --- | --- | --- |
| ID and version | `PER-02 v1.1` | n/a |
| Role-based name | "First-time home buyer" | n/a |
| Status | Proto-persona hypothesis, or research-based for a stated scope | Required |
| Context of use | Environment, devices, connectivity, time pressure, interruptions | Observed / inferred / assumed |
| Goals and jobs | Top 3 jobs as job stories | Observed / inferred / assumed |
| Current behavior | Tools, steps, workarounds, frequency | Observed / inferred / assumed |
| Pain points | Ranked, with participant counts | Observed / inferred / assumed |
| Decision criteria | What makes them choose or switch | Observed / inferred / assumed |
| Functional needs | Vision, hearing, motor, cognitive, language, literacy | Observed / inferred / assumed |
| Vocabulary | Words they use for key concepts | Observed |
| Quotes | Verbatim, with participant ID | Observed only |
| Design implications | What the team should do differently | Derived |
| Sources | Study IDs, dates, sample | Required |

For client projects that need the complete record, use the deep schema: the [persona build skill](../../../library/draft-skills/design-persona-build/SKILL.md) with its [118-field template](../../../library/templates/persona.md). It covers bilingual labels, the W01-W35 components and traceability from need to requirement to acceptance criterion.

## Inclusive personas

- Include functional needs in every persona rather than one "accessibility persona".
- Microsoft's Inclusive Design persona spectrum: a need can be permanent (one arm), temporary (arm injury) or situational (holding a baby). Designing for the permanent case serves all three.
- Represent assistive technology use, low bandwidth, older devices, shared devices and low literacy where research shows them.
- Avoid protected traits (race, religion, health, sexuality) unless the research question needs them and participants consented to that use.

## B2B personas

Separate the roles in a buying committee: economic buyer (budget), champion (pushes the purchase), end user (daily use), admin (setup, security, billing), and blocker (security, legal, procurement). Each needs different content and different screens. Query `audience.b2b-buying-committee` in the atlas for defaults.

## Using personas

- **Recruiting**: screeners and quotas map to persona variables.
- **Design reviews**: walk each key flow as the primary persona, then as a secondary persona with different functional needs.
- **Prioritization**: score features by persona and job importance.
- **Content**: vocabulary and reading level come from the persona's evidence.
- **Measurement**: segment analytics and SUS results by persona where you can identify them.

## Common failures

- Demographic personas ("Sarah, 34, loves yoga"). Fix: behavioral variables and goals; age only if it changes the design.
- Stock portraits that imply race, age or gender the research did not establish. Fix: role-based illustrations, initials or no image.
- Invented quotes. Fix: verbatim quotes with participant IDs, or no quotes.
- Personas nobody uses. Fix: tie each persona to 2-3 named decisions and put them in the design review template.
- One persona per stakeholder request. Fix: merge segments that do not change the design.

AI can draft a proto-persona from existing data in minutes. Label it a hypothesis, list its assumptions, and plan the research that will test them.
