---
type: llm
weight: 3
---

Passes only if the response:
- Puts Pix first or prominently, with a QR code AND a "Pix copia e cola" copy-paste code with a copy button, plus an expiry time and a waiting/confirmation state.
- Shows a Pix price (often discounted) next to the card price, and card installments in the local format, for example "12x de R$ 102,88 sem juros".
- Includes boleto bancário (with its delayed confirmation explained) or explains why it is omitted.
- Includes a CPF field with a mask (000.000.000-00) and real validation, and explains why it is needed.
- Formats prices the Brazilian way: "R$ 1.234,56" (dot thousands, comma decimals).
- Gives sample copy in Brazilian Portuguese (pt-BR) for the buttons and labels, while the rest of the answer stays in English.
- Mentions LGPD or consumer-code (CDC) implications, or trust signals such as Reclame Aqui, in at least one line.
