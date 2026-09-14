# Design research and remaining gaps

Version-Timestamp: 2026-09-08 20:12:05 AST

Research checked 2026-09-08. Original synthesis supports authored methods, not copied vendor defaults or completed visual examples. Source categories below distinguish standards, design-system choices, research and font discovery. No fonts/libraries installed and no client sources transmitted.

| Source | What it contributes | Limit and resulting action |
| --- | --- | --- |
| [National Gallery of Art: elements](https://www.nga.gov/educational-resources/elements-art) | Art-element vocabulary | Educational framework; adapt composition questions to the task |
| [Elliot Jay Stocks: type selection](https://github.com/elliotjaystocks/choosing-type-checklist) | Purpose, completeness and practical font selection | Author guidance, not mandatory pairings; compare real specimens |
| [Google Fonts repository](https://github.com/google/fonts) | Broad free font discovery with per-family files/licenses | Exact release/rights/glyph checks still required |
| [OFL FAQ](https://openfontlicense.org/ofl-faq/) | Use versus modification/redistribution distinction | Inspect the selected font's license and notices, not the directory name alone |
| [Fontshare license](https://www.fontshare.com/licenses/itf-ffl) | Free proprietary font alternative | Page body not fully readable in this intake; full terms remain a use prerequisite |
| [Web font practices](https://web.dev/articles/font-best-practices) | Loading/fallback can affect layout and usability | Measure actual project loading; no universal file-size benefit |
| [Carbon color](https://carbondesignsystem.com/elements/color/overview/) | Roles and themes as a system | IBM-specific values are not client defaults |
| [Carbon motion](https://carbondesignsystem.com/elements/motion/overview/) | Functional and expressive movement, choreography | Brand-specific choices, not universal timing or a ban on all bounce |
| [Color-emotion research, Jonauskaite et al.](https://researchportal.helsinki.fi/en/publications/universal-patterns-in-color-emotion-associations-are-further-shap/) | Study reports shared associations modulated by linguistic/geographic factors | Abstract-level discovery; not evidence a palette increases conversion or fits a specific client |
| [MDN scroll animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations) and [W3C draft](https://www.w3.org/TR/scroll-animations-1/) | Scroll/view timelines and implementation vocabulary | Draft/documentation do not establish installed-browser support |
| [GSAP matchMedia](https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/) | Conditional animation lifecycle/reversion | Optional library, not installed or adopted here |
| [W3C text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), [use of color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) | Measurable combination checks and alternatives | Apply criterion scope/exceptions; colors alone cannot be certified accessible |
| [W3C text spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) and [reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) | Resilient typography/layout | For applicable web content test user overrides and reflow, not just a static specimen |
| [W3C animation from interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html), [pause/stop/hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html), [flash limits](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html) | Distinct accessibility conditions | AAA interaction control differs from A auto-motion/flash requirements |

## Gap audit

| Gap found | Added now | Remaining evidence |
| --- | --- | --- |
| Scattered fundamentals and generic-output judgment | Foundations skill and shared craft review | Actual candidate comparisons, human comprehension and design-owner acceptance |
| Familiar font defaults and incomplete font handoff | Typography skill, eight discovery leads, decision template | Exact file/license inspection, specimens, glyph/language/native tests |
| Swatches without full role/state/context decisions | Color skill, hypothesis and combination record | Real measured pairs, cultural/context validation and output proofs |
| Motion effects described without reusable behavior contracts | Motion skill, 20 recipes and specification | Browser/device or media implementations, performance and accessibility tests |
| Cross-skill records could diverge | Explicit owners, references and invalidation rules | Real project execution must verify references; no duplicate-record automation added |
| Packaging can lag current instructions | Optional catalog/routing integration | Refreshed portable package and clean intended-agent execution |

Principles are not proof of beautiful output. The next useful evidence is a small set of distinctly different synthetic visual studies and selected motion demos, each with actual renders and review. A real client pilot remains deferred. Do not label the library exhaustive or runtime-ready solely because instructions exist.
