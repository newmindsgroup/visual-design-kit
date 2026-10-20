// Version-Timestamp: 2026-10-20 02:52:00 UTC
import { useCallback, useRef, useState } from 'react';

/**
 * The value/defaultValue/onValueChange trio used by every stateful component. Controlled when `value` is
 * not undefined; warns in development if a component switches between controlled and uncontrolled.
 */
export function useControllable<T>(value: T | undefined, defaultValue: T, onChange?: (next: T) => void): [T, (next: T) => void] {
  const [internal, setInternal] = useState<T>(defaultValue);
  const controlled = value !== undefined;
  const wasControlled = useRef(controlled);
  if (import.meta.env?.DEV && wasControlled.current !== controlled) {
    console.warn('useControllable: a component switched between controlled and uncontrolled. Pick one for its lifetime.');
    wasControlled.current = controlled;
  }
  const current = controlled ? value : internal;
  const set = useCallback(
    (next: T) => {
      if (!controlled) setInternal(next);
      onChange?.(next);
    },
    [controlled, onChange],
  );
  return [current, set];
}
