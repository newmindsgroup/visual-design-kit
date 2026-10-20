---
type: llm
weight: 3
---

Passes only if ALL of these hold:
- Names a specific Arabic typeface (for example IBM Plex Sans Arabic, Noto Naskh Arabic, Noto Sans Arabic, Amiri, Readex Pro, Cairo, Tajawal, Almarai or a named commercial Arabic face) AND a Latin face chosen to match its weight and color (for example the same superfamily such as IBM Plex Sans with IBM Plex Sans Arabic, or Noto with Noto), with that matching stated as the reason.
- Sets Arabic body text larger than the English body (roughly 10-20% larger, or a larger point size given explicitly) and with more line-height than the English (Arabic roughly 1.6-1.9 or an equivalent leading in points; English lower).
- States that Arabic must not be letter-spaced/tracked and must not use synthetic italics (emphasis by weight or color instead). One of the two is enough if the other is implied.
- Makes an explicit decision on the numeral system for the Arabic pages (Eastern Arabic-Indic digits ٠-٩ versus Western 0-9), gives a reason tied to Saudi or print/formal context, and says to keep one system per surface or table.
- For the financial tables: tabular (fixed-width) figures, decimal or right alignment of numbers, and how negative numbers or currency are shown; mentions that number direction stays left-to-right inside RTL text or that bidi isolation is needed.
- Addresses RTL page logic for the spread (Arabic page order or binding side, mirrored margins or column order).
Fails if it gives one shared size and line-height for both scripts, or never decides on numerals.
