---
type: llm
weight: 3
---

Passes only if the response rebuilds each recurring layout once in Canva as a Brand Template with named autofill fields (text fields such as event title, date, rep name and title; image fields for photos), then fills it through the Canva connector or the Connect API (autofill or create a design from the brand template). It says autofill and brand templates are available on Canva Pro, Teams or Enterprise according to Canva's current API spec (older guide pages said Enterprise only; verify), and that publishing a brand template needs an admin or designer role.
Fails if it says autofill requires Canva Enterprise without noting the newer spec, or plans to import a fresh PDF each month as the editable route.
