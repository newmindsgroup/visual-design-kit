// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Page chrome shared by the specimen and the composed billing screen.
import { DirectionProvider } from '@radix-ui/react-direction';
import type { ReactNode } from 'react';
import { SegmentedControl, SegmentedItem } from '../components/radio-group';
import { ToastProvider } from '../components/toast';
import { TooltipProvider } from '../components/tooltip';
import { cx } from '../lib/cx';
import { BRANDS, setDisplay, THEMES, useDisplay, type Brand, type Direction, type Theme } from './display';

export function AppProviders({ children }: { children: ReactNode }) {
  const { dir } = useDisplay();
  return (
    <DirectionProvider dir={dir}>
      <TooltipProvider>
        <ToastProvider>{children}</ToastProvider>
      </TooltipProvider>
    </DirectionProvider>
  );
}

export function SkipLink({ target = 'main' }: { target?: string }) {
  return (
    <a
      href={`#${target}`}
      className={cx(
        'sr-only focus:not-sr-only focus:fixed focus:start-4 focus:top-4 focus:z-toast',
        'focus:rounded-md focus:bg-surface-raised focus:px-4 focus:py-2 focus:text-sm focus:font-semibold focus:text-default focus:shadow-lg',
      )}
    >
      Skip to content
    </a>
  );
}

/** The kit mark: four squares in accent and neutral roles, so it re-colors with brand and theme. */
export function KitMark({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" className={cx('size-6 shrink-0', className)}>
      <rect x="2" y="2" width="9" height="9" rx="2" className="fill-accent" />
      <rect x="13" y="2" width="9" height="9" rx="4.5" className="fill-(--color-fg-default)" />
      <rect x="2" y="13" width="9" height="9" rx="4.5" className="fill-(--color-border-strong)" />
      <rect x="13" y="13" width="9" height="9" rx="2" className="fill-accent" opacity="0.45" />
    </svg>
  );
}

export function DisplayControls({ className }: { className?: string }) {
  const display = useDisplay();
  return (
    <div className={cx('flex flex-wrap items-center gap-x-5 gap-y-2', className)} data-slot="display-controls">
      <SegmentedControl
        label="Theme"
        value={display.theme}
        onValueChange={(value) => setDisplay({ theme: value as Theme })}
        size="sm"
      >
        {THEMES.map((t) => (
          <SegmentedItem key={t.value} value={t.value}>
            {t.label}
          </SegmentedItem>
        ))}
      </SegmentedControl>
      <SegmentedControl label="Brand" value={display.brand} onValueChange={(value) => setDisplay({ brand: value as Brand })} size="sm">
        {BRANDS.map((b) => (
          <SegmentedItem key={b.value} value={b.value}>
            {b.label}
          </SegmentedItem>
        ))}
      </SegmentedControl>
      <SegmentedControl label="Direction" value={display.dir} onValueChange={(value) => setDisplay({ dir: value as Direction })} size="sm">
        <SegmentedItem value="ltr">LTR</SegmentedItem>
        <SegmentedItem value="rtl">RTL</SegmentedItem>
      </SegmentedControl>
    </div>
  );
}

const pages = [
  { id: 'components', href: './index.html', label: 'Components' },
  { id: 'billing', href: './billing.html', label: 'Billing screen' },
] as const;

export function SiteHeader({ current }: { current: (typeof pages)[number]['id'] }) {
  return (
    <header className="border-b border-subtle bg-canvas lg:sticky lg:top-0 lg:z-sticky" data-slot="site-header">
      <div className="mx-auto flex max-w-(--container-xl) flex-wrap items-center gap-x-6 gap-y-3 px-(--gutter) py-3">
        <a href="./index.html" className="flex items-center gap-2 rounded-sm text-default no-underline">
          <KitMark />
          <span className="font-display text-md font-semibold tracking-tight">VDK</span>
          <span className="text-sm text-muted">React reference system</span>
        </a>
        <nav aria-label="Pages" className="me-auto">
          <ul className="flex items-center gap-1">
            {pages.map((page) => (
              <li key={page.id}>
                <a
                  href={page.href}
                  aria-current={page.id === current ? 'page' : undefined}
                  className={cx(
                    'inline-flex h-8 items-center rounded-md px-3 text-sm font-medium no-underline transition-colors duration-fast',
                    page.id === current ? 'bg-sunken text-default' : 'text-muted hover:bg-sunken hover:text-default',
                  )}
                >
                  {page.label}
                </a>
              </li>
            ))}
          </ul>
        </nav>
        <DisplayControls />
      </div>
    </header>
  );
}

export function SiteFooter() {
  return (
    <footer className="border-t border-subtle">
      <div className="mx-auto flex max-w-(--container-xl) flex-col gap-2 px-(--gutter) py-8 text-sm text-muted sm:flex-row sm:items-center sm:justify-between">
        <p>
          Visual Design Kit · <code className="text-xs">library/examples/react-system</code> · MIT
        </p>
        <p>
          Every color, size and timing comes from <code className="text-xs">tokens.css</code>.
        </p>
      </div>
    </footer>
  );
}
