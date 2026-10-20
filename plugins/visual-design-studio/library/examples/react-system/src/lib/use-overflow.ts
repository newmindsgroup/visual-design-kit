// Version-Timestamp: 2026-10-20 02:52:00 UTC
import { useLayoutEffect, useState, type RefObject } from 'react';

/**
 * True when the element scrolls horizontally or vertically. Scroll regions only become keyboard focusable
 * (tabIndex 0) while they overflow, so they are reachable without adding empty tab stops (WCAG 2.1.1).
 */
export function useOverflow(ref: RefObject<HTMLElement | null>, axis: 'x' | 'y' = 'x'): boolean {
  const [overflowing, setOverflowing] = useState(false);
  useLayoutEffect(() => {
    const el = ref.current;
    if (!el) return;
    const measure = () => {
      const next = axis === 'x' ? el.scrollWidth > el.clientWidth + 1 : el.scrollHeight > el.clientHeight + 1;
      setOverflowing(next);
    };
    measure();
    const observer = new ResizeObserver(measure);
    observer.observe(el);
    for (const child of Array.from(el.children)) observer.observe(child);
    return () => observer.disconnect();
  }, [ref, axis]);
  return overflowing;
}
