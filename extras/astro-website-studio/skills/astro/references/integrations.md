# Integration decisions and AI documentation

Version-Timestamp: 2026-10-14 10:29:10 AST

The Astro directory includes community submissions. Listing or download count is not a security review. Verify exact package identity, publisher, source repository, license, maintenance, peer-version compatibility, runtime support, permissions, and data flows before adoption. Record purpose and alternatives. Apply the environment's third-party vetting process before client or production use.

| Need | Candidate | Selection rule |
| --- | --- | --- |
| Sitemap | @astrojs/sitemap | Configure canonical site URL and exclude private/draft routes |
| Markdown with components | @astrojs/mdx | Add only when plain Markdown cannot meet authoring needs |
| React interaction | @astrojs/react | Reuse React where justified; hydrate only interactive components |
| Documentation product | Starlight | Evaluate its navigation/search model against the brief |
| Request-time hosting | Matching Vercel, Cloudflare, Netlify, or Node adapter | Verify exact feature and runtime compatibility |
| Tailwind styling | Current Tailwind Vite integration | Follow version-matched docs; legacy @astrojs/tailwind is for Tailwind 3 |

Astro >=5.2 supports astro add tailwind installing @tailwindcss/vite for Tailwind 4. Do not equate this command with the legacy Astro Tailwind package. Preserve existing styling unless a change is requested. Current Vercel examples import from @astrojs/vercel; check the installed adapter version.

Astro's official docs MCP uses Streamable HTTP at https://mcp.docs.astro.build/mcp and a remote kapa.ai-backed documentation index. It is optional. Use direct official docs as a fallback. Configure it only when authorized and vetted; do not change global tool configuration as a side effect of using this skill. Send generic or sanitized technical questions. Do not send client source, private URLs, credentials, or internal architecture without specific data approval. Never represent docs retrieval as code execution or runtime verification.

For forms or CRM connections, specify destination, validation, spam controls, user feedback, timeout/error handling, privacy, and duplicate prevention. Use mocks or approved test destinations until a live write is authorized. Framework form handling does not establish CRM delivery.

Sources: [directory](https://astro.build/integrations/), [AI guidance](https://docs.astro.build/en/guides/build-with-ai/), [styling](https://docs.astro.build/en/guides/styling/), [Vercel adapter](https://docs.astro.build/en/guides/integrations-guide/vercel/).


Forms can post from a static page to an approved external endpoint, or use version-supported Astro Actions/API routes on a compatible server runtime. An external endpoint does not itself require an Astro adapter; request-time Astro handlers do. Verify the relevant Actions/API behavior and server-only environment facilities before choosing an implementation.

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-14 10:32:00 AST
