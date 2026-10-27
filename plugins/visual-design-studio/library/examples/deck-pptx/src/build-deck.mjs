// Version-Timestamp: 2026-10-23 20:10:44 UTC
// Token-driven, editable 10-slide sales deck built with PptxGenJS (MIT).
//   node src/build-deck.mjs                 PowerPoint-native: native charts and tables
//   node src/build-deck.mjs --canva-safe    text boxes, images, simple shapes; charts as PNG; no native charts or tables
// Options: --brand=<id> --mode=<light|dark|high-contrast> --out=<dir> --tokens=<tokens.resolved.json> --system-fonts
// Output: <out>/deck-<brand>-<native|canva-safe>.pptx (default out/ next to this example, gitignored).
import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import PptxGenJS from 'pptxgenjs';
import { loadTokens, makeTheme } from './tokens.mjs';
import { barChartPng } from './png.mjs';
import { deck, PLACEHOLDER_NOTE } from './content.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
export const SLIDE_COUNT = 10;
const W = 13.333;
const H = 7.5;

export async function buildDeck({ canvaSafe = false, brand, mode, outDir = path.resolve(here, '../out'), tokens, systemFonts = false } = {}) {
  const tok = await loadTokens({ file: tokens, brand, mode });
  const t = makeTheme(tok, { systemFonts });
  const c = t.color;
  const M = t.space.margin;
  const contentW = W - 2 * M;
  const label = canvaSafe ? 'canva-safe' : 'native';

  const pptx = new PptxGenJS();
  pptx.layout = 'LAYOUT_WIDE'; // 13.333 x 7.5 in, 16:9
  pptx.title = `${deck.company} proposal (placeholder)`;
  pptx.company = 'Fictional placeholder';
  pptx.subject = `Visual Design Kit deck example, ${label} mode, brand ${tok.brand}/${tok.mode}`;
  pptx.theme = { headFontFace: t.font.display, bodyFontFace: t.font.body };

  const head = { fontFace: t.font.display, color: c.fg, bold: true, margin: 0 };
  const body = { fontFace: t.font.body, color: c.fg, fontSize: t.size.body, margin: 0, lineSpacingMultiple: t.lineHeight.snug };
  const track = (size, em) => +(size * em).toFixed(2);

  // Slide masters: one dark (title, closing), one content master with title placeholder, footer and number.
  pptx.defineSlideMaster({
    title: 'KIT_DARK',
    background: { color: c.inverse },
    objects: [{ rect: { x: M, y: H - M - 0.06, w: 1.2, h: 0.06, fill: { color: c.accentSubtle } } }],
  });
  pptx.defineSlideMaster({
    title: 'KIT_CONTENT',
    background: { color: c.canvas },
    objects: [
      {
        placeholder: {
          options: { name: 'title', type: 'title', x: M, y: M * 0.8, w: contentW, h: 1.0, ...head, fontSize: t.size.title, align: 'left', valign: 'top' },
          text: '',
        },
      },
      { line: { x: M, y: H - M * 0.75, w: contentW, h: 0, line: { color: c.border, width: 0.75 } } },
      { text: { text: deck.footer, options: { x: M, y: H - M * 0.7, w: 8, h: 0.3, fontFace: t.font.body, fontSize: t.size.caption, color: c.muted, margin: 0 } } },
    ],
    slideNumber: { x: W - M - 0.6, y: H - M * 0.7, w: 0.6, h: 0.3, fontFace: t.font.body, fontSize: t.size.caption, color: c.muted, align: 'right' },
  });

  const content = (title) => {
    const s = pptx.addSlide({ masterName: 'KIT_CONTENT' });
    s.addText(title, { placeholder: 'title', align: 'left' });
    s.addNotes(PLACEHOLDER_NOTE);
    return s;
  };
  const top = M * 0.8 + 1.35; // first content row under the title
  const card = (s, x, y, w, h, fill = c.surface) =>
    s.addShape(pptx.ShapeType.roundRect, { x, y, w, h, fill: { color: fill }, line: { color: c.border, width: 0.75 }, rectRadius: t.radius.card });

  // 1. Title
  {
    const s = pptx.addSlide({ masterName: 'KIT_DARK' });
    s.addNotes(PLACEHOLDER_NOTE);
    s.addText(deck.title.kicker.toUpperCase(), { x: M, y: M, w: contentW, h: 0.4, fontFace: t.font.body, fontSize: t.size.small, color: c.accentSubtle, charSpacing: track(t.size.small, t.tracking.caps), margin: 0 });
    s.addText(deck.title.headline, { x: M, y: 2.0, w: contentW * 0.8, h: 2.2, ...head, color: c.fgInverse, fontSize: t.size.hero, lineSpacingMultiple: t.lineHeight.tight, charSpacing: track(t.size.hero, t.tracking.tight), valign: 'bottom' });
    s.addText(deck.title.sub, { x: M, y: 4.4, w: contentW * 0.7, h: 0.6, ...body, color: c.fgInverse, fontSize: t.size.subtitle });
    s.addText(deck.title.meta, { x: M, y: H - M - 0.55, w: contentW, h: 0.35, ...body, color: c.fgInverse, fontSize: t.size.caption });
  }

  // 2. Agenda
  {
    const s = content('Agenda');
    deck.agenda.forEach((item, i) => {
      const col = i < 3 ? 0 : 1;
      const row = i % 3;
      const x = M + col * (contentW / 2);
      const y = top + row * 1.25;
      s.addText(String(i + 1).padStart(2, '0'), { x, y, w: 0.9, h: 0.6, ...head, color: c.accent, fontSize: t.size.title });
      s.addText(item, { x: x + 1.0, y: y + 0.08, w: contentW / 2 - 1.3, h: 0.6, ...body, fontSize: t.size.subtitle });
    });
  }

  // 3. Problem
  {
    const s = content(deck.problem.title);
    s.addText(
      deck.problem.points.map((p) => ({ text: p, options: { bullet: { indent: 18 }, paraSpaceAfter: 10 } })),
      { x: M, y: top, w: contentW * 0.58, h: 3.6, ...body, valign: 'top' },
    );
    const cx = M + contentW * 0.64;
    card(s, cx, top, contentW * 0.36, 3.4, c.accentSubtle);
    s.addText(deck.problem.stat, { x: cx + t.space.pad, y: top + 0.4, w: contentW * 0.36 - 2 * t.space.pad, h: 1.6, ...head, color: c.accentFg, fontSize: t.size.metric });
    s.addText(deck.problem.statLabel, { x: cx + t.space.pad, y: top + 2.1, w: contentW * 0.36 - 2 * t.space.pad, h: 1.0, ...body, color: c.accentFg, valign: 'top' });
  }

  // 4. Solution: three steps joined by simple arrows
  {
    const s = content(deck.solution.title);
    const gap = 0.55;
    const w = (contentW - 2 * gap) / 3;
    deck.solution.steps.forEach((step, i) => {
      const x = M + i * (w + gap);
      card(s, x, top, w, 3.6);
      s.addShape(pptx.ShapeType.ellipse, { x: x + t.space.pad, y: top + t.space.pad, w: 0.6, h: 0.6, fill: { color: c.accent }, line: { color: c.accent } });
      s.addText(String(i + 1), { x: x + t.space.pad, y: top + t.space.pad, w: 0.6, h: 0.6, ...head, color: c.onAccent, fontSize: t.size.body, align: 'center', valign: 'middle' });
      s.addText(step.label, { x: x + t.space.pad, y: top + 1.35, w: w - 2 * t.space.pad, h: 0.5, ...head, fontSize: t.size.subtitle });
      s.addText(step.text, { x: x + t.space.pad, y: top + 1.95, w: w - 2 * t.space.pad, h: 1.4, ...body, color: c.muted, valign: 'top' });
      if (i < 2) s.addShape(pptx.ShapeType.rightArrow, { x: x + w + 0.1, y: top + 1.6, w: gap - 0.2, h: 0.35, fill: { color: c.borderStrong }, line: { color: c.borderStrong } });
    });
  }

  // 5. Three-column proof
  {
    const s = content(deck.proof.title);
    const gap = t.space.gap;
    const w = (contentW - 2 * gap) / 3;
    deck.proof.columns.forEach((col, i) => {
      const x = M + i * (w + gap);
      card(s, x, top, w, 3.8);
      s.addText(col.head, { x: x + t.space.pad, y: top + t.space.pad, w: w - 2 * t.space.pad, h: 0.5, ...head, fontSize: t.size.body });
      s.addText(col.metric, { x: x + t.space.pad, y: top + 1.0, w: w - 2 * t.space.pad, h: 1.2, ...head, color: c.accent, fontSize: t.size.hero });
      s.addText(col.label, { x: x + t.space.pad, y: top + 2.25, w: w - 2 * t.space.pad, h: 0.8, ...body, valign: 'top' });
      s.addText(col.note, { x: x + t.space.pad, y: top + 3.2, w: w - 2 * t.space.pad, h: 0.35, ...body, color: c.muted, fontSize: t.size.caption });
    });
  }

  // 6. Metric slide: native column chart, or a PNG chart with editable text labels
  let chartPng = null;
  {
    const m = deck.metric;
    const s = content(m.title);
    const chart = { x: M, y: top, w: contentW * 0.62, h: 4.0 };
    if (canvaSafe) {
      const { png, bars } = barChartPng({
        values: m.values,
        max: m.max,
        colors: { highlight: c.accent, rest: c.borderStrong },
        gridColor: c.border,
        baseColor: c.muted,
      });
      chartPng = png;
      const plotH = chart.h - 0.45; // room for category labels under the image
      s.addImage({ data: `image/png;base64,${png.toString('base64')}`, x: chart.x, y: chart.y, w: chart.w, h: plotH, altText: `Column chart: ${m.labels.map((l, i) => `${l} ${m.values[i]} h`).join(', ')} (fictional data)` });
      bars.forEach((bar, i) => {
        const bx = chart.x + bar.x * chart.w;
        const bw = bar.w * chart.w;
        s.addText(String(m.values[i]), { x: bx - 0.2, y: chart.y + bar.y * plotH - 0.42, w: bw + 0.4, h: 0.38, ...head, fontSize: t.size.small, align: 'center' });
        s.addText(m.labels[i], { x: bx - 0.2, y: chart.y + plotH + 0.08, w: bw + 0.4, h: 0.35, ...body, color: c.muted, fontSize: t.size.small, align: 'center' });
      });
    } else {
      s.addChart(pptx.ChartType.bar, [{ name: 'Hours returned', labels: m.labels, values: m.values }], {
        ...chart,
        barDir: 'col',
        barGapWidthPct: 80,
        chartColors: [c.accent],
        valAxisMaxVal: m.max,
        valAxisMinVal: 0,
        valAxisMajorUnit: m.max / 4,
        valAxisHidden: true,
        valGridLine: { color: c.border, size: 0.75 },
        catGridLine: { style: 'none' },
        catAxisLabelColor: c.muted,
        catAxisLabelFontFace: t.font.body,
        catAxisLabelFontSize: t.size.small,
        catAxisLineShow: true,
        showValue: true,
        dataLabelPosition: 'outEnd',
        dataLabelColor: c.fg,
        dataLabelFontFace: t.font.display,
        dataLabelFontSize: t.size.small,
        dataLabelFontBold: true,
        showLegend: false,
        altText: 'Column chart of hours returned per quarter (fictional data)',
      });
    }
    const rx = M + contentW * 0.68;
    s.addText(m.headline, { x: rx, y: top + 0.4, w: contentW * 0.32, h: 1.6, ...head, color: c.accent, fontSize: t.size.metric });
    s.addText(m.caption, { x: rx, y: top + 2.1, w: contentW * 0.32, h: 1.2, ...body, valign: 'top' });
  }

  // 7. Case study: quote plus results (native table, or a shape-and-text grid)
  {
    const cs = deck.caseStudy;
    const s = content(cs.title);
    s.addText(cs.quote, { x: M, y: top, w: contentW * 0.36, h: 3.6, ...head, fontSize: t.size.subtitle, lineSpacingMultiple: t.lineHeight.snug, valign: 'top' });
    const tx = M + contentW * 0.42;
    const tw = contentW * 0.58;
    const colW = [tw * 0.42, tw * 0.24, tw * 0.34];
    if (canvaSafe) {
      const rowH = 0.72;
      cs.rows.forEach((row, r) => {
        const y = top + r * rowH;
        s.addShape(pptx.ShapeType.rect, { x: tx, y, w: tw, h: rowH, fill: { color: r === 0 ? c.tableHeaderBg : r % 2 ? c.surface : c.tableRowAlt }, line: { color: c.border, width: 0.75 } });
        let x = tx;
        row.forEach((cell, k) => {
          s.addText(cell, { x: x + 0.15, y, w: colW[k] - 0.3, h: rowH, ...body, fontSize: t.size.small, bold: r === 0, color: r === 0 ? c.tableHeaderFg : c.fg, align: k ? 'right' : 'left', valign: 'middle' });
          x += colW[k];
        });
      });
    } else {
      const rows = cs.rows.map((row, r) =>
        row.map((cell, k) => ({
          text: cell,
          options: { bold: r === 0, color: r === 0 ? c.tableHeaderFg : c.fg, fill: { color: r === 0 ? c.tableHeaderBg : r % 2 ? c.surface : c.tableRowAlt }, align: k ? 'right' : 'left' },
        })),
      );
      s.addTable(rows, { x: tx, y: top, w: tw, colW, rowH: 0.72, fontFace: t.font.body, fontSize: t.size.small, valign: 'middle', border: { type: 'solid', pt: 0.75, color: c.border }, margin: 0.12 });
    }
  }

  // 8. Team: initials in circles (no photos of real people in a placeholder deck)
  {
    const s = content(deck.team.title);
    const n = deck.team.people.length;
    const w = contentW / n;
    deck.team.people.forEach((p, i) => {
      const x = M + i * w;
      const d = 1.6;
      s.addShape(pptx.ShapeType.ellipse, { x: x + (w - d) / 2, y: top + 0.2, w: d, h: d, fill: { color: c.accentSubtle }, line: { color: c.accentSubtle } });
      s.addText(p.initials, { x: x + (w - d) / 2, y: top + 0.2, w: d, h: d, ...head, color: c.accentFg, fontSize: t.size.title, align: 'center', valign: 'middle' });
      s.addText(p.name, { x, y: top + 2.1, w, h: 0.45, ...head, fontSize: t.size.body, align: 'center' });
      s.addText(p.role, { x, y: top + 2.6, w, h: 0.45, ...body, color: c.muted, fontSize: t.size.small, align: 'center' });
    });
  }

  // 9. Pricing and next steps
  {
    const pr = deck.pricing;
    const s = content(pr.title);
    const pw = contentW * 0.64;
    if (canvaSafe) {
      const gap = 0.3;
      const w = (pw - 2 * gap) / 3;
      pr.tiers.forEach((tier, i) => {
        const x = M + i * (w + gap);
        const featured = i === 1;
        card(s, x, top, w, 3.6, featured ? c.accentSubtle : c.surface);
        s.addText(tier.name, { x: x + 0.25, y: top + 0.25, w: w - 0.5, h: 0.5, ...head, fontSize: t.size.body, color: featured ? c.accentFg : c.fg });
        s.addText(tier.price, { x: x + 0.25, y: top + 0.9, w: w - 0.5, h: 0.8, ...head, fontSize: t.size.body, color: featured ? c.accentFg : c.fg });
        s.addText(tier.detail, { x: x + 0.25, y: top + 1.8, w: w - 0.5, h: 1.6, ...body, fontSize: t.size.small, color: c.muted, valign: 'top' });
      });
    } else {
      const rows = [
        ['Option', 'Price', 'Includes'].map((h) => ({ text: h, options: { bold: true, color: c.tableHeaderFg, fill: { color: c.tableHeaderBg } } })),
        ...pr.tiers.map((tier, r) => [tier.name, tier.price, tier.detail].map((cell, k) => ({ text: cell, options: { bold: k === 0, color: c.fg, fill: { color: r % 2 ? c.tableRowAlt : c.surface } } }))),
      ];
      s.addTable(rows, { x: M, y: top, w: pw, colW: [pw * 0.22, pw * 0.28, pw * 0.5], rowH: 0.8, fontFace: t.font.body, fontSize: t.size.small, valign: 'middle', border: { type: 'solid', pt: 0.75, color: c.border }, margin: 0.12 });
    }
    const nx = M + pw + 0.5;
    const nw = contentW - pw - 0.5;
    s.addText('Next steps', { x: nx, y: top, w: nw, h: 0.5, ...head, fontSize: t.size.subtitle });
    s.addText(
      pr.next.map((step) => ({ text: step, options: { bullet: { type: 'number' }, paraSpaceAfter: 10 } })),
      { x: nx, y: top + 0.65, w: nw, h: 2.8, ...body, fontSize: t.size.small, valign: 'top' },
    );
  }

  // 10. Closing
  {
    const s = pptx.addSlide({ masterName: 'KIT_DARK' });
    s.addNotes(PLACEHOLDER_NOTE);
    s.addText(deck.closing.headline, { x: M, y: 2.0, w: contentW * 0.8, h: 2.2, ...head, color: c.fgInverse, fontSize: t.size.hero, lineSpacingMultiple: t.lineHeight.tight, charSpacing: track(t.size.hero, t.tracking.tight), valign: 'bottom' });
    s.addText(deck.closing.contact, { x: M, y: 4.5, w: contentW, h: 0.5, ...body, color: c.fgInverse, fontSize: t.size.subtitle });
  }

  await mkdir(outDir, { recursive: true });
  const file = path.join(outDir, `deck-${tok.brand}-${label}.pptx`);
  const buffer = await pptx.write({ outputType: 'nodebuffer' });
  await writeFile(file, buffer);
  if (chartPng) {
    // The same chart as a standalone file, for re-uploading into Canva if someone deletes the image.
    await writeFile(path.join(outDir, `chart-${tok.brand}-metric.png`), chartPng);
  }
  return { file, bytes: buffer.length, slides: SLIDE_COUNT, mode: label, brand: tok.brand, fonts: t.font };
}

function parseArgs(argv) {
  const opts = {};
  for (const arg of argv) {
    if (arg === '--canva-safe') opts.canvaSafe = true;
    else if (arg === '--system-fonts') opts.systemFonts = true;
    else if (arg.startsWith('--brand=')) opts.brand = arg.slice(8);
    else if (arg.startsWith('--mode=')) opts.mode = arg.slice(7);
    else if (arg.startsWith('--out=')) opts.outDir = path.resolve(arg.slice(6));
    else if (arg.startsWith('--tokens=')) opts.tokens = path.resolve(arg.slice(9));
    else throw new Error(`Unknown option ${arg}`);
  }
  return opts;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const result = await buildDeck(parseArgs(process.argv.slice(2)));
    const { display, body, displayFallback, bodyFallback } = result.fonts;
    console.log(`Wrote ${result.file} (${result.slides} slides, ${result.mode}, ${Math.round(result.bytes / 1024)} KB)`);
    if (display === displayFallback && body === bodyFallback) console.log(`Fonts: ${display} and ${body} (system fonts, --system-fonts).`);
    else console.log(`Fonts named: ${display} (fallback ${displayFallback}), ${body} (fallback ${bodyFallback}). Install them on every machine that opens the deck; PPTX does not embed fonts reliably.`);
  } catch (error) {
    console.error(`build-deck: ${error.message}`);
    process.exit(1);
  }
}
