// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Alert (inline, in content) and Banner (page-level, full width): persistent status that stays until resolved.
// Icon + title + text carry the meaning; the status color reinforces it (WCAG 1.4.1).
import type { ReactNode } from 'react';
import { cx, variants } from '../lib/cx';
import { closeButtonClass } from './button';
import { IconCheckCircle, IconDanger, IconInfo, IconWarning, IconX } from './icons';
import type { StatusTone } from './types';

export type AlertTone = Exclude<StatusTone, 'neutral'>;

const alertStyles = variants({
  base: 'flex items-start gap-3 text-default',
  variants: {
    tone: {
      info: 'border-(--color-info-border) bg-info',
      success: 'border-(--color-success-border) bg-success',
      warning: 'border-(--color-warning-border) bg-warning',
      danger: 'border-(--color-danger-border) bg-danger',
    },
    layout: {
      inline: 'rounded-md border p-4',
      banner: 'border-b px-(--gutter) py-3',
    },
  },
  defaultVariants: { tone: 'info', layout: 'inline' },
});

const toneText: Record<AlertTone, string> = {
  info: 'text-info',
  success: 'text-success',
  warning: 'text-warning',
  danger: 'text-danger',
};

const toneIcon: Record<AlertTone, typeof IconInfo> = {
  info: IconInfo,
  success: IconCheckCircle,
  warning: IconWarning,
  danger: IconDanger,
};

export interface AlertProps {
  tone?: AlertTone;
  title: ReactNode;
  children?: ReactNode;
  /** Up to two buttons or links that resolve the status. */
  actions?: ReactNode;
  /** Shows a dismiss button. Omit for statuses that must stay until fixed. */
  onDismiss?: () => void;
  dismissLabel?: string;
  /**
   * Announce changes: 'polite' (role=status) for updates, 'assertive' (role=alert) for urgent errors that
   * appear after an action. Leave 'off' for alerts present on page load.
   */
  live?: 'off' | 'polite' | 'assertive';
  className?: string;
  id?: string;
  /** Focus target for error summaries (tabIndex -1). */
  tabIndex?: number;
}

function AlertImpl({
  tone = 'info',
  title,
  children,
  actions,
  onDismiss,
  dismissLabel = 'Dismiss',
  live = 'off',
  layout,
  className,
  id,
  tabIndex,
}: AlertProps & { layout: 'inline' | 'banner' }) {
  const Icon = toneIcon[tone];
  const role = live === 'assertive' ? 'alert' : live === 'polite' ? 'status' : undefined;
  return (
    <div
      id={id}
      tabIndex={tabIndex}
      role={role}
      data-slot={layout === 'banner' ? 'banner' : 'alert'}
      data-tone={tone}
      className={alertStyles({ tone, layout, className })}
    >
      <Icon className={cx('mt-0.5', toneText[tone])} />
      <div
        className={cx(
          'flex min-w-0 flex-1 gap-x-4 gap-y-1',
          layout === 'banner' ? 'flex-col sm:flex-row sm:flex-wrap sm:items-center' : 'flex-col',
        )}
      >
        <p className={cx('font-semibold leading-snug', toneText[tone])}>{title}</p>
        {children ? <div className="text-sm leading-normal text-default">{children}</div> : null}
        {actions ? (
          <div className={cx('flex flex-wrap items-center gap-2', layout === 'banner' ? 'sm:ms-auto' : 'mt-2')}>{actions}</div>
        ) : null}
      </div>
      {onDismiss ? (
        <button type="button" onClick={onDismiss} aria-label={dismissLabel} className={cx(closeButtonClass, '-me-1 -mt-1')}>
          <IconX size="sm" />
        </button>
      ) : null}
    </div>
  );
}

export function Alert(props: AlertProps) {
  return <AlertImpl {...props} layout="inline" />;
}

export function Banner(props: AlertProps) {
  return <AlertImpl {...props} layout="banner" />;
}
