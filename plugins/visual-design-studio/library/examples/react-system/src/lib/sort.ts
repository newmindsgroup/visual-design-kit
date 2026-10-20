// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Table sorting used by DataTable. Plain TypeScript so node:test can import it.

export type SortDirection = 'ascending' | 'descending';
export interface SortDescriptor {
  column: string;
  direction: SortDirection;
}
export type SortValue = string | number | Date | null | undefined;

const collator = new Intl.Collator(undefined, { numeric: true, sensitivity: 'base' });

function isMissing(value: SortValue): value is null | undefined {
  return value === null || value === undefined || (typeof value === 'number' && Number.isNaN(value));
}

/** Compares two values: numbers and dates numerically, strings with a locale collator. Missing values are not handled here. */
export function compareValues(a: Exclude<SortValue, null | undefined>, b: Exclude<SortValue, null | undefined>): number {
  const x = a instanceof Date ? a.getTime() : a;
  const y = b instanceof Date ? b.getTime() : b;
  if (typeof x === 'number' && typeof y === 'number') return x - y;
  return collator.compare(String(x), String(y));
}

/**
 * Returns a new sorted array. Missing values (null, undefined, NaN) sort last in both directions,
 * ties break by row id ascending so the order is stable and deterministic.
 */
export function sortRows<Row>(
  rows: readonly Row[],
  getValue: (row: Row) => SortValue,
  direction: SortDirection,
  getId: (row: Row) => string,
): Row[] {
  const sign = direction === 'ascending' ? 1 : -1;
  return [...rows].sort((ra, rb) => {
    const a = getValue(ra);
    const b = getValue(rb);
    const aMissing = isMissing(a);
    const bMissing = isMissing(b);
    if (aMissing && !bMissing) return 1;
    if (!aMissing && bMissing) return -1;
    if (!aMissing && !bMissing) {
      const diff = compareValues(a, b);
      if (diff !== 0) return diff * sign;
    }
    return collator.compare(getId(ra), getId(rb));
  });
}

/** Header activation: a new column starts ascending (or `firstDirection`), the same column toggles. */
export function nextSort(current: SortDescriptor | null | undefined, column: string, firstDirection: SortDirection = 'ascending'): SortDescriptor {
  if (current && current.column === column) {
    return { column, direction: current.direction === 'ascending' ? 'descending' : 'ascending' };
  }
  return { column, direction: firstDirection };
}

/** Header checkbox state for a selection over the visible row ids. */
export function selectionState(visibleIds: readonly string[], selected: ReadonlySet<string>): boolean | 'indeterminate' {
  if (visibleIds.length === 0) return false;
  let count = 0;
  for (const id of visibleIds) if (selected.has(id)) count += 1;
  if (count === 0) return false;
  return count === visibleIds.length ? true : 'indeterminate';
}
