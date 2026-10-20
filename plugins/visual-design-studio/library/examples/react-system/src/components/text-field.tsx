// Version-Timestamp: 2026-10-20 02:52:00 UTC
// TextField: single-line text input with label, hint and error. Spec: component-specs/text-field.md (TF-S1 to TF-S8).
import type { ChangeEvent, ComponentProps, ReactNode } from 'react';
import { cx, variants } from '../lib/cx';
import { describedBy, FieldError, FieldHint, FieldLabel, useFieldIds, type NecessityIndicator } from './field';
import type { PreviewState, Size } from './types';

export const fieldControlStyles = variants({
  base: [
    'relative flex w-full items-center gap-2 rounded-(--input-radius) border',
    'transition-colors duration-fast ease-standard focus-within:focus-ring',
  ],
  variants: {
    size: {
      sm: 'h-8 px-2 text-sm',
      md: 'h-10 px-(--input-padding-x) text-(length:--input-font-size)',
      lg: 'h-12 px-4 text-md',
    },
    // Each state owns its colors so no two classes in one result compete for the same property.
    state: {
      default:
        'border-(--input-border) bg-(--input-bg) text-(--input-fg) hover:border-(--color-fg-muted) hc:hover:border-strong focus-within:border-(--input-border-focus)',
      invalid: 'border-(--input-border-invalid) bg-(--input-bg) text-(--input-fg)',
      disabled: 'cursor-not-allowed border-default bg-(--input-bg-disabled) text-subtle',
      readonly: 'border-dashed border-default bg-sunken text-default',
    },
  },
  defaultVariants: { size: 'md', state: 'default' },
});

export type TextFieldProps = Omit<ComponentProps<'input'>, 'size' | 'children'> & {
  /** Visible label. Required: placeholders are never a label. */
  label: ReactNode;
  /** Help text read before typing (linked with aria-describedby). */
  hint?: ReactNode;
  /** Error message. Setting it marks the field invalid; it replaces nothing, the hint stays. */
  error?: ReactNode;
  /** Invalid without an inline message (for example when the message lives in a form summary). */
  invalid?: boolean;
  size?: Size;
  necessityIndicator?: NecessityIndicator;
  /** Non-interactive prefix inside the field, such as a currency symbol or protocol. */
  startAdornment?: ReactNode;
  /** Suffix inside the field: a unit, or an interactive control such as a clear button. */
  endAdornment?: ReactNode;
  /** Called with the new string value on every edit (alongside the native onChange). */
  onValueChange?: (value: string) => void;
  /** Classes for the input element itself; `className` goes on the outer wrapper. */
  inputClassName?: string;
  /**
   * Keep labels visible. Hide one only in a toolbar where an adjacent icon and placeholder make the purpose
   * obvious (a search field); the label is still the accessible name.
   */
  labelVisible?: boolean;
  'data-preview-state'?: PreviewState;
};

export function TextField({
  label,
  hint,
  error,
  invalid,
  size = 'md',
  necessityIndicator = 'none',
  startAdornment,
  endAdornment,
  onValueChange,
  onChange,
  className,
  inputClassName,
  labelVisible = true,
  id,
  required,
  disabled,
  readOnly,
  'aria-describedby': ariaDescribedBy,
  'data-preview-state': previewState,
  ...rest
}: TextFieldProps) {
  const ids = useFieldIds(id);
  const isInvalid = Boolean(error) || Boolean(invalid);
  const state = disabled ? 'disabled' : readOnly ? 'readonly' : isInvalid ? 'invalid' : 'default';

  const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
    onChange?.(event);
    onValueChange?.(event.target.value);
  };

  return (
    <div
      data-slot="text-field"
      data-invalid={isInvalid || undefined}
      data-disabled={disabled || undefined}
      className={cx('flex min-w-0 flex-col gap-1', className)}
    >
      <FieldLabel
        htmlFor={ids.id}
        id={ids.labelId}
        required={required}
        necessityIndicator={necessityIndicator}
        disabled={disabled}
        className={labelVisible ? undefined : 'sr-only'}
      >
        {label}
      </FieldLabel>
      {hint ? <FieldHint id={ids.hintId}>{hint}</FieldHint> : null}
      <div className={cx(fieldControlStyles({ size, state }), hint ? 'mt-1' : null)} data-preview-state={previewState}>
        {startAdornment ? (
          <span className="flex shrink-0 items-center text-muted [&>svg]:size-(--size-icon-md)" data-slot="adornment">
            {startAdornment}
          </span>
        ) : null}
        <input
          id={ids.id}
          required={required}
          disabled={disabled}
          readOnly={readOnly}
          aria-invalid={isInvalid || undefined}
          aria-describedby={describedBy(hint ? ids.hintId : null, error ? ids.errorId : null, ariaDescribedBy)}
          onChange={handleChange}
          className={cx(
            'h-full min-w-0 flex-1 bg-transparent text-inherit outline-none placeholder:text-muted',
            'disabled:cursor-not-allowed read-only:cursor-default',
            inputClassName,
          )}
          {...rest}
        />
        {endAdornment ? (
          <span className="flex shrink-0 items-center text-muted [&>svg]:size-(--size-icon-md)" data-slot="adornment">
            {endAdornment}
          </span>
        ) : null}
      </div>
      {error ? (
        <FieldError id={ids.errorId} className="mt-1">
          {error}
        </FieldError>
      ) : null}
    </div>
  );
}
