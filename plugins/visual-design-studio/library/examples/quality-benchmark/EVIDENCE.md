# Execution evidence

Version-Timestamp: 2026-09-16T18:27:08.062526-04:00

Parent: [briefs and method](README.md). [Portable verification record](verification.json). Checks establish the stated technical behavior, not human acceptance.

## Executed

- Two fictional compositions, comparison controls and headline revisions are rendered at 320, 390, 768, 1024 and 1440 CSS pixels. All 20 candidate/revision cases pass the current browser suite, with no console errors. Twenty-three screenshots were retained for inspection.
- Exact local fonts, blocked-font fallback, text-spacing overrides, actual text bounds, keyboard navigation and deliberate orphan/clipping controls were exercised. Screenshots of desktop, mobile, spacing and fallback states were inspected. User spacing can change line shapes; content is preserved rather than forcing the designed shape with no-wrap. Native browser zoom was not run.
- Source photo, wordmark, other copy and palette comparisons pass after both headline revisions. Deliberate photo, wordmark and palette faults are detected. A separate fresh-context worker recovered the revised FORM source and verified its photo hash, while rejecting the false-claim alternative. It did not establish native plugin discovery or pixel approval.
- Both one-page PDF proofs were rendered and inspected. Text remains selectable and PDF tags exist. This is not a PDF accessibility certification.
- The twelve-second, 24 fps WebM contains 288 rendered frames at 1280 by 720. Every source frame retains the wordmark region. Actual encoded playback completed with 287 sampled decoded-frame callbacks and a minimum of 2539 white pixels in the checked wordmark region. The callback API may omit an initial or otherwise skipped frame; this is not a claim that every encoded frame was observed. The separate source check covers all 288 source frames. Representative transition and hold frames were inspected. Browser play/pause, loop, reduced motion and failed timeline loading were tested. No physical display was tested.
- Local reference retrieval searched a downloaded library and inspected the original typography page at PDF page 177, printed page 159. The original adaptation and limits are in README. No book bytes or excerpts are distributed.

## Repairs retained as learning

Initial wraps exposed isolated words in longer revised headlines. Local size and width adjustments repaired them without changing approved meaning. A missing CSS closing brace and a collapsed mobile container were caught through rendered checks. A video export initially lost its persistent wordmark; the source layer was corrected and all-frame source and encoded-playback checks added. Earlier failed reports and exports remain in the ignored private work packet. Only the repaired exports ship here.

## Review boundary

The independent final review is recorded in the repository release record after it returns. Human aesthetic selection, actual client execution, language specialist review, assistive technology, color-managed production and target device acceptance remain project-specific. The examples demonstrate a stronger process; they do not certify that every future output will be excellent.

The independent reviewer preferred the intended FORM and TIDAL candidates over the neutral comparison alternatives and rejected the false-claim and exclusive-message controls. Those judgments are model review, not user preference. Caption contrast was made independent of photographic texture after review. Full findings and disposition are recorded in the repository release report. Measured static contrast pairs are in verification.json; this is selected-pair evidence, not a full accessibility audit.

A follow-up playback check hashes the served movie bytes before playback and compares them with the local export. The hashes match. This repeat observed 286 callbacks across the full twelve seconds; the earlier run observed 287. Both retained the checked wordmark region. Callback count varies with scheduling and is never treated as an exact encoded frame count.
