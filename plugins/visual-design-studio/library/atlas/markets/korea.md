---
id: market.korea
axis: market
name: South Korea
aliases: [Korea, South Korea, Korean market, ko-KR, Hangul, K-wave, Hallyu]
summary: Hangul-script, hyper-connected mobile market where KakaoTalk, Naver and Toss lead, Samsung devices dominate, trends move fast, and PIPA consent rules are among the strictest in Asia.
tags: [korea, south korea, korean, hangul, ko-kr, kakaotalk, naver, toss, pipa, pretendard]
pairs_with: [industry.fintech-banking, industry.beauty-cosmetics, industry.ecommerce-dtc, industry.gaming-esports, industry.media-entertainment-streaming, industry.fashion-apparel, style.vibrant-gradient-saas, style.playful-bubbly, style.y2k-cyber, channel.native-app, channel.social-media]
avoid_with: []
version_timestamp: __TS__
---

# South Korea

## Language and script

- Korean (`ko-KR`) is written in Hangul, a featural alphabet whose letters (jamo) combine into square syllable blocks. Hanja (Chinese characters) are rare outside names, newspapers and legal or academic contexts. Latin appears for brands, loanwords and "Konglish". English proficiency varies; a Korean-language UI is expected.
- **Spacing and breaking:** Korean uses spaces between word groups (띄어쓰기). Use `word-break: keep-all` with `overflow-wrap: break-word` so words are not split mid-block (default CJK breaking splits anywhere); set `line-break: strict`. Hangul has no capitals and no true italics; avoid synthesized slant.
- **Speech levels:** 합쇼체 (formal, ~습니다/ㅂ니다) for banking, government, news and B2B; 해요체 (friendly polite, ~해요) for modern apps and consumer brands (Toss, Karrot style). Avoid 반말 (casual) unless the brand persona is a friend or character. Address customers as 고객님. Be consistent in endings across a product.
- Age: Korea moved to "international age" (만 나이) for most legal purposes in 2023; ask for birth date rather than age, and show 만 N세 where age matters.
- Names: family name first, typically one-syllable family name plus two-syllable given name (김민준). Ask 성 and 이름 as separate fields or one combined field; do not force Western order. Do not require middle names.
- Input: Hangul IME composition fires double-Enter issues like Japanese; test `isComposing`. Normalize text to NFC (macOS file systems and some inputs produce decomposed jamo that break search and equality).
- Text expansion: Korean text is usually within about ±20% of English width; fewer characters but square glyphs and honorific endings lengthen UI strings (e.g., "결제하기", "주문 내역을 확인해 주세요"). Test with real copy.
- Calendars: Gregorian for business; lunar calendar (음력) sets Seollal (Lunar New Year) and Chuseok, the two biggest gifting and travel periods.

## Typography and layout

| Item | Default | Override when |
| --- | --- | --- |
| Sans (open, OFL) | Pretendard (Latin from Inter, Hangul; variable and dynamic-subset builds), Noto Sans KR, IBM Plex Sans KR, SUIT, Wanted Sans, Spoqa Han Sans Neo, Nanum Gothic / NanumSquare | Brand personality; Pretendard is a common modern UI default |
| Serif / Myeongjo | Noto Serif KR, Nanum Myeongjo, Gowun Batang, Hahmlet | Editorial, literary, luxury |
| Rounded / display | Jua, Black Han Sans, Do Hyeon, Gowun Dodum | Playful campaigns |
| Free-to-use, own license | Gmarket Sans, KoPub, Sandoll fonts | Check license terms before bundling |
| System stack | "Pretendard", -apple-system, "Apple SD Gothic Neo", "Malgun Gothic", "Noto Sans KR", sans-serif | |
| Body size | 14-16px (mobile 14-15px common; desktop 16px); secondary 12px minimum | Older users: 16-18px |
| Line-height | 1.6-1.7 body, 1.3-1.4 headings | Dense UI 1.5 |
| Letter-spacing | -0.01em to -0.03em on headings and body is common in Korean UI; 0 for small labels | Do not tighten Hangul below -0.04em |
| Weights | 400/500/700; avoid Thin at small sizes | |

- Full Hangul fonts are heavy (several MB). Use dynamic subsets (Pretendard offers them), unicode-range slicing, or system fonts first. Latin glyphs inside Korean fonts should match your Latin brand font; Pretendard's Inter-based Latin is a practical default.
- Punctuation: modern Korean uses half-width Latin punctuation (, . ? !) with normal spacing, “ ” and ‘ ’ quotes, and ~ for ranges; CJK full-width brackets 「」『』 are formal or literary. Keep Latin/number spacing natural; no extra autospacing needed.
- Layout: Korean apps are polished and mobile-first with card-based, tidy, high-density UIs; bottom tab navigation is common; Toss popularized simple, one-question-per-screen flows with large type; Naver and Coupang pages are dense. Reviews with photos, ratings and "best" ranking sections are standard in commerce.
- Vertical text is rare today; use only for decorative/traditional contexts (hanok, calligraphy, poetry).
- Text in images: avoid; Korean search (Naver) and accessibility need live text.
- Print: A4 and B5 are common; business cards 90 x 50 mm; Korean books read left to right horizontally today.

## Color and symbolism

- Traditional Obangsaek (오방색) five colors: blue (east), red (south), yellow (center), white (west), black (north) appear in hanbok, festivals, packaging and the Taegukgi flag (red/blue taeguk, black trigrams, white field). Use as a reference for heritage-inspired work, not as decoration for everything.
- White: purity and mourning (traditional); black: formal and mourning; red: energy, celebration, football fandom (Red Devils) and also, traditionally, writing a living person's name in red ink is taboo (associated with death). Avoid red text for names.
- Number 4 (사, death) is avoided in elevators, room and gift counts; 3, 7 and 8 are favored.
- Finance charts: red means rising and blue means falling (reverse of the US). Match local platform conventions.
- Local brand colors are strongly recognized: Naver green, Kakao yellow, Toss blue, Coupang red. Avoid color-and-shape combinations that look like their marks.
- Aesthetics: K-beauty favors soft pastels, dewy glass and clean white; K-pop and gaming favor neon, chrome and Y2K revivals; fintech favors high-contrast blue/black with large numerals. Keep contrast accessible.

## Imagery and representation

- Appearance norms are intense (lookism, extensive retouching, cosmetic surgery culture). Avoid body-shaming or appearance-anxiety messaging, and be wary of unrealistic retouching in beauty and health ads.
- Korea has long been ethnically homogeneous but is diversifying (foreign workers, international marriages, migrant families, expatriates); include diverse faces and avoid stereotyping them.
- Gender-related symbols, gestures, slang and imagery can trigger strong online backlash (a 2021 convenience-store poster hand-gesture controversy is a widely cited example). Have local reviewers vet gestures, slang and character poses.
- Rising Sun flag (旭日旗) motifs are offensive; avoid red-white sunburst rays. Maps and names are sensitive: label the "East Sea" (alongside the "Sea of Japan" for international audiences as appropriate), Dokdo, and the Korean Peninsula carefully; avoid casual North Korea references.
- Hierarchy and respect: age and seniority shape tone; show elders with respect, and families at Seollal/Chuseok with gift sets (선물세트). Weddings, 100-day baby celebrations and school exam culture are culturally significant.
- Characters and stickers are big business (Kakao Friends, LINE Friends/BT21): mascots and emoticons suit consumer brands.
- K-culture globalization: Hallyu audiences abroad may expect Korean visual references; avoid pastiche without understanding.

## Formats and conventions

| Item | Convention | Example |
| --- | --- | --- |
| Date | YYYY년 M월 D일 or YYYY.MM.DD | 2026년 10월 20일 |
| Time | 24-hour or 오전/오후 | 오후 3:30 |
| Number | Comma thousands; large numbers in 만 (10^4), 억 (10^8) | 1.2만 원, 3억 원 |
| Currency | KRW (원, ₩), no decimals | ₩12,345 or 12,345원 |
| Address | Road-name address (도로명주소): province/city, district, road + number, detail; 5-digit postal code (우편번호) | 서울특별시 강남구 테헤란로 152 (06236) |
| Phone | +82; mobile 010-1234-5678 | 010-1234-5678 |
| Name | Family name first | 김민준 |
| Identity | Phone-based identity verification (PASS, KakaoTalk, Naver, Toss); resident registration number (주민등록번호) collection is restricted | Avoid collecting the RRN |

- Address search: use a postcode/address search widget (Kakao/Daum Postcode, Juso API) rather than free text; always add detail address (동/호수) field.
- Prices include VAT (10%). Installments (할부, 2-12 months) are shown at checkout.
- Holidays: Seollal and Chuseok (3-4 day breaks) are the biggest gifting seasons; commerce also peaks around Black Friday sale festivals and platform sale days.

## Platforms, devices and payments

- Samsung Galaxy dominates (roughly 70% of smartphones); iPhone is about a quarter and growing (StatCounter; verify). 5G and fixed fiber are among the fastest worldwide; users expect instant loading and polished motion. Foldables and tablets are common among enthusiasts.
- **KakaoTalk** is used by nearly all smartphone owners; Kakao services include Kakao Pay, Kakao Map, Kakao Bank, Kakao T and Alimtalk (business notification messages that replace SMS for transactional notices). **Naver** is both search portal and platform (Naver Search, Blog, Cafe, Smartstore, Naver Pay, Naver Map); Naver SEO is separate from Google SEO. Others: Toss (finance super app), Coupang (Rocket Delivery), Baemin and Yogiyo (delivery), Karrot (Danggeun) local marketplace, Olive Young, Musinsa, Kurly, YouTube, Instagram, TikTok, DC Inside, Band.
- Payments: credit/debit cards with installments, Samsung Pay, Naver Pay, Kakao Pay, Toss Pay, Payco, bank account transfer (계좌이체), virtual-account deposit (무통장입금 with a deadline), mobile carrier billing (휴대폰결제), simple-pay one-click flows. Show app-card verification (ISP/앱카드) and ARS fallback only where needed.
- Maps: Naver Map and Kakao Map dominate; Google Maps navigation has been restricted by domestic map data rules (verify current status), so embed Korean maps for local products.
- Korea's in-app payment law (Telecommunications Business Act amendment, 2021) bars app stores from forcing their own billing; alternative payment options exist.
- Identity and signing: PASS (carrier app), Kakao, Naver and bank certificates replaced the old public certificate (공동인증서) in 2020.

## Regulatory and compliance notes

- **PIPA** (Personal Information Protection Act; PIPC regulator) is strict: consent must be itemized and separate for collection/use, third-party provision, overseas transfer, sensitive data and marketing; required and optional consents must be clearly distinguished and optional consent cannot be a condition of service; the resident registration number cannot be collected without a legal basis; a privacy policy and a chief privacy officer are required; foreign companies above thresholds need a domestic agent. Cookie banners are less prescriptive than the EU, but consent for personal data use must follow PIPA.
- **Marketing messages:** the Network Act requires prior opt-in for ads by phone/text/email, "(광고)" labels at the start, easy opt-out, and separate consent for night-time (9 pm-8 am) sending.
- **E-commerce:** the Act on Consumer Protection in Electronic Commerce provides a 7-day withdrawal right, mandates seller information in the footer (business registration number and mail-order sales report number, 통신판매업 신고번호) and, from February 2025 amendments, restricts dark patterns (hidden renewals, obstructive cancellations, sneak-in items; verify details).
- **AI:** the AI Basic Act (effective January 22, 2026) requires advance notice for generative/high-impact AI and labels on generated content (with a grace period before fines; verify).
- **Accessibility:** the Act on Prohibition of Discrimination against Persons with Disabilities requires accessible websites and apps (KWCAG 2.2, based on WCAG 2.1) for public and many private services; kiosks must be barrier-free.
- **Games:** probability disclosure for random items. **Youth:** age ratings and parental controls.
- Confirm requirements with counsel for the specific product and jurisdiction.

## Localization pitfalls

- Using Japanese or Chinese fonts for Hangul; missing `lang="ko"`; default CJK breaking splitting words mid-block (forgetting `keep-all`).
- Wrong tone: casual 반말 in banking, or stiff 합쇼체 in a friendly app; mixing endings.
- Western address and name forms; free-text addresses without a lookup; mandatory RRN fields.
- Missing KakaoTalk/Naver login, Naver Pay, Kakao Pay, virtual-account deposit and installments; card-only checkout.
- Bundled consent ("I agree to all") without itemized required/optional consents; pre-checked marketing boxes.
- Red-ink names, number 4 numbering, rising-sun sunburst visuals; treating Korea as a Japan variant.
- Not optimizing for Naver search/blog; ignoring Alimtalk for notifications.
- Ignoring the speed expectation: slow loading and unpolished animation feel unfinished.

## Reference anchors

- W3C Requirements for Hangul Text Layout (klreq) and the National Institute of Korean Language orthography rules
- Pretendard (orioncactus/pretendard), Noto Sans/Serif KR, IBM Plex Sans KR; Sandoll and Yoon Design Group for commercial type
- Toss Design System (TDS), Naver Design System (NDS/Naver Design), Kakao Design (Kakao Friends) public guidelines
- KWCAG 2.2 (Korea Web Accessibility Guidelines), the NIA Web Accessibility Quality Mark, and PIPC (pipc.go.kr) guidance
- Ahn Sang-soo (Hangul typographer), Hangul Day and Sejong-era Hunminjeongeum as typographic heritage
- Samsung One UI and Samsung Design System as mobile references
