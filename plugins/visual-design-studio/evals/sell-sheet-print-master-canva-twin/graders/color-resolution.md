---
type: llm
weight: 2
---

Passes only if the response specifies CMYK output built with the printer's own ICC profile (asks the printer which one; GRACoL 2013 / CRPC6 for US coated sheetfed is an acceptable named default), images at 300 ppi effective at final size, and either CMYK images or a conversion with that profile, plus small black text as 100K.
Fails if the print master is left in RGB or sRGB, or images are specified at 72 or 150 ppi.
