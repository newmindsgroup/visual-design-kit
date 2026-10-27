---
type: llm
weight: 3
---

Passes only if the response keeps two artifacts: a print master produced outside Canva (for example the kit's HTML/CSS layout rendered to PDF/X with WeasyPrint, or InDesign) that goes to the printer, and a Canva editable twin for the quarterly copy changes. It must say why: Canva's standard or API PDF export has no CMYK, bleed or crop-mark options, so it is not a print master. If the team does print from their Canva edits, it says to export by hand with Canva's "PDF Print" with crop marks and bleed (CMYK where the plan allows; verify) and then preflight.
Fails if it accepts the designer's plan to send a standard Canva PDF export to the printer without these caveats.
