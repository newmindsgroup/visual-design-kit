---
type: llm
weight: 1
---

Passes if the response gives a correct PostgreSQL query that joins customers and orders on customer_id, filters created_at to the last 90 days (for example `created_at >= now() - interval '90 days'`), groups by customer, sums total_cents (optionally converting to currency units), orders by the sum descending and limits to 5. Fails if it omits the date filter or the grouping.
