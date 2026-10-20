// Version-Timestamp: 2026-10-20 02:52:00 UTC
// EmptyState: explains why there is nothing here and offers the next step (create, import, clear filters).
import type { ReactNode } from 'react';
import { cx } from '../lib/cx';

export interface EmptyStateProps {
  title: ReactNode;
  description?: ReactNode;
  /** Decorative icon (24px) shown in a tonal circle. */
  icon?: ReactNode;
  /** One primary action, optionally one secondary. */
  actions?: ReactNode;
  /** Heading level that fits the page outline. */
  headingLevel?: 2 | 3 | 4;
  size?: 'sm' | 'md';
  className?: string;
}

export function EmptyState({ title, description, icon, actions, headingLevel = 3, size = 'md', className }: EmptyStateProps) {
  const Heading = `h${headingLevel}` as 'h2' | 'h3' | 'h4';
  return (
    <div
      data-slot="empty-state"
      className={cx(
        'mx-auto flex max-w-(--measure-narrow) flex-col items-center text-center',
        size === 'sm' ? 'gap-2 px-4 py-8' : 'gap-3 px-6 py-12',
        className,
      )}
    >
      {icon ? (
        <div
          aria-hidden="true"
          className={cx(
            'mb-1 grid place-items-center rounded-full border border-subtle bg-sunken text-muted [&>svg]:size-(--size-icon-lg)',
            size === 'sm' ? 'size-10' : 'size-12',
          )}
        >
          {icon}
        </div>
      ) : null}
      <Heading className={cx('font-display font-semibold leading-snug tracking-tight text-default', size === 'sm' ? 'text-md' : 'text-lg')}>
        {title}
      </Heading>
      {description ? <p className="text-sm leading-normal text-muted">{description}</p> : null}
      {actions ? <div className="mt-2 flex flex-wrap items-center justify-center gap-3">{actions}</div> : null}
    </div>
  );
}
