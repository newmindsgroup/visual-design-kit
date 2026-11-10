---
max_turns: 20
timeout_seconds: 420
allowed_tools: [Read, Glob, Grep, Skill]
---

We're building a SaaS billing app in Next.js with shadcn/ui on the Radix base. package.json has next, react 19, tailwindcss 4, the @radix-ui packages shadcn installed, lucide-react and motion. A teammate hand-rolled our notifications: a useState array of divs fixed bottom-right that disappear after 2 seconds, and we also use it to show "Payment failed - Retry". Next we need a bottom drawer for plan details on mobile, a Cmd+K command menu for admins, and the price on the pricing page should animate when you switch monthly/annual. Which library should we use for each, how do we install it, and what should we change?
