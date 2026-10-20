# Research methods

Version-Timestamp: 2026-10-20 02:04:32 UTC

Pick the method from the question, not from habit. Attitudinal methods tell you what people say; behavioral methods tell you what they do. Qualitative methods explain why; quantitative methods tell you how many and how much.

## Method selection matrix

| Question you need answered | Method | Sample (starting point) | Typical duration | Output |
| --- | --- | --- | --- | --- |
| How do people do this today, and where does it hurt? | Contextual inquiry or field study | 5-8 per segment | 1-3 weeks | Workflows, workarounds, environment constraints |
| Why do people choose, switch or quit? | Semi-structured interviews (JTBD switch interviews for purchase decisions) | 5-8 per segment; saturation often near 12 total | 1-2 weeks | Needs, jobs, forces, vocabulary |
| How does use change over days or weeks? | Diary study | 10-15 participants, 1-4 weeks | 2-6 weeks | Longitudinal patterns, triggers, context |
| Can people complete key tasks with this design? | Moderated or unmoderated usability test | 5 per round per user group | 1-2 weeks per round | Prioritized issues with severity |
| How usable is it against a benchmark or competitor? | Quantitative usability test | About 40 per group | 2-4 weeks | Success rate, time, SUS with intervals |
| How do people group this content? | Open card sort (hybrid or closed to validate) | 15-20 (open); 20-30 (closed) | 1 week | Similarity matrix, candidate groups and labels |
| Can people find things in this hierarchy? | Tree test | About 50 per tree variant; 30 minimum | 1 week | Task success, directness, first clicks |
| Where do people click first on this screen? | First-click test | 30-50 (convention) | Days | Click maps per task |
| Does the page communicate its purpose at a glance? | Five-second test | 20-50 unmoderated (convention) | Days | Recall and comprehension answers |
| How many people have this need or attitude? | Survey | About 100 for +/-10%, about 385 for +/-5% | 1-3 weeks | Proportions, segments |
| Which variant performs better at scale? | A/B or multivariate test | From a power calculation | 2-6 weeks | Effect size with confidence |
| What happens in the product now? | Analytics, funnels, search logs, session replay | All traffic (with consent) | Ongoing | Drop-off points, paths, zero-result searches |
| What are people already telling us? | Support tickets, app reviews, sales notes | Last 3-12 months | Days | Recurring problems, vocabulary |
| Which visual direction fits the brand words? | Desirability study (Microsoft Product Reaction Cards, 118 words) | 20-30 per direction (convention) | Days | Word frequencies per direction |

Combine one behavioral and one attitudinal method when stakes are high: interviews explain what the analytics funnel shows; a tree test confirms what a card sort suggests.

## Interview guide template

Length 45-60 minutes. One moderator, one note-taker. Record only with consent.

```text
1. Intro (3 min)      Who we are, purpose, no right or wrong answers, recording consent, they can stop anytime.
2. Warm-up (5 min)    Role or life context. "Walk me through a typical week where <topic> comes up."
3. Last time (15 min) "Tell me about the last time you <did the task>." Get the story in order:
                      trigger, steps, tools, people involved, what went wrong, how it ended.
4. Deep dive (15 min) Probe the moments that carried emotion or effort.
5. Alternatives (7 min) "What did you try before? What else did you consider? What made you switch?"
6. Wrap-up (5 min)    "Anything I should have asked?" Incentive, thanks, consent for follow-up.
```

Probes that work: "What happened next?", "Why was that important?", "Can you show me?", "How did you decide?", "What did that cost you?", "Tell me more about...". Silence for 3-5 seconds after an answer often produces the most useful detail.

Avoid: hypotheticals ("Would you use...?"), leading questions ("Wasn't that frustrating?"), double-barreled questions, yes/no questions, pitching the solution, and asking for feature wish lists. For discovery, Rob Fitzpatrick's *The Mom Test* rules apply: talk about their life, not your idea; ask about specifics in the past; talk less, listen more.

## Usability testing

- **Why 5 per round.** Nielsen and Landauer (1993) modeled problem discovery as 1 - (1 - L)^n; with the average L of 0.31 they observed, 5 users reveal about 85% of the problems affecting that group. L varies by product and task, the rule holds per distinct user group, and its value comes from iterating: three rounds of 5 beat one round of 15.
- **Quantitative studies differ.** Metrics need narrow intervals; NN/g recommends about 40 participants for most quantitative usability studies.
- **Tasks are scenarios, not instructions.** Bad: "Click Settings and change your password." Good: "You think someone else knows your password. Make sure they can no longer sign in." Never use the interface's own labels in the task.
- **Session plan.** 45-60 minutes moderated (30 minutes unmoderated), 5-8 tasks, easiest first, one pilot session before the real ones. Define success criteria and critical errors before the first session.
- **Moderation.** Concurrent think-aloud. Do not help; answer questions with "What would you do if I weren't here?" Record assists as a separate outcome.
- **Capture per task.** Success (yes / with assist / no), time, errors, path, SEQ rating, notable quotes with timestamp.
- **Include assistive-technology users** when the product will be used by them (always, for public services): 1-2 screen reader, magnification or switch users per round, recruited through specialist panels, with their own devices and settings.
- **Remote unmoderated** suits clear tasks and quick iteration; **moderated** suits complex products, early prototypes and follow-up questions.
- **Report.** Lead with the top 5 findings, each with the count of participants affected, severity (0-4), a screenshot or clip, and a recommendation.

## Card sorting and tree testing

**Card sort setup.** 30-60 cards (fatigue rises past 60), each a real piece of content written in plain words, not internal labels. Open sorts generate groups and labels; closed sorts test existing groups; hybrid allows new groups. Analyze with a similarity matrix and dendrogram, then read participants' group names for vocabulary. 15 participants per user group is the commonly cited minimum (Nielsen, 2004, drawing on Tullis and Wood); 20-30 gives more stable groupings.

**Tree test setup.** Text-only hierarchy, no visual design. 8-10 tasks per participant, each a realistic goal with one correct destination (or a defined set). Randomize task order. About 50 participants per variant; test two candidate trees against each other when the choice is open.

**Read the results.** Per task: success rate, direct success (no backtracking), time, and first click. Flag tasks under about 70% success or with scattered first clicks (a common convention, not a standard). First clicks matter: in Bailey and Wolfson's first-click research, participants whose first click was correct completed the task far more often than those whose first click was wrong (about 87% versus 46%).

## Surveys

Margin of error at 95% confidence for a large population, worst case p = 0.5:

| Completes | Margin of error |
| --- | --- |
| 100 | +/-9.8% |
| 385 | +/-5.0% |
| 1,068 | +/-3.0% |

- Keep it under 10 minutes (10-15 questions). Pilot with 3-5 people and time it.
- One idea per question; balanced, fully labeled 5- or 7-point scales; include "Not applicable" where it applies.
- Randomize option order unless the order is natural; put demographics last.
- Screen with behavior ("In the last 30 days, how many times did you...") rather than identity.
- Self-selected samples (pop-ups, social posts) skew toward strong opinions; describe the sample honestly.
- Do not ask what analytics can already measure.

## Diary studies

10-15 participants for 1-4 weeks. Start with an onboarding call, use 1-2 short prompts per day or event-triggered entries ("each time you..."), accept photos and voice notes, send reminders, check entries daily and follow up while memory is fresh, and close with an exit interview. Stage incentives across the study to limit dropout; over-recruit by 20-30% (convention).

## Analytics and A/B tests

- Analytics answer what, where and how many, never why. Instrument key events, funnels, retention cohorts and site search. Mask personal data in session replay and collect it only with the consent the jurisdiction requires.
- **A/B test checklist.** Written hypothesis; one primary metric plus guardrails (revenue, error rate, unsubscribes); sample size from a power calculation (alpha 0.05, power 0.8, a realistic minimum detectable effect); run whole weekly cycles, at least 1-2 weeks; do not stop at the first significant peek; check sample ratio mismatch; segment only when pre-registered.
- **Worked example.** Baseline conversion 5.0%, minimum detectable effect +10% relative (to 5.5%), two-sided alpha 0.05, power 0.8: about 31,000 visitors per variant.
- A variant that deceives users is a dark pattern even when it wins. See `web-design` [conversion](../../web-design/references/conversion.md) for the rules.

## Recruiting and consent

- **Screener.** Behavior-based questions, the target hidden among distractors, explicit disqualifiers (works in UX, market research or for a competitor), quotas for device, region, age range, ability and experience level. Over-recruit 10-20% for no-shows.
- **Incentives.** Pay in proportion to time and expertise; specialists and executives cost several times consumer rates. Rates move; check a current incentive report (for example User Interviews' annual research incentives report) before budgeting.
- **Consent covers:** purpose, what is recorded, who sees it, how long it is kept, how to withdraw, and separate permission to use clips. Children: parental consent plus the child's own assent. Health, financial or other sensitive data: collect only what the question needs and confirm requirements with counsel for the specific product and jurisdiction (GDPR lawful basis and special-category data in the EU and UK; HIPAA where US protected health information is involved).
- **Data handling.** Store contact details separately from notes, use participant IDs (P01, P02) in all synthesis, delete recordings on the stated schedule.
- **Accessible sessions.** Ask about accommodations in advance, test the tools with assistive technology, allow extra time.

## Synthesis

1. Debrief for 15 minutes after each session while memory is fresh.
2. Write one observation per note, tagged with participant ID and timestamp. Keep observation separate from interpretation.
3. Affinity-map into themes; count how many participants support each theme and note counterexamples.
4. Write insight statements: "[Who] [does or struggles with what] because [why], so [implication for design]."
5. Rate each problem's severity (0-4) and attach evidence.
6. Turn insights into recommendations with an owner and a test to confirm the fix.
7. Store findings as atomic, linkable records (fact, insight, recommendation) so later projects can reuse them.

AI can cluster transcripts and draft themes quickly. Check every theme against the source notes, keep the participant counts real, and never present synthetic participants or generated quotes as research.
