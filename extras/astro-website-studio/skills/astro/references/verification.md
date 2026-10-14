# Observable acceptance

Version-Timestamp: 2026-10-14 10:29:10 AST

Read project quality-gate configuration and package scripts. Use the project's package manager to run applicable checks. A typical project needs Astro diagnostics (astro check with its required dependencies), build, and appropriate tests/lint. Do not invent scripts, silently add tooling, or treat astro build as a typecheck. Record exit statuses and missing checks.

Inspect rendered desktop and mobile pages with actual browser evidence. Exercise changed navigation, keyboard/focus, hover, reduced motion, loading, errors, and no-JS behavior where relevant. Check image dimensions/alternatives, content layout, and accessible form feedback. Verify browser console and network failures.

For public content, inspect production output for titles, descriptions, canonical URLs, locale/hreflang behavior, structured data, robots, sitemap, redirects, and draft exclusion. On migrations, compare old URLs against the redirect map. A staging robots rule must not accidentally ship to production.

Test forms against an authorized test destination or mock: invalid input, upstream failure, duplicate submission, and success. Record whether downstream receipt was actually confirmed. Test CMS create/edit/preview/publish behavior and update latency with the chosen source when authorized.

Measure a representative production build with declared tooling, environment, and budgets. Compare JS payload and image/font/script behavior. Lighthouse is lab evidence; field Core Web Vitals require real-user data. Do not promise a score before measurement.

Local preview is not proof of deployed adapter behavior. For request-time routes, run adapter-aware checks and, when authorized, verify a preview deployment for caching, runtime compatibility, secrets, errors, and personalization isolation. Record rollback steps before production release. Deployment remains a separate authorization.

Background development-server behavior is version-sensitive. Track the server this task owns and its URL/PID using the supported CLI for the installed version. Verify readiness rather than guessing ports. Stop only task-owned servers and close only task-created disposable browser tabs after review needs are resolved.

Sources: [testing](https://docs.astro.build/en/guides/testing/), [AI/background guidance](https://docs.astro.build/en/guides/build-with-ai/), [deployment](https://docs.astro.build/en/guides/deploy/).


Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-14 10:32:00 AST
