# Headless UI playground extension

Version-Timestamp: 2026-10-14 14:03:25 AST

Local candidate 0.4.1 adds pinned @headlessui/vue 1.7.23, an original shared HeadlessOverlay.vue and two studies: branded-dialog and mobile-drawer. Total: 42 records, 22 implemented studies and 20 researched recipes. No form backend, client assets or production release.

New browser harness first failed because the studies did not exist. Subsequent focus-return failure led to explicit after-leave focus restoration guarded against unmount/navigation. Panel root covers the viewport. Vue portals only mount after hydration. Astro navigate owns unmodified drawer link navigation; ordinary hrefs preserve browser modified-click behavior.

Initial eight Chromium automated check groups passed: both variants at 1440/390/320px, forward/backward focus trap, Escape/close/backdrop dismissal, focus return, no overflow, open and closed axe, OS/local reduced motion, observable entrance/completed opacity, pause, noJS fallback, navigation portal/inert/scroll-lock cleanup and destination focus. No hydration/Teleport warnings or browser page errors were observed in these groups. Desktop dialog and narrow drawer screenshots inspected.

Astro diagnostics and Vue typecheck pass; production build emits 43 routes. npm audit: zero known vulnerabilities. Dependency source/license/script/data-flow review approved with project adoption constraints. Independent Fable approach review returned; milestone receipt recorded in maintainer packet when returned. This document does not substitute for that receipt.

Safari, Firefox, VoiceOver, real mobile hardware and client visual approval remain unverified. Check receiving project versions, tokens, privacy and interactions before adopting.

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-14 14:03:25 AST

Version-Timestamp: 2026-10-14 14:06:36 AST

Independent milestone review returned from claude-fable-5-1. Findings resolved: self-removing route listener, mandatory AXE_SCRIPT, guarded internal navigation with native fallback, explicit focus-restoration rationale, browser-error result group, backdrop reduced-motion assertions. Final 10 Chromium automated check groups pass, including five route round trips with CDP event listener counts returning to baseline and browser-back teardown while open. Existing 40-case regression suite passes. Review suggestions about persisted elements are outside this example, which uses no transition:persist. Assistive-technology and real-device limitations remain.

Version-Timestamp: 2026-10-14 15:15:59 AST

Known native Safari finding: plain Tab with the authoring browser keyboard preference moved focus outside the dialog. Option+Tab and Option+Shift+Tab wrapped correctly. Drawer native testing and speech announcements remain incomplete. See the repository docs/SAFARI-CHECKPOINT.md. Chromium results above do not establish Safari or screen-reader acceptance. Detailed raw review receipts stay in private maintainer storage and are not bundled. AI review is advisory and does not grant production acceptance.
