// Version-Timestamp: 2026-10-20 02:52:00 UTC
import { cx } from '../lib/cx';
import type { IconSize } from './icons';

const sizeClass: Record<IconSize, string> = {
  sm: 'size-(--size-icon-sm)',
  md: 'size-(--size-icon-md)',
  lg: 'size-(--size-icon-lg)',
};

/**
 * Decorative busy indicator. Never the only signal: pair it with text or aria-busy on the busy element.
 * Reduced motion stops the rotation and leaves a static three-quarter ring.
 */
export function Spinner({ size = 'md', className }: { size?: IconSize; className?: string }) {
  return (
    <svg
      viewBox="0 0 24 24"
      fill="none"
      aria-hidden="true"
      focusable="false"
      data-slot="spinner"
      className={cx('shrink-0 animate-spinner motion-reduce:animate-none', sizeClass[size], className)}
    >
      <circle cx="12" cy="12" r="8.5" stroke="currentColor" strokeOpacity="0.25" strokeWidth="2.5" />
      <path d="M20.5 12A8.5 8.5 0 0 0 12 3.5" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" />
    </svg>
  );
}
