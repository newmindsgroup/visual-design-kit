---
id: market.brazil-portuguese
axis: market
name: Brazil
aliases: [Brasil, Brazilian market, pt-BR, Brazilian Portuguese, Pix market]
summary: Portuguese-speaking, mobile-first market where Pix, boleto and card installments shape checkout, LGPD and consumer code rules apply, and WhatsApp is the default channel.
tags: [brazil, brasil, portuguese, pt-br, pix, boleto, lgpd, whatsapp, cpf, installments]
pairs_with: [industry.fintech-banking, industry.ecommerce-dtc, industry.marketplaces-platforms, industry.food-beverage-cpg, industry.beauty-cosmetics, style.playful-bubbly, style.vibrant-gradient-saas, channel.native-app, channel.social-media, audience.low-bandwidth-entry-devices]
avoid_with: []
version_timestamp: __TS__
---

# Brazil

## Language and script

- Brazilian Portuguese (`pt-BR`), Latin script with ã õ ç and accents (á é í ó ú â ê ô à). It differs from European Portuguese in vocabulary and grammar: tela, celular, ônibus, café da manhã, "você" versus pt-PT telemóvel, autocarro, "tu". The 1990 orthographic agreement is in force in Brazil. Never reuse pt-PT copy.
- Register: "você" is standard in apps and ads; "tu" is natural in the far south (Rio Grande do Sul) and parts of the north and northeast; "o senhor / a senhora" for older customers in finance and healthcare. Tone is warm and personal; diminutives (um minutinho) and exclamation appear in consumer copy but should be used with care in regulated contexts.
- Inclusive language: "todes" and "@" are used in some communities but are contested and not standard; prefer neutral rewording (pessoas, equipe) in broad communications and offer "nome social" (social name) fields.
- Reading: plain language works; Brazil has high functional-literacy challenges in some segments (INAF studies; verify), so favor short sentences, icons paired with text and audio/video explainers.
- Indigenous languages (Tupi-Guarani, Nheengatu, Kaingang and others) and sign language (Libras) are official; provide Libras video for public-service content where relevant.
- Expansion: English to Portuguese +20-30%; Portuguese labels like "Finalizar compra" and "Meus pedidos" need button room.

## Typography and layout

- Fonts with Latin Extended-A and accented capitals: Inter, Poppins, Nunito, Montserrat, Roboto, Open Sans, DM Sans. Serif options: Source Serif 4, Merriweather, Lora.
- Body 16px, line-height 1.5; marketplaces use dense card grids, price-forward typography and small supplementary text; keep minimum 12px for secondary text, 14px for important info.
- Price display: "R$ 1.234,56" with the number prominent, cents smaller and raised, and installments below: "12x de R$ 102,88 sem juros". Show the Pix price (often discounted) alongside the card price.
- Mobile-first: design at 360-412px width; ensure tap targets of 44px or more; sticky "Comprar" buttons.
- Hyphenation: set `lang="pt-BR"`; use `hyphens: auto` in narrow columns.
- Print: A4; envelopes and forms follow Correios formats; Portuguese uses full-width legal text blocks in contracts, so layered summaries help.

## Color and symbolism

- Green, yellow, blue and white (national flag) carry pride. Since 2018 the green-and-yellow palette and the yellow national football shirt have been used as political symbols by some movements; check context before leaning on a flag palette in civic, media or nonprofit work.
- Football (futebol) team colors are strong identities (Flamengo red and black, Corinthians black and white, Palmeiras green, Grêmio blue, etc.); avoid combos that read as a rival jersey in sports-adjacent campaigns.
- Purple is linked to mourning and Lent in Brazilian Catholic culture, and also appears in fintech branding (Nubank's purple is a major example), so context decides; black and white at funerals; white at Réveillon (New Year's Eve, with offerings to Iemanjá).
- Warm saturated palettes are common in consumer categories, while finance and healthcare tend to blue, green and purple. Ensure contrast; yellow-on-white text fails.
- Festival palettes: Carnival (Feb/Mar), Festas Juninas (June), Black Friday (November) and Natal (December); retailers refresh color accents seasonally.

## Imagery and representation

- Brazil's 2022 census (IBGE) reports about 45% pardo (mixed), 10% preto (Black) and 43% white, with Indigenous and Asian minorities (verify); majority of Brazilians identify as Black or mixed. Ads historically under-represented Black Brazilians; show Black and mixed people as leads in everyday, professional and aspirational roles, not only in sports, music or service roles.
- Regional variety: the Northeast, North, Southeast, South and Center-West differ in accents, food and climate; avoid using Rio beaches, Carnival, samba and favelas as the default for all Brazil. The largest cities (São Paulo, Rio) are only part of the audience; include interior cities and rural life.
- Gender and body diversity are watched by consumers and regulators; the advertising self-regulator CONAR reviews complaints on stereotypes, children's advertising and sexualization.
- Influencers must label paid content (CONAR guidance: "publi", "publicidade"); do not disguise ads.
- Religion: Catholic and Evangelical majorities, with Afro-Brazilian religions (Candomblé, Umbanda), spiritism and others; avoid religious symbolism in commercial contexts unless the brand has standing.
- Family and community imagery works, but include singles, same-sex couples, single parents and chosen families.

## Formats and conventions

| Item | Convention | Example |
| --- | --- | --- |
| Date | DD/MM/YYYY; long: 20 de outubro de 2026 (lowercase month) | 20/10/2026 |
| Time | 24-hour | 15h30 or 15:30 |
| Number | Period thousands, comma decimal | 1.234.567,89 |
| Currency | R$ followed by a no-break space | R$ 1.234,56 |
| Address | Rua/Avenida, number, complemento, bairro, city, UF, CEP | Av. Paulista, 1000, Bela Vista, São Paulo, SP, 01310-100 |
| Phone | +55 (DDD) 9XXXX-XXXX; mobile has 9 digits with a leading 9 | +55 (11) 91234-5678 |
| Tax ID | CPF (11 digits) for people, CNPJ (14 digits) for companies | 123.456.789-09 |
| Name | Given name plus one or more surnames; "nome social" option | |

- CEP autofill (ViaCEP is a widely used public lookup) saves typing; keep editable fields for bairro and complemento.
- CPF is required at checkout for invoices (nota fiscal) and most banking; validate check digits, mask input (000.000.000-00), and explain why you ask. Foreign users need a passport alternative flow.
- Weekday names are lowercase; months are lowercase; use "R$" not "BRL" in UI.

## Platforms, devices and payments

- Android holds roughly 80% of mobile traffic (StatCounter; verify), with many mid- and entry-level devices; prepaid and data limits push users to lightweight apps and WhatsApp unlimited plans (zero-rating).
- WhatsApp is the default customer channel for sales and support; Instagram, TikTok, YouTube, Kwai and Facebook lead social. Marketplaces: Mercado Livre, Shopee, Amazon Brasil, Magazine Luiza, Americanas, Shein, Temu; iFood for food delivery.
- **Pix** (Banco Central do Brasil instant payment, launched November 2020) accounts for about half of all payments transactions by count (Central Bank report, November 2025; verify), with 24/7 settlement, QR codes and the "Pix copia e cola" copyable code. Pix Automático (recurring pay) launched in 2025. Design: QR plus copy-and-paste string, 15-30 minute expiry timer, auto-confirmation, and receipt. Offer a Pix discount (5-10% is common) where margins allow.
- **Boleto bancário:** barcode slip (linha digitável) with due date for unbanked or cash-preferring users; show the PDF, copy button and expiry; cancellation if unpaid in a few days.
- **Credit card with installments (parcelamento):** up to 10-12x "sem juros" is a standard expectation. Debit, Nubank, Mercado Pago, PicPay, PagBank, Itaú, Bradesco, Banco do Brasil, Caixa are well known; Apple Pay and Google Pay are available. Open Finance Brasil enables bank-account sharing and payment initiation.
- Retailer store credit ("crediário") and lottery shops (lotéricas) for cash payment remain relevant for lower-income segments.
- Super-app patterns: unified wallets, bill payment, and Pix inside shopping apps are commonplace.

## Regulatory and compliance notes

- **Privacy (LGPD, Law 13.709/2018):** ten legal bases (not only consent); consent must be free, informed, unambiguous and specific; publish a DPO (encarregado) contact; provide a channel for data-subject rights (access, correction, deletion, portability); ANPD enforces and was converted to a regulatory agency in 2026 (verify). Cookie banners should separate non-essential categories and avoid pre-ticked boxes.
- **Consumer Defense Code (CDC, Law 8.078/1990):** 7-day withdrawal right for distance purchases (art. 49), clear price and total, Portuguese-language information, and the e-commerce Decree 7.962/2013 requiring seller identification (name, CNPJ, address), clear contract summary, easy cancellation and customer service channels. The "SAC" decree (11.034/2022) sets customer service standards for regulated sectors.
- **Children:** ECA Digital (Law 15.211/2025) took effect in March 2026 for digital products likely to be used by minors: age verification beyond self-declaration, parental supervision tools, limits on advertising to minors; verify scope and ANPD guidance.
- **Accessibility:** Brazilian Inclusion Law (LBI, Law 13.146/2015, art. 63) requires accessible websites for companies with presence in Brazil; government sites follow eMAG. Target WCAG 2.2 AA and Libras where relevant.
- **Advertising:** CONAR code; influencer disclosures; financial promotions under Central Bank and CVM rules.
- Confirm requirements with counsel for the specific product and jurisdiction.

## Localization pitfalls

- Using pt-PT assets or machine translation; Portuguese users from Portugal notice Brazilian terms and vice versa.
- Checkout without Pix or boleto, or hiding installments; cart abandonment rises when a CPF field is missing, unclear or fails validation of a valid number.
- Displaying US-style dates or prices; confusing "1.234,56" with "1,234.56".
- Valentine's Day is June 12 (Dia dos Namorados) in Brazil; Mother's Day is the second Sunday of May; Black Friday is a major retail event; the 13th salary (décimo terceiro) boosts November-December spending.
- Seasons are reversed: Christmas is summer, so avoid snow-only imagery.
- Short "Fale conosco" contact paths without WhatsApp or phone; customers expect human support.
- Assuming a landline-style phone format; mobile numbers must accept the ninth digit.
- Treating Brazil as Spanish Latin America; language, payments and law differ.

## Reference anchors

- Banco Central do Brasil, Pix documentation and brand guide (bcb.gov.br/estabilidadefinanceira/pix)
- Nubank design and brand work as a public reference for Brazilian fintech
- ANPD (gov.br/anpd) LGPD guidance; Procon and Senacon consumer guidance
- eMAG (accessibility model for Brazilian government sites) and Brazil's Gov.br design system
- Academia Brasileira de Letras, VOLP (Vocabulário Ortográfico) for orthography
- IBGE census data for demographics
