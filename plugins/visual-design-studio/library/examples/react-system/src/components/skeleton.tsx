// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Skeleton: placeholder shapes for content that takes 1-10 s. Decorative (aria-hidden); the loading region
// itself carries aria-busy and a status message. Reduced motion stops the pulse.
import type { ComponentProps } from 'react';
import { cx } from '../lib/cx';

export type SkeletonProps = Omit<ComponentProps<'div'>, 'children'> & {
  /** rect: small blocks (4px radius); box: media and cards (12px); text: a line; circle: avatars. */
  shape?: 'rect' | 'box' | 'text' | 'circle';
};

export function Skeleton({ shape = 'rect', className, ...rest }: SkeletonProps) {
  return (
    <div
      aria-hidden="true"
      data-slot="skeleton"
      className={cx(
        'animate-skeleton bg-(--color-border-subtle) motion-reduce:animate-none',
        shape === 'circle' ? 'rounded-full' : shape === 'text' ? 'h-3 rounded-full' : shape === 'box' ? 'rounded-lg' : 'rounded-sm',
        className,
      )}
      {...rest}
    />
  );
}

/** Lines of text; the last line is shorter so the block reads as a paragraph. */
export function SkeletonText({ lines = 3, className }: { lines?: number; className?: string }) {
  return (
    <div aria-hidden="true" className={cx('grid gap-2', className)}>
      {Array.from({ length: lines }, (_, i) => (
        <Skeleton key={i} shape="text" className={i === lines - 1 && lines > 1 ? 'w-3/5' : 'w-full'} />
      ))}
    </div>
  );
}
