# Photoshop production workflow

Version-Timestamp: 2026-09-10 20:21:06 AST

Use for retouching, masking, raster compositing and image masters requiring layers or nondestructive edits. A connector returning a finished image is suitable for a flattened-image task but does not prove editable PSD production.

Before action: identify the source image/master, required layer/mask structure, permitted edit region and invariants, target dimensions, resolution units, color profile/bit depth and transparency. Confirm the specific local UXP/script/UI or connector capability; a Photoshop installation is not an authenticated cloud API entitlement.

Use a candidate copy. Keep the source and needed layers/masks separate; retain nondestructive adjustment and smart-object structure when required. Do not flatten or overwrite the master to satisfy an export path. Record unsupported operation/conversion losses; preserve metadata or remove it according to the task, not a silent default.

Acceptance: reopen the actual PSD/other required master in Photoshop and verify named layers, masks, editable text/objects as applicable, and preserved regions. Inspect flattened delivery exports for dimensions, profile, edge/transparency quality and artifacts. Check the declared change against the baseline visually and with useful pixel/structure measures. Record exact evidence; no layered-master claim from PNG/JPEG alone.

Check actual export profile presence, color-space identity and rendering intent against the source. A profile's presence does not prove byte equality or cross-device color fidelity. Export from an isolated duplicate and preserve the layered master. Verify selected smart-object content, replacement fit and clipping separately when used.

Use [shared production routing](../../../SOFTWARE-PRODUCTION.md) and [medium acceptance](../../../TOOLCHAINS.md); the existing work record and handoff remain authoritative.
