---
type: llm
weight: 1
---

Passes only if, when the response proposes building the spot in code with Remotion, it states that Remotion is not MIT (source-available under the Remotion License), that organizations with 4 or more people, counting contractors on the project, need a Company License, and that scripted or CLI renders (`npx remotion render`, `renderMedia()`) count as automation under the v5 terms (to verify). Also passes if the response does not propose Remotion at all and names another editable timeline (After Effects, Premiere, Resolve).
Fails if it proposes Remotion and calls it free or MIT for any company size.
