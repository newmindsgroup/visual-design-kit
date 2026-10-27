#!/usr/bin/env node
// Version-Timestamp: 2026-10-23 20:38:00 UTC
// Agent-Attribution: computer=vm; tool=Claude Code; version=2.1.309; timestamp=2026-10-23 20:38:00 UTC
//
// render_collateral.mjs: render a token-driven collateral template to a screen PDF and one PNG per page or frame.
// Node 18+. No bundled dependencies: Playwright (and optionally axe-core) are resolved at runtime, the same way as
// design-critique/scripts/render_review.mjs.
//
//   node render_collateral.mjs <template.html> [--brand meridian,ember] [--out DIR] [--scale N]
//
// The PDF is a screen/accessible PDF from Chromium (tagged, outline, CSS page size, RGB, no bleed). It is not a
// print master: produce that with WeasyPrint (see references/print-production-pipeline.md) and check it with
// preflight_pdf.py. Look at every PNG before you call the piece finished.

import { createRequire } from 'node:module';
import { existsSync, mkdirSync, readFileSync, statSync, writeFileSync, createReadStream } from 'node:fs';
import { basename, dirname, extname, join, resolve, sep } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import http from 'node:http';

const VERSION = '0.8.0';
const SCRIPT_DIR = dirname(fileURLToPath(import.meta.url));
const DEFAULT_WRAP_SELECTOR = 'h1,h2,h3,h4,p,li,blockquote,figcaption,dd,[data-wrap]';

const HELP = `render_collateral.mjs ${VERSION}: render a collateral template to a screen PDF and PNGs.

Usage
  node render_collateral.mjs <template.html | URL> [options]

Options
  --brand LIST         Comma list of data-brand values to render (default meridian,ember). "keep" renders the
                       brand written in the HTML
  --out DIR            Output folder (default ./collateral-render/<template name>)
  --selector SEL       Page or frame elements (default .page)
  --scale N            PNG device pixel ratio (default: <meta name="collateral:png-scale">, else 2)
  --no-pdf             Skip the PDF
  --no-png             Skip the PNGs
  --serve              Serve the template folder over http://127.0.0.1 instead of file://
  --root DIR           Root folder for --serve (default: the template's folder)
  --wait MS            Settle time after fonts load (default 300)
  --no-axe             Skip axe-core even when it resolves
  --strict             Exit 2 on overflow, clipped text, missing brand fonts, failed requests or serious axe
                       violations
  --help               Show this help

Output
  <name>-<brand>.pdf        Chromium page.pdf: tagged, outline, preferCSSPageSize, printBackground (RGB, trim size)
  <name>-<brand>-pNN.png    one PNG per page or frame, screen styles, bleed included when the page has data-bleed
  report.json               layout checks, loaded fonts, axe summary, file list

Environment
  PLAYWRIGHT_MODULE    Path to a playwright (or playwright-core) package folder
  PLAYWRIGHT_CHROMIUM  Chromium or headless_shell executable to launch
  AXE_SCRIPT           Path to axe.min.js (otherwise axe-core is resolved like Playwright)
`;

function fail(message, code = 1) {
  process.stderr.write(`render_collateral: ${message}\n`);
  process.exit(code);
}

function parseArgs(argv) {
  const opts = { brands: 'meridian,ember', selector: '.page', scale: null, pdf: true, png: true, serve: false,
    wait: 300, axe: true, strict: false };
  const positional = [];
  const needValue = (i, flag) => { if (i + 1 >= argv.length) fail(`${flag} needs a value`); return argv[i + 1]; };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    switch (arg) {
      case '--help': case '-h': process.stdout.write(HELP); process.exit(0); break;
      case '--brand': case '--brands': opts.brands = needValue(i, arg); i += 1; break;
      case '--out': opts.out = needValue(i, arg); i += 1; break;
      case '--selector': opts.selector = needValue(i, arg); i += 1; break;
      case '--scale': opts.scale = Number(needValue(i, arg)); i += 1; break;
      case '--no-pdf': opts.pdf = false; break;
      case '--no-png': opts.png = false; break;
      case '--serve': opts.serve = true; break;
      case '--root': opts.root = needValue(i, arg); i += 1; break;
      case '--wait': opts.wait = Number(needValue(i, arg)); i += 1; break;
      case '--no-axe': opts.axe = false; break;
      case '--strict': opts.strict = true; break;
      default:
        if (arg.startsWith('--')) fail(`unknown option ${arg} (see --help)`);
        positional.push(arg);
    }
  }
  if (positional.length !== 1) fail('give exactly one template file or URL (see --help)');
  opts.target = positional[0];
  opts.brandList = opts.brands.split(',').map((b) => b.trim()).filter(Boolean);
  if (!opts.brandList.length) fail('--brand is empty');
  if (opts.scale !== null && !(opts.scale > 0 && opts.scale <= 8)) fail('--scale must be between 0 and 8');
  if (!opts.pdf && !opts.png) fail('nothing to do: both --no-pdf and --no-png given');
  return opts;
}

// ---------- dependency resolution (same order as render_review.mjs) ----------

function requireFrom(dir) { return createRequire(join(dir, 'noop.js')); }

async function loadPlaywright() {
  const tried = [];
  const pick = (mod) => (mod && mod.chromium ? mod : mod && mod.default && mod.default.chromium ? mod.default : null);
  const env = process.env.PLAYWRIGHT_MODULE;
  if (env) {
    try { const mod = pick(requireFrom(process.cwd())(resolve(env))); if (mod) return mod; tried.push(`PLAYWRIGHT_MODULE=${env}: no chromium export`); }
    catch (error) { tried.push(`PLAYWRIGHT_MODULE=${env}: ${error.message.split('\n')[0]}`); }
  }
  for (const name of ['playwright', 'playwright-core']) {
    try { const mod = pick(await import(name)); if (mod) return mod; } catch (error) { tried.push(`import('${name}'): ${error.code || error.message.split('\n')[0]}`); }
    try { const mod = pick(requireFrom(process.cwd())(name)); if (mod) return mod; } catch (error) { tried.push(`require('${name}') from cwd: ${error.code || error.message.split('\n')[0]}`); }
  }
  fail(`Playwright not found.\n  Install it where you run this script:  npm install playwright && npx playwright install chromium\n  or point to an existing copy:           PLAYWRIGHT_MODULE=/abs/path/node_modules/playwright\n  Tried:\n    ${tried.join('\n    ')}`);
  return null;
}

function loadAxeSource() {
  if (process.env.AXE_SCRIPT) {
    if (!existsSync(process.env.AXE_SCRIPT)) return { source: null, note: `AXE_SCRIPT=${process.env.AXE_SCRIPT} does not exist` };
    return { source: readFileSync(process.env.AXE_SCRIPT, 'utf8'), path: process.env.AXE_SCRIPT };
  }
  const bases = [process.cwd(), SCRIPT_DIR];
  if (process.env.PLAYWRIGHT_MODULE) bases.push(dirname(resolve(process.env.PLAYWRIGHT_MODULE)));
  for (const base of bases) {
    try { const path = requireFrom(base).resolve('axe-core/axe.min.js'); return { source: readFileSync(path, 'utf8'), path }; } catch { /* next */ }
  }
  return { source: null, note: 'axe-core not found: npm install axe-core, or set AXE_SCRIPT=/abs/path/axe.min.js' };
}

// ---------- local static server (only with --serve) ----------

const MIME = { '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8', '.json': 'application/json; charset=utf-8', '.svg': 'image/svg+xml',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.avif': 'image/avif',
  '.woff': 'font/woff', '.woff2': 'font/woff2', '.ttf': 'font/ttf', '.otf': 'font/otf', '.txt': 'text/plain; charset=utf-8' };

function startServer(root) {
  return new Promise((resolveServer) => {
    const server = http.createServer((req, res) => {
      let path;
      try { path = resolve(root, `.${decodeURIComponent(new URL(req.url, 'http://x').pathname)}`); } catch { res.writeHead(400).end(); return; }
      if (path !== root && !path.startsWith(root + sep)) { res.writeHead(403).end(); return; }
      if (existsSync(path) && statSync(path).isDirectory()) path = join(path, 'index.html');
      if (!existsSync(path)) { res.writeHead(404).end(); return; }
      res.writeHead(200, { 'content-type': MIME[extname(path).toLowerCase()] || 'application/octet-stream', 'cache-control': 'no-store' });
      createReadStream(path).pipe(res);
    });
    server.listen(0, '127.0.0.1', () => resolveServer(server));
  });
}

// ---------- in-page checks (serialized into the page; must stay self-contained) ----------

function inspectPages({ selector, wrapSelector }) {
  const toPx = (value) => {
    const m = String(value || '').trim().match(/^([\d.]+)\s*(in|mm|cm|pt|px)?$/);
    if (!m) return 0;
    const n = parseFloat(m[1]);
    return { in: 96, mm: 96 / 25.4, cm: 96 / 2.54, pt: 96 / 72, px: 1 }[m[2] || 'px'] * n;
  };
  const shown = (el) => {
    const cs = getComputedStyle(el);
    return cs.display !== 'none' && cs.visibility === 'visible' && !el.closest('[hidden]');
  };
  const label = (el) => {
    const parts = [];
    for (let n = el; n && n.nodeType === 1 && parts.length < 3; n = n.parentElement) {
      if (n.matches && n.matches(selector)) break;
      let part = n.localName + [...n.classList].slice(0, 2).map((c) => `.${c}`).join('');
      if (n.dataset && n.dataset.field) part += `[data-field=${n.dataset.field}]`;
      parts.unshift(part);
    }
    return parts.join(' > ');
  };
  const words = (el) => {
    const out = [];
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    for (let node = walker.nextNode(); node; node = walker.nextNode()) {
      if (!node.parentElement || !shown(node.parentElement)) continue;
      const re = /\S+/g;
      let m;
      while ((m = re.exec(node.data))) out.push({ node, start: m.index, end: m.index + m[0].length, text: m[0] });
    }
    return out;
  };
  const rectOf = (w) => { const r = document.createRange(); r.setStart(w.node, w.start); r.setEnd(w.node, w.end); return r.getClientRects()[0]; };

  return [...document.querySelectorAll(selector)].map((page, index) => {
    const box = page.getBoundingClientRect();
    const overflow = [];
    const clipped = [];
    const lonely = [];
    for (const el of page.querySelectorAll('*')) {
      if (!shown(el) || el.closest('.bleed-art,[data-allow-overflow]')) continue;
      const r = el.getBoundingClientRect();
      if (r.width === 0 && r.height === 0) continue;
      if (r.left < box.left - 0.5 || r.top < box.top - 0.5 || r.right > box.right + 0.5 || r.bottom > box.bottom + 0.5) {
        overflow.push({ element: label(el), by: Math.round(Math.max(box.left - r.left, box.top - r.top, r.right - box.right, r.bottom - box.bottom)) });
      }
      const cs = getComputedStyle(el);
      if (cs.overflow !== 'visible' && (el.scrollHeight > el.clientHeight + 1 || el.scrollWidth > el.clientWidth + 1) && el.textContent.trim()) {
        clipped.push({ element: label(el), scroll: [el.scrollWidth, el.scrollHeight], box: [el.clientWidth, el.clientHeight] });
      }
    }
    for (const el of page.querySelectorAll(wrapSelector)) {
      if (!shown(el)) continue;
      const list = words(el);
      if (list.length < 4) continue;
      const last = rectOf(list[list.length - 1]);
      const prev = rectOf(list[list.length - 2]);
      if (last && prev && last.top - prev.top > last.height / 2) lonely.push({ element: label(el), word: list[list.length - 1].text });
    }
    // Overflow only counts once per element chain: keep the outermost reported element.
    const outer = overflow.filter((o) => !overflow.some((p) => p !== o && o.element.startsWith(`${p.element} > `)));
    return {
      index: index + 1,
      label: page.getAttribute('aria-label') || '',
      size: [Math.round(box.width), Math.round(box.height)],
      bleedPx: toPx(page.dataset.bleed),
      overflow: outer,
      clipped,
      lonelyLastWord: lonely,
    };
  });
}

async function fontReport(page) {
  return page.evaluate(async () => {
    await document.fonts.ready;
    const root = getComputedStyle(document.documentElement);
    const first = (stack) => (stack || '').split(',')[0].trim().replace(/^["']|["']$/g, '');
    const roles = { display: first(root.getPropertyValue('--font-family-display')), body: first(root.getPropertyValue('--font-family-body')) };
    const loaded = [...document.fonts].filter((f) => f.status === 'loaded').map((f) => `${f.family.replace(/"/g, '')} ${f.weight}`);
    const missing = Object.entries(roles).filter(([, family]) => family && !loaded.some((l) => l.startsWith(`${family} `))).map(([role, family]) => `${role}: ${family}`);
    return { roles, loaded: [...new Set(loaded)], missing };
  });
}

async function runAxe(page, source, preload) {
  await page.addScriptTag({ content: source });
  return page.evaluate(async (preloadCss) => {
    const result = await window.axe.run(document, { preload: preloadCss, runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'] }, resultTypes: ['violations'] });
    return {
      version: window.axe.version,
      violations: result.violations.map((v) => ({ id: v.id, impact: v.impact, nodes: v.nodes.length, targets: v.nodes.slice(0, 3).map((n) => n.target.join(' ')) })),
    };
  }, preload);
}

// ---------- main ----------

async function main() {
  const opts = parseArgs(process.argv.slice(2));
  const isUrl = /^https?:\/\//.test(opts.target);
  const file = isUrl ? null : resolve(opts.target);
  if (file && !existsSync(file)) fail(`no such file: ${opts.target}`);
  const name = isUrl ? (basename(new URL(opts.target).pathname, extname(new URL(opts.target).pathname)) || 'page') : basename(file, extname(file));
  const outDir = resolve(opts.out || join('collateral-render', name));
  mkdirSync(outDir, { recursive: true });

  let server = null;
  let baseUrl;
  if (isUrl) baseUrl = opts.target;
  else if (opts.serve) {
    const root = resolve(opts.root || dirname(file));
    if (!file.startsWith(root + sep)) fail('--root must contain the template');
    server = await startServer(root);
    baseUrl = `http://127.0.0.1:${server.address().port}/${file.slice(root.length + 1).split(sep).map(encodeURIComponent).join('/')}`;
  } else baseUrl = pathToFileURL(file).href;

  const playwright = await loadPlaywright();
  const axe = opts.axe ? loadAxeSource() : { source: null, note: 'skipped (--no-axe)' };
  let browser;
  try {
    browser = await playwright.chromium.launch({ headless: true, executablePath: process.env.PLAYWRIGHT_CHROMIUM || undefined });
  } catch (error) {
    if (server) server.close();
    fail(`could not launch Chromium: ${error.message.split('\n')[0]}\n  Install a browser with: npx playwright install chromium\n  or set PLAYWRIGHT_CHROMIUM=/abs/path/to/chrome-or-headless_shell`);
  }

  const report = { tool: `render_collateral ${VERSION}`, target: opts.target, browser: `chromium ${browser.version()}`,
    axe: axe.source ? { source: axe.path } : { source: null, note: axe.note }, brands: [],
    note: 'The PDF is a screen PDF (RGB, trim size, no bleed or marks). Print masters come from WeasyPrint; run preflight_pdf.py on both.' };
  let problems = 0;

  for (const brand of opts.brandList) {
    const probe = await browser.newPage();
    await probe.goto(baseUrl, { waitUntil: 'load' });
    const meta = await probe.evaluate(() => {
      const m = document.querySelector('meta[name="collateral:png-scale"]');
      const pages = [...document.querySelectorAll('.page')].map((p) => p.getBoundingClientRect().width);
      return { scale: m ? Number(m.content) : null, width: Math.ceil(Math.max(0, ...pages)) };
    });
    await probe.close();
    const scale = opts.scale || meta.scale || 2;
    const context = await browser.newContext({ viewport: { width: Math.max(meta.width + 160, 800), height: 1000 }, deviceScaleFactor: scale, colorScheme: 'light' });
    const page = await context.newPage();
    const failedRequests = [];
    let listening = true; // stop recording once our own probes (axe) start
    page.on('requestfailed', (req) => listening && failedRequests.push(`${req.url()} (${req.failure() ? req.failure().errorText : 'failed'})`));
    page.on('response', (res) => { if (listening && res.status() >= 400) failedRequests.push(`${res.url()} (HTTP ${res.status()})`); });
    const url = brand === 'keep' ? baseUrl : `${baseUrl}${baseUrl.includes('?') ? '&' : '?'}brand=${encodeURIComponent(brand)}`;
    await page.goto(url, { waitUntil: 'load' });
    if (brand !== 'keep') await page.evaluate((b) => document.documentElement.setAttribute('data-brand', b), brand);
    const fonts = await fontReport(page);
    await page.waitForTimeout(opts.wait);
    const label = brand === 'keep' ? (await page.evaluate(() => document.documentElement.dataset.brand || 'default')) : brand;

    const checks = await page.evaluate(inspectPages, { selector: opts.selector, wrapSelector: DEFAULT_WRAP_SELECTOR });
    const files = [];
    if (opts.png) {
      const handles = await page.$$(opts.selector);
      for (let i = 0; i < handles.length; i += 1) {
        await handles[i].scrollIntoViewIfNeeded();
        const box = await handles[i].boundingBox();
        const bleed = checks[i] ? checks[i].bleedPx : 0;
        const scroll = await page.evaluate(() => [window.scrollX, window.scrollY]);
        const clip = { x: box.x + scroll[0] - bleed, y: box.y + scroll[1] - bleed, width: box.width + 2 * bleed, height: box.height + 2 * bleed };
        const png = join(outDir, `${name}-${label}-p${String(i + 1).padStart(2, '0')}.png`);
        await page.screenshot({ path: png, clip, fullPage: true });
        files.push(png);
      }
    }

    let axeResult = null;
    if (axe.source) {
      listening = false;
      try { axeResult = await runAxe(page, axe.source, url.startsWith('http')); } catch (error) { axeResult = { error: error.message.split('\n')[0] }; }
    }

    if (opts.pdf) {
      await page.emulateMedia({ media: 'print' });
      await page.evaluate(() => document.documentElement.setAttribute('data-render', 'screen-pdf'));
      const pdf = join(outDir, `${name}-${label}.pdf`);
      await page.pdf({ path: pdf, preferCSSPageSize: true, printBackground: true, tagged: true, outline: true });
      files.push(pdf);
      await page.evaluate(() => document.documentElement.removeAttribute('data-render'));
      await page.emulateMedia({ media: 'screen' });
    }
    await context.close();

    const serious = axeResult && axeResult.violations ? axeResult.violations.filter((v) => ['serious', 'critical'].includes(v.impact)) : [];
    const count = checks.reduce((n, c) => n + c.overflow.length + c.clipped.length, 0) + fonts.missing.length + failedRequests.length + serious.length;
    problems += count;
    report.brands.push({ brand: label, scale, fonts, pages: checks, failedRequests, axe: axeResult, files });
  }
  await browser.close();
  if (server) server.close();

  writeFileSync(join(outDir, 'report.json'), `${JSON.stringify(report, null, 2)}\n`);
  const lines = [`render_collateral ${VERSION}: ${opts.target}`, `  ${report.browser}; axe: ${axe.source ? 'on' : axe.note}`];
  for (const b of report.brands) {
    lines.push(`  ${b.brand}: ${b.pages.length} page(s) at scale ${b.scale}; fonts ${b.fonts.missing.length ? `MISSING ${b.fonts.missing.join(', ')}` : `ok (${b.fonts.roles.display} / ${b.fonts.roles.body})`}`
      + `${b.failedRequests.length ? `; ${b.failedRequests.length} failed request(s)` : ''}`
      + `${b.axe ? (b.axe.error ? `; axe error ${b.axe.error}` : `; axe ${b.axe.violations.length} violation(s)`) : ''}`);
    for (const p of b.pages) {
      const notes = [];
      if (p.overflow.length) notes.push(`overflow ${p.overflow.map((o) => `${o.element} (+${o.by}px)`).slice(0, 3).join('; ')}`);
      if (p.clipped.length) notes.push(`clipped ${p.clipped.map((c) => c.element).slice(0, 3).join('; ')}`);
      if (p.lonelyLastWord.length) notes.push(`single-word last line ${p.lonelyLastWord.map((w) => `${w.element} "${w.word}"`).slice(0, 3).join('; ')}`);
      lines.push(`    p${String(p.index).padStart(2, '0')} ${p.size.join('x')}${p.label ? ` ${p.label}` : ''}: ${notes.length ? notes.join(' | ') : 'ok'}`);
    }
    if (b.axe && b.axe.violations) for (const v of b.axe.violations.slice(0, 5)) lines.push(`    axe ${v.impact} ${v.id} x${v.nodes}: ${v.targets[0] || ''}`);
    for (const r of b.failedRequests.slice(0, 5)) lines.push(`    failed request ${r}`);
  }
  lines.push(`  wrote ${outDir}`);
  lines.push('  Look at every PNG: overflow, single-word last lines, contrast, crop of bleed art, placeholder text left in.');
  process.stdout.write(`${lines.join('\n')}\n`);
  if (opts.strict && problems) process.exit(2);
}

main().catch((error) => fail(error.stack || String(error)));
