# Website work sections

Version-Timestamp: 2026-09-11T20:48:53-04:00

Parent: [website workflow](../WEBSITE-WORKFLOW.md). Add only relevant sections to the existing [design record](design-work.md). Its version, evidence and approval fields remain authoritative.

## Brief and requirements

Outcome; audience/need IDs; scope and exclusions; existing site/brand/content references; platforms and constraints; critical journeys; launch versus later requirements; acceptance criteria; owner. Unknown values include consequences and the next step, not guessed answers.

## Page contract

For each selected page: stable ID and URL; visitor question; purpose; source content IDs; primary action and destination; template; parent and entry points; sections in order. For each section: question answered, message, proof/source or hypothesis, content/asset ID, component ID, responsive transformation and acceptance check. A sitemap node and an interaction state retain separate IDs.

## Template and CMS contract

Content type; field ID/type; required/default behavior; validation; relationships; source owner; draft/published visibility; missing/long content behavior; preview; localized equivalent. Separate editable content from protected design tokens. Map each field to actual page regions.

## Responsive and media contract

Describe transformations at content-driven widths, DOM reading order, focal points, typography and orphan prevention, states, touch/keyboard behavior and loading/failure alternatives. Media records include rights, dimensions, alternatives, source version and target budget.

## Integration contract

Action; destination; minimal payload; ownership; consent requirement; authentication boundary; submitting/confirmed/failed/unknown states; reconciliation; cancellation; fallback. A receipt is not fulfillment. Keep secrets out of this record.

## Acceptance and release

Criterion ID; actual artifact/version; method; environment; expected outcome; observed outcome; evidence; failure/hold; repair owner. Record staging separately from live, and automated results separately from manual, user and assistive-technology checks. Release version, authority, cutover, rollback and monitoring owner are selected only when in scope.
