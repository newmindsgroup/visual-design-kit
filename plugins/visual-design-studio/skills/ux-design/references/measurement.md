# UX measurement

Version-Timestamp: 2026-10-20 02:04:32 UTC

Measure to decide, not to decorate a report. Pick one or two metrics per question, collect them the same way every time, and report intervals rather than single numbers when samples are small.

## Which metric for which question

| Question | Metric | Collect |
| --- | --- | --- |
| Can people do the task? | Task success rate | Every usability task |
| How efficient is it? | Time on task (successful attempts), error count | Every usability task |
| How hard did the task feel? | SEQ (Single Ease Question) | Immediately after each task |
| How usable is the product overall? | SUS, or UMUX-Lite when time is short | End of session or in-product survey |
| How is the product performing at scale? | HEART metrics from analytics | Continuously |
| Will people recommend us? | NPS, with caveats below | Relationship survey, quarterly at most |
| How much effort did support or a service take? | Customer Effort Score | After a service interaction |

## SUS (System Usability Scale)

Created by John Brooke (1986) and free to use with attribution. Ten statements, each rated 1 (strongly disagree) to 5 (strongly agree). Replace "system" with "website" or "app" if needed.

1. I think that I would like to use this system frequently.
2. I found the system unnecessarily complex.
3. I thought the system was easy to use.
4. I think that I would need the support of a technical person to be able to use this system.
5. I found the various functions in this system were well integrated.
6. I thought there was too much inconsistency in this system.
7. I would imagine that most people would learn to use this system very quickly.
8. I found the system very cumbersome to use.
9. I felt very confident using the system.
10. I needed to learn a lot of things before I could get going with this system.

**Scoring.** Odd items: rating minus 1. Even items: 5 minus rating. Sum the ten contributions (0-40) and multiply by 2.5 for a 0-100 score. Average across participants.

**Worked example.** Ratings 4, 2, 4, 1, 4, 2, 5, 2, 4, 1 give odd contributions 3+3+3+4+3 = 16 and even contributions 3+4+3+3+4 = 17. (16 + 17) x 2.5 = 82.5.

**Benchmarks.** The average SUS score is about 68 across hundreds of studies (Sauro and Lewis). A score is not a percentage; 68 is the 50th percentile. The Sauro-Lewis curved grading scale (*Quantifying the User Experience*, 2nd ed., 2016; verify against the source before quoting grades to a client):

| Grade | SUS range | Grade | SUS range |
| --- | --- | --- | --- |
| A+ | 84.1-100 | C+ | 71.1-72.5 |
| A | 80.8-84.0 | C | 65.0-71.0 |
| A- | 78.9-80.7 | C- | 62.7-64.9 |
| B+ | 77.2-78.8 | D | 51.7-62.6 |
| B | 74.1-77.1 | F | 0-51.6 |
| B- | 72.6-74.0 | | |

**Use it well.** Administer after tasks, before any discussion. SUS stabilizes quickly (Tullis and Stetson, 2004, found about 12 participants gave results close to the full sample), but report a 95% confidence interval. SUS tells you how usable the product feels, not why; pair it with observed issues. An all-positive wording variant is acceptable when mis-coding of alternating items is a risk.

## SEQ (Single Ease Question)

"Overall, how difficult or easy was the task to complete?" rated 1 (very difficult) to 7 (very easy), asked right after each task. MeasuringU's historical average is about 5.5; tasks well below that, or with low success, are the first to investigate. Follow a low rating with "What made it difficult?"

## UMUX-Lite

Two statements rated 1-7: "This system's capabilities meet my requirements" and "This system is easy to use." Score = ((item 1 + item 2) / 2 - 1) x 100 / 6, giving 0-100 on roughly the SUS scale. The older regression adjustment (0.65 x score + 22.9) underestimates SUS at high usability (Lah, Lewis and Sumak, 2020); use it only to reproduce older studies.

## Task metrics

**Task success.** Define success and partial success before testing. With fewer than about 20 participants, report counts ("4 of 5 completed") rather than percentages. If a number is required, give the adjusted-Wald 95% interval: 4 of 5 is 36-98%, which shows how little a 5-person percentage means. MeasuringU's analysis of about 1,100 tasks put the average completion rate near 78% (verify the current figure before using it as a benchmark).

**Time on task.** Use successful attempts only. Times are right-skewed, so report the median or geometric mean, not the arithmetic mean. Compare with an expert's time on the same task to see the learning gap.

**Errors.** Define them per task: slips (right intention, wrong action, such as a mis-tap) and mistakes (wrong intention, such as choosing the wrong plan). Report errors per task and flag critical errors (data loss, wrong payment, wrong recipient) separately.

**Directness and first click.** For tree tests and navigation tasks, report the share of participants who succeeded without backtracking and the share whose first click was correct.

## NPS and its caveats

"How likely are you to recommend [product] to a friend or colleague?" 0-10. Promoters 9-10, passives 7-8, detractors 0-6. NPS = % promoters - % detractors, from -100 to +100 (Reichheld, *Harvard Business Review*, 2003).

- Not a usability metric. Never run it after a single test session.
- Collapsing 11 points into 3 groups throws away information and makes NPS volatile; samples in the low hundreds still carry intervals of many points.
- Not diagnostic: always ask "What is the main reason for your score?" and code the answers.
- Response styles differ by culture and market; compare a market with itself over time, not with other markets.
- Inappropriate where people would not recommend anything (utilities, enterprise tools chosen by procurement, sensitive health services).
- Report the full distribution alongside the score.

## Google HEART framework

Kerry Rodden, Hilary Hutchinson and Xin Fu (CHI 2010). Pick the categories that matter, then go from goals to signals to metrics.

| Category | Goal (example: team task app) | Signal | Metric |
| --- | --- | --- | --- |
| Happiness | People feel the app helps them finish work | In-app survey responses | UMUX-Lite average per month |
| Engagement | Teams plan their week in the app | Tasks created and updated | Weekly active teams with 3+ planning sessions |
| Adoption | New teams start using core features | First project created | % of new sign-ups creating a project within 7 days |
| Retention | Teams keep using it | Return visits | Week-4 team retention by sign-up cohort |
| Task success | Creating and assigning tasks is fast and error-free | Task creation events, undo, validation errors | Median time to create and assign; error rate per 100 tasks |

Rules: one or two metrics per category, defined so they can move; segment by cohort and platform; pair every metric with a guardrail (engagement that rises because people are stuck is not success).

## Reporting results

- Benchmark the same tasks, wording and participant profile before and after a change.
- Show intervals and the sample size beside every number.
- Separate statistical significance from practical significance: a 0.4-point SUS change is noise for most decisions.
- Lead with the decision: "Checkout success rose from 31 of 40 to 37 of 40; ship the new address step."
