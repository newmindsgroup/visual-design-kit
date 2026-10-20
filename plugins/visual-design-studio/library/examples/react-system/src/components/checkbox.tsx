// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Checkbox: independent on/off choice, or agreement. Radix Checkbox (role=checkbox, Space toggles, mixed state).
import * as RadixCheckbox from '@radix-ui/react-checkbox';
import type { ComponentProps, ReactNode } from 'react';
import { cx } from '../lib/cx';
import { describedBy, FieldError, useFieldIds } from './field';
import { IconCheck, IconMinus } from './icons';
import type { PreviewState } from './types';

type RootProps = Omit<ComponentProps<typeof RadixCheckbox.Root>, 'children' | 'asChild' | 'aria-label'>;

interface CheckboxOwnProps {
  /** Secondary text under the label, linked with aria-describedby. */
  description?: ReactNode;
  error?: ReactNode;
  invalid?: boolean;
  'data-preview-state'?: PreviewState;
}

/** A visible label, or (inside tables and similar) an aria-label. One of the two is required. */
export type CheckboxProps = RootProps &
  CheckboxOwnProps &
  ({ label: ReactNode; 'aria-label'?: never } | { label?: never; 'aria-label': string });

/** The 20px box inside a 24px hit area (44px on coarse pointers). Exported for static previews. */
export const checkboxBoxClass = cx(
  'grid size-5 place-items-center rounded-sm border border-(--input-border) bg-(--input-bg) text-on-accent',
  'transition-colors duration-fast ease-standard hc:border-2',
  'group-hover:border-(--color-fg-muted) group-focus-visible:focus-ring',
  'group-data-[state=checked]:border-accent group-data-[state=checked]:bg-accent',
  'group-data-[state=indeterminate]:border-accent group-data-[state=indeterminate]:bg-accent',
  'group-aria-invalid:border-(--input-border-invalid)',
  'group-disabled:border-default group-disabled:bg-sunken group-disabled:text-subtle',
  'group-disabled:group-data-[state=checked]:border-default group-disabled:group-data-[state=checked]:bg-sunken',
  'group-disabled:group-data-[state=indeterminate]:border-default group-disabled:group-data-[state=indeterminate]:bg-sunken',
);

export function Checkbox({
  label,
  description,
  error,
  invalid,
  id,
  className,
  disabled,
  'aria-describedby': ariaDescribedBy,
  ...rest
}: CheckboxProps) {
  const ids = useFieldIds(id);
  const isInvalid = Boolean(error) || Boolean(invalid);
  const descId = `${ids.id}-desc`;

  const control = (
    <RadixCheckbox.Root
      id={ids.id}
      disabled={disabled}
      aria-invalid={isInvalid || undefined}
      aria-describedby={describedBy(description ? descId : null, error ? ids.errorId : null, ariaDescribedBy)}
      data-slot="checkbox"
      className={cx(
        'group relative inline-grid size-(--size-target-min) shrink-0 cursor-pointer place-items-center rounded-sm outline-none',
        'disabled:cursor-not-allowed pointer-coarse:after:absolute pointer-coarse:after:-inset-2.5',
      )}
      {...rest}
    >
      <span className={checkboxBoxClass} data-slot="checkbox-box">
        <RadixCheckbox.Indicator className="grid place-items-center">
          <IconCheck size="sm" strokeWidth={2.5} className="group-data-[state=indeterminate]:hidden" />
          <IconMinus size="sm" strokeWidth={2.5} className="hidden group-data-[state=indeterminate]:block" />
        </RadixCheckbox.Indicator>
      </span>
    </RadixCheckbox.Root>
  );

  if (!label) return <span className={cx('inline-flex', className)}>{control}</span>;

  return (
    <div data-slot="checkbox-field" className={cx('flex items-start gap-2', className)}>
      {control}
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
        {error ? (
          <FieldError id={ids.errorId} className="mt-1">
            {error}
          </FieldError>
        ) : null}
      </div>
    </div>
  );
}
