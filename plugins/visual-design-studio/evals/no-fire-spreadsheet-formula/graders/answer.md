---
type: llm
weight: 1
---

Passes if the response gives a working Google Sheets formula such as `=SUMIFS(C:C, D:D, "Paid", B:B, ">="&EOMONTH(TODAY(),-1)+1, B:B, "<="&EOMONTH(TODAY(),0))` (or an equivalent SUMPRODUCT/QUERY/FILTER approach that limits to the current month and status "Paid"), and briefly explains it. Fails if the date condition is missing or wrong.
