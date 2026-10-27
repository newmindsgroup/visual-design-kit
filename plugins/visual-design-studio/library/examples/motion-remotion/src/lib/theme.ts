// Visual Design Kit, MIT. Part of a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// Pure token selection: no Remotion or React imports, so `npm test` runs it without a browser.
// Input is the kit's library/tokens/dist/tokens.resolved.json (format visual-design-kit/tokens-resolved).

export type Bezier = [number, number, number, number];

export interface ResolvedTokens {
  format: string;
  defaultBrand: string;
  defaultMode: string;
  brands: Record<string, {name: string}>;
  modes: Record<string, {name: string; colorScheme: string}>;
  values: Record<string, Record<string, Record<string, unknown>>>;
}

export interface Theme {
  brand: string;
  brandName: string;
  mode: string;
  color: {
    canvas: string;
    surface: string;
    inverse: string;
    fg: string;
    fgMuted: string;
    fgInverse: string;
    onAccent: string;
    accent: string;
    accentSubtle: string;
    border: string;
  };
  font: {display: string; body: string; displayStack: string; bodyStack: string};
  durationMs: {fast: number; moderate: number; slow: number; slower: number};
  ease: {
    standard: Bezier;
    decelerate: Bezier;
    accelerate: Bezier;
    emphasizedDecelerate: Bezier;
    emphasizedAccelerate: Bezier;
    linear: Bezier;
  };
}

export function parseMs(value: unknown): number {
  if (typeof value === 'number') return value;
  if (typeof value === 'string') {
    const text = value.trim();
    if (text.endsWith('ms')) return Number(text.slice(0, -2));
    if (text.endsWith('s')) return Number(text.slice(0, -1)) * 1000;
  }
  throw new Error(`Not a duration: ${String(value)}`);
}

function bezier(value: unknown, name: string): Bezier {
  if (!Array.isArray(value) || value.length !== 4 || value.some((n) => typeof n !== 'number')) {
    throw new Error(`Token ${name} is not a cubic-bezier`);
  }
  return value as Bezier;
}

function hex(value: unknown, name: string): string {
  if (typeof value !== 'string' || !/^#[0-9a-f]{6}([0-9a-f]{2})?$/i.test(value)) {
    throw new Error(`Token ${name} is not a hex color`);
  }
  return value;
}

function stack(value: unknown): string {
  const families = Array.isArray(value) ? value.map(String) : [String(value)];
  return families.map((f) => (/\s/.test(f) ? `"${f}"` : f)).join(', ');
}

export function selectTheme(tokens: ResolvedTokens, brand?: string, mode?: string): Theme {
  if (tokens.format !== 'visual-design-kit/tokens-resolved') {
    throw new Error('Expected the kit tokens.resolved.json');
  }
  const b = brand ?? tokens.defaultBrand;
  const m = mode ?? tokens.defaultMode;
  const byBrand = tokens.values[b];
  if (!byBrand) throw new Error(`Unknown brand "${b}" (have: ${Object.keys(tokens.values).join(', ')})`);
  const v = byBrand[m];
  if (!v) throw new Error(`Unknown mode "${m}" (have: ${Object.keys(byBrand).join(', ')})`);
  const get = (name: string) => {
    if (!(name in v)) throw new Error(`Missing token ${name}`);
    return v[name];
  };
  const display = get('font.family.display') as string[];
  const body = get('font.family.body') as string[];
  return {
    brand: b,
    brandName: tokens.brands[b]?.name ?? b,
    mode: m,
    color: {
      canvas: hex(get('color.bg.canvas'), 'color.bg.canvas'),
      surface: hex(get('color.bg.surface'), 'color.bg.surface'),
      inverse: hex(get('color.bg.inverse'), 'color.bg.inverse'),
      fg: hex(get('color.fg.default'), 'color.fg.default'),
      fgMuted: hex(get('color.fg.muted'), 'color.fg.muted'),
      fgInverse: hex(get('color.fg.inverse'), 'color.fg.inverse'),
      onAccent: hex(get('color.fg.on-accent'), 'color.fg.on-accent'),
      accent: hex(get('color.accent.default'), 'color.accent.default'),
      accentSubtle: hex(get('color.accent.subtle'), 'color.accent.subtle'),
      border: hex(get('color.border.subtle'), 'color.border.subtle'),
    },
    font: {display: display[0], body: body[0], displayStack: stack(display), bodyStack: stack(body)},
    durationMs: {
      fast: parseMs(get('duration.fast')),
      moderate: parseMs(get('duration.moderate')),
      slow: parseMs(get('duration.slow')),
      slower: parseMs(get('duration.slower')),
    },
    ease: {
      standard: bezier(get('ease.standard'), 'ease.standard'),
      decelerate: bezier(get('ease.decelerate'), 'ease.decelerate'),
      accelerate: bezier(get('ease.accelerate'), 'ease.accelerate'),
      emphasizedDecelerate: bezier(get('ease.emphasized-decelerate'), 'ease.emphasized-decelerate'),
      emphasizedAccelerate: bezier(get('ease.emphasized-accelerate'), 'ease.emphasized-accelerate'),
      linear: bezier(get('ease.linear'), 'ease.linear'),
    },
  };
}

/** WCAG 2.x relative luminance contrast ratio for two #rrggbb colors (alpha ignored). */
export function contrastRatio(a: string, b: string): number {
  const lum = (h: string) => {
    const [r, g, bl] = [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16) / 255).map((c) =>
      c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4,
    );
    return 0.2126 * r + 0.7152 * g + 0.0722 * bl;
  };
  const [hi, lo] = [lum(a), lum(b)].sort((x, y) => y - x);
  return (hi + 0.05) / (lo + 0.05);
}

/** Hex to Lottie [r, g, b, a] in 0-1; matches lottie_build.py hex_to_lottie. */
export function hexToLottie(value: string): [number, number, number, number] {
  let digits = value.replace('#', '');
  if (digits.length === 3 || digits.length === 4) digits = [...digits].map((c) => c + c).join('');
  if (digits.length === 6) digits += 'ff';
  if (digits.length !== 8) throw new Error(`Not a hex color: ${value}`);
  const out = [0, 2, 4, 6].map((i) => Math.round((parseInt(digits.slice(i, i + 2), 16) / 255) * 10000) / 10000);
  return out as [number, number, number, number];
}
