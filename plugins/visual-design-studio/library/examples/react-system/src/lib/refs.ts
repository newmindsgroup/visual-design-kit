// Version-Timestamp: 2026-10-20 02:52:00 UTC
import type { Ref, RefCallback } from 'react';

/** Combines refs so a component can keep its own ref and forward the consumer's (React 19 `ref` prop). */
export function mergeRefs<T>(...refs: Array<Ref<T> | undefined>): RefCallback<T> {
  return (value) => {
    const cleanups: Array<() => void> = [];
    for (const ref of refs) {
      if (typeof ref === 'function') {
        const cleanup = ref(value);
        if (typeof cleanup === 'function') cleanups.push(cleanup);
      } else if (ref) {
        (ref as { current: T | null }).current = value;
      }
    }
    return () => {
      for (const cleanup of cleanups) cleanup();
      for (const ref of refs) if (ref && typeof ref !== 'function') (ref as { current: T | null }).current = null;
    };
  };
}
