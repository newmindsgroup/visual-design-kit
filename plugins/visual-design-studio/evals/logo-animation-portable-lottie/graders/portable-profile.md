---
type: llm
weight: 3
---

Passes only if the response defines a portable Lottie profile limited to features of the Lottie spec v1.0 (shapes, transforms, masks, precomps) and requires all four changes to the draft: remove the expressions (rebuild the wiggle as plain keyframes), convert the live text layer to outlines or shapes, replace the Gaussian blur (feathered shapes or opacity), and replace the 3D camera with 2D scale or parallax.
Fails if it keeps the expressions or the live text layer, or says the file will play the same everywhere as built.
