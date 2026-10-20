// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Composed screen: billing settings for an invented workspace, built only from src/components.
import { useEffect, useMemo, useRef, useState } from 'react';
import { Banner } from '../components/alert';
import { Badge } from '../components/badge';
import { Button } from '../components/button';
import { Card, CardDescription, CardEyebrow, CardFooter, CardHeader, CardTitle } from '../components/card';
import { DataTable, type DataTableColumn } from '../components/data-table';
import { EmptyState } from '../components/empty-state';
import {
  IconBell,
  IconCard,
  IconDownload,
  IconArrowRight,
  IconFolder,
  IconReceipt,
  IconSearch,
  IconSettings,
  IconUsers,
  IconX,
} from '../components/icons';
import { Select, SelectItem } from '../components/select';
import { Skeleton } from '../components/skeleton';
import { Switch } from '../components/switch';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../components/tabs';
import { TextField } from '../components/text-field';
import { useToast } from '../components/toast';
import { Tooltip } from '../components/tooltip';
import { cx } from '../lib/cx';
import { formatAmount, formatCurrency, invoices, plans, type Invoice, type InvoiceStatus, type Plan } from '../shared/data';
import { invoiceColumns } from '../shared/invoice-columns';
import { AppProviders, SiteFooter, SiteHeader, SkipLink } from '../shared/shell';
import { CancelDialog, ChangePlanDialog } from './dialogs';
import { PaymentDetails } from './payment-details';

const settingsNav = [
  { id: 'general', label: 'General', icon: <IconSettings /> },
  { id: 'members', label: 'Members', icon: <IconUsers /> },
  { id: 'billing', label: 'Billing', icon: <IconReceipt /> },
  { id: 'projects', label: 'Projects', icon: <IconFolder /> },
  { id: 'notifications', label: 'Notifications', icon: <IconBell /> },
];

const SEATS_USED = 18;
const SEAT_LIMIT = 25;

function SettingsNav() {
  return (
    <nav aria-label="Workspace settings" className="min-w-0 lg:w-56 lg:shrink-0">
      <p className="hidden px-3 text-xs font-semibold uppercase tracking-caps text-muted lg:block">Harbor Studio</p>
      <ul className="-mx-1 flex gap-1 overflow-x-auto px-1 pb-1 lg:mx-0 lg:mt-3 lg:grid lg:overflow-visible lg:px-0 lg:pb-0">
        {settingsNav.map((item) => (
          <li key={item.id} className="shrink-0">
            <a
              href={item.id === 'billing' ? './billing.html' : '#main'}
              aria-current={item.id === 'billing' ? 'page' : undefined}
              className={cx(
                'relative flex h-10 items-center gap-3 whitespace-nowrap rounded-md px-3 text-sm font-medium no-underline transition-colors duration-fast [&>svg]:size-(--size-icon-md)',
                item.id === 'billing'
                  ? 'bg-sunken text-default before:absolute before:inset-y-2 before:start-0 before:w-0.5 before:rounded-full before:bg-accent [&>svg]:text-accent'
                  : 'text-muted hover:bg-sunken hover:text-default',
              )}
            >
              {item.icon}
              {item.label}
            </a>
          </li>
        ))}
      </ul>
    </nav>
  );
}

function SeatMeter({ used, limit }: { used: number; limit: number }) {
  const pct = Math.round((used / limit) * 100);
  return (
    <div className="grid gap-2">
      <div className="flex items-baseline justify-between gap-3 text-sm">
        <span className="font-medium text-default">Seats</span>
        <span className="text-muted">
          <bdi className="tabular-nums">{used}</bdi> of <bdi className="tabular-nums">{limit}</bdi> used
        </span>
      </div>
      <div className="h-2 overflow-hidden rounded-full bg-sunken ring-1 ring-(--color-border-subtle) ring-inset" aria-hidden="true">
        <div className="h-full rounded-full bg-accent" style={{ inlineSize: `${pct}%` }} />
      </div>
    </div>
  );
}

function PlanCard({
  plan,
  cycle,
  cancelled,
  onChangePlan,
  onCancel,
  onResume,
}: {
  plan: Plan;
  cycle: 'monthly' | 'annual';
  cancelled: boolean;
  onChangePlan: () => void;
  onCancel: () => void;
  onResume: () => void;
}) {
  const perSeat = cycle === 'annual' ? plan.annual : plan.monthly;
  const total = cycle === 'annual' ? perSeat * SEATS_USED * 12 : perSeat * SEATS_USED;
  return (
    <Card asChild variant="elevated" className="lg:col-span-2">
      <section aria-labelledby="plan-title">
      <CardHeader>
        <div className="grid gap-1">
          <CardEyebrow>Current plan</CardEyebrow>
          <CardTitle asChild size="lg">
            <h2 id="plan-title">
              {plan.name} · {cycle === 'annual' ? 'Annual' : 'Monthly'}
            </h2>
          </CardTitle>
        </div>
        {cancelled ? <Badge tone="warning">Ends 14 Mar 2027</Badge> : <Badge tone="success">Renews 14 Mar 2027</Badge>}
      </CardHeader>
      <div className="flex flex-wrap items-end gap-x-3 gap-y-1">
        <p className="font-display text-4xl font-semibold tracking-tight text-default">{formatAmount(total)}</p>
        <p className="pb-1 text-sm text-muted">
          per {cycle === 'annual' ? 'year' : 'month'} · {SEATS_USED} seats × {formatCurrency(perSeat)} per seat per month
        </p>
      </div>
      <SeatMeter used={SEATS_USED} limit={SEAT_LIMIT} />
      <CardFooter className="border-t border-subtle pt-4">
        <Button onClick={onChangePlan}>Change plan</Button>
        <Button variant="secondary">Add seats</Button>
        {cancelled ? (
          <Button variant="ghost" className="sm:ms-auto" onClick={onResume}>
            Resume subscription
          </Button>
        ) : (
          <Button variant="ghost" className="sm:ms-auto" onClick={onCancel}>
            Cancel subscription
          </Button>
        )}
      </CardFooter>
      </section>
    </Card>
  );
}

function UsageCard() {
  const [loaded, setLoaded] = useState(false);
  useEffect(() => {
    const t = window.setTimeout(() => setLoaded(true), 900);
    return () => window.clearTimeout(t);
  }, []);
  const rows = [
    { label: 'Storage', value: '61.4 GB', detail: 'of 250 GB' },
    { label: 'API requests', value: '1.28 M', detail: 'this cycle' },
    { label: 'Active projects', value: '42', detail: 'no limit' },
  ];
  return (
    <Card asChild>
      <section aria-labelledby="usage-title" aria-busy={!loaded || undefined}>
      <CardHeader>
        <div className="grid gap-1">
          <CardEyebrow>Usage</CardEyebrow>
          <CardTitle asChild>
            <h2 id="usage-title">Since 14 Sep</h2>
          </CardTitle>
        </div>
      </CardHeader>
      <p role="status" className="sr-only">
        {loaded ? 'Usage loaded' : 'Loading usage'}
      </p>
      <dl className="grid gap-3">
        {rows.map((row) => (
          <div key={row.label} className="flex items-baseline justify-between gap-3 border-b border-subtle pb-3 last:border-b-0 last:pb-0">
            <dt className="text-sm text-muted">{row.label}</dt>
            <dd className="text-end">
              {loaded ? (
                <>
                  {/* bdi keeps "61.4 GB" in one direction run when the page is right to left */}
                  <bdi className="font-semibold tabular-nums text-default">{row.value}</bdi>{' '}
                  <span className="text-sm text-muted">{row.detail}</span>
                </>
              ) : (
                <Skeleton shape="text" className="ms-auto w-24" />
              )}
            </dd>
          </div>
        ))}
      </dl>
      <CardDescription>Usage resets on each renewal date. Overage is billed at the end of the cycle.</CardDescription>
      </section>
    </Card>
  );
}

type StatusFilter = 'all' | InvoiceStatus;

function InvoicesPanel() {
  const { toast } = useToast();
  const [query, setQuery] = useState('');
  const [status, setStatus] = useState<StatusFilter>('all');
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [downloading, setDownloading] = useState(false);

  const rows = useMemo(() => {
    const q = query.trim().toLowerCase();
    return invoices.filter(
      (inv) =>
        (status === 'all' || inv.status === status) &&
        (!q || inv.id.toLowerCase().includes(q) || inv.description.toLowerCase().includes(q)),
    );
  }, [query, status]);

  const columns = useMemo<Array<DataTableColumn<Invoice>>>(
    () => [
      ...invoiceColumns,
      {
        id: 'actions',
        header: <span className="sr-only">Actions</span>,
        headerLabel: 'Actions',
        cell: (row) => (
          <Tooltip content={`Download ${row.id}`} mode="label">
            <Button
              iconOnly
              size="sm"
              variant="ghost"
              aria-label={`Download ${row.id}`}
              onClick={() => toast({ tone: 'success', title: `${row.id}.pdf downloaded` })}
            >
              <IconDownload />
            </Button>
          </Tooltip>
        ),
        className: 'w-px',
      },
    ],
    [toast],
  );

  const filtered = query.trim() !== '' || status !== 'all';

  return (
    <div className="grid gap-4">
      <div className="flex flex-wrap items-end gap-3">
        <TextField
          className="min-w-0 flex-1 basis-56"
          label="Search invoices"
          labelVisible={false}
          type="search"
          placeholder="Search by number or description"
          startAdornment={<IconSearch />}
          value={query}
          onValueChange={setQuery}
        />
        <Select
          className="w-44"
          label="Status"
          labelVisible={false}
          value={status}
          onValueChange={(v) => setStatus(v as StatusFilter)}
        >
          <SelectItem value="all">All statuses</SelectItem>
          <SelectItem value="paid">Paid</SelectItem>
          <SelectItem value="open">Open</SelectItem>
          <SelectItem value="failed">Failed</SelectItem>
          <SelectItem value="refunded">Refunded</SelectItem>
        </Select>
      </div>
      <div
        className={cx(
          'flex min-h-10 flex-wrap items-center gap-3 rounded-md px-3 py-1',
          selected.size > 0 ? 'bg-accent-subtle' : 'bg-transparent',
        )}
      >
        <p className="text-sm font-medium text-default" role="status">
          {selected.size > 0 ? `${selected.size} selected` : `${rows.length} of ${invoices.length} invoices`}
        </p>
        {selected.size > 0 ? (
          <div className="ms-auto flex flex-wrap gap-2">
            <Button
              size="sm"
              variant="secondary"
              startIcon={<IconDownload />}
              loading={downloading}
              loadingLabel="Preparing…"
              onClick={() => {
                setDownloading(true);
                window.setTimeout(() => {
                  setDownloading(false);
                  toast({ tone: 'success', title: `${selected.size} invoices downloaded`, description: 'Saved as one ZIP file.' });
                }, 900);
              }}
            >
              Download PDFs
            </Button>
            <Button size="sm" variant="ghost" startIcon={<IconX />} onClick={() => setSelected(new Set())}>
              Clear selection
            </Button>
          </div>
        ) : null}
      </div>
      <DataTable
        caption="Invoices"
        captionVisible={false}
        columns={columns}
        rows={rows}
        getRowId={(row) => row.id}
        defaultSort={{ column: 'date', direction: 'descending' }}
        selectionMode="multiple"
        selectedKeys={selected}
        onSelectionChange={setSelected}
        emptyState={
          <EmptyState
            size="sm"
            icon={<IconSearch />}
            title={filtered ? 'No invoices match these filters' : 'No invoices yet'}
            description={filtered ? 'Try another search, or clear the filters to see all invoices.' : 'Invoices appear after your first renewal.'}
            actions={
              filtered ? (
                <Button
                  size="sm"
                  variant="secondary"
                  onClick={() => {
                    setQuery('');
                    setStatus('all');
                  }}
                >
                  Clear filters
                </Button>
              ) : null
            }
          />
        }
      />
    </div>
  );
}

function NotificationsPanel() {
  return (
    <Card padding="none">
      <div className="divide-y divide-subtle">
        <Switch className="p-5" label="Renewal reminders" description="Email the billing contact 7 days before each renewal." defaultChecked />
        <Switch className="p-5" label="Seat limit alerts" description="Notify admins when 90% of seats are in use." defaultChecked />
        <Switch className="p-5" label="Usage overage alerts" description="Email when API requests pass the plan allowance." />
        <Switch
          className="p-5"
          label="Failed payment alerts"
          description="Always on for workspace owners. Change who is an owner in Members."
          defaultChecked
          disabled
        />
      </div>
    </Card>
  );
}

export function BillingApp() {
  const { toast } = useToast();
  const [tab, setTab] = useState('invoices');
  const [planId, setPlanId] = useState<Plan['id']>('team');
  const [cycle, setCycle] = useState<'monthly' | 'annual'>('annual');
  const [changeOpen, setChangeOpen] = useState(false);
  const [cancelOpen, setCancelOpen] = useState(false);
  const [cancelled, setCancelled] = useState(false);
  const replaceCardRef = useRef<HTMLButtonElement | null>(null);
  const plan = plans.find((p) => p.id === planId) ?? plans[1];

  return (
    <>
      <SkipLink />
      <SiteHeader current="billing" />
      {cancelled ? (
        <Banner
          tone="info"
          title="Subscription cancelled."
          live="polite"
          actions={
            <Button size="sm" variant="secondary" onClick={() => setCancelled(false)}>
              Resume subscription
            </Button>
          }
        >
          Harbor Studio moves to the Free plan on 14 March 2027. Projects over the Free limit become read-only.
        </Banner>
      ) : (
        <Banner
          tone="warning"
          title="Your card expires this month."
          actions={
            <Button
              size="sm"
              variant="secondary"
              startIcon={<IconCard />}
              onClick={() => {
                setTab('payment');
                window.setTimeout(() => replaceCardRef.current?.focus(), 0);
              }}
            >
              Update card
            </Button>
          }
        >
          The Visa ending 4242 expires on 31 October 2026, before the next charge.
        </Banner>
      )}
      <div className="mx-auto flex max-w-(--container-xl) flex-col gap-8 px-(--gutter) py-8 lg:flex-row lg:gap-12 lg:py-12">
        <SettingsNav />
        <main id="main" tabIndex={-1} className="min-w-0 flex-1 outline-none">
          <header className="flex flex-wrap items-end justify-between gap-4">
            <div>
              <p className="text-sm text-muted">Settings</p>
              <h1 className="mt-1 font-display text-3xl font-semibold tracking-tight text-default sm:text-4xl">Billing</h1>
              <p className="mt-2 max-w-(--measure-body) text-md text-muted">
                Plan, payment method and invoices for the Harbor Studio workspace. Only owners and billing admins see this page.
              </p>
            </div>
            <a
              href="./index.html#data-table"
              className="inline-flex items-center gap-1 rounded-sm text-sm font-medium text-accent underline decoration-from-font underline-offset-4 hover:decoration-2"
            >
              How this screen is built
              <IconArrowRight size="sm" />
            </a>
          </header>

          <div className="mt-8 grid gap-6 lg:grid-cols-3">
            <PlanCard
              plan={plan}
              cycle={cycle}
              cancelled={cancelled}
              onChangePlan={() => setChangeOpen(true)}
              onCancel={() => setCancelOpen(true)}
              onResume={() => setCancelled(false)}
            />
            <UsageCard />
          </div>

          <Tabs value={tab} onValueChange={setTab} className="mt-10">
            <TabsList aria-label="Billing sections">
              <TabsTrigger value="invoices" count={invoices.length}>
                Invoices
              </TabsTrigger>
              <TabsTrigger value="payment">Payment details</TabsTrigger>
              <TabsTrigger value="notifications">Notifications</TabsTrigger>
            </TabsList>
            <TabsContent value="invoices">
              <InvoicesPanel />
            </TabsContent>
            <TabsContent value="payment">
              <PaymentDetails replaceCardRef={replaceCardRef} />
            </TabsContent>
            <TabsContent value="notifications">
              <NotificationsPanel />
            </TabsContent>
          </Tabs>
        </main>
      </div>
      <SiteFooter />

      <ChangePlanDialog
        open={changeOpen}
        onOpenChange={setChangeOpen}
        currentPlan={planId}
        currentCycle={cycle}
        seats={SEATS_USED}
        onConfirm={(nextPlan, nextCycle) => {
          const previous = { planId, cycle };
          setPlanId(nextPlan);
          setCycle(nextCycle);
          const name = plans.find((p) => p.id === nextPlan)?.name ?? nextPlan;
          toast({
            tone: 'success',
            title: `Plan changed to ${name}`,
            description: 'The prorated difference is on your next invoice.',
            action: {
              label: 'Undo',
              altText: 'Change the plan back from the Change plan dialog',
              onAction: () => {
                setPlanId(previous.planId);
                setCycle(previous.cycle);
                toast({ tone: 'info', title: 'Plan change undone' });
              },
            },
          });
        }}
      />
      <CancelDialog
        open={cancelOpen}
        onOpenChange={setCancelOpen}
        planName={plan.name}
        onConfirm={() => {
          setCancelled(true);
          toast({ tone: 'neutral', title: 'Subscription cancelled', description: 'You can resume it any time before 14 March 2027.' });
        }}
      />
    </>
  );
}


export function BillingRoot() {
  return (
    <AppProviders>
      <BillingApp />
    </AppProviders>
  );
}
