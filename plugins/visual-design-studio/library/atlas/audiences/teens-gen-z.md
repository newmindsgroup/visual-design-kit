---
id: audience.teens-gen-z
axis: audience
name: Teens and Gen Z
aliases: [teenagers, teens, gen z, young adults, digital natives, students, youth]
summary: Phone-first 13-24 year olds who expect speed, expressive identity and peer-made content; designing for them now also means age assurance, privacy-by-default and no engagement dark patterns.
tags: [teens, gen z, youth, mobile-first, dark mode, social, creators, age assurance, students]
pairs_with: [style.neo-brutalist, style.y2k-cyber, style.collage-mixed-media, style.risograph-print-texture, style.kinetic-experimental-type, style.playful-bubbly, industry.gaming-esports, industry.media-entertainment-streaming, channel.social-media, channel.native-app]
avoid_with: [style.classic-luxury-serif, style.corporate-modern, archetype.ruler]
version_timestamp: 2026-10-20 02:08:35 UTC
---

# Teens and Gen Z

## Who and what they need

- **Two groups under one label.** Ages 13-17 are minors under child-safety law, often on school or shared devices, with parents as co-owners of money and consent. Ages 18-24 are adults with their own payment methods, jobs and housing decisions. Segment before designing.
- **Needs:** identity expression (themes, avatars, profile control), speed (no signup wall, no waiting), peer validation and belonging, privacy from parents, brands and strangers, and money-conscious choices (student pricing, transparent fees).
- **Context:** portrait phone, one thumb, bursts of attention between other apps, sound off in public, cheap data plans and mid-range Android devices alongside iPhones; school-managed Chromebooks and restricted networks.
- **Skepticism:** they detect corporate "youth speak" instantly. NN/g's teen usability studies (2005, 2013) found teens less patient and less successful at tasks than adults, and they rejected condescending "teen" styling in favor of clear, fast sites.

## Design defaults

| Variable | Default for this audience | General default | Source or reasoning |
| --- | --- | --- | --- |
| Minimum body text | 16px body; UI labels 13px floor; captions never below 12px | 16px | WCAG has no minimum size; teens read on small screens in poor light |
| Target size | 48px, bottom-reachable primary actions, bottom tab bar of 3-5 items | 44px | Apple HIG 44pt; Material 48dp; one-thumb use |
| Contrast | AA 4.5:1 minimum in both themes; dark mode as a first-class default; body 12-16:1 rather than pure white on pure black | 4.5:1 | WCAG 2.2 SC 1.4.3 and 1.4.11; pure #FFF on #000 is 21:1 and causes halation |
| Reading level | Grade 6-8, conversational, 15 words per sentence, UI strings under 20 words | Grade 8 | plainlanguage.gov; slang dated within months, so keep it rare |
| Line length | 35-50 characters on mobile; captions two lines maximum | 60-75ch | Small viewports, scan reading |
| Motion | 150-250ms, physics-based springs, gesture-driven; honor reduced motion; no autoplay-by-default for minors | 120-240ms | WCAG 2.2 SC 2.2.2; regulators target autoplay and infinite scroll for minors |
| Information density | Medium-high, visual-first, vertical 9:16 cards; at most 5 top-level destinations | Medium | Feed conventions set expectations |
| Session length | Micro-sessions of 30-90 seconds many times a day; resume instantly where they left off | Task-based | Working default; pair with break prompts for under-18 accounts |
| Error tolerance | Low patience: signup in 3 steps or fewer, passkey or phone-number login, optimistic UI, instant undo, skeleton screens | Standard | NN/g teen studies on impatience; thresholds are working defaults |
| Notifications | Quiet hours on by default for under-18 (for example 22:00-07:00), user-tunable | Opt-in | Addictive-feed and minors' laws in several jurisdictions (verify) |

## Interaction and content

- **Onboarding:** let people browse before account creation; offer passkey, Apple/Google sign-in and phone number; ask for date of birth with a neutral age screen (no "must be 13" hint) and route minors to protective defaults.
- **Privacy defaults for under-18:** private profiles, no stranger DMs, location off, no ad personalization, clear one-tap report and block.
- **Customization:** themes, accent colors, app icons and profile layouts are features, not decoration; persist across devices.
- **Social proof:** creator and peer content beats brand voice; show real user content with consent and moderation.
- **Payments:** minors lack cards; design parent-approval requests, prepaid and gift-card flows, and show total cost before any purchase.
- **Wellbeing:** "take a break" prompts, a visible usage summary, no punitive streak loss, crisis resources in sensitive categories.
- **Copy:** short, direct, honest; humor in low-stakes moments only; no emoji-as-icons substituting for labels.

## Visual tone

- **Dark first, high chroma, one loud accent.** Ink #0F0F14 (oklch 0.17 0.010 285) with text #ECECF1 (oklch 0.94 0.007 286) is 16.23:1; lime #C7F23B (oklch 0.90 0.202 122) on that ink is 14.74:1; hot pink #FF4D6D (oklch 0.68 0.213 15) is 5.95:1; secondary text #8B8B99 (oklch 0.64 0.021 286) is 5.69:1. Violet #7C5CFF (oklch 0.60 0.230 286) is only 4.40:1, so keep it for large elements, and avoid the default purple-to-pink gradient.
- **Type:** expressive display (Bricolage Grotesque, Unbounded, Familjen Grotesk, all OFL) with a plain body face (DM Sans, Instrument Sans). Commercial: GT America, Neue Montreal.
- **Style:** stickers, collage, grain, riso texture, hand marks, big cropped type, thick outlines. Authenticity beats polish, but body text stays clean.
- **Imagery:** user-generated, vertical, unretouched; diverse by default; avoid stock "students laughing at laptops".
- **No single "Gen Z look".** A 14-year-old gamer and a 23-year-old grad-school applicant share a generation label, not a taste.

## Pitfalls

- Slang and memes as decoration ("How do you do, fellow kids"); they age faster than a design cycle.
- Treating ages 13-17 like 18-24; the legal and consent models differ.
- Infinite scroll, autoplay, streak loss and variable rewards by default for minors.
- Dark mode only, neon on black for long text, or gray-on-black small print.
- Assuming desktop or the newest iPhone; many teens use cracked, mid-range or school-managed devices.
- Ignoring parents as stakeholders (consent, payments, safety dashboards).
- Overusing emoji as UI and gradients as identity; both are generic.

## Regulatory and compliance notes

Age assurance is moving fast; verify each item as of your launch date.

- **US COPPA** covers under-13 only, so teens are governed by other rules: state teen-privacy and social-media age and parental-consent laws, many litigated (verify current injunctions); addictive-feed laws such as New York's SAFE for Kids Act and California SB 976 restrict algorithmic feeds and overnight notifications to minors (verify status). App-store age-verification acts (Utah, Texas, Louisiana; Texas enjoined in litigation; California from 2027) are in flux.
- **UK:** the ICO Children's code covers under-18s. The Online Safety Act's Ofcom children's codes have been in force since 25 July 2025, requiring "highly effective age assurance" for pornography and other primary priority content, plus protective design for other services likely to be accessed by children. The government has signaled under-16 social media restrictions (reported timing 2027; verify on gov.uk and Ofcom).
- **Australia:** the Social Media Minimum Age law took effect 10 December 2025; age-restricted platforms must take reasonable steps to keep under-16s from holding accounts.
- **EU:** DSA Article 28 guidelines (2025) recommend high-privacy defaults and age verification for high-risk services, and Article 28(2) bars profiling-based ads to known minors. An EU age-verification app blueprint is being piloted by several member states (verify progress); GDPR Article 8 sets parental consent at 13-16 by country.
- **Design impact:** privacy-preserving age checks (estimation, ID, carrier or bank signals) with non-biometric fallbacks, minimal data retention, protective defaults when age is unknown or under threshold, and no profiling-based ads for minors.

Confirm requirements with counsel for the specific product and jurisdiction.

## Reference anchors

- Nielsen Norman Group teen usability reports (*Usability of Websites for Teenagers*, 2005; updated 2013; verify edition)
- Pew Research Center, *Teens, Social Media and Technology* (annual survey; verify the latest edition)
- UK ICO Children's code; Ofcom Protection of Children Codes; Australia eSafety Commissioner guidance
- Duolingo, Discord and Spotify for expressive identity, friendly tone and playful but legible UI
- Apple Human Interface Guidelines for Screen Time and parental-control patterns
- Neo-brutalist and zine-influenced creator brands for visual-language references (study, do not copy)
