// Version-Timestamp: 2026-10-23 20:10:44 UTC
// Reads the kit's resolved tokens (library/tokens/dist/tokens.resolved.json) and maps them to slide units.
// Mapping defaults (override in DECK_SCALE below when a brand needs a different slide density):
//   type: 1rem token = 16pt on a 13.333 x 7.5 in (16:9) slide, so font.size.lg (1.25rem) = 20pt body text
//   layout: 1rem token = 0.2in, so space.12 (3rem) = 0.6in outer margin
//   radius: px tokens at 96px per inch, so card.radius 12px = 0.125in
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
export const defaultTokensPath = path.resolve(here, '../../../tokens/dist/tokens.resolved.json');

export const DECK_SCALE = { ptPerRem: 16, inchPerRem: 0.2, pxPerInch: 96 };

// Fallback families in priority order: installed on Windows and macOS, so PowerPoint and Keynote both have them.
const OFFICE_SAFE = ['Arial', 'Georgia', 'Times New Roman', 'Consolas', 'Helvetica Neue', 'Segoe UI', 'Cambria'];

export async function loadTokens({ file = process.env.TOKENS_RESOLVED || defaultTokensPath, brand, mode } = {}) {
  const data = JSON.parse(await readFile(file, 'utf8'));
  const b = brand || data.defaultBrand;
  const m = mode || data.defaultMode;
  const values = data.values?.[b]?.[m];
  if (!values) {
    const brands = Object.keys(data.values || {}).join(', ');
    throw new Error(`No tokens for brand "${b}" mode "${m}" in ${file}. Brands: ${brands}`);
  }
  return { brand: b, brandName: data.brands?.[b]?.name || b, mode: m, values, file };
}

export function makeTheme(tok, { systemFonts = false } = {}) {
  const v = (name) => {
    if (!(name in tok.values)) throw new Error(`Token ${name} missing from ${tok.file}`);
    return tok.values[name];
  };
  const hex = (name) => {
    const value = String(v(name));
    if (!/^#[0-9a-f]{6}([0-9a-f]{2})?$/i.test(value)) throw new Error(`Token ${name} is not a hex color: ${value}`);
    return value.slice(1, 7).toUpperCase();
  };
  const rem = (name) => parseFloat(v(name));
  const pt = (name, factor = 1) => Math.round(rem(name) * DECK_SCALE.ptPerRem * factor);
  const inch = (name) => +(rem(name) * DECK_SCALE.inchPerRem).toFixed(3);
  const pxIn = (name) => +(parseFloat(v(name)) / DECK_SCALE.pxPerInch).toFixed(3);
  const em = (name) => parseFloat(v(name));

  const pickFont = (stack) => {
    const safe = OFFICE_SAFE.find((f) => stack.includes(f)) || 'Arial';
    return { face: systemFonts ? safe : stack[0], fallback: safe };
  };
  const display = pickFont(v('font.family.display'));
  const body = pickFont(v('font.family.body'));

  return {
    brandName: tok.brandName,
    font: { display: display.face, body: body.face, displayFallback: display.fallback, bodyFallback: body.fallback },
    color: {
      canvas: hex('color.bg.canvas'),
      surface: hex('color.bg.surface'),
      sunken: hex('color.bg.sunken'),
      inverse: hex('color.bg.inverse'),
      fg: hex('color.fg.default'),
      muted: hex('color.fg.muted'),
      fgInverse: hex('color.fg.inverse'),
      onAccent: hex('color.fg.on-accent'),
      accent: hex('color.accent.default'),
      accentStrong: hex('color.accent.active'),
      accentSubtle: hex('color.accent.subtle'),
      accentFg: hex('color.accent.fg'),
      border: hex('color.border.subtle'),
      borderStrong: hex('color.border.default'),
      tableHeaderBg: hex('table.header-bg'),
      tableHeaderFg: hex('table.header-fg'),
      tableRowAlt: hex('table.row-bg-alt'),
    },
    size: {
      hero: pt('font.size.5xl'),
      title: pt('font.size.3xl'),
      subtitle: pt('font.size.xl'),
      body: pt('font.size.lg'),
      small: pt('font.size.md'),
      caption: pt('font.size.sm'),
      metric: pt('font.size.5xl', 1.5),
    },
    weightBoldFrom: v('font.weight.semibold'),
    lineHeight: { tight: v('line-height.tight'), snug: v('line-height.snug'), normal: v('line-height.normal') },
    tracking: { tight: em('letter-spacing.tight'), caps: em('letter-spacing.caps') },
    space: { margin: inch('space.12'), gap: inch('space.6'), pad: inch('space.6'), small: inch('space.3') },
    radius: { card: pxIn('card.radius'), sm: pxIn('radius.sm') },
  };
}
