// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Switch: a setting that takes effect immediately. Never inside a form that has a Save button (use Checkbox).
import * as RadixSwitch from '@radix-ui/react-switch';
import type { ComponentProps, ReactNode } from 'react';
import { cx } from '../lib/cx';
import { describedBy, useFieldIds } from './field';
import { IconCheck } from './icons';
import type { PreviewState } from './types';

type RootProps = Omit<ComponentProps<typeof RadixSwitch.Root>, 'children' | 'asChild'>;

export type SwitchProps = RootProps & {
  label: ReactNode;
  description?: ReactNode;
  /** 'start' puts the label before the switch (settings rows); 'end' puts it after. */
  labelPlacement?: 'start' | 'end';
  'data-preview-state'?: PreviewState;
};

/** Track 44x24px with an 18px thumb; the check mark inside the thumb is the non-color "on" cue. */
export const switchTrackClass = cx(
  'group relative inline-flex h-6 w-11 shrink-0 cursor-pointer items-center rounded-full border outline-none',
  'transition-colors duration-fast ease-standard focus-visible:focus-ring',
  'data-[state=unchecked]:border-strong data-[state=unchecked]:bg-sunken data-[state=unchecked]:hover:bg-(--color-border-subtle)',
  'data-[state=checked]:border-accent data-[state=checked]:bg-accent data-[state=checked]:hover:bg-accent-hover',
  'disabled:cursor-not-allowed disabled:data-[state=unchecked]:border-default disabled:data-[state=checked]:border-default disabled:data-[state=checked]:bg-(--color-border-default)',
  'pointer-coarse:after:absolute pointer-coarse:after:inset-x-0 pointer-coarse:after:-inset-y-2.5',
);

export const switchThumbClass = cx(
  'pointer-events-none ms-0.5 grid size-4.5 place-items-center rounded-full shadow-sm',
  'transition duration-moderate ease-emphasized-decelerate',
  'data-[state=unchecked]:bg-(--color-border-strong) data-[state=checked]:bg-(--color-fg-on-accent) data-[state=checked]:text-accent',
  'data-[state=checked]:translate-x-5 rtl:data-[state=checked]:-translate-x-5',
  'group-disabled:shadow-none group-disabled:data-[state=unchecked]:bg-(--color-border-default) group-disabled:data-[state=checked]:bg-surface group-disabled:data-[state=checked]:text-subtle',
);

export function Switch({ label, description, labelPlacement = 'start', id, className, disabled, ...rest }: SwitchProps) {
  const ids = useFieldIds(id);
  const descId = `${ids.id}-desc`;
  return (
    <div
      data-slot="switch-field"
      className={cx(
        'flex items-start gap-4',
        labelPlacement === 'start' ? 'justify-between' : 'flex-row-reverse justify-end gap-3',
        className,
      )}
    >
      <div className="grid min-w-0 gap-0.5">
        <label
          htmlFor={ids.id}
          className={cx('cursor-pointer text-md leading-snug text-default', disabled && 'cursor-not-allowed text-muted')}
        >
          {label}
        </label>
        {description ? (
          <p id={descId} className="text-sm leading-snug text-muted">
            {description}
          </p>
        ) : null}
      </div>
      <RadixSwitch.Root
        id={ids.id}
        disabled={disabled}
        aria-describedby={describedBy(description ? descId : null)}
        data-slot="switch"
        className={switchTrackClass}
        {...rest}
      >
        <RadixSwitch.Thumb className={switchThumbClass} data-slot="switch-thumb">
          <IconCheck size="custom" strokeWidth={3} className="size-3 opacity-0 transition-opacity duration-fast group-data-[state=checked]:opacity-100" />
        </RadixSwitch.Thumb>
      </RadixSwitch.Root>
    </div>
  );
}
