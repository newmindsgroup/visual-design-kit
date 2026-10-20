---
type: llm
weight: 3
---

Passes only if the response and its CSS:
- Use `writing-mode: vertical-rl` (columns flowing right to left) with `text-orientation: mixed` or an equivalent explanation of how Latin and digits rotate.
- Handle short numbers with tate-chu-yoko via `text-combine-upright` (for example `digits 2` or `all` on a span).
- Apply Japanese line-breaking rules (kinsoku): `line-break: strict` or equivalent, so closing punctuation and small kana do not start a line.
- Name a Mincho/serif Japanese face suited to literary text (for example Noto Serif JP, Shippori Mincho, Zen Old Mincho, or a named commercial Mincho such as Yu Mincho or Hiragino Mincho) with fallbacks, and address font file size (subsetting, unicode-range slicing, or system fonts).
- Give a line-height around 1.7-2.0 and a column length or measure appropriate to vertical text (for example about 30-45 characters per column).
- Use no italics; emphasis by emphasis dots (`text-emphasis`, for example sesame) or weight, and mention ruby/furigana.
- Address reading navigation: horizontal scrolling or pagination that runs right to left, and a horizontal fallback for small screens or UI chrome.
