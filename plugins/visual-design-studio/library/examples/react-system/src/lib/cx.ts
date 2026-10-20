// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Props-to-class helpers. Plain TypeScript (erasable syntax only) so node:test can import it directly.

export type ClassValue = string | number | false | null | undefined | ClassValue[];

/** Joins truthy class names, flattening arrays. `cx('a', cond && 'b', ['c', null])` -> "a b c". */
export function cx(...inputs: ClassValue[]): string {
  const out: string[] = [];
  const push = (value: ClassValue): void => {
    if (value === null || value === undefined || value === false || value === '') return;
    if (Array.isArray(value)) {
      for (const item of value) push(item);
      return;
    }
    const text = String(value).trim();
    if (text) out.push(text);
  };
  for (const input of inputs) push(input);
  return out.join(' ');
}

type VariantMap = Record<string, Record<string, ClassValue>>;

/** A variant whose options are only "true"/"false" is exposed as a boolean prop. */
type OptionOf<Options> = keyof Options extends 'true' | 'false' ? boolean : keyof Options & string;

export type VariantSelection<V extends VariantMap> = { [K in keyof V]?: OptionOf<V[K]> };

export interface Recipe<V extends VariantMap> {
  base?: ClassValue;
  variants: V;
  defaultVariants?: VariantSelection<V>;
  /** Extra classes when every listed variant matches, e.g. { variant: 'ghost', size: 'sm', class: '...' }. */
  compoundVariants?: Array<VariantSelection<V> & { class: ClassValue }>;
}

export type RecipeFn<V extends VariantMap> = ((props?: VariantSelection<V> & { className?: ClassValue }) => string) & {
  /** The variant names and their options, for docs, Figma Code Connect maps and tests. */
  options: { [K in keyof V]: Array<keyof V[K] & string> };
};

/**
 * Maps typed props to Tailwind classes (a small, dependency-free take on the class-variance pattern).
 * Unknown option values throw in development so typos surface early instead of rendering unstyled.
 */
export function variants<V extends VariantMap>(recipe: Recipe<V>): RecipeFn<V> {
  const names = Object.keys(recipe.variants) as Array<keyof V & string>;
  const fn = (props: VariantSelection<V> & { className?: ClassValue } = {}): string => {
    const resolved: Record<string, string> = {};
    const classes: ClassValue[] = [recipe.base];
    for (const name of names) {
      const raw = props[name] ?? recipe.defaultVariants?.[name];
      if (raw === undefined) continue;
      const key = String(raw);
      const options = recipe.variants[name];
      if (!Object.prototype.hasOwnProperty.call(options, key)) {
        throw new Error(`variants(): unknown ${name}="${key}". Expected one of ${Object.keys(options).join(', ')}.`);
      }
      resolved[name] = key;
      classes.push(options[key]);
    }
    for (const compound of recipe.compoundVariants ?? []) {
      const { class: extra, ...conditions } = compound;
      const matches = Object.entries(conditions).every(([name, value]) => resolved[name] === String(value));
      if (matches) classes.push(extra);
    }
    classes.push(props.className);
    return cx(...classes);
  };
  const options = {} as { [K in keyof V]: Array<keyof V[K] & string> };
  for (const name of names) options[name] = Object.keys(recipe.variants[name]) as Array<keyof V[typeof name] & string>;
  return Object.assign(fn, { options });
}
