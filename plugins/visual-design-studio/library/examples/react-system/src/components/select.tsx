// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Select: one of about 6-15 options (Radix Select: combobox trigger + listbox, typeahead, Esc closes).
// For 15+ or searchable options use a combobox instead.
import * as RadixSelect from '@radix-ui/react-select';
import type { ReactNode } from 'react';
import { cx } from '../lib/cx';
import { usePopoverLayerClass } from '../lib/layer';
import { describedBy, FieldError, FieldHint, FieldLabel, useFieldIds, type NecessityIndicator } from './field';
import { IconCheck, IconChevronDown, IconChevronUp } from './icons';
import { fieldControlStyles } from './text-field';
import type { PreviewState, Size } from './types';

export interface SelectProps {
  label: ReactNode;
  hint?: ReactNode;
  error?: ReactNode;
  invalid?: boolean;
  /** Shown when there is no value. An example or instruction, not the label. */
  placeholder?: string;
  value?: string;
  defaultValue?: string;
  onValueChange?: (value: string) => void;
  open?: boolean;
  defaultOpen?: boolean;
  onOpenChange?: (open: boolean) => void;
  disabled?: boolean;
  required?: boolean;
  /** Form field name; Radix renders a hidden native select so the value submits with the form. */
  name?: string;
  autoComplete?: string;
  size?: Size;
  necessityIndicator?: NecessityIndicator;
  /** See TextField: hide only in toolbars where the value makes the purpose obvious. */
  labelVisible?: boolean;
  id?: string;
  className?: string;
  children: ReactNode;
  'data-preview-state'?: PreviewState;
}

export function Select({
  label,
  hint,
  error,
  invalid,
  placeholder,
  size = 'md',
  necessityIndicator = 'none',
  labelVisible = true,
  id,
  className,
  children,
  disabled,
  required,
  'data-preview-state': previewState,
  ...rootProps
}: SelectProps) {
  const ids = useFieldIds(id);
  const layer = usePopoverLayerClass();
  const isInvalid = Boolean(error) || Boolean(invalid);
  const state = disabled ? 'disabled' : isInvalid ? 'invalid' : 'default';

  return (
    <div data-slot="select" className={cx('flex min-w-0 flex-col gap-1', className)}>
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
      <RadixSelect.Root disabled={disabled} required={required} {...rootProps}>
        <RadixSelect.Trigger
          id={ids.id}
          aria-invalid={isInvalid || undefined}
          aria-describedby={describedBy(hint ? ids.hintId : null, error ? ids.errorId : null)}
          data-preview-state={previewState}
          className={cx(
            fieldControlStyles({ size, state }),
            'justify-between text-start outline-none focus-visible:focus-ring data-placeholder:text-(--input-placeholder)',
            'cursor-pointer disabled:cursor-not-allowed',
            hint ? 'mt-1' : null,
          )}
        >
          <span className="min-w-0 flex-1 truncate">
            <RadixSelect.Value placeholder={placeholder} />
          </span>
          <RadixSelect.Icon className="shrink-0 text-muted">
            <IconChevronDown size={size === 'sm' ? 'sm' : 'md'} />
          </RadixSelect.Icon>
        </RadixSelect.Trigger>
        <RadixSelect.Portal>
          <RadixSelect.Content
            position="popper"
            sideOffset={4}
            collisionPadding={8}
            className={cx(
              layer,
              'min-w-(--radix-select-trigger-width) max-h-(--radix-select-content-available-height) overflow-hidden',
              'rounded-md border border-default bg-surface-raised text-default shadow-md',
              'data-[state=open]:animate-popover-in data-[state=closed]:animate-popover-out',
            )}
          >
            <RadixSelect.ScrollUpButton className="flex h-6 items-center justify-center text-muted">
              <IconChevronUp size="sm" />
            </RadixSelect.ScrollUpButton>
            <RadixSelect.Viewport className="p-1">{children}</RadixSelect.Viewport>
            <RadixSelect.ScrollDownButton className="flex h-6 items-center justify-center text-muted">
              <IconChevronDown size="sm" />
            </RadixSelect.ScrollDownButton>
          </RadixSelect.Content>
        </RadixSelect.Portal>
      </RadixSelect.Root>
      {error ? (
        <FieldError id={ids.errorId} className="mt-1">
          {error}
        </FieldError>
      ) : null}
    </div>
  );
}

export interface SelectItemProps {
  value: string;
  children: ReactNode;
  /** Secondary line shown in the list only (not in the trigger). */
  description?: ReactNode;
  disabled?: boolean;
  textValue?: string;
}

export function SelectItem({ value, children, description, disabled, textValue }: SelectItemProps) {
  return (
    <RadixSelect.Item
      value={value}
      disabled={disabled}
      textValue={textValue}
      className={cx(
        'relative flex min-h-(--size-target-comfortable) cursor-pointer select-none flex-col justify-center rounded-sm py-2 ps-8 pe-3 text-md outline-none',
        'data-highlighted:bg-accent-subtle data-highlighted:text-accent',
        'data-disabled:cursor-not-allowed data-disabled:text-subtle',
      )}
    >
      <RadixSelect.ItemIndicator className="absolute start-2 top-1/2 -translate-y-1/2 text-accent">
        <IconCheck size="sm" />
      </RadixSelect.ItemIndicator>
      <RadixSelect.ItemText>{children}</RadixSelect.ItemText>
      {description ? <span className="text-sm text-muted">{description}</span> : null}
    </RadixSelect.Item>
  );
}

export function SelectGroup({ label, children }: { label: ReactNode; children: ReactNode }) {
  return (
    <RadixSelect.Group>
      <RadixSelect.Label className="px-3 pt-3 pb-1 text-xs font-semibold uppercase tracking-caps text-muted">{label}</RadixSelect.Label>
      {children}
    </RadixSelect.Group>
  );
}

export function SelectSeparator() {
  return <RadixSelect.Separator className="my-1 h-px bg-(--color-border-subtle)" />;
}
