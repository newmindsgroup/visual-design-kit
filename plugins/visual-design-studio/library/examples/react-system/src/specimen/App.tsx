// Version-Timestamp: 2026-10-20 02:52:00 UTC
import { useEffect, useState } from 'react';
import { Badge } from '../components/badge';
import { Button } from '../components/button';
import { IconArrowRight, IconCheckCircle } from '../components/icons';
import { Switch } from '../components/switch';
import { cx } from '../lib/cx';
import { BRANDS, THEMES } from '../shared/display';
import { AppProviders, SiteFooter, SiteHeader, SkipLink } from '../shared/shell';
import { ButtonSection } from './sections-actions';
import { AlertSection, BadgeSection, CardSection, DataTableSection, EmptyStateSection, SkeletonSection } from './sections-display';
import { CheckboxSection, RadioSection, SelectSection, SwitchSection, TextFieldSection } from './sections-inputs';
import { DialogSection, TabsSection, ToastSection, TooltipSection } from './sections-overlays';

const sections = [
  { id: 'button', title: 'Button' },
  { id: 'text-field', title: 'Text field' },
  { id: 'select', title: 'Select' },
  { id: 'checkbox', title: 'Checkbox' },
  { id: 'switch', title: 'Switch' },
  { id: 'radio-group', title: 'Radio group' },
  { id: 'dialog', title: 'Dialog' },
  { id: 'tabs', title: 'Tabs' },
  { id: 'toast', title: 'Toast' },
  { id: 'tooltip', title: 'Tooltip' },
  { id: 'card', title: 'Card' },
  { id: 'badge', title: 'Badge' },
  { id: 'alert', title: 'Alert and Banner' },
  { id: 'data-table', title: 'Data table' },
  { id: 'empty-state', title: 'Empty state' },
  { id: 'skeleton', title: 'Skeleton' },
];

function useActiveSection(ids: string[]) {
  const [active, setActive] = useState<string | null>(null);
  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries.filter((e) => e.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (visible[0]) setActive(visible[0].target.id);
      },
      { rootMargin: '-20% 0px -70% 0px' },
    );
    for (const id of ids) {
      const el = document.getElementById(id);
      if (el) observer.observe(el);
    }
    return () => observer.disconnect();
  }, [ids]);
  return active;
}

function SideNav() {
  const active = useActiveSection(sections.map((s) => s.id));
  return (
    <nav aria-label="Components" className="sticky top-20 hidden w-52 shrink-0 self-start py-12 lg:block">
      <p className="px-2 text-xs font-semibold uppercase tracking-caps text-muted">Components</p>
      <ol className="mt-3 grid gap-0.5">
        {sections.map((s, i) => (
          <li key={s.id}>
            <a
              href={`#${s.id}`}
              aria-current={active === s.id ? 'true' : undefined}
              className={cx(
                'flex items-center gap-3 rounded-md px-2 py-1 text-sm no-underline transition-colors duration-fast',
                active === s.id ? 'bg-sunken font-medium text-default' : 'text-muted hover:bg-sunken hover:text-default',
              )}
            >
              <span className="w-5 font-mono text-xs text-muted" aria-hidden="true">
                {String(i + 1).padStart(2, '0')}
              </span>
              {s.title}
            </a>
          </li>
        ))}
      </ol>
      <a
        href="./billing.html"
        className="mt-6 flex items-center gap-2 rounded-md border-t border-subtle px-2 pt-4 text-sm font-medium text-accent no-underline hover:underline"
      >
        Composed screen
        <IconArrowRight size="sm" />
      </a>
    </nav>
  );
}

function ThemeTile({ brand, theme }: { brand: (typeof BRANDS)[number]; theme: (typeof THEMES)[number] }) {
  return (
    <div data-brand={brand.value} data-theme={theme.value} className="grid gap-4 bg-canvas p-5 text-default">
      <div className="flex items-center justify-between gap-3">
        <span className="text-xs font-semibold uppercase tracking-caps text-muted">
          {brand.label} · {theme.label}
        </span>
        <span className="flex gap-1" aria-hidden="true">
          <span className="size-3 rounded-full bg-accent" />
          <span className="size-3 rounded-full bg-accent-subtle ring-1 ring-(--color-border-default)" />
          <span className="size-3 rounded-full bg-inverse" />
        </span>
      </div>
      <p className="font-display text-2xl font-semibold leading-tight tracking-tight">Invoice paid</p>
      <div className="flex flex-wrap items-center gap-2">
        <Button size="sm">Download</Button>
        <Button size="sm" variant="secondary">
          Share
        </Button>
        <Badge tone="success" icon={<IconCheckCircle />}>
          $412.50
        </Badge>
      </div>
      <Switch label="Auto-pay" defaultChecked />
    </div>
  );
}

function Intro() {
  return (
    <section aria-labelledby="intro-title" className="pb-16 pt-10 lg:pt-14">
      <p className="text-xs font-semibold uppercase tracking-caps text-accent">Visual Design Kit · Reference implementation</p>
      <h1 id="intro-title" className="mt-4 max-w-(--container-md) font-display text-4xl font-semibold leading-tight tracking-tight text-default sm:text-5xl">
        Sixteen components, every state, one set of tokens.
      </h1>
      <p className="mt-6 max-w-(--measure-body) text-lg leading-relaxed text-muted">
        React, Radix Primitives and Tailwind CSS v4. Components read only semantic and component tokens from{' '}
        <code className="font-mono text-md text-default">tokens.css</code>, so the same code renders Meridian or Ember, in light, dark
        or high contrast, left to right or right to left. Copy a component into a project, or read it as the spec in code.
      </p>
      <div className="mt-8 flex flex-wrap gap-3">
        <Button asChild endIcon={<IconArrowRight />}>
          <a href="./billing.html">See the composed screen</a>
        </Button>
        <Button asChild variant="secondary">
          <a href="#button">Browse components</a>
        </Button>
      </div>
      <dl className="mt-12 grid grid-cols-2 gap-px overflow-hidden rounded-lg border border-subtle bg-(--color-border-subtle) sm:grid-cols-4">
        {[
          ['16', 'components with typed props'],
          ['6', 'brand and theme contexts'],
          ['WCAG 2.2 AA', 'axe-checked in each context'],
          ['0', 'raw colors in component code'],
        ].map(([value, label]) => (
          <div key={label} className="flex flex-col-reverse justify-end gap-1 bg-surface p-5">
            <dt className="text-sm text-muted">{label}</dt>
            <dd className="font-display text-2xl font-semibold tracking-tight text-default tabular-nums">{value}</dd>
          </div>
        ))}
      </dl>
      <figure className="m-0 mt-12">
        <figcaption className="mb-3 flex flex-wrap items-baseline justify-between gap-2">
          <span className="text-sm font-semibold text-default">The same components in all six contexts</span>
          <span className="text-xs text-muted">
            Nested <code className="font-mono">data-brand</code> and <code className="font-mono">data-theme</code> wrappers; static
          </span>
        </figcaption>
        <div inert className="grid gap-px overflow-hidden rounded-lg border border-subtle bg-(--color-border-subtle) sm:grid-cols-2 xl:grid-cols-3">
          {BRANDS.flatMap((brand) => THEMES.map((theme) => <ThemeTile key={`${brand.value}-${theme.value}`} brand={brand} theme={theme} />))}
        </div>
      </figure>
    </section>
  );
}

function ComposedCta() {
  return (
    <section aria-labelledby="composed-title" className="border-t border-subtle py-16">
      <div className="grid gap-6 rounded-xl border border-subtle bg-surface p-8 sm:p-10 lg:grid-cols-3 lg:items-center">
        <div className="lg:col-span-2">
          <p className="text-xs font-semibold uppercase tracking-caps text-accent">Composed screen</p>
          <h2 id="composed-title" className="mt-2 font-display text-3xl font-semibold tracking-tight text-default">
            Billing settings for a design studio workspace
          </h2>
          <p className="mt-3 max-w-(--measure-body) text-md leading-relaxed text-muted">
            A banner, plan cards, tabs, a sortable and selectable invoice table, a validated form, a plan-change dialog, a
            destructive confirmation and toasts, built only from the parts above.
          </p>
        </div>
        <div className="lg:justify-self-end">
          <Button asChild size="lg" endIcon={<IconArrowRight />}>
            <a href="./billing.html">Open the billing screen</a>
          </Button>
        </div>
      </div>
    </section>
  );
}

export function SpecimenApp() {
  return (
    <AppProviders>
      <SkipLink />
      <SiteHeader current="components" />
      <div className="mx-auto flex max-w-(--container-xl) gap-12 px-(--gutter)">
        <SideNav />
        <main id="main" tabIndex={-1} className="min-w-0 flex-1 outline-none">
          <Intro />
          <ButtonSection />
          <TextFieldSection />
          <SelectSection />
          <CheckboxSection />
          <SwitchSection />
          <RadioSection />
          <DialogSection />
          <TabsSection />
          <ToastSection />
          <TooltipSection />
          <CardSection />
          <BadgeSection />
          <AlertSection />
          <DataTableSection />
          <EmptyStateSection />
          <SkeletonSection />
          <ComposedCta />
        </main>
      </div>
      <SiteFooter />
    </AppProviders>
  );
}
