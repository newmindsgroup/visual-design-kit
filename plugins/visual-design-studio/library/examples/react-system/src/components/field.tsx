// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Shared field parts: label, hint, error and the id wiring every form control uses.
import { useId, type ComponentProps, type ReactNode } from 'react';
import { cx } from '../lib/cx';
import { IconDanger } from './icons';

/**
 * Which fields carry a visible marker. Pick one convention per form ("mark the minority"):
 * 'optional' labels non-required fields "(optional)", 'required' adds an asterisk to required ones
 * (explain the asterisk once at the top of the form), 'none' shows no marker.
 * The native `required` attribute is always set from `required`, whatever the marker.
 */
export type NecessityIndicator = 'optional' | 'required' | 'none';

export interface FieldIds {
  id: string;
  labelId: string;
  hintId: string;
  errorId: string;
}

export function useFieldIds(id?: string): FieldIds {
  const generated = useId();
  const base = id ?? `field${generated.replace(/[^a-zA-Z0-9_-]/g, '')}`;
  return { id: base, labelId: `${base}-label`, hintId: `${base}-hint`, errorId: `${base}-error` };
}

/** Joins describedby ids, dropping empty ones. Hint comes before error so it is read first. */
export function describedBy(...ids: Array<string | false | null | undefined>): string | undefined {
  const list = ids.filter(Boolean).join(' ').trim();
  return list || undefined;
}

export function FieldLabel({
  children,
  required,
  necessityIndicator = 'none',
  disabled,
  className,
  ...rest
}: ComponentProps<'label'> & { required?: boolean; necessityIndicator?: NecessityIndicator; disabled?: boolean }) {
  return (
    <label
      data-slot="field-label"
      className={cx('text-sm font-medium leading-snug text-default', disabled && 'text-muted', className)}
      {...rest}
    >
      {children}
      <NecessityMark required={required} necessityIndicator={necessityIndicator} />
    </label>
  );
}

export function NecessityMark({ required, necessityIndicator = 'none' }: { required?: boolean; necessityIndicator?: NecessityIndicator }) {
  if (necessityIndicator === 'optional' && !required) {
    return <span className="ms-1 font-regular text-muted">(optional)</span>;
  }
  if (necessityIndicator === 'required' && required) {
    // The input's native required state is what assistive technology announces; the asterisk is visual.
    return (
      <span className="ms-0.5 text-danger" aria-hidden="true">
        *
      </span>
    );
  }
  return null;
}

export function FieldHint({ children, className, ...rest }: ComponentProps<'p'>) {
  return (
    <p data-slot="field-hint" className={cx('text-sm leading-snug text-muted', className)} {...rest}>
      {children}
    </p>
  );
}

export function FieldError({ children, className, ...rest }: ComponentProps<'p'> & { children: ReactNode }) {
  return (
    <p data-slot="field-error" className={cx('flex items-start gap-1 text-sm font-medium leading-snug text-danger', className)} {...rest}>
      <IconDanger size="sm" className="mt-0.5" />
      <span>{children}</span>
    </p>
  );
}
