# Heuristics, severity and UX laws

Version-Timestamp: 2026-10-20 02:04:32 UTC

Use heuristics to find problems fast, severity to decide what to fix first, and UX laws to explain why a design works or fails. None of them replaces watching real users.

## Nielsen's 10 usability heuristics with concrete checks

Source: Jakob Nielsen, NN/g (1994; wording refreshed 2020).

| # | Heuristic | Check each screen and state for |
| --- | --- | --- |
| 1 | Visibility of system status | Every action shows a response within 0.1-1 s; anything over 1 s shows progress; current location is marked (active nav with `aria-current`, breadcrumbs, step "2 of 4"); save state is visible ("Saved 2 min ago") |
| 2 | Match between system and the real world | Labels use the users' words (from interviews and search logs), not internal jargon; dates, currency and units follow the locale; order follows the real-world task |
| 3 | User control and freedom | Undo for reversible destructive actions; Cancel and Back on every step; Esc closes overlays; browser Back works and preserves state |
| 4 | Consistency and standards | One word per concept across the product; platform conventions honored (logo goes home, links look like links); the same component behaves the same everywhere |
| 5 | Error prevention | Constraints instead of warnings (pickers for valid dates, disabled impossible options with a reason); forgiving input formats; confirmation only for irreversible actions |
| 6 | Recognition rather than recall | Options visible rather than remembered; recent items and autocomplete; information from step 1 shown again at step 3; no re-typing of known data (WCAG 3.3.7) |
| 7 | Flexibility and efficiency of use | Keyboard shortcuts, command palette, bulk actions, saved filters and templates for experts, invisible to novices until needed |
| 8 | Aesthetic and minimalist design | Each element supports the current task; secondary content behind progressive disclosure; one primary action per region |
| 9 | Help users recognize, diagnose and recover from errors | Errors in plain language, next to the cause, saying what happened and how to fix it; input preserved; no bare error codes |
| 10 | Help and documentation | Contextual help at the point of need; searchable, task-based docs; help offered in the same place on every page (WCAG 3.2.6) |

## Running a heuristic evaluation

- **Evaluators.** 3-5 independent evaluators. Nielsen's research found a single evaluator finds about 35% of problems and five find about 75%. A review by one person or one AI model is a useful first pass; label it "expert inspection" and follow up with users.
- **Passes.** First pass: walk the key tasks end to end. Second pass: inspect each screen and state against the 10 heuristics plus the WCAG 2.2 AA checklist in `ui-design` [accessibility](../../ui-design/references/accessibility.md).
- **Record each issue** as: ID, location (screen and state ID), heuristic, description, evidence (screenshot), severity, recommendation.
- **Merge** duplicates after independent passes, then have each evaluator rate severity separately and average the ratings.

## Severity scale 0-4

| Rating | Meaning | Action |
| --- | --- | --- |
| 0 | Not a usability problem | None |
| 1 | Cosmetic | Fix if time allows |
| 2 | Minor: causes hesitation or small delays | Low priority; batch into later work |
| 3 | Major: causes errors, large delays or abandonment for some users | High priority; fix before release |
| 4 | Catastrophe: blocks task completion, loses data or money, or excludes a group (for example keyboard or screen reader users) | Must fix before release |

Rate on three factors (Nielsen): **frequency** (how many users hit it), **impact** (how hard it is to overcome) and **persistence** (once, or every time). A quick matrix:

| Impact \ Frequency | Few users, rarely | Many users, or every time |
| --- | --- | --- |
| Annoyance, easy workaround | 1 | 2 |
| Delay or error, recoverable | 2 | 3 |
| Task fails, data or money lost, group excluded | 3 | 4 |

## UX laws and principles

### Fitts's law
Time to reach a target grows with distance and shrinks with size: MT = a + b log2(D/W + 1) (Fitts, 1954; Shannon formulation). Make frequent and primary targets large and close to where the pointer or thumb already is. Screen edges and corners act as very large targets for a mouse. Minimum target 24x24 CSS px (`--size-target-min`, WCAG 2.5.8); 44x44 for touch (`--size-target-comfortable`). Keep destructive actions away from frequent ones.

### Hick-Hyman law
Decision time rises with the logarithm of the number of equally likely choices (Hick, 1952; Hyman, 1953). At decision points, show fewer options, recommend one, and move rare options behind "More". It does not mean "fewer menu items is always better": people scan a familiar, well-ordered list (alphabetical countries, sorted dates) quickly.

### Jakob's law
Users spend most of their time on other products and expect yours to work the same way (Nielsen, 2000). Use conventions for structural patterns: logo top-left links home, search behind a magnifier icon, cart top-right, underlined links, standard form controls. Spend novelty on the value proposition and the visual language, not on basic controls.

### Miller's law, with its caveat
Miller (1956) described an immediate-memory span of about 7 plus or minus 2 items. It is often misused as "menus must have 7 items". Menus are seen, not memorized, so the limit does not apply to them. Later work puts working-memory capacity nearer 4 chunks (Cowan, 2001). Use the idea for chunking (phone numbers 3-3-4, card numbers in groups of 4, codes in pairs of 3) and for not asking people to remember information between screens.

### Tesler's law (conservation of complexity)
Every task carries complexity that cannot be removed, only moved (Larry Tesler). Move it from the user to the system: smart defaults, address lookup, autofill, inferring the country from the postcode. Do not hide controls that experts need in the name of simplicity.

### Doherty threshold
Productivity rises sharply when the system responds in under about 400 ms (Doherty and Thadani, IBM, 1982). Acknowledge input within 100 ms, use optimistic updates for low-risk actions, show skeletons for content, and keep UI transitions within `--duration-slow` (320 ms).

### Postel's law (robustness principle)
Be liberal in what you accept and conservative in what you send (Jon Postel, early TCP specifications). Accept phone numbers with spaces, dashes and country codes; trim whitespace; treat email addresses as case-insensitive; accept "3/4/26" and "March 4 2026" then display one unambiguous format.

### Peak-end rule
People judge an experience largely by its most intense moment and its end (Kahneman and colleagues, 1993). Fix the worst pain point first, then design the ending: a clear confirmation with next steps, a receipt, a graceful offboarding. A great middle does not rescue a broken ending.

### Aesthetic-usability effect
People rate attractive interfaces as easier to use (Kurosu and Kashimura, 1995; Tractinsky, 1997). Use it, but expect it to mask problems in testing: participants who like the look under-report friction. Judge by task success and observed errors, not by ratings alone.

### Von Restorff (isolation) effect
The item that differs from its neighbors is remembered (von Restorff, 1933). Make the single primary action visually distinct in size, weight or color and never rely on color alone (WCAG 1.4.1). Highlighting everything highlights nothing; ad-like styling triggers banner blindness.

### Serial position effect
Items at the start and end of a list are recalled best (Ebbinghaus; Murdock, 1962). Put the most important navigation items first and last, front-load headings and link text with the key word, and keep critical information out of the middle of long lists.

### Goal-gradient effect
Effort increases as people approach a goal (Hull, 1932). Kivetz, Urminsky and Zheng (2006) found a 12-stamp coffee card with 2 stamps pre-filled was completed faster than a 10-stamp card starting empty. Show progress in onboarding and checkout, count completed setup as step 1, and never fake progress.

### Zeigarnik effect, with its caveat
Zeigarnik (1927) reported that interrupted tasks are remembered better than finished ones. Replications are mixed, and the memory advantage is weak; the tendency to resume interrupted tasks is better supported. Use it to make tasks resumable (saved drafts, "Continue where you left off", setup checklists), not as a manipulation lever.

### Also useful
- **Gestalt grouping.** Proximity, similarity and common region tell people what belongs together; spacing does more than borders.
- **Choice overload.** The famous jam study (Iyengar and Lepper, 2000) did not replicate consistently; a meta-analysis found an average effect near zero (Scheibehenne and colleagues, 2010). Too many options hurt when options are hard to compare, so help comparison rather than cutting arbitrarily.

## Cognitive load

Cognitive load theory (Sweller, 1988) separates intrinsic load (the task's own difficulty), extraneous load (caused by the design) and germane load (effort that builds understanding). Design removes extraneous load.

- One primary task per screen on mobile; one primary action per region everywhere.
- 3-5 options at a decision point, with a recommended default.
- Labels next to the thing they label; no split attention between distant legend and chart.
- Recognition over recall: keep earlier choices visible in a summary.
- Progressive disclosure for advanced settings, but never hide what the current decision needs.
- Plain language at the target reading level ([content design](content-design.md)).
- Consistent layout so attention goes to content, not to finding controls.
- For complex professional tools, measure workload after tasks with NASA-TLX (Hart and Staveland, 1988) alongside task success.
