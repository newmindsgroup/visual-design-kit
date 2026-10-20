// Version-Timestamp: 2026-10-20 02:52:00 UTC
// DataTable: compare rows and columns. Spec: component-specs/data-table.md (TBL-S1 to TBL-S8).
// Native table semantics (caption, th scope, aria-sort on the sorted header, buttons inside sortable headers),
// no role=grid. Text aligns to the start, numbers to the end with tabular figures.
import { useId, useMemo, useRef, useState, type ReactNode } from 'react';
import { cx } from '../lib/cx';
import { nextSort, selectionState, sortRows, type SortDescriptor, type SortDirection, type SortValue } from '../lib/sort';
import { useControllable } from '../lib/use-controllable';
import { useOverflow } from '../lib/use-overflow';
import { Checkbox } from './checkbox';
import { EmptyState } from './empty-state';
import { IconArrowDown, IconArrowUp, IconInbox, IconSort } from './icons';
import { Skeleton } from './skeleton';

export type { SortDescriptor, SortDirection } from '../lib/sort';

export interface DataTableColumn<Row> {
  id: string;
  header: ReactNode;
  /** Plain-text column name for announcements when `header` is not a string. */
  headerLabel?: string;
  cell: (row: Row) => ReactNode;
  /** Makes the column sortable. Return null for missing values (always sorted last). */
  sortValue?: (row: Row) => SortValue;
  /** Direction on first activation. Dates and amounts often start descending. */
  firstSortDirection?: SortDirection;
  /** End-aligned with tabular figures. */
  numeric?: boolean;
  /** Render cells as row headers (th scope=row), usually the identifying column. */
  rowHeader?: boolean;
  className?: string;
}

export type Density = 'compact' | 'default' | 'comfortable';

export interface DataTableProps<Row> {
  /** Names the table (caption). Required; hide it visually with captionVisible={false} when a heading already says it. */
  caption: ReactNode;
  captionVisible?: boolean;
  columns: ReadonlyArray<DataTableColumn<Row>>;
  rows: readonly Row[];
  getRowId: (row: Row) => string;
  /** Used in row checkbox names: "Select INV-2041". Defaults to the row id. */
  getRowLabel?: (row: Row) => string;
  sort?: SortDescriptor | null;
  defaultSort?: SortDescriptor | null;
  onSortChange?: (sort: SortDescriptor) => void;
  selectionMode?: 'none' | 'multiple';
  selectedKeys?: ReadonlySet<string>;
  defaultSelectedKeys?: Iterable<string>;
  onSelectionChange?: (keys: Set<string>) => void;
  loading?: boolean;
  loadingRowCount?: number;
  /** Announced while loading, e.g. "Loading invoices". */
  loadingLabel?: string;
  /** Shown in place of rows when there are none (and not loading). */
  emptyState?: ReactNode;
  density?: Density;
  striped?: boolean;
  className?: string;
}

const cellPaddingClass: Record<Density, string> = {
  compact: 'h-8 py-1',
  default: 'h-10 py-2',
  comfortable: 'h-12 py-3',
};

const EMPTY = new Set<string>();

export function DataTable<Row>({
  caption,
  captionVisible = true,
  columns,
  rows,
  getRowId,
  getRowLabel,
  sort: sortProp,
  defaultSort = null,
  onSortChange,
  selectionMode = 'none',
  selectedKeys,
  defaultSelectedKeys,
  onSelectionChange,
  loading = false,
  loadingRowCount = 5,
  loadingLabel = 'Loading',
  emptyState,
  density = 'default',
  striped = false,
  className,
}: DataTableProps<Row>) {
  const captionId = `table${useId().replace(/[^a-zA-Z0-9_-]/g, '')}-caption`;
  const scrollRef = useRef<HTMLDivElement | null>(null);
  const overflowing = useOverflow(scrollRef, 'x');
  const [announcement, setAnnouncement] = useState('');

  const [sort, setSort] = useControllable<SortDescriptor | null>(sortProp, defaultSort, (next) => {
    if (next) onSortChange?.(next);
  });
  const [selected, setSelected] = useControllable<ReadonlySet<string>>(
    selectedKeys,
    defaultSelectedKeys ? new Set(defaultSelectedKeys) : EMPTY,
    (next) => onSelectionChange?.(new Set(next)),
  );

  const sortedRows = useMemo(() => {
    const column = sort ? columns.find((c) => c.id === sort.column) : undefined;
    if (!sort || !column?.sortValue) return rows;
    return sortRows(rows, column.sortValue, sort.direction, getRowId);
  }, [rows, columns, sort, getRowId]);

  const visibleIds = useMemo(() => sortedRows.map(getRowId), [sortedRows, getRowId]);
  const selectable = selectionMode === 'multiple';
  const headerState = selectionState(visibleIds, selected);
  const columnCount = columns.length + (selectable ? 1 : 0);
  const pad = cellPaddingClass[density];

  const activateSort = (column: DataTableColumn<Row>) => {
    const next = nextSort(sort, column.id, column.firstSortDirection);
    setSort(next);
    const name = column.headerLabel ?? (typeof column.header === 'string' ? column.header : column.id);
    setAnnouncement(`Sorted by ${name}, ${next.direction}`);
  };

  const toggleRow = (id: string, checked: boolean) => {
    const next = new Set(selected);
    if (checked) next.add(id);
    else next.delete(id);
    setSelected(next);
  };

  const toggleAll = (checked: boolean) => {
    const next = new Set(selected);
    for (const id of visibleIds) {
      if (checked) next.add(id);
      else next.delete(id);
    }
    setSelected(next);
  };

  return (
    <div
      data-slot="data-table"
      data-density={density}
      className={cx('min-w-0 overflow-hidden rounded-lg border border-(--table-border) bg-(--table-row-bg)', className)}
    >
      <p role="status" className="sr-only">
        {loading ? loadingLabel : announcement}
      </p>
      <div
        ref={scrollRef}
        role={overflowing ? 'region' : undefined}
        aria-labelledby={overflowing ? captionId : undefined}
        tabIndex={overflowing ? 0 : undefined}
        className="overflow-x-auto outline-none focus-visible:focus-ring-inset"
      >
        <table className="w-full border-collapse text-(length:--table-font-size) leading-normal" aria-busy={loading || undefined}>
          <caption
            id={captionId}
            className={cx(
              captionVisible
                ? 'border-b border-(--table-border) px-(--table-cell-padding-x) py-3 text-start font-display text-md font-semibold text-default'
                : 'sr-only',
            )}
          >
            {caption}
          </caption>
          <thead>
            <tr>
              {selectable ? (
                <th scope="col" className="w-px border-b border-(--table-border) bg-(--table-header-bg) ps-3 pe-0">
                  <Checkbox
                    aria-label="Select all rows"
                    checked={headerState}
                    disabled={loading || visibleIds.length === 0}
                    onCheckedChange={(value) => toggleAll(value === true)}
                  />
                </th>
              ) : null}
              {columns.map((column) => {
                const active = sort?.column === column.id;
                const ariaSort = active ? sort.direction : undefined;
                return (
                  <th
                    key={column.id}
                    scope="col"
                    aria-sort={ariaSort}
                    className={cx(
                      'h-10 whitespace-nowrap border-b border-(--table-border) bg-(--table-header-bg) px-(--table-cell-padding-x)',
                      'text-xs font-semibold uppercase tracking-caps text-(--table-header-fg)',
                      column.numeric ? 'text-end' : 'text-start',
                    )}
                  >
                    {column.sortValue ? (
                      <button
                        type="button"
                        onClick={() => activateSort(column)}
                        disabled={loading}
                        className={cx(
                          'relative -mx-2 inline-flex h-8 cursor-pointer items-center gap-1 rounded-sm px-2 uppercase tracking-caps outline-none',
                          'transition-colors duration-fast hover:bg-(--table-row-bg-hover) hover:text-default focus-visible:focus-ring',
                          'disabled:cursor-not-allowed',
                          active && 'text-default',
                          column.numeric && 'flex-row-reverse',
                        )}
                      >
                        <span>{column.header}</span>
                        {active ? (
                          sort.direction === 'ascending' ? (
                            <IconArrowUp size="sm" className="text-accent" />
                          ) : (
                            <IconArrowDown size="sm" className="text-accent" />
                          )
                        ) : (
                          <IconSort size="sm" className="text-subtle" />
                        )}
                      </button>
                    ) : (
                      column.header
                    )}
                  </th>
                );
              })}
            </tr>
          </thead>
          <tbody>
            {loading ? (
              Array.from({ length: loadingRowCount }, (_, i) => (
                <tr key={`loading-${i}`} className="border-b border-(--table-border) last:border-b-0">
                  {selectable ? (
                    <td className={cx('w-px ps-3 pe-0', pad)}>
                      <Skeleton className="size-5" />
                    </td>
                  ) : null}
                  {columns.map((column, c) => (
                    <td key={column.id} className={cx('px-(--table-cell-padding-x)', pad)}>
                      <Skeleton
                        shape="text"
                        className={cx(column.numeric ? 'ms-auto w-16' : c === 0 ? 'w-28' : 'w-full max-w-40')}
                      />
                    </td>
                  ))}
                </tr>
              ))
            ) : sortedRows.length === 0 ? (
              <tr>
                <td colSpan={columnCount} className="p-0">
                  {emptyState ?? <EmptyState size="sm" icon={<IconInbox />} title="Nothing to show" />}
                </td>
              </tr>
            ) : (
              sortedRows.map((row) => {
                const id = getRowId(row);
                const isSelected = selected.has(id);
                return (
                  <tr
                    key={id}
                    data-slot="table-row"
                    data-selected={isSelected || undefined}
                    className={cx(
                      'border-b border-(--table-border) text-(--table-row-fg) transition-colors duration-fast last:border-b-0',
                      striped && 'even:bg-(--table-row-bg-alt)',
                      'hover:bg-(--table-row-bg-hover) data-selected:bg-(--table-row-bg-selected)',
                    )}
                  >
                    {selectable ? (
                      <td className={cx('w-px ps-3 pe-0', pad)}>
                        <Checkbox
                          aria-label={`Select ${getRowLabel ? getRowLabel(row) : id}`}
                          checked={isSelected}
                          onCheckedChange={(value) => toggleRow(id, value === true)}
                        />
                      </td>
                    ) : null}
                    {columns.map((column) => {
                      const Cell = column.rowHeader ? 'th' : 'td';
                      return (
                        <Cell
                          key={column.id}
                          scope={column.rowHeader ? 'row' : undefined}
                          className={cx(
                            'px-(--table-cell-padding-x) align-middle',
                            pad,
                            column.numeric ? 'whitespace-nowrap text-end tabular-nums' : 'text-start',
                            column.rowHeader && 'font-medium',
                            column.className,
                          )}
                        >
                          {column.cell(row)}
                        </Cell>
                      );
                    })}
                  </tr>
                );
              })
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
