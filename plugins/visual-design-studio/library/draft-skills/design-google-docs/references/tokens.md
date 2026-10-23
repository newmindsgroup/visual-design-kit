# Neutral document tokens

Version-Timestamp: 2026-10-05 13:07:59 AST

These are starting tokens, not a client brand. Override with approved brand guidance and repeat contrast and rendered checks.

| Role | Starting value |
| --- | --- |
| Body | Arial, 11.5pt, regular, 120% line spacing, 6pt after |
| Title | 24pt bold, 110%, 12pt after |
| Heading 1 | 17pt bold, 18pt before, 8pt after |
| Heading 2 | 14pt bold, 18pt before, 8pt after |
| Heading 3 | 12.5pt bold, 14pt before, 6pt after |
| Metadata | 10pt, muted, 4pt after |
| Cell prose | 11.5pt, 115%, 3pt after |
| Labels | 11pt bold; keep ordinary body text separate |
| Body ink | #243746 |
| Supporting ink | #526170 |
| Action label ink | #17656B |
| Paper | #FFFFFF |
| Neutral surface | #EFF4F6 |
| Response surface | #EDF5F3 |
| Decorative rule | #D7E0E5, 0.5 to 0.75pt; never sole meaningful boundary |

Compute WCAG contrast for every text/background pairing actually used. Required minimum: 4.5:1. These three ink colors should pass on the three listed surfaces; verify rather than relying on this expectation. Meaningful controls/boundaries need an additional 3:1 non-text check when applicable.

Widths are contextual. Choose from measured available space and content, not a universal page size. A single-column form can be wider than its original printed layout while still requiring horizontal scrolling in a small split panel. State that limitation and test it. Data tables may need a broader region than prose, but dense five-column comparisons often need content restructuring rather than smaller fonts.

Platform references, verified during initial method development on 2026-10-05:

- [Google Docs pageless format and viewer text width](https://support.google.com/docs/answer/11528737)
- [Native updateNamedStyle, updateTableColumnProperties and pinTableHeaderRows requests](https://developers.google.com/workspace/docs/api/reference/rest/v1/documents/request)

Check current schemas before composing mutations. In updateTableColumnProperties the field is tableColumnProperties, not columnProperties. Use actual tab IDs and table anchors. Exclude zero-length terminal ranges from text-style requests.
