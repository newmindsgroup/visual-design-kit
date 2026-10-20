// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Theme, brand and direction live on <html> (data-theme, data-brand, dir). The inline script in each HTML
// entry sets them before first paint from ?theme=&brand=&dir=, then localStorage, then the OS preference.
import { useSyncExternalStore } from 'react';

export type Theme = 'light' | 'dark' | 'high-contrast';
export type Brand = 'meridian' | 'ember';
export type Direction = 'ltr' | 'rtl';
export interface Display {
  theme: Theme;
  brand: Brand;
  dir: Direction;
}

export const THEMES: ReadonlyArray<{ value: Theme; label: string }> = [
  { value: 'light', label: 'Light' },
  { value: 'dark', label: 'Dark' },
  { value: 'high-contrast', label: 'High contrast' },
];
export const BRANDS: ReadonlyArray<{ value: Brand; label: string }> = [
  { value: 'meridian', label: 'Meridian' },
  { value: 'ember', label: 'Ember' },
];

const STORAGE_KEY = 'vdk-react-system:display';
const listeners = new Set<() => void>();
let cache: { key: string; value: Display } | null = null;

function read(): Display {
  const root = document.documentElement;
  const theme = (root.getAttribute('data-theme') as Theme | null) ?? 'light';
  const brand = (root.getAttribute('data-brand') as Brand | null) ?? 'meridian';
  const dir = root.getAttribute('dir') === 'rtl' ? 'rtl' : 'ltr';
  const key = `${theme}|${brand}|${dir}`;
  if (!cache || cache.key !== key) cache = { key, value: { theme, brand, dir } };
  return cache.value;
}

export function setDisplay(patch: Partial<Display>): void {
  const next = { ...read(), ...patch };
  const root = document.documentElement;
  root.setAttribute('data-theme', next.theme);
  root.setAttribute('data-brand', next.brand);
  root.setAttribute('dir', next.dir);
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
  } catch {
    // Storage can be unavailable (private mode); the attributes still apply for this page view.
  }
  // Keep explicit URL parameters in step so a reload shows what is on screen.
  const url = new URL(window.location.href);
  let changed = false;
  for (const [param, value] of Object.entries({ theme: next.theme, brand: next.brand, dir: next.dir })) {
    if (url.searchParams.has(param) && url.searchParams.get(param) !== value) {
      url.searchParams.set(param, value);
      changed = true;
    }
  }
  if (changed) window.history.replaceState(null, '', url);
  for (const listener of listeners) listener();
}

function subscribe(listener: () => void) {
  listeners.add(listener);
  return () => {
    listeners.delete(listener);
  };
}

export function useDisplay(): Display {
  return useSyncExternalStore(subscribe, read, read);
}
