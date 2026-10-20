// Version-Timestamp: 2026-10-20 02:52:00 UTC
import { useState, type ReactElement } from 'react';
import { Alert, Banner } from '../components/alert';
import { Badge } from '../components/badge';
import { Button } from '../components/button';
import { Card, CardDescription, CardEyebrow, CardFooter, CardHeader, CardLink, CardTitle } from '../components/card';
import { DataTable, type Density } from '../components/data-table';
import { EmptyState } from '../components/empty-state';
import { IconArrowUp, IconCheckCircle, IconDanger, IconFolder, IconInfo, IconPlus, IconReceipt, IconSearch, IconWarning } from '../components/icons';
import { SegmentedControl, SegmentedItem } from '../components/radio-group';
import { Skeleton, SkeletonText } from '../components/skeleton';
import type { Tone } from '../components/types';
import { formatAmount, invoices } from '../shared/data';
import { invoiceColumns } from '../shared/invoice-columns';
import { Example, Kbd, Plate, Section, Token } from './doc';

export function CardSection() {
  return (
    <Section
      id="card"
      number="11"
      title="Card"
      summary="A container for one self-contained object. Use cards for things that are truly separate; scan-heavy collections belong in lists and tables."
      contract={[
        ['Keyboard', <>A linked card is one tab stop: the title link stretches over the card; secondary actions sit above it.</>],
        ['Semantics', <>Plain container; <Token>CardTitle</Token> is an <Token>h3</Token> by default, change it with <Token>asChild</Token> to fit the outline.</>],
        ['Tokens', <><Token>--card-*</Token>: <Token>bg-surface</Token>, <Token>border-subtle</Token>, <Token>radius-lg</Token>, <Token>--card-shadow</Token> on elevated only</>],
      ]}
    >
      <div className="grid gap-6 md:grid-cols-3">
        <Card variant="outlined">
          <CardHeader>
            <CardEyebrow>Monthly recurring revenue</CardEyebrow>
            <Badge tone="success" size="sm" icon={<IconArrowUp />}>
              4.2%
            </Badge>
          </CardHeader>
          <p className="font-display text-4xl font-semibold tracking-tight text-default">{formatAmount(48210)}</p>
          <CardDescription>Up from {formatAmount(46268)} in September. Outlined: the default for dashboards.</CardDescription>
        </Card>
        <Card variant="elevated" interactive>
          <CardEyebrow>Project · updated 2 h ago</CardEyebrow>
          <CardTitle>
            <CardLink href="#card">Atlas redesign</CardLink>
          </CardTitle>
          <CardDescription>Marketing site on the new grid and type scale. The whole card is the link; it has one focus ring.</CardDescription>
          <CardFooter>
            <Badge tone="accent">In review</Badge>
            <span className="text-sm text-muted">214 files</span>
          </CardFooter>
        </Card>
        <Card variant="sunken">
          <CardTitle>Need more seats?</CardTitle>
          <CardDescription>Seats added today are prorated to the day. Sunken cards suit secondary, tonal content.</CardDescription>
          <CardFooter>
            <Button size="sm" variant="secondary" startIcon={<IconPlus />}>
              Add seats
            </Button>
          </CardFooter>
        </Card>
      </div>
    </Section>
  );
}

const tones: Tone[] = ['neutral', 'accent', 'info', 'success', 'warning', 'danger'];
const toneIcons: Partial<Record<Tone, ReactElement>> = {
  info: <IconInfo />,
  success: <IconCheckCircle />,
  warning: <IconWarning />,
  danger: <IconDanger />,
};

export function BadgeSection() {
  return (
    <Section
      id="badge"
      number="12"
      title="Badge"
      summary="A short, non-interactive status or count. The words carry the meaning; tone and icon reinforce it."
      contract={[
        ['Keyboard', <>Not focusable. If it needs to do something, it is a button.</>],
        ['Semantics', <>Plain text in a <Token>span</Token>; icons are decorative. Prop <Token>tone</Token> is shared with Alert and Toast.</>],
        ['Tokens', <><Token>--badge-*</Token> pairs, contrast-checked by <Token>tokens.py lint</Token>; <Token>radius-full</Token></>],
      ]}
    >
      <Plate title="Tones and variants">
        <div className="grid gap-4">
          {(['subtle', 'outline'] as const).map((variant) => (
            <div key={variant} className="flex flex-wrap items-center gap-x-3 gap-y-3">
              <span className="w-16 text-xs font-semibold uppercase tracking-caps text-muted">{variant}</span>
              {tones.map((tone) => (
                <Badge key={tone} tone={tone} variant={variant} icon={toneIcons[tone]}>
                  {tone[0].toUpperCase() + tone.slice(1)}
                </Badge>
              ))}
            </div>
          ))}
          <div className="flex flex-wrap items-center gap-x-3 gap-y-3">
            <span className="w-16 text-xs font-semibold uppercase tracking-caps text-muted">sm</span>
            <Badge size="sm">Draft</Badge>
            <Badge size="sm" tone="accent">
              New
            </Badge>
            <Badge size="sm" tone="success">
              12 paid
            </Badge>
          </div>
        </div>
      </Plate>
    </Section>
  );
}

export function AlertSection() {
  const [dismissed, setDismissed] = useState(false);
  return (
    <Section
      id="alert"
      number="13"
      title="Alert and Banner"
      summary="Persistent status that stays until it is resolved: inline next to its cause, or as a banner across the page. Not for confirmations (toast) or decisions (dialog)."
      contract={[
        ['Keyboard', <>Actions and the optional dismiss button are normal tab stops.</>],
        ['Semantics', <>Static by default; <Token>live="polite"</Token> (<Token>status</Token>) or <Token>"assertive"</Token> (<Token>alert</Token>) when it appears after an action.</>],
        ['Tokens', <><Token>--color-{'{status}'}-bg</Token>, <Token>-border</Token>, <Token>-fg</Token> for icon and title; body text <Token>fg-default</Token></>],
      ]}
    >
      <Plate title="Alert" note="Icon, title and text: status is never color alone">
        <div className="grid gap-4">
          <Alert tone="info" title="Prices change on 1 January 2027">
            Team moves to $22 per seat per month. Your annual price is locked until 14 March 2027.
          </Alert>
          <Alert tone="success" title="Payment method updated">
            Future invoices are charged to the Visa ending 8817.
          </Alert>
          <Alert
            tone="warning"
            title="Card expires this month"
            actions={
              <>
                <Button size="sm" variant="secondary">
                  Update card
                </Button>
                <Button size="sm" variant="ghost">
                  Remind me later
                </Button>
              </>
            }
          >
            The Visa ending 4242 expires on 31 October 2026. Update it before the 14 November renewal.
          </Alert>
          {!dismissed ? (
            <Alert tone="danger" title="Payment failed for INV-2017" onDismiss={() => setDismissed(true)} dismissLabel="Dismiss payment alert">
              The bank declined the charge of $48.00. We'll retry on 25 October.
            </Alert>
          ) : (
            <Button size="sm" variant="ghost" onClick={() => setDismissed(false)}>
              Show the dismissed alert again
            </Button>
          )}
        </div>
      </Plate>
      <Plate title="Banner" note="Full width, at the top of the page or app shell" bodyClassName="p-0 sm:p-0">
        <Banner
          tone="warning"
          title="Your trial ends in 3 days."
          actions={
            <Button size="sm" variant="secondary">
              Choose a plan
            </Button>
          }
        >
          Projects stay read-only until you pick a plan.
        </Banner>
      </Plate>
    </Section>
  );
}

export function DataTableSection() {
  const [density, setDensity] = useState<Density>('default');
  const [mode, setMode] = useState<'data' | 'loading' | 'empty'>('data');
  const [selected, setSelected] = useState<Set<string>>(new Set(['INV-2031']));
  return (
    <Section
      id="data-table"
      number="14"
      title="Data table"
      summary="Compare rows and columns. Text aligns to the start, numbers to the end in tabular figures; missing values say so instead of showing zero."
      contract={[
        [
          'Keyboard',
          <>
            Sort buttons and row checkboxes are tab stops; cells are not. The table scrolls in a focusable region when it is wider
            than its container (<Kbd>←</Kbd> <Kbd>→</Kbd>).
          </>,
        ],
        [
          'Semantics',
          <>
            Native <Token>table</Token>, <Token>caption</Token>, <Token>th scope</Token>; <Token>aria-sort</Token> on the sorted
            header only; sort changes and loading are announced; missing values sort last.
          </>,
        ],
        ['Tokens', <><Token>--table-*</Token>: header <Token>bg-sunken</Token>, selected <Token>accent-subtle</Token>, cell padding <Token>space-4</Token> by <Token>space-2</Token></>],
      ]}
    >
      <Plate title="Live" note="Activate a column header to sort; select rows with the checkboxes">
        <div className="mb-4 flex flex-wrap items-center gap-x-6 gap-y-3">
          <SegmentedControl label="Density" value={density} onValueChange={(v) => setDensity(v as Density)} size="sm">
            <SegmentedItem value="compact">Compact</SegmentedItem>
            <SegmentedItem value="default">Default</SegmentedItem>
            <SegmentedItem value="comfortable">Comfortable</SegmentedItem>
          </SegmentedControl>
          <SegmentedControl label="Data" value={mode} onValueChange={(v) => setMode(v as typeof mode)} size="sm">
            <SegmentedItem value="data">Rows</SegmentedItem>
            <SegmentedItem value="loading">Loading</SegmentedItem>
            <SegmentedItem value="empty">Empty</SegmentedItem>
          </SegmentedControl>
          <p className="text-sm text-muted sm:ms-auto" aria-live="polite">
            {selected.size} selected
          </p>
        </div>
        <DataTable
          caption="Invoices, Harbor Studio"
          columns={invoiceColumns}
          rows={mode === 'empty' ? [] : invoices}
          getRowId={(row) => row.id}
          defaultSort={{ column: 'date', direction: 'descending' }}
          selectionMode="multiple"
          selectedKeys={selected}
          onSelectionChange={setSelected}
          loading={mode === 'loading'}
          loadingLabel="Loading invoices"
          density={density}
          emptyState={
            <EmptyState
              size="sm"
              icon={<IconReceipt />}
              title="No invoices yet"
              description="Your first invoice appears here after the trial ends."
            />
          }
        />
      </Plate>
    </Section>
  );
}

export function EmptyStateSection() {
  return (
    <Section
      id="empty-state"
      number="15"
      title="Empty state"
      summary="Say why the area is empty and offer the next step. First use invites creation; no results offers to clear filters."
      contract={[
        ['Keyboard', <>Only its actions are focusable.</>],
        ['Semantics', <>Heading level set by <Token>headingLevel</Token> to fit the page outline; icon is decorative.</>],
        ['Tokens', <><Token>bg-sunken</Token> icon disc, <Token>font-display</Token> title, <Token>measure-narrow</Token> text width</>],
      ]}
    >
      <div className="grid gap-6 md:grid-cols-2">
        <Card padding="none">
          <EmptyState
            icon={<IconFolder />}
            title="Create your first project"
            description="Projects hold files, comments and approvals for one piece of client work."
            actions={
              <>
                <Button startIcon={<IconPlus />}>New project</Button>
                <Button variant="ghost">Import</Button>
              </>
            }
          />
        </Card>
        <Card padding="none">
          <EmptyState
            icon={<IconSearch />}
            title="No invoices match “refunded, 2025”"
            description="Try another year, or clear the filters to see all 48 invoices."
            actions={<Button variant="secondary">Clear filters</Button>}
          />
        </Card>
      </div>
    </Section>
  );
}

export function SkeletonSection() {
  return (
    <Section
      id="skeleton"
      number="16"
      title="Skeleton"
      summary="Placeholder shapes for content that takes 1-10 seconds. Under a second, show nothing; over ten, show progress and a way to cancel."
      contract={[
        ['Keyboard', <>Not focusable.</>],
        ['Semantics', <>Shapes are <Token>aria-hidden</Token>; the region sets <Token>aria-busy</Token> and announces a loading status.</>],
        ['Tokens', <><Token>--color-border-subtle</Token> fill; pulse at <Token>duration-slower</Token> x 3, stopped by reduced motion</>],
      ]}
    >
      <div className="grid gap-6 md:grid-cols-3">
        <Card aria-busy="true">
          <span className="sr-only">Loading revenue</span>
          <Example>
            <Skeleton shape="text" className="w-32" />
            <Skeleton className="h-10 w-40" />
            <SkeletonText lines={2} />
          </Example>
        </Card>
        <Card aria-busy="true">
          <span className="sr-only">Loading project</span>
          <div className="flex items-center gap-3">
            <Skeleton shape="circle" className="size-10" />
            <div className="grid flex-1 gap-2">
              <Skeleton shape="text" className="w-2/3" />
              <Skeleton shape="text" className="w-1/3" />
            </div>
          </div>
          <Skeleton shape="box" className="h-24 w-full" />
        </Card>
        <Card aria-busy="true">
          <span className="sr-only">Loading activity</span>
          <SkeletonText lines={4} />
        </Card>
      </div>
    </Section>
  );
}
