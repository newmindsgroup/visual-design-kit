# Verification and evidence

Version-Timestamp: 2026-10-14 11:13:07 AST

Copy the standalone example to a new project-owned or ignored working directory before dependency installation. The installed plugin library is read-only for adopters. Keep node_modules, .astro, dist, QA outputs and client assets out of reusable payloads. Use the example lockfile with npm ci; verify the installed Node/package-manager constraints. Installing dependencies executes third-party code, so use the environment's vetting and authorization policy.

Example checks: npm test, npm run check, npm run check:vue, npm run build. The optional tests/browser.mjs uses verified Playwright and axe-core installations supplied through PLAYWRIGHT_MODULE and AXE_SCRIPT, plus an optional CHROME_EXECUTABLE. Launch preview bound to 127.0.0.1 and pass MOTION_BASE_URL/MOTION_QA_OUTPUT. Do not claim skipped optional QA ran.

Exercise each selected effect's observable property or state change. Include pointer/focus feedback, keyboard controls, no-JS initial content, normal/reduced/live-preference changes, pause/resume, touch/coarse pointers, narrow overflow, route/back/repeated cleanup and graphics context failure. Inspect desktop/mobile screenshots. Browser screenshots alone do not verify animation over time; pair with behavior/frame evidence.

Measure payload/long tasks/frame spacing when relevant and record method/hardware/budget. Lab headless results are not field Core Web Vitals or real-device smoothness. Browser emulation does not prove Safari, Firefox, assistive technology or physical touch support. Preserve failed logs and distinguish harness defects from runtime failures.

Before plugin packaging, use the owner build helper, verify catalog entries/reference paths and exact payload hashes, inspect archive contents for dependencies/caches/secrets, and keep the old installed cache for rollback. Refresh through supported installation tools only when authorized; verify installed bytes and state. Existing project pins stay unchanged. Publishing/team distribution remains separate from local installation.

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-14 11:13:07 AST
