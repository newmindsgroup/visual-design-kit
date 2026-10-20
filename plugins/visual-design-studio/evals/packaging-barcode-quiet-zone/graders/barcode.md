---
type: llm
weight: 3
---

Passes only if the response:
- Recommends an EAN-13 (accepted in both US and EU) or UPC-A, with numbers allocated by GS1 to the brand owner.
- Uses the GS1 dimensions: X-dimension 0.330 mm at 100%, allowed 80-200% magnification, EAN-13 about 37.3 mm wide including quiet zones at 100%, and quiet zones of 11X left and 7X right (about 3.63 mm and 2.31 mm at 100%), with a "verify against the current GS1 General Specifications" hedge.
- Notices that even at the 80% minimum an EAN-13 with quiet zones is about 29.8 mm wide, so it does not fit a 25 mm panel, and proposes a real fix (move it to a wider panel such as the back or base, rotate it on a taller panel, or ask GS1 about EAN-8 for small packs) instead of shrinking below 80% or cutting the quiet zones.
- Says not to truncate bar height, and specifies dark bars (black) on a light background, with red, orange or yellow bars ruled out.
- Mentions placement away from folds, edges and seams, vector output from barcode software, and verification with an ISO/IEC 15416 verifier.
Fails if it specifies a barcode narrower than 80% magnification or quiet zones smaller than the GS1 minimum to fit the panel.
