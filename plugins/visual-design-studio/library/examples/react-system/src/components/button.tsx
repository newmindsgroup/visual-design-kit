// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Button: one command. Spec: library/examples/component-specs/button.md (BTN-S1 to BTN-S7).
import { Slot, Slottable } from '@radix-ui/react-slot';
import { useLayoutEffect, useRef, type ComponentProps, type MouseEvent, type ReactNode } from 'react';
import { cx, variants } from '../lib/cx';
import { mergeRefs } from '../lib/refs';
import { Spinner } from './spinner';
import type { PreviewState } from './types';

export const buttonStyles = variants({
  base: [
    'group/button relative inline-flex shrink-0 select-none items-center justify-center whitespace-nowrap',
    'rounded-(--button-radius) border font-semibold leading-none no-underline',
    'transition duration-(--button-duration) ease-(--button-easing)',
    'outline-none focus-visible:focus-ring active:translate-y-px',
    'disabled:cursor-not-allowed disabled:border-transparent disabled:bg-sunken disabled:text-subtle disabled:translate-y-0',
    'aria-busy:cursor-progress pointer-coarse:after:absolute',
  ],
  variants: {
    variant: {
      primary:
        'border-transparent bg-(--button-primary-bg) text-(--button-primary-fg) hover:bg-(--button-primary-bg-hover) active:bg-(--button-primary-bg-active)',
      secondary:
        'border-(--button-secondary-border) bg-(--button-secondary-bg) text-(--button-secondary-fg) hover:bg-(--button-secondary-bg-hover) active:bg-accent-subtle active:text-accent',
      ghost:
        'border-transparent bg-transparent text-(--button-ghost-fg) hover:bg-(--button-ghost-bg-hover) active:bg-(--button-ghost-bg-hover) active:text-(--color-accent-active)',
      danger:
        'border-(--button-danger-border) bg-(--button-danger-bg) text-(--button-danger-fg) hover:border-(--button-danger-fg) active:border-(--button-danger-fg) active:bg-surface',
    },
    size: {
      sm: 'h-8 gap-1 text-sm',
      md: 'h-10 gap-2 text-(length:--button-font-size)',
      lg: 'h-12 gap-2 text-md',
    },
    iconOnly: { true: 'px-0', false: '' },
    fullWidth: { true: 'w-full', false: '' },
  },
  // Padding and the coarse-pointer hit area (44px) depend on both size and shape, so they live here
  // instead of in `size`; no two classes in one result ever set the same property.
  compoundVariants: [
    { iconOnly: false, size: 'sm', class: 'px-3 pointer-coarse:after:inset-x-0 pointer-coarse:after:-inset-y-1.5' },
    { iconOnly: false, size: 'md', class: 'px-4 pointer-coarse:after:inset-x-0 pointer-coarse:after:-inset-y-0.5' },
    { iconOnly: false, size: 'lg', class: 'px-5' },
    { iconOnly: true, size: 'sm', class: 'w-8 pointer-coarse:after:-inset-1.5' },
    { iconOnly: true, size: 'md', class: 'w-10 pointer-coarse:after:-inset-0.5' },
    { iconOnly: true, size: 'lg', class: 'w-12' },
  ],
  defaultVariants: { variant: 'primary', size: 'md', iconOnly: false, fullWidth: false },
});

export type ButtonVariant = 'primary' | 'secondary' | 'ghost' | 'danger';
export type ButtonSize = 'sm' | 'md' | 'lg';

const iconSlotClass: Record<ButtonSize, string> = {
  sm: '[&>svg]:size-(--size-icon-sm)',
  md: '[&>svg]:size-(--size-icon-md)',
  lg: '[&>svg]:size-(--size-icon-lg)',
};
const spinnerSize = { sm: 'sm', md: 'md', lg: 'lg' } as const;

interface ButtonOwnProps {
  /** Visual emphasis. One primary per region; danger only on the final destructive confirm. */
  variant?: ButtonVariant;
  /** sm 32px, md 40px (default), lg 48px. Coarse pointers get a 44px hit area on sm and md. */
  size?: ButtonSize;
  /** Busy: shows a spinner, sets aria-busy and aria-disabled, ignores clicks, keeps width and focus. */
  loading?: boolean;
  /** Label while loading, e.g. "Saving…". Defaults to the normal label. */
  loadingLabel?: ReactNode;
  /** Decorative icon before the label (mirrors with the text direction). */
  startIcon?: ReactNode;
  /** Decorative icon after the label. */
  endIcon?: ReactNode;
  fullWidth?: boolean;
  /** Render the single child element (for example a router link) with button styles. */
  asChild?: boolean;
  /** Documentation only: render hover, focus or pressed styling without interaction. */
  'data-preview-state'?: PreviewState;
}

type NativeButtonProps = Omit<ComponentProps<'button'>, 'aria-label'>;

/** Icon-only buttons must have an accessible name; the type makes `aria-label` required. */
export type ButtonProps = NativeButtonProps &
  ButtonOwnProps &
  ({ iconOnly?: false; 'aria-label'?: string } | { iconOnly: true; 'aria-label': string });

export function Button(props: ButtonProps) {
  const {
    variant = 'primary',
    size = 'md',
    loading = false,
    loadingLabel,
    startIcon,
    endIcon,
    fullWidth = false,
    asChild = false,
    iconOnly = false,
    className,
    children,
    onClick,
    type,
    disabled,
    style,
    ref,
    ...rest
  } = props;

  const ownRef = useRef<HTMLButtonElement | null>(null);
  const restWidth = useRef<number | undefined>(undefined);
  // Remember the resting width so the busy state cannot shrink the button (BTN-S4: stable width).
  useLayoutEffect(() => {
    if (!loading && ownRef.current) restWidth.current = ownRef.current.getBoundingClientRect().width;
  });

  if (import.meta.env?.DEV && iconOnly && !props['aria-label']) {
    console.error('Button: iconOnly buttons need an aria-label.');
  }

  const classes = buttonStyles({ variant, size, iconOnly, fullWidth, className });

  if (asChild) {
    return (
      <Slot className={classes} ref={ref as never} {...(rest as object)}>
        {startIcon ? <span className={cx('inline-flex', iconSlotClass[size])} aria-hidden="true">{startIcon}</span> : null}
        <Slottable>{children}</Slottable>
        {endIcon ? <span className={cx('inline-flex', iconSlotClass[size])} aria-hidden="true">{endIcon}</span> : null}
      </Slot>
    );
  }

  const busy = loading && !disabled;
  const handleClick = (event: MouseEvent<HTMLButtonElement>) => {
    if (busy) {
      event.preventDefault();
      return;
    }
    onClick?.(event);
  };

  const leading = busy ? <Spinner size={spinnerSize[size]} /> : startIcon;
  const label = busy && loadingLabel ? loadingLabel : children;

  return (
    <button
      ref={mergeRefs(ref, ownRef)}
      type={type ?? 'button'}
      disabled={disabled}
      aria-disabled={busy || undefined}
      aria-busy={busy || undefined}
      data-slot="button"
      data-variant={variant}
      data-size={size}
      onClick={handleClick}
      className={classes}
      style={busy && restWidth.current ? { ...style, minInlineSize: `${restWidth.current}px` } : style}
      {...rest}
    >
      {iconOnly ? (
        <span className={cx('inline-flex', iconSlotClass[size])} aria-hidden="true">
          {busy ? <Spinner size={spinnerSize[size]} /> : children}
        </span>
      ) : (
        <>
          {leading ? (
            <span className={cx('inline-flex', iconSlotClass[size])} aria-hidden="true">
              {leading}
            </span>
          ) : null}
          <span>{label}</span>
          {endIcon && !busy ? (
            <span className={cx('inline-flex', iconSlotClass[size])} aria-hidden="true">
              {endIcon}
            </span>
          ) : null}
        </>
      )}
    </button>
  );
}

/**
 * Neutral icon-only control for closing and dismissing surfaces (dialogs, toasts, alerts).
 * Ghost buttons use the accent color; dismiss controls should not compete with the surface's own actions.
 */
export const closeButtonClass = cx(
  'relative inline-grid size-8 shrink-0 place-items-center rounded-(--button-radius) text-muted outline-none',
  'transition-colors duration-fast ease-standard hover:bg-sunken hover:text-default active:bg-(--color-border-subtle)',
  'focus-visible:focus-ring pointer-coarse:after:absolute pointer-coarse:after:-inset-1.5',
);
