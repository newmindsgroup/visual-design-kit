---
max_turns: 20
timeout_seconds: 420
allowed_tools: [Read, Glob, Grep, Skill]
---

We're building the project settings screen for our SvelteKit app (Svelte 5, no component library yet). It has a project name field, a visibility select, a members table with about 30 rows where each row has a role menu and a Remove button, notification switches, and an API key that we show once after you create it. Our in-app assistant and browser agents like ChatGPT's should be able to change these settings for people. Nothing exists in the repo yet, so don't look for files. Which UI library should we build it on, and how do we make the screen safe and easy for an agent to operate?
