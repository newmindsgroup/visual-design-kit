---
type: llm
weight: 1
---

Passes only if the response does both:
- Says the critique is based on a description, not a rendered page, so it is conceptual or provisional, and says what to render to confirm it (for example a screenshot or render at real widths such as 390, 768 and 1440 px).
- States that #9CA3AF on white is about 2.5:1 (2.4-2.6 accepted), below the 4.5:1 WCAG AA minimum for body text, and gives a darker replacement hex with its ratio (for example #4B5563 at about 7.6:1, or #6B7280 at about 4.8:1).
Fails if it critiques as if it had seen the page, or flags the gray as "low contrast" without a computed ratio and a replacement value with its ratio.
