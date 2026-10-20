// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Fictional sample data for the specimen and the billing screen. "Harbor Studio" is an invented workspace.

export type InvoiceStatus = 'paid' | 'open' | 'failed' | 'refunded';

export interface Invoice {
  id: string;
  /** ISO date */
  date: string;
  description: string;
  status: InvoiceStatus;
  /** In US dollars; null when the amount is still being calculated. */
  amount: number | null;
}

export const invoices: Invoice[] = [
  { id: 'INV-2048', date: '2026-10-01', description: 'Team plan, annual renewal (18 seats)', status: 'open', amount: 4320 },
  { id: 'INV-2031', date: '2026-09-14', description: 'Seat change: +3 seats, prorated', status: 'paid', amount: 412.5 },
  { id: 'INV-2017', date: '2026-08-02', description: 'Storage add-on, 100 GB', status: 'failed', amount: 48 },
  { id: 'INV-2009', date: '2026-07-19', description: 'Seat change: −1 seat, credit', status: 'refunded', amount: 137.5 },
  { id: 'INV-1994', date: '2026-06-30', description: 'Priority support, quarterly', status: 'paid', amount: 1200 },
  { id: 'INV-1982', date: '2026-06-03', description: 'Usage overage: API requests (1.2 M)', status: 'paid', amount: 86.4 },
  { id: 'INV-1970', date: '2026-05-11', description: 'Storage add-on, 100 GB', status: 'paid', amount: 48 },
  { id: 'INV-1953', date: '2026-04-01', description: 'Usage estimate for April (pending)', status: 'open', amount: null },
];

const currency = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' });
const dateFormat = new Intl.DateTimeFormat('en-US', { year: 'numeric', month: 'short', day: 'numeric', timeZone: 'UTC' });

export const formatCurrency = (value: number) => currency.format(value);
export const formatDate = (iso: string) => dateFormat.format(new Date(`${iso}T00:00:00Z`));

export const statusLabel: Record<InvoiceStatus, string> = {
  paid: 'Paid',
  open: 'Open',
  failed: 'Failed',
  refunded: 'Refunded',
};

export const countries = [
  { value: 'au', label: 'Australia' },
  { value: 'ca', label: 'Canada' },
  { value: 'de', label: 'Germany' },
  { value: 'ie', label: 'Ireland' },
  { value: 'jp', label: 'Japan' },
  { value: 'nl', label: 'Netherlands' },
  { value: 'nz', label: 'New Zealand' },
  { value: 'sg', label: 'Singapore' },
  { value: 'ae', label: 'United Arab Emirates' },
  { value: 'gb', label: 'United Kingdom' },
  { value: 'us', label: 'United States' },
];

export interface Plan {
  id: 'starter' | 'team' | 'business';
  name: string;
  /** Per seat per month, billed annually */
  annual: number;
  monthly: number;
  summary: string;
}

export const plans: Plan[] = [
  { id: 'starter', name: 'Starter', annual: 12, monthly: 15, summary: 'Up to 10 seats, 50 GB storage, community support.' },
  { id: 'team', name: 'Team', annual: 20, monthly: 24, summary: 'Up to 50 seats, 250 GB storage, SSO, audit log.' },
  { id: 'business', name: 'Business', annual: 32, monthly: 38, summary: 'Unlimited seats, 1 TB storage, SCIM, priority support.' },
];
