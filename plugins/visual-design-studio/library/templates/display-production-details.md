# Display production detail checklist

Version-Timestamp: 2026-09-11T21:22:42-04:00

Parent: [media workflow](../MEDIA-QUALITY-WORKFLOW.md). Cases: [prepared exercises](../examples/media-quality-recipes/README.md).

Supplement the existing production packet. Mark each field observed, proposed, unknown or not applicable with a reason; do not interpret completed planning as tested behavior.

| Area | Required record | Acceptance evidence |
| --- | --- | --- |
| Zone hierarchy | Screen and zone IDs, bounds, priority, reading order, motion allowance, viewing assumptions | Whole-scene preview and timed-entry observations |
| Format adaptation | Anchors, safe margins, product invariants, crop rules, type limits, overflow exception | Each final variant, long/localized copy and missing asset checks |
| Fallback | Main/fallback hashes, validity, trigger, runtime owner, restoration rule | Missing/corrupt/slow media injection and visible fallback |
| Attract transition | State/event table, first-touch semantics, cancellation, timeout/extension and session identity | Rapid touch, late response, reset, extension and reduced-motion traces |
| Optimization | Verified player specification, master/export IDs, actual dimensions/codec/FPS/size/alpha policy | Before/after visual comparison and target playback measurements |
| Campaign review | Complete version-bound asset manifest and affected dependencies | Contact sheet, full playback, interaction walkthrough and repair log |

No fixture construction or installation engineering is included. Device limitations inform content design and delivery only.
