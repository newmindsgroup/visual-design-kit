// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Badge: a short, non-interactive status or count. The text carries the meaning; tone only reinforces it.
import type { ComponentProps, ReactNode } from 'react';
import { cx, variants } from '../lib/cx';
import type { Tone } from './types';

export const badgeStyles = variants({
  base: [
    'inline-flex shrink-0 items-center gap-1 whitespace-nowrap rounded-(--badge-radius) border',
    'font-medium leading-none tabular-nums [&>svg]:size-(--size-icon-sm) [&>svg]:-ms-0.5',
  ],
  variants: {
    tone: {
      neutral: '',
      accent: '',
      info: '',
      success: '',
      warning: '',
      danger: '',
    },
    variant: {
      subtle: 'hc:border-current',
      outline: 'bg-transparent',
    },
    size: {
      sm: 'h-5 px-1.5 text-xs',
      md: 'h-6 px-(--badge-padding-x) text-(length:--badge-font-size)',
    },
  },
  // Color pairs come from the --badge-* component tokens (contrast-checked by tokens.py lint).
  compoundVariants: [
    { variant: 'subtle', tone: 'neutral', class: 'border-transparent bg-(--badge-neutral-bg) text-(--badge-neutral-fg)' },
    { variant: 'subtle', tone: 'accent', class: 'border-transparent bg-(--badge-accent-bg) text-(--badge-accent-fg)' },
    { variant: 'subtle', tone: 'info', class: 'border-transparent bg-(--badge-info-bg) text-(--badge-info-fg)' },
    { variant: 'subtle', tone: 'success', class: 'border-transparent bg-(--badge-success-bg) text-(--badge-success-fg)' },
    { variant: 'subtle', tone: 'warning', class: 'border-transparent bg-(--badge-warning-bg) text-(--badge-warning-fg)' },
    { variant: 'subtle', tone: 'danger', class: 'border-transparent bg-(--badge-danger-bg) text-(--badge-danger-fg)' },
    { variant: 'outline', tone: 'neutral', class: 'border-default text-muted' },
    { variant: 'outline', tone: 'accent', class: 'border-accent text-accent' },
    { variant: 'outline', tone: 'info', class: 'border-(--badge-info-border) text-info' },
    { variant: 'outline', tone: 'success', class: 'border-(--badge-success-border) text-success' },
    { variant: 'outline', tone: 'warning', class: 'border-(--badge-warning-border) text-warning' },
    { variant: 'outline', tone: 'danger', class: 'border-(--badge-danger-border) text-danger' },
  ],
  defaultVariants: { tone: 'neutral', variant: 'subtle', size: 'md' },
});

export type BadgeProps = ComponentProps<'span'> & {
  tone?: Tone;
  variant?: 'subtle' | 'outline';
  size?: 'sm' | 'md';
  /** Decorative leading icon (16px). Use it so status never relies on color alone in dense tables. */
  icon?: ReactNode;
};

export function Badge({ tone, variant, size, icon, className, children, ...rest }: BadgeProps) {
  return (
    <span data-slot="badge" data-tone={tone ?? 'neutral'} className={badgeStyles({ tone, variant, size, className })} {...rest}>
      {icon}
      {children}
    </span>
  );
}
