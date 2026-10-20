# Email design

Version-Timestamp: 2026-10-20 02:07:10 UTC

Email is web design with a 2005 rendering engine, images turned off, a dark mode you do not control and a reader who decides in two seconds. Design a simple single column with live text, a single clear action and a layout that degrades gracefully, then test in real clients. For the channel overview see the atlas entry [email](../../../library/atlas/channels/email.md).

## Layout defaults

| Item | Default | Notes |
| --- | --- | --- |
| Container | 600px wide (600-640px range), centered | Fluid to 100% below about 480px |
| Columns | Single column on mobile; two columns only for short, parallel items on desktop | Stack columns in source order |
| Body text | 16px (14px minimum), line-height 1.5, left-aligned | Centered body text is harder to read beyond two lines |
| Headings | 22-32px, 1.2-1.3 line-height | Real `<h1>`-`<h3>` elements, inline-styled |
| Padding | 24-32px side padding on desktop, 16-20px on mobile | |
| Buttons | 44-48px tall, 16px+ bold text, at least 120px wide, full-width on mobile if primary | Bulletproof HTML, never an image |
| Primary actions | One primary call to action per email; secondary as text links | |
| Images | 2x resolution (1200px wide for a 600px slot), width set by attribute | JPEG for photos, PNG for transparency and flat art, GIF for simple animation |
| Fonts | Web-safe stack first; brand web font as progressive enhancement | Gmail and classic Outlook for Windows ignore most web fonts |

## Structure

1. **Preheader** (hidden preview text): 40-100 characters that complement the subject line. Pad after it so body text does not leak into the preview.
2. **Header:** logo as an image with `alt` set to the brand name, linked to the site; keep it small (logo height about 32-48px).
3. **Hero:** headline in live text, one image or none, the primary button.
4. **Body:** short sections, each with a heading, 1-3 short paragraphs and an optional link.
5. **Secondary content:** cards or a list; single column on mobile.
6. **Footer:** company name and physical postal address, unsubscribe link, preference center, why the reader receives this email, social links as text or small icons with alt text.

Legal and deliverability notes that shape the footer and headers (confirm with counsel and your email service provider): CAN-SPAM (US) requires a valid physical postal address and a working opt-out; CASL (Canada) requires consent and sender identification; GDPR and PECR (EU, UK) require a lawful basis, usually consent, for marketing email. Gmail and Yahoo bulk-sender rules (from 2024) require SPF, DKIM and DMARC, one-click unsubscribe (RFC 8058) and low spam-complaint rates.

## Live text vs images

- Many clients block images by default or for some senders (classic Outlook for Windows, some corporate gateways). An all-image email arrives blank.
- Put every message, headline and call to action in live HTML text. Images support; they do not carry the message.
- Give meaningful images alt text that says what the image communicates; style alt text (font, color, size) so it reads well when images are blocked. Use `alt=""` on decorative images and spacers.
- Never bake the call to action, prices, dates or legal text into an image.
- Set `width`, `height`, `alt` and `style="display:block"` on images to avoid gaps and layout jumps.

## Bulletproof button

A padding-based HTML button with a VML fallback for classic Outlook for Windows (which renders with Word):

```html
<!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"
  href="https://example.com/demo" style="height:48px;v-text-anchor:middle;width:220px;"
  arcsize="17%" strokecolor="#0B5C66" fillcolor="#0B5C66">
  <w:anchorlock/>
  <center style="color:#FFFFFF;font-family:Arial,sans-serif;font-size:16px;font-weight:bold;">Book a demo</center>
</v:roundrect>
<![endif]-->
<!--[if !mso]><!-- -->
<a href="https://example.com/demo"
   style="background-color:#0B5C66;border-radius:8px;color:#FFFFFF;display:inline-block;
          font-family:Arial,sans-serif;font-size:16px;font-weight:bold;line-height:48px;
          text-align:center;text-decoration:none;width:220px;-webkit-text-size-adjust:none;">Book a demo</a>
<!--<![endif]-->
```

White on #0B5C66 is 7.67:1. Compute contrast for every brand button color; for example, white on bright orange #FF6A00 is only 2.87:1 and fails, while #111111 on the same orange is 6.58:1.

## Dark mode

Clients behave in three ways (behavior changes with app versions; test current clients):

| Behavior | What happens | Design response |
| --- | --- | --- |
| No change | Your colors render as coded | Supply your own dark styles with `prefers-color-scheme` where supported |
| Partial inversion | Light backgrounds become dark; dark text becomes light; some colors kept | Avoid thin light text on light backgrounds; check every color pair |
| Full inversion | Most colors inverted or remapped, including some you set | Use transparent PNG logos with a light outline or a contained shape; avoid pure black and pure white |

Techniques:

```html
<meta name="color-scheme" content="light dark">
<meta name="supported-color-schemes" content="light dark">
<style>
  :root { color-scheme: light dark; supported-color-schemes: light dark; }
  @media (prefers-color-scheme: dark) {
    .bg-body  { background-color: #121212 !important; }
    .text-main { color: #F5F5F5 !important; }
    .logo-light { display: none !important; }
    .logo-dark  { display: block !important; }
  }
  /* Outlook.com adds these attributes when it applies dark mode */
  [data-ogsc] .text-main { color: #F5F5F5 !important; }
  [data-ogsb] .bg-body   { background-color: #121212 !important; }
</style>
```

- Use off-black (#111111 or #121212) and off-white (#FAFAFA or #F5F5F5) rather than pure #000 and #FFF, which invert harshly. #F5F5F5 on #121212 is 17.18:1.
- Logos: a version that works on both, or a light-on-dark swap where supported, or a white padded container around a dark logo.
- Images with transparent backgrounds may sit on an unexpected dark background; add a subtle light edge or use a solid background.

## Gmail clipping and file size

- Gmail clips messages whose HTML exceeds about 102KB and hides the rest behind "[Message clipped]" (the threshold comes from email-industry testing; Google does not document it). The clipped part can include the unsubscribe link and tracking pixel.
- The limit counts the HTML source, including inline CSS, comments and long tracking URLs, but not image files.
- Keep HTML under about 90KB: minify, remove comments and unused CSS, shorten tracking parameters, avoid repeating long inline style blocks.
- Total image weight: keep heroes around 100-200KB and animated GIFs under 1MB (ideally about 500KB). Older Outlook for Windows versions (2007-2016, and some corporate installs) show only the first frame of a GIF, so the first frame must carry the message.

## Code foundations

- Tables for layout with `role="presentation"`; inline CSS for core styles; a `<style>` block for media queries and dark mode.
- `<html lang="en">` (or the content language), `<meta charset="utf-8">`, a viewport meta tag, and a `<title>` matching the subject.
- Fluid-hybrid layout: `max-width` containers that work without media queries, enhanced by them where supported.
- Encode special characters as HTML entities to avoid rendering and clipping problems.
- Frameworks: MJML, Maizzle and React Email (all MIT-licensed) compile responsive, tested markup; check output size against the clipping limit.
- Send a plain-text alternative (multipart/alternative) with every HTML email.
- Check feature support at caniemail.com before using any CSS feature.

## Accessibility

- Semantic headings in order; one `<h1>`.
- Body 16px, left-aligned, line-height 1.5; no justified text.
- Text contrast at least 4.5:1, including links and button text; compute it.
- Descriptive link text ("See the October schedule", not "click here"); underline links in body copy.
- Alt text for meaningful images, `alt=""` for decorative ones.
- Logical reading order in the source; columns stack in that order on mobile.
- No information conveyed by color alone; no flashing GIFs (no more than 3 flashes per second).
- Touch targets at least 44x44px with space between links.

## Testing

1. Render previews in Litmus or Email on Acid across Apple Mail (macOS, iOS), Gmail (web, iOS, Android), Outlook (classic Windows, new Outlook, Outlook for Mac, Outlook.com), Yahoo Mail and Samsung Email.
2. Send real test emails to real accounts on at least 3 clients.
3. Check with images off, in dark mode, at 320px width and with 200% text zoom.
4. Check HTML size under the clipping limit, every link and tracking parameter, the plain-text version, and the preheader.
5. Read it with a screen reader (VoiceOver on iOS or macOS) once per template.

## Common failures

- Image-only email → live text with supporting images.
- Button as an image → bulletproof HTML button.
- Logo disappears in dark mode → dual logo or contained mark.
- Clipped in Gmail, losing the unsubscribe → HTML under about 90KB.
- 12px gray body text → 16px, 4.5:1 contrast.
- Three competing calls to action in the hero → one primary.
