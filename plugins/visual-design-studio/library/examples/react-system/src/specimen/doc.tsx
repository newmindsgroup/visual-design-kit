// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Documentation layout for the specimen: sections, plates and static state matrices.
import type { ReactNode } from 'react';
import { cx } from '../lib/cx';

export function Token({ children }: { children: ReactNode }) {
  return <code className="whitespace-nowrap rounded-sm bg-sunken px-1 py-0.5 font-mono text-xs text-default">{children}</code>;
}

export function Kbd({ children }: { children: ReactNode }) {
  return (
    <kbd className="inline-flex h-5 min-w-5 items-center justify-center rounded-sm border border-default bg-surface px-1 font-mono text-xs text-default shadow-sm">
      {children}
    </kbd>
  );
}

export interface SectionProps {
  id: string;
  number: string;
  title: string;
  summary: ReactNode;
  /** Short contract rows: keyboard, semantics, tokens. */
  contract: Array<[string, ReactNode]>;
  children: ReactNode;
}

export function Section({ id, number, title, summary, contract, children }: SectionProps) {
  return (
    <section id={id} aria-labelledby={`${id}-title`} className="border-t border-subtle py-16">
      <div className="grid gap-x-10 gap-y-6 xl:grid-cols-12">
        <div className="xl:col-span-5">
          <p className="font-mono text-sm text-accent" aria-hidden="true">
            {number}
          </p>
          <h2 id={`${id}-title`} className="mt-1 font-display text-3xl font-semibold tracking-tight text-default">
            {title}
          </h2>
          <p className="mt-3 max-w-(--measure-narrow) text-md leading-relaxed text-muted">{summary}</p>
        </div>
        <dl className="grid content-start gap-x-6 gap-y-4 text-sm sm:grid-cols-3 xl:col-span-7 xl:pt-8">
          {contract.map(([term, description]) => (
            <div key={term} className="border-t border-subtle pt-3">
              <dt className="text-xs font-semibold uppercase tracking-caps text-muted">{term}</dt>
              <dd className="mt-2 leading-normal text-default">{description}</dd>
            </div>
          ))}
        </dl>
      </div>
      <div className="mt-10 grid gap-6">{children}</div>
    </section>
  );
}

export function Plate({
  title,
  note,
  children,
  className,
  bodyClassName,
}: {
  title: string;
  note?: ReactNode;
  children: ReactNode;
  className?: string;
  bodyClassName?: string;
}) {
  return (
    <figure className={cx('m-0 min-w-0 overflow-hidden rounded-lg border border-subtle bg-surface', className)}>
      <figcaption className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1 border-b border-subtle px-5 py-3">
        <span className="text-sm font-semibold text-default">{title}</span>
        {note ? <span className="text-xs text-muted">{note}</span> : null}
      </figcaption>
      <div className={cx('p-5 sm:p-6', bodyClassName)}>{children}</div>
    </figure>
  );
}

const colsClass: Record<number, string> = {
  3: 'lg:grid-cols-3',
  4: 'lg:grid-cols-4',
  5: 'lg:grid-cols-5',
  6: 'lg:grid-cols-6',
  7: 'lg:grid-cols-7',
};

/**
 * Static render of each state, side by side. Marked inert: these are pictures of states (forced with
 * data-preview-state), so they are skipped by Tab and by assistive technology. The live examples follow.
 *
 * layout "rows": one row per variant with state names as column headers (wide screens).
 * layout "grid": every cell carries its own state name and wraps into `columns` columns (form controls).
 */
export function StateMatrix({
  states,
  rows,
  layout = 'rows',
  columns,
  stretch = false,
}: {
  states: string[];
  rows: Array<{ label: string; cells: ReactNode[] }>;
  layout?: 'rows' | 'grid';
  columns?: number;
  /** Let each specimen fill its cell (text fields, selects). */
  stretch?: boolean;
}) {
  const cellClass = cx('flex min-w-0 flex-col justify-start gap-2 px-4 py-5', stretch ? 'items-stretch' : 'items-start');
  if (layout === 'grid') {
    return (
      <div inert className="specimen-grid -m-5 sm:-m-6">
        {rows.map((row) => (
          <div key={row.label} className={cx('grid grid-cols-1 sm:grid-cols-2', colsClass[columns ?? states.length])}>
            {row.cells.map((cell, i) => (
              <div key={states[i]} className={cellClass}>
                <span className="text-xs font-semibold uppercase tracking-caps text-muted">{states[i]}</span>
                {cell}
              </div>
            ))}
          </div>
        ))}
      </div>
    );
  }
  return (
    <div inert className="specimen-grid -m-5 sm:-m-6">
      <div className="hidden border-b border-subtle bg-surface lg:flex">
        <div className="w-28 shrink-0" />
        <div className={cx('grid flex-1', colsClass[states.length])}>
          {states.map((state) => (
            <div key={state} className="px-4 py-2 text-xs font-semibold uppercase tracking-caps text-muted">
              {state}
            </div>
          ))}
        </div>
      </div>
      {rows.map((row) => (
        <div key={row.label} className="border-b border-subtle last:border-b-0 lg:flex">
          <div className="flex w-28 shrink-0 items-center px-5 pt-4 text-sm font-medium text-default lg:px-4 lg:pt-0">
            {row.label}
          </div>
          <div className={cx('grid flex-1 grid-cols-2 sm:grid-cols-3', colsClass[states.length])}>
            {row.cells.map((cell, i) => (
              <div key={states[i]} className={cx(cellClass, 'lg:justify-center')}>
                <span className="text-xs font-semibold uppercase tracking-caps text-muted lg:hidden">{states[i]}</span>
                {cell}
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

/** A labeled cluster of live examples inside a plate. */
export function Example({ label, children, className }: { label?: string; children: ReactNode; className?: string }) {
  return (
    <div className={cx('grid gap-3', className)}>
      {label ? <p className="text-xs font-semibold uppercase tracking-caps text-muted">{label}</p> : null}
      {children}
    </div>
  );
}
