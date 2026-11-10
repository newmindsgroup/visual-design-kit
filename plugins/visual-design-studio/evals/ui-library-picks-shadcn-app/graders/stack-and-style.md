---
type: llm
weight: 2
---

Passes only if the response:
- Starts from what is installed: keeps Radix and `motion`, and does not add GSAP or another animation library for these components.
- Says the new components must be restyled to the product's own tokens (radius, color, type) rather than shipped with shadcn's default theme, or points to a token mapping for shadcn's CSS variables.
- Gives install commands that match the stack (shadcn CLI `add` commands or npm/pnpm package names that exist: `sonner`, `vaul`, `cmdk`, `@number-flow/react`).

Fails if it invents package names or tells the team to copy component code from an unnamed source.
