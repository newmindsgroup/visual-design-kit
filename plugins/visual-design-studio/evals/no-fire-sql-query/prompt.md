---
max_turns: 6
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
---

For our revenue dashboard, write a PostgreSQL query that returns the top 5 customers by total order value in the last 90 days. Tables: customers(id, name) and orders(id, customer_id, total_cents, created_at).
