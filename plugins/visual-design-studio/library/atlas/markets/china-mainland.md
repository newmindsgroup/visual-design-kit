---
id: market.china-mainland
axis: market
name: Mainland China
aliases: [China, PRC, Chinese market, Simplified Chinese, zh-CN, zh-Hans, WeChat ecosystem, Great Firewall]
summary: Simplified-Chinese mobile super-app market where WeChat, Alipay and Douyin dominate, info-dense interfaces are normal, and PIPL, ICP licensing and ad-law rules shape design and hosting.
tags: [china, mainland china, simplified chinese, wechat, alipay, mini program, icp, pipl, douyin, cjk]
pairs_with: [industry.ecommerce-dtc, industry.beauty-cosmetics, industry.luxury-goods, industry.fashion-apparel, industry.gaming-esports, industry.media-entertainment-streaming, style.maximalist-eclectic, style.vibrant-gradient-saas, channel.native-app, channel.social-media]
avoid_with: []
version_timestamp: __TS__
---

# Mainland China

## Language and script

- Simplified Chinese (`zh-Hans-CN`, Han script, several thousand commonly used characters), standard Mandarin (Putonghua). Cantonese is spoken in Guangdong but written Chinese is shared; Hong Kong, Macau and Taiwan use Traditional characters and different vocabulary, so treat them as separate markets (`zh-Hant-HK`, `zh-Hant-TW`). Ethnic-minority scripts (Uyghur, Tibetan, Mongolian) appear in autonomous regions. English is used for premium and tech branding but rarely carries a mass-market message.
- Always set `lang="zh-Hans"` or `zh-CN`; without it browsers may choose another regional Han glyph variant (for example 骨, 直, 海 look different in Japan, Korea and Taiwan).
- Software sold in China is expected to support GB 18030 (verify the current edition).
- Tone and copy: crisp, upbeat, benefit-led; four-character phrases and rhythm are valued. Official or financial copy is formal; social copy is playful with internet slang that changes quickly (use local writers). Use 您 (formal "you") for banking, healthcare and premium brands; 你 for youth and casual apps.
- Names: brand names need a Chinese name that sounds right and carries good meaning; check homophones and tones in Mandarin and Cantonese (a classic case is Coca-Cola's 可口可乐). Number symbolism: 8 (八, fā, wealth) and 9 (久, long-lasting) are favored; 4 (四, sì) sounds like death and is avoided in pricing and numbering; 520 reads as "I love you" in slang.
- **Advertising law:** superlatives such as 最 (most), 第一 (No. 1), 顶级, 国家级 ("best", "top-tier", "national-level") are prohibited in ads unless substantiated by law (Advertising Law, Art. 9). Copy needs legal review.
- Text expansion: Chinese uses about 30-50% fewer characters than English, but each is a full-width square, so area is similar. Buttons are 2-4 characters (立即购买, 加入购物车). Chinese measure words (个, 件, 条) must be planned for counts: 共 3 件商品.
- Production: use unambiguous simplified forms; avoid machine-converted Traditional/Simplified; proof by native editors.

## Typography and layout

| Item | Default | Override when |
| --- | --- | --- |
| Fonts (open) | Noto Sans SC / Noto Serif SC and Source Han Sans / Serif (OFL), LXGW WenKai (OFL, Kai style), ZCOOL (OFL, display), Smiley Sans (OFL) | Brand voice |
| Fonts (free-to-use, own licenses) | HarmonyOS Sans SC, MiSans, OPPO Sans, Alibaba PuHuiTi 3.0 | Check each license before bundling |
| System stack | "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif | Best default for web performance |
| Body size | 14-16px mobile, 14-16px desktop; secondary 12px minimum | Elderly mode: 18-20px+ |
| Line-height | 1.6-1.8 body, 1.3-1.5 headings | Dense lists: 1.5 |
| Letter-spacing | 0 to 0.05em on body; never negative | Display may tighten slightly |
| Weights | 400/500/700; avoid Light at small sizes | Heavy display 900 for campaigns |

- Fonts are large (4-20 MB per weight): use system fonts first, or subset by character frequency/unicode-range (Google Fonts slices Noto Sans SC, but Google Fonts is unreliable in mainland China, so self-host or use a China-accessible CDN). Set `font-display: swap`.
- **Punctuation:** full-width ，。、；：？！; curly quotes “ ” and ‘ ’ in mainland usage; ellipsis ……(two characters), dash ——(two characters); book titles 《》. In Mainland horizontal text the period sits bottom-left; Taiwan centers it. Never begin a line with closing punctuation or end one with opening punctuation: use `line-break: strict` and avoid manual breaks. Add a thin space (about 0.25em) between Han and Latin letters or digits, or use `text-autospace` where supported.
- Justified text is acceptable for Chinese because characters are equal width; italics are not used (use bold, color or emphasis dots via `text-emphasis`). Do not use uppercase transforms for CJK.
- **Vertical text** (`writing-mode: vertical-rl`) is traditional but is used mainly in decoration, poetry, seals, packaging for tea and liquor; punctuation shifts to the upper right in vertical text. Avoid for UI and body copy.
- Layout: information-dense mobile pages with banners, coupons, countdown timers, ranking lists, red badges and floating buttons are normal; user expectation is value and social proof. Premium and luxury brands succeed with restraint, but still show product details, KOL proof and shopping cues. Use WeUI (WeChat), Ant Design (Ant Group), TDesign (Tencent) and HarmonyOS design guidelines for platform-native patterns.
- Mini programs: keep content out of the WeChat capsule area (top-right menu, roughly 87 x 32 pt; verify the current spec) and respect safe areas.
- Elder-friendly mode (关怀模式, large fonts, simplified screens) is a recognized regulatory and market expectation for major apps.

## Color and symbolism

- Red signals luck, joy and prosperity (weddings, Spring Festival, red envelopes/hongbao); gold signals wealth. Red-and-gold is festive but easy to overuse; tint it for luxury.
- Yellow was an imperial color but "yellow" (黄色) also means pornographic in slang; use with context. White is associated with mourning in traditional contexts, though modern brands use it for purity and tech; black is formal or mourning. A green hat (绿帽子) implies a cuckold: avoid green hats in imagery and merchandise.
- Stock and finance: red means rising and green falling in mainland charts (reverse of the US). Do not copy Western chart colors; follow the platform convention.
- Guochao (国潮, "national trend") mixes traditional motifs with modern design for young consumers; use real craft references, not generic dragons.
- Seasonal palettes: Spring Festival (lunar new year, red/gold), Qingming (somber), Dragon Boat (green), Mid-Autumn (moon, gold, deep blue), Singles' Day 11.11 (red/pink/bright), 618 shopping festival, 520/Qixi (romance), Golden Week (Oct 1). Dates follow the lunar calendar; verify annually.

## Imagery and representation

- Represent contemporary China: tier-1 megacities, new-tier cities and lower-tier towns, with working professionals, families, students, elders, rural entrepreneurs and livestream sellers. Avoid orientalist tropes (red lanterns everywhere, kung fu, pagodas, pandas for every brand, chopstick props) unless culturally apt.
- Models: local casting with familiar celebrity endorsement and KOL/KOC partnerships is standard. Foreign-looking models in mass-market ads can feel premium or alien depending on category.
- Politically sensitive topics and symbols are legally risky: Taiwan, Hong Kong, Tibet, Xinjiang, Tiananmen, territorial disputes. Maps must use state-approved standard maps; incorrect borders or omitting Taiwan are treated as "problem maps" with penalties. The national flag and emblem cannot be used in trademarks or commercial advertising.
- Avoid clocks as gifts (送钟 sounds like "attending a funeral"), sharing pears (分梨 sounds like parting) and the number 4 in gift sets.
- Content standards: no content that harms national image, promotes superstition, or targets minors improperly; AI-generated content must be labeled.
- Beauty and body norms are intense; avoid lookism and appearance anxiety messaging; regulators scrutinize ostentatious displays of wealth and content that reaches minors.

## Formats and conventions

| Item | Convention | Example |
| --- | --- | --- |
| Date | YYYY年M月D日 or YYYY-MM-DD; lunar dates for festivals | 2026年10月20日 |
| Time | 24-hour; 上午/下午 colloquially | 15:30 |
| Number | Western digits; large numbers in 万 (10^4) and 亿 (10^8) | 1.2万, 3.4亿 |
| Currency | CNY ¥ (or ￥ full-width) or 元; two decimals | ¥1,234.56 or 1,234.56元 |
| Address | Province, city, district, street, number, building, room (big to small); 6-digit postal code | 上海市浦东新区世纪大道100号 |
| Phone | +86, 11-digit mobile starting 13-19; login by SMS code | +86 138 0013 8000 |
| Name | Family name first (王小明); separate 姓 and 名 fields; sort by pinyin | |
| ID | 18-digit resident ID with check digit X; needed for real-name services | Mask; collect only when required |

- Consumer prices include VAT; Fapiao (发票, official invoices) are requested at checkout, especially by businesses; provide an "request invoice" flow.
- Online purchases generally allow a 7-day no-reason return (Consumer Rights Protection Law), with exceptions; show return rules clearly.
- Week starts Monday in official calendars; many apps start on Sunday; make it configurable.

## Platforms, devices and payments

- WeChat (Weixin) is the daily super app: messaging, Moments, Official Accounts, Mini Programs, WeChat Pay, Channels. Others: Douyin (TikTok's China app), Xiaohongshu (RED), Weibo, Bilibili, Zhihu, Kuaishou, Taobao/Tmall, JD.com, Pinduoduo, Meituan, Dianping, Didi, Baidu and Amap (Gaode).
- Devices: Android (Huawei, Xiaomi, OPPO, vivo, Honor) and iPhone (roughly a fifth to a quarter of smartphones; verify). Huawei's HarmonyOS NEXT does not run Android apps. Google Mobile Services is absent on mainland Android: no Google Play, FCM, Maps, Fonts or reCAPTCHA. Distribute through OEM stores (Huawei AppGallery, Xiaomi, OPPO, vivo, Tencent) and the Apple App Store China with local filing.
- Payments: **Alipay** and **WeChat Pay** (QR-based, near-universal), UnionPay cards and QuickPass, Apple Pay (UnionPay cards), Ant Credit Pay (花呗) and installment options; digital yuan (e-CNY) pilots. International Visa/Mastercard are marginal for domestic sites. Visitors can link foreign cards to Alipay+/WeChat Pay. Cash on delivery is rare.
- Login: WeChat or phone number with SMS code; real-name verification is required for many services. SMS signatures and templates must be pre-approved.
- Hosting and networks: cross-border traffic is slow or blocked by the Great Firewall (Google, YouTube, Facebook, Instagram, X, WhatsApp, many CDNs). Host in mainland China with a local cloud (Alibaba Cloud, Tencent Cloud, Huawei Cloud, Baidu) and use local analytics, push and map SDKs.
- Livestream commerce, group buying and gamified coupons are common growth mechanics; design for fast vertical video.

## Regulatory and compliance notes

- **PIPL** (effective November 1, 2021): consent plus other legal bases; separate consent for sensitive data (biometrics, location, financial, minors under 14), third-party sharing and cross-border transfers; local representative for foreign processors; privacy impact assessments; the Data Security Law and Cybersecurity Law (amended in 2025; verify) add data classification and localization duties. Cross-border transfer needs a security assessment, standard contract or certification, with 2024 relaxations.
- **App rules:** necessary-personal-information lists by app type, privacy dialog at first launch, no forced bundled consent, SDK disclosures, MIIT app filing, and algorithm rules that require users to be able to turn off personalized recommendations.
- **ICP:** websites hosted in mainland China require an ICP filing; commercial sites (e-commerce, content) need an ICP license (value-added telecom permit), generally through a local entity. Display the ICP number (and Public Security filing mark) in the footer.
- **Content and advertising:** Advertising Law (ban on absolute superlatives, claims substantiation, KOL disclosure), AI-generated content labeling (explicit and implicit labels from September 1, 2025), deep synthesis rules, real-name registration, minors' modes and gaming playtime limits, and licensing for games (publication approval).
- **Accessibility:** the Barrier-Free Environment Construction Law (effective September 2023) covers information accessibility; elderly-friendly app campaigns by MIIT.
- **Consumer:** e-commerce law and consumer protection law; clear pricing and return terms.
- Confirm requirements with counsel for the specific product and jurisdiction.

## Localization pitfalls

- Shipping a Western site: Google Fonts, reCAPTCHA, Google Maps, YouTube embeds and CDNs fail or slow to a crawl; no ICP, no hosting.
- Minimalist pages with sparse info are read as untrustworthy for mass-market commerce; but over-dense luxury also fails: calibrate to tier.
- Wrong numbers (4), clocks, green hats, white-and-black funeral combinations; unlucky brand-name translation.
- Western chart colors (green up, red down); date format MM/DD; Western name order.
- Using Traditional Chinese for mainland users, or Simplified for Taiwan and Hong Kong; wrong `lang`, causing wrong glyph variants.
- Payment flows without Alipay/WeChat Pay; login only via email.
- Missing PIPL consent separation; copy with banned superlatives; unlabeled AI content.
- Omitting mini-program and WeChat share cards; poor share-image sizes (5:4, 1:1).

## Reference anchors

- W3C Requirements for Chinese Text Layout (clreq) and Unicode CJK guidance; GB/T 15834 punctuation standard
- Noto Sans/Serif CJK and Source Han (Adobe/Google, OFL); LXGW WenKai
- WeChat Mini Program design guidelines and WeUI; Ant Design; Tencent TDesign; HarmonyOS design guidelines
- Alipay and WeChat Pay merchant documentation; UnionPay brand guidelines
- Lü Jingren (book design) and Han Meilin (Beijing 2008 Fuwa mascots) for contemporary Chinese design; Li-Ning and Florasis as public "guochao" brand examples
- CAC (cac.gov.cn) and MIIT announcements for algorithm, AI labeling and app rules
