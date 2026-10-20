# Worked example: neighborhood dental group rebrand

Version-Timestamp: 2026-10-20 02:05:00 UTC

A fictional run of the full workflow, condensed. Use it to calibrate depth and tone, not as a template to copy.

## Brief as received

> "Bright Path Dental has 4 clinics in San Antonio and is opening 8 more. We need a new identity and website. Lots of our patients are families and many prefer Spanish. The current brand looks like every other dentist."

## 1. Intake

| Variable | Value | Status |
| --- | --- | --- |
| Objective | New-patient bookings as clinics open; recognizable across 12 locations | given + inferred |
| Deliverable / channel | Identity + marketing website with online booking | given |
| Industry | `industry.healthcare-provider` | given |
| Market | `market.united-states` + `market.us-hispanic-puerto-rico-caribbean` (bilingual EN/ES, Texas) | inferred from "prefer Spanish" |
| Audience | Parents 28-45 booking for families; anxious adult patients | inferred |
| Archetype | `archetype.caregiver` primary, `archetype.everyperson` secondary | inferred |
| Tier | `tier.mid-market` | unknown (asked) |
| Locks | Name "Bright Path" stays | asked |
| Constraints | WCAG 2.2 AA, HIPAA-aware booking, bilingual site | inferred |

Questions asked (3): name lock (kept), price position (mid-market confirmed), Spanish scope (full bilingual site, not just a toggle on key pages; recommended and accepted).

## 2-3. Atlas and category scan

`python3 atlas.py query "dental clinic families bilingual spanish texas healthcare rebrand website"` returned `industry.healthcare-provider`, `market.us-hispanic-puerto-rico-caribbean`, `channel.marketing-website`, `archetype.caregiver`.

Scan of 9 local and national competitors: **crowded** = teal or blue, tooth icons, smiling-family stock photography, "Your smile is our priority"; **open** = warmth and neighborhood belonging, genuinely bilingual voice, transparent pricing and insurance info.

## 4. Directions

| | Position | Recipe | Insight |
| --- | --- | --- | --- |
| **A "Clean Bright"** | Category-expected | `style.clinical-calm` + `style.corporate-modern`, caregiver, mid-market | Meets expectations with better craft and accessibility |
| **B "Casa"** | Adjacent (neighborhood hospitality) | `style.mid-century-modern` warmth, everyperson + caregiver, bilingual-first voice | Families choose a dentist like a neighborhood place, not a hospital |
| **C "Smile Club"** | Category-breaking | `style.playful-bubbly` + `style.bold-geometric-sport`, jester, saturated color | Kids love it; turns visits into a club |

Distinctness: A-B differ on palette (cool vs warm), imagery (photo vs illustration), voice (clinical vs neighborly), type (grotesque vs humanist serif display): 4 of 6. A-C: 5 of 6. B-C: 3 of 6 (palette saturation, motion, voice). All pass.

## 5. Stylescapes

Three pages from the template; the B hero showed a bilingual headline set as equals ("Your neighborhood dentist. / Tu dentista del barrio."), warm terracotta and cream, and illustrated street-corner clinic facades unique to each location.

## 6. Scores (regulated preset; produced with `scripts/score_directions.py`)

| Criterion (weight) | A | B | C |
| --- | --- | --- | --- |
| Objective fit (15) | 3 | 4 | 4 |
| Audience fit (15) | 4 | 5 | 3 |
| Differentiation (10) | 2 | 4 | 5 |
| Brand truth (10) | 3 | 4 | 3 |
| Accessibility (20) | 5 | 4 | 3 |
| Feasibility (10) | 5 | 4 | 4 |
| Scalability (5) | 4 | 4 | 3 |
| Longevity (5) | 4 | 4 | 2 |
| Risk (10) | 5 | 4 | 3 |
| **Weighted** | 3.95 | **4.15** | 3.40 |

Sensitivity: lowering differentiation by 10 points makes A and B tie at 4.17. So the decision rests on one question for the client: is standing out from the 9 competitors a goal for the expansion?

## 7. Recommendation (as presented)

**B "Casa".** It is the only direction that turns the bilingual audience into the brand idea instead of a translation task, and per-location illustrated facades scale naturally to 12 openings. **Runner-up:** A, if the client decides differentiation matters less than maximum clinical reassurance. **Risks:** illustration cost per location (mitigate with a modular facade kit); warm palette must keep 4.5:1 text contrast (checked in tokens lint). **Next:** refine B into tokens, logo territories within B, and the booking flow.
