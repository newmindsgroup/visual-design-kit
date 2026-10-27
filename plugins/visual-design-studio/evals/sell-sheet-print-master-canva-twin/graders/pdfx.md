---
type: llm
weight: 2
---

Passes only if the response specifies PDF/X (PDF/X-4 by default, PDF/X-1a if the printer asks) with the output intent set to the printer's ICC profile, and says the file still needs a preflight (Acrobat Preflight, PitStop or the printer's own) and a printer proof, because PDF/X export alone does not prove conformance.
Fails if it treats a plain PDF export as print-ready with no output intent and no preflight.
