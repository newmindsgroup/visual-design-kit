// Version-Timestamp: 2026-10-20 02:52:00 UTC
import type { ReactNode } from 'react';
import { Badge } from '../components/badge';
import type { DataTableColumn } from '../components/data-table';
import { IconCheckCircle, IconDanger, IconInfo, IconMinus } from '../components/icons';
import type { Tone } from '../components/types';
import { formatCurrency, formatDate, statusLabel, type Invoice, type InvoiceStatus } from './data';

const statusTone: Record<InvoiceStatus, Tone> = { paid: 'success', open: 'info', failed: 'danger', refunded: 'neutral' };
const statusIcon: Record<InvoiceStatus, ReactNode> = {
  paid: <IconCheckCircle />,
  open: <IconInfo />,
  failed: <IconDanger />,
  refunded: <IconMinus />,
};
const statusOrder: Record<InvoiceStatus, number> = { failed: 0, open: 1, paid: 2, refunded: 3 };

export function InvoiceStatusBadge({ status }: { status: InvoiceStatus }) {
  return (
    <Badge tone={statusTone[status]} icon={statusIcon[status]}>
      {statusLabel[status]}
    </Badge>
  );
}

export const invoiceColumns: Array<DataTableColumn<Invoice>> = [
  {
    id: 'id',
    header: 'Invoice',
    rowHeader: true,
    cell: (row) => <span className="font-mono text-xs">{row.id}</span>,
    sortValue: (row) => row.id,
  },
  {
    id: 'date',
    header: 'Date',
    cell: (row) => <span className="whitespace-nowrap">{formatDate(row.date)}</span>,
    sortValue: (row) => row.date,
    firstSortDirection: 'descending',
  },
  {
    id: 'description',
    header: 'Description',
    cell: (row) => <span className="block min-w-48 text-muted">{row.description}</span>,
  },
  {
    id: 'status',
    header: 'Status',
    cell: (row) => <InvoiceStatusBadge status={row.status} />,
    sortValue: (row) => statusOrder[row.status],
  },
  {
    id: 'amount',
    header: 'Amount',
    numeric: true,
    cell: (row) => (row.amount === null ? <span className="text-muted">Pending</span> : formatCurrency(row.amount)),
    sortValue: (row) => row.amount,
    firstSortDirection: 'descending',
  },
];
