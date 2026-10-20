// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Radio group, radio cards and segmented control: one choice from 2-5 visible options.
// Radix RadioGroup: one tab stop, arrow keys move and select (mirrored in RTL via DirectionProvider).
import * as RadixRadio from '@radix-ui/react-radio-group';
import type { ComponentProps, ReactNode } from 'react';
import { cx } from '../lib/cx';
import { describedBy, FieldError, FieldHint, NecessityMark, useFieldIds, type NecessityIndicator } from './field';
import type { PreviewState } from './types';

type RootProps = Omit<ComponentProps<typeof RadixRadio.Root>, 'asChild' | 'aria-label' | 'aria-labelledby'>;

export type RadioGroupProps = RootProps & {
  /** Group label (exposed as the radiogroup's accessible name). */
  label: ReactNode;
  hint?: ReactNode;
  error?: ReactNode;
  necessityIndicator?: NecessityIndicator;
  /** Show the group label visually (default) or only to assistive technology. */
  labelVisible?: boolean;
};

export function RadioGroup({
  label,
  hint,
  error,
  necessityIndicator = 'none',
  labelVisible = true,
  orientation = 'vertical',
  id,
  className,
  children,
  required,
  ...rest
}: RadioGroupProps) {
  const ids = useFieldIds(id);
  return (
    <div data-slot="radio-group-field" className={cx('flex min-w-0 flex-col gap-1', className)}>
      <span id={ids.labelId} className={cx('text-sm font-medium leading-snug text-default', !labelVisible && 'sr-only')}>
        {label}
        <NecessityMark required={required} necessityIndicator={necessityIndicator} />
      </span>
      {hint ? <FieldHint id={ids.hintId}>{hint}</FieldHint> : null}
      <RadixRadio.Root
        id={ids.id}
        orientation={orientation}
        required={required}
        aria-labelledby={ids.labelId}
        aria-describedby={describedBy(hint ? ids.hintId : null, error ? ids.errorId : null)}
        aria-invalid={error ? true : undefined}
        data-slot="radio-group"
        className={cx(
          'mt-1',
          orientation === 'horizontal' ? 'flex flex-wrap gap-x-6 gap-y-3' : 'grid gap-3',
        )}
        {...rest}
      >
        {children}
      </RadixRadio.Root>
      {error ? (
        <FieldError id={ids.errorId} className="mt-1">
          {error}
        </FieldError>
      ) : null}
    </div>
  );
}

export const radioCircleClass = cx(
  'grid size-5 place-items-center rounded-full border border-(--input-border) bg-(--input-bg)',
  'transition-colors duration-fast ease-standard hc:border-2',
  'group-hover:border-(--color-fg-muted) group-focus-visible:focus-ring',
  'group-data-[state=checked]:border-accent group-data-[state=checked]:border-2',
  'group-disabled:border-default group-disabled:bg-sunken',
);

export interface RadioProps {
  value: string;
  label: ReactNode;
  description?: ReactNode;
  disabled?: boolean;
  id?: string;
  className?: string;
  'data-preview-state'?: PreviewState;
}

export function Radio({ value, label, description, disabled, id, className, 'data-preview-state': previewState }: RadioProps) {
  const ids = useFieldIds(id);
  const descId = `${ids.id}-desc`;
  return (
    <div data-slot="radio-field" className={cx('flex items-start gap-2', className)}>
      <RadixRadio.Item
        id={ids.id}
        value={value}
        disabled={disabled}
        aria-describedby={description ? descId : undefined}
        data-preview-state={previewState}
        data-slot="radio"
        className={cx(
          'group relative inline-grid size-(--size-target-min) shrink-0 cursor-pointer place-items-center rounded-full outline-none',
          'disabled:cursor-not-allowed pointer-coarse:after:absolute pointer-coarse:after:-inset-2.5',
        )}
      >
        <span className={radioCircleClass} data-slot="radio-circle">
          <RadixRadio.Indicator className="size-2.5 rounded-full bg-accent group-disabled:bg-(--color-border-strong)" data-slot="radio-dot" />
        </span>
      </RadixRadio.Item>
      <div className="grid min-w-0 gap-0.5 py-0.5">
        <label
          htmlFor={ids.id}
          className={cx('text-md leading-snug', disabled ? 'cursor-not-allowed text-muted' : 'cursor-pointer text-default')}
        >
          {label}
        </label>
        {description ? (
          <p id={descId} className="text-sm leading-snug text-muted">
            {description}
          </p>
        ) : null}
      </div>
    </div>
  );
}

export interface RadioCardProps {
  value: string;
  label: ReactNode;
  description?: ReactNode;
  /** Right-aligned detail such as a price; read after the label. */
  meta?: ReactNode;
  /** Small marker such as a "Current plan" badge. */
  badge?: ReactNode;
  disabled?: boolean;
  className?: string;
}

/** A whole-card radio for choices that need more than a line of explanation (plans, delivery options). */
export function RadioCard({ value, label, description, meta, badge, disabled, className }: RadioCardProps) {
  const ids = useFieldIds();
  return (
    <RadixRadio.Item
      value={value}
      disabled={disabled}
      aria-labelledby={ids.labelId}
      aria-describedby={describedBy(meta ? `${ids.id}-meta` : null, description ? `${ids.id}-desc` : null)}
      data-slot="radio-card"
      className={cx(
        'group relative flex w-full cursor-pointer items-start gap-3 rounded-lg border border-default bg-surface p-4 text-start outline-none',
        'transition-colors duration-fast ease-standard hover:border-strong focus-visible:focus-ring',
        'data-[state=checked]:border-accent data-[state=checked]:bg-accent-subtle data-[state=checked]:ring-1 data-[state=checked]:ring-accent data-[state=checked]:ring-inset',
        'disabled:cursor-not-allowed disabled:bg-sunken',
        className,
      )}
    >
      <span className={cx(radioCircleClass, 'mt-0.5')} data-slot="radio-circle">
        <RadixRadio.Indicator className="size-2.5 rounded-full bg-accent" data-slot="radio-dot" />
      </span>
      <span className="grid min-w-0 flex-1 gap-1">
        <span className="flex flex-wrap items-center gap-2">
          <span id={ids.labelId} className="font-semibold text-default">
            {label}
          </span>
          {badge}
        </span>
        {description ? (
          <span id={`${ids.id}-desc`} className="text-sm text-muted group-data-[state=checked]:text-default">
            {description}
          </span>
        ) : null}
      </span>
      {meta ? (
        <span id={`${ids.id}-meta`} className="shrink-0 text-end text-sm font-semibold tabular-nums text-default">
          {meta}
        </span>
      ) : null}
    </RadixRadio.Item>
  );
}

export type SegmentedControlProps = Omit<RootProps, 'orientation'> & {
  label: ReactNode;
  /** Visible label beside the control (default) or screen-reader only. */
  labelVisible?: boolean;
  size?: 'sm' | 'md';
};

/** One of 2-5 views or modes with immediate effect (radiogroup semantics, segmented appearance). */
export function SegmentedControl({ label, labelVisible = true, size = 'md', className, children, ...rest }: SegmentedControlProps) {
  const ids = useFieldIds();
  return (
    <div data-slot="segmented-control" className={cx('flex min-w-0 items-center gap-2', className)} data-size={size}>
      <span id={ids.labelId} className={cx('text-xs font-semibold uppercase tracking-caps text-muted', !labelVisible && 'sr-only')}>
        {label}
      </span>
      <RadixRadio.Root
        orientation="horizontal"
        aria-labelledby={ids.labelId}
        className="inline-flex rounded-md border border-subtle bg-sunken p-0.5"
        {...rest}
      >
        {children}
      </RadixRadio.Root>
    </div>
  );
}

export function SegmentedItem({ value, children, disabled, className }: { value: string; children: ReactNode; disabled?: boolean; className?: string }) {
  return (
    <RadixRadio.Item
      value={value}
      disabled={disabled}
      className={cx(
        'inline-flex h-8 min-w-(--size-target-comfortable) cursor-pointer items-center justify-center gap-1 whitespace-nowrap rounded-sm border border-transparent px-3 text-sm font-medium text-muted outline-none',
        'transition-colors duration-fast ease-standard hover:text-default focus-visible:focus-ring',
        'data-[state=checked]:border-default data-[state=checked]:bg-surface-raised data-[state=checked]:text-default data-[state=checked]:shadow-sm',
        'disabled:cursor-not-allowed disabled:text-subtle',
        'in-data-[size=sm]:h-7 in-data-[size=sm]:px-2',
        className,
      )}
    >
      {children}
    </RadixRadio.Item>
  );
}
