# Measured typography and spacing checks

Version-Timestamp: 2026-10-17 08:36:43 AST

This extends the existing typography and production capabilities. It is a review aid, not automatic visual approval.

1. Declare final dimensions, unit, intended reading conditions, trim safety and optical text padding separately. Images can intentionally bleed; text insets do not constrain decorative image edges.
2. Use loaded font files and actual content. Record line counts and final-line word count. When phrases fragment, widen the measure, reallocate grid space or reduce column count before reducing readable type. Preserve required meaning and exact strings. Do not distort glyphs or blanket no-wrap long phrases.
3. Measure text bounds against its own panel, not only the page. Check hidden-overflow ancestors, masks, panel boundaries and gap to the next section. A bounding-box check cannot fully validate a nonrectangular mask: inspect its render.
4. Define format-specific thresholds. A short service phrase may target two lines; a paragraph or narrow label may justifiably differ. Do not impose running-text character counts on labels.
5. Inspect actual-size exports independently. For print, confirm physical dimensions and embedded fonts, and record the actual paper proof as pending until performed. For responsive layouts, inspect narrow/wide views, fallback fonts and enlargement where applicable.
6. Retain before/after evidence. Name concept author and later editor separately. Regenerate checks after changes. An unresolved failure holds composition acceptance.

## Measurement receipt and checker

Run `python3 scripts/composition_checks.py /absolute/project/receipt.json` from the library. Exit 0 means reported measurements meet declared thresholds and font/render evidence references are present. It does not verify those referenced files or their truth. Exit 1 reports threshold violations or invalid receipt fields. Exit 2 reports usage, file-read, JSON parsing or recursion errors. Synthetic tests exercise the checker only, not visual quality.

Receipt fields: `unit` (pt or css_px), `font_evidence`, `render_evidence`, `elements` (nonempty). Each element: `id`, `insets` [left,top,right,bottom], `minimum_inset`, `font_size`, `minimum_font_size`, `lines`, `maximum_lines`, `last_line_words`, `clipped`, `gap_after`, `minimum_gap_after`. All element values use the receipt-level unit; the checker cannot detect mixed units. `lines` counts rendered lines; `last_line_words` counts words on the final line. Isolated final words are review candidates. Exemptions belong in a separate human disposition and do not turn a failed machine check into a pass. No network or assets are read by the checker.

## Public sources and limits

- [Butterick: line length](https://practicaltypography.com/line-length.html): assess measure relative to type. Its running-text range is not a compulsory width for short labels.
- [Butterick: line spacing](https://practicaltypography.com/line-spacing.html): 120 to 145 percent is a starting range for most text, not every display headline.
- [Adobe: balancing ragged lines](https://helpx.adobe.com/indesign/using/aligning-text.html): balancing can help suitable short text. Browser balancing remains an enhancement requiring inspection.

These sources do not establish a universal flyer margin or automated aesthetic score. No client copy or imagery belongs in the reusable test fixtures.
