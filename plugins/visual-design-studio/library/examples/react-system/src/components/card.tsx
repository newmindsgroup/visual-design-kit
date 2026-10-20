// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Card: a container for one self-contained object. Card things that are truly separate; use lists or tables
// for collections people scan. One primary link per card (CardLink stretches over the card).
import { Slot } from '@radix-ui/react-slot';
import type { ComponentProps } from 'react';
import { cx, variants } from '../lib/cx';

export const cardStyles = variants({
  base: 'relative flex min-w-0 flex-col rounded-(--card-radius) text-default',
  variants: {
    /** outlined: border on surface; elevated: border plus --card-shadow; sunken: tonal, no border. */
    variant: {
      outlined: 'border border-(--card-border) bg-(--card-bg)',
      elevated: 'border border-(--card-border) bg-(--card-bg) shadow-(--card-shadow)',
      sunken: 'border border-transparent bg-sunken',
    },
    padding: {
      none: '',
      sm: 'gap-3 p-4',
      md: 'gap-4 p-(--card-padding)',
    },
    interactive: {
      true: 'transition-colors duration-fast ease-standard hover:border-default has-[a:active]:border-strong',
      false: '',
    },
  },
  defaultVariants: { variant: 'outlined', padding: 'md', interactive: false },
});

export type CardProps = ComponentProps<'div'> & {
  variant?: 'outlined' | 'elevated' | 'sunken';
  padding?: 'none' | 'sm' | 'md';
  /** Set when the card contains a CardLink: adds hover feedback for the whole surface. */
  interactive?: boolean;
  /** Render as the child element, for example <article> or <li>. */
  asChild?: boolean;
};

export function Card({ variant, padding, interactive, asChild, className, ...rest }: CardProps) {
  const Comp = asChild ? Slot : 'div';
  return <Comp data-slot="card" className={cardStyles({ variant, padding, interactive, className })} {...rest} />;
}

export function CardHeader({ className, ...rest }: ComponentProps<'div'>) {
  return <div data-slot="card-header" className={cx('flex items-start justify-between gap-3', className)} {...rest} />;
}

export function CardEyebrow({ className, ...rest }: ComponentProps<'p'>) {
  return <p className={cx('text-xs font-semibold uppercase tracking-caps text-muted', className)} {...rest} />;
}

export type CardTitleProps = ComponentProps<'h3'> & { asChild?: boolean };

/** Defaults to h3; use asChild to render the heading level your page outline needs. */
export function CardTitle({ asChild, className, ...rest }: CardTitleProps) {
  const Comp = asChild ? Slot : 'h3';
  return (
    <Comp
      data-slot="card-title"
      className={cx('font-display text-lg font-semibold leading-snug tracking-tight text-default', className)}
      {...rest}
    />
  );
}

export function CardDescription({ className, ...rest }: ComponentProps<'p'>) {
  return <p data-slot="card-description" className={cx('text-sm leading-normal text-muted', className)} {...rest} />;
}

export function CardFooter({ className, ...rest }: ComponentProps<'div'>) {
  return <div data-slot="card-footer" className={cx('mt-auto flex flex-wrap items-center gap-3', className)} {...rest} />;
}

/**
 * The card's primary link. Its ::after covers the whole card, so the card is one large target and the
 * focus ring outlines the card. Put secondary actions in a `relative z-base` wrapper so they stay clickable.
 */
export function CardLink({ className, ...rest }: ComponentProps<'a'>) {
  return (
    <a
      data-slot="card-link"
      className={cx(
        'text-default no-underline outline-none hover:underline',
        'after:absolute after:inset-0 after:rounded-(--card-radius) focus-visible:after:focus-ring',
        className,
      )}
      {...rest}
    />
  );
}
