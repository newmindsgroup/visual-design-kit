// Version-Timestamp: 2026-10-20 02:52:00 UTC
import { useRef, useState } from 'react';
import { Button, closeButtonClass } from '../components/button';
import { Dialog, DialogBody, DialogClose, DialogContent, DialogFooter, DialogTrigger, dialogSurfaceStyles } from '../components/dialog';
import { IconCopy, IconDownload, IconInfo, IconLink, IconTrash, IconUsers, IconX } from '../components/icons';
import { Select, SelectItem } from '../components/select';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../components/tabs';
import { TextField } from '../components/text-field';
import { ToastPreview, useToast } from '../components/toast';
import { Tooltip, tooltipSurfaceClass } from '../components/tooltip';
import { cx } from '../lib/cx';
import { Example, Kbd, Plate, Section, Token } from './doc';

function InviteDialog() {
  const [open, setOpen] = useState(false);
  const [email, setEmail] = useState('');
  const [error, setError] = useState<string | undefined>();
  const first = useRef<HTMLInputElement | null>(null);
  const { toast } = useToast();
  return (
    <Dialog
      open={open}
      onOpenChange={(next) => {
        setOpen(next);
        if (!next) {
          setEmail('');
          setError(undefined);
        }
      }}
    >
      <DialogTrigger asChild>
        <Button startIcon={<IconUsers />}>Invite member</Button>
      </DialogTrigger>
      <DialogContent
        title="Invite a member"
        description="They get an email with a link that expires in 7 days."
        initialFocusRef={first}
        data-testid="invite-dialog"
      >
        <form
          noValidate
          onSubmit={(event) => {
            event.preventDefault();
            if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
              setError('Enter an email address in the correct format, like name@example.com');
              first.current?.focus();
              return;
            }
            setOpen(false);
            toast({ tone: 'success', title: 'Invitation sent', description: `${email} can join Harbor Studio for 7 days.` });
          }}
          className="flex min-h-0 flex-1 flex-col"
        >
          <DialogBody>
            <div className="grid gap-4">
              <TextField
                ref={first}
                label="Email address"
                type="email"
                autoComplete="off"
                value={email}
                onValueChange={(v) => {
                  setEmail(v);
                  if (error) setError(undefined);
                }}
                error={error}
                required
              />
              <Select label="Role" defaultValue="member">
                <SelectItem value="member" description="Create and edit projects">
                  Member
                </SelectItem>
                <SelectItem value="billing" description="Manage plan, invoices and payment">
                  Billing admin
                </SelectItem>
                <SelectItem value="owner" description="Full access, including deleting the workspace">
                  Owner
                </SelectItem>
              </Select>
            </div>
          </DialogBody>
          <DialogFooter>
            <DialogClose asChild>
              <Button variant="secondary">Cancel</Button>
            </DialogClose>
            <Button type="submit">Send invitation</Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
}

function DeleteDialog() {
  const { toast } = useToast();
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="secondary" startIcon={<IconTrash />}>
          Delete project
        </Button>
      </DialogTrigger>
      <DialogContent
        role="alertdialog"
        size="sm"
        closeButton={false}
        title="Delete “Atlas redesign”?"
        description="The project, its 214 files and 38 comments are deleted for everyone. This cannot be undone."
      >
        <DialogFooter>
          <DialogClose asChild>
            <Button variant="secondary">Keep project</Button>
          </DialogClose>
          <DialogClose asChild>
            <Button variant="danger" onClick={() => toast({ tone: 'neutral', title: 'Project deleted', description: 'Atlas redesign was removed.' })}>
              Delete project
            </Button>
          </DialogClose>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}

function LongDialog() {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="ghost">Read the terms</Button>
      </DialogTrigger>
      <DialogContent title="Subscription terms" description="Summary of the Team plan agreement, version 2026-09.">
        <DialogBody label="Subscription terms">
          <ol className="grid list-decimal gap-3 ps-5 text-sm leading-relaxed text-default">
            {Array.from({ length: 14 }, (_, i) => (
              <li key={i}>
                {
                  [
                    'Fees are charged per seat at the start of each billing period.',
                    'Adding seats mid-period is prorated to the day; removing seats creates a credit.',
                    'Annual plans renew automatically unless cancelled 30 days before renewal.',
                    'Invoices are payable within 30 days when paying by bank transfer.',
                    'Taxes are calculated from the billing country on the invoice date.',
                  ][i % 5]
                }
              </li>
            ))}
          </ol>
        </DialogBody>
        <DialogFooter>
          <DialogClose asChild>
            <Button>Done</Button>
          </DialogClose>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}

export function DialogSection() {
  return (
    <Section
      id="dialog"
      number="07"
      title="Dialog"
      summary="Only for decisions that block progress and short focused tasks. Confirmations name the consequence and put the safe action first."
      contract={[
        [
          'Keyboard',
          <>
            Focus moves in (first field, or the safe action in a confirmation); <Kbd>Tab</Kbd> cycles inside; <Kbd>Esc</Kbd>{' '}
            closes; focus returns to the trigger.
          </>,
        ],
        [
          'Semantics',
          <>
            Radix Dialog: <Token>dialog</Token> or <Token>alertdialog</Token>, <Token>aria-modal</Token>, named by the title,
            described by the description; long bodies become a focusable region.
          </>,
        ],
        [
          'Tokens',
          <>
            <Token>--dialog-*</Token>: <Token>surface-raised</Token>, <Token>radius-xl</Token>, <Token>shadow-xl</Token>,{' '}
            <Token>overlay-scrim</Token>, <Token>z-modal</Token>, <Token>duration-slow</Token>
          </>,
        ],
      ]}
    >
      <div className="grid gap-6 lg:grid-cols-5">
        <Plate title="Anatomy" note="Static render" className="lg:col-span-3" bodyClassName="specimen-grid">
          <div inert className="grid place-items-center py-4">
            <div className={dialogSurfaceStyles({ size: 'sm' })}>
              <div className="flex items-start gap-4 px-(--dialog-padding) pt-(--dialog-padding) pb-4">
                <div className="grid min-w-0 flex-1 gap-1">
                  <p className="font-display text-xl font-semibold leading-snug tracking-tight">Remove 3 seats?</p>
                  <p className="text-sm text-muted">Your next invoice drops to $3,600. Removed members lose access today.</p>
                </div>
                <span className={cx(closeButtonClass, '-me-2 -mt-1')}>
                  <IconX />
                </span>
              </div>
              <div className="px-(--dialog-padding) pb-(--dialog-padding)">
                <p className="text-sm text-default">Seats in use: 15 of 18 after the change.</p>
              </div>
              <div className="flex flex-col-reverse gap-3 border-t border-subtle bg-surface px-(--dialog-padding) py-4 sm:flex-row sm:justify-end">
                <Button variant="secondary">Cancel</Button>
                <Button>Remove seats</Button>
              </div>
            </div>
          </div>
        </Plate>
        <Plate title="Live" className="lg:col-span-2">
          <div className="grid gap-4">
            <Example label="Form dialog">
              <div>
                <InviteDialog />
              </div>
            </Example>
            <Example label="Destructive confirmation">
              <div>
                <DeleteDialog />
              </div>
            </Example>
            <Example label="Overflowing body">
              <div>
                <LongDialog />
              </div>
            </Example>
          </div>
        </Plate>
      </div>
    </Section>
  );
}

export function TabsSection() {
  return (
    <Section
      id="tabs"
      number="08"
      title="Tabs"
      summary="Switch between views of one object. Not for site navigation, and not for steps in a process."
      contract={[
        [
          'Keyboard',
          <>
            <Kbd>←</Kbd> <Kbd>→</Kbd> move and activate (mirrored in RTL); <Kbd>Home</Kbd>, <Kbd>End</Kbd>; <Kbd>Tab</Kbd> moves
            into the panel.
          </>,
        ],
        ['Semantics', <>Radix Tabs: <Token>tablist</Token>, <Token>tab</Token>, <Token>tabpanel</Token>; one tab stop; counts are part of the name.</>],
        ['Tokens', <>Indicator <Token>bg-accent</Token> 2px; text <Token>fg-muted</Token> to <Token>fg-default</Token>; panel focus ring</>],
      ]}
    >
      <Plate title="Live" note="Focus a tab, then use the arrow keys">
        <Tabs defaultValue="overview" data-testid="specimen-tabs">
          <TabsList aria-label="Project views">
            <TabsTrigger value="overview">Overview</TabsTrigger>
            <TabsTrigger value="activity" count={12}>
              Activity
            </TabsTrigger>
            <TabsTrigger value="files" count={214}>
              Files
            </TabsTrigger>
            <TabsTrigger value="archive" disabled>
              Archive
            </TabsTrigger>
          </TabsList>
          <TabsContent value="overview">
            <p className="max-w-(--measure-body) text-md text-default">
              Atlas redesign moves the marketing site to the new grid and type scale. Launch is planned for 3 November.
            </p>
          </TabsContent>
          <TabsContent value="activity">
            <p className="text-md text-default">12 updates this week, most recently a comment from Lina on the pricing page.</p>
          </TabsContent>
          <TabsContent value="files">
            <p className="text-md text-default">214 files, 1.8 GB. The largest is hero-loop.mp4 (412 MB).</p>
          </TabsContent>
        </Tabs>
      </Plate>
    </Section>
  );
}

export function ToastSection() {
  const { toast } = useToast();
  return (
    <Section
      id="toast"
      number="09"
      title="Toast"
      summary="Short confirmation of something the person just did, with one optional action such as Undo. Errors that need action go inline, never in a toast."
      contract={[
        [
          'Keyboard',
          <>
            <Kbd>F8</Kbd> jumps to notifications; actions are reachable; <Kbd>Esc</Kbd> or swipe dismisses.
          </>,
        ],
        [
          'Semantics',
          <>
            Radix Toast announces through a live region (<Token>status</Token>; warnings assertive); timers pause on hover,
            focus and window blur; 10 s when there is an action.
          </>,
        ],
        ['Tokens', <><Token>surface-raised</Token>, <Token>shadow-lg</Token>, status <Token>fg</Token> icons, <Token>z-toast</Token>, <Token>duration-slow</Token> entrance</>],
      ]}
    >
      <div className="grid gap-6 lg:grid-cols-2">
        <Plate title="Tones" note="Static renders" bodyClassName="specimen-grid">
          <div inert className="grid gap-3">
            <ToastPreview tone="success" title="Invoice INV-2031 sent" description="Emailed to accounts@harbor.studio." />
            <ToastPreview tone="neutral" title="3 invoices archived" actionLabel="Undo" />
            <ToastPreview tone="info" title="Export started" description="We'll email you when the CSV is ready." />
            <ToastPreview tone="warning" title="You're offline" description="Changes will sync when you reconnect." />
          </div>
        </Plate>
        <Plate title="Live">
          <div className="flex flex-wrap gap-3">
            <Button
              variant="secondary"
              onClick={() => toast({ tone: 'success', title: 'Invoice INV-2031 sent', description: 'Emailed to accounts@harbor.studio.' })}
            >
              Send invoice
            </Button>
            <Button
              variant="secondary"
              onClick={() => {
                toast({
                  title: '3 invoices archived',
                  action: {
                    label: 'Undo',
                    altText: 'Restore them from the Archived filter',
                    onAction: () => toast({ tone: 'info', title: 'Invoices restored' }),
                  },
                });
              }}
            >
              Archive with undo
            </Button>
            <Button variant="secondary" onClick={() => toast({ tone: 'info', title: 'Export started', description: "We'll email you when the CSV is ready." })}>
              Start export
            </Button>
          </div>
        </Plate>
      </div>
    </Section>
  );
}

export function TooltipSection() {
  return (
    <Section
      id="tooltip"
      number="10"
      title="Tooltip"
      summary="Names icon-only buttons and adds short, non-essential detail. Never the only place for instructions, and never on disabled controls."
      contract={[
        [
          'Keyboard',
          <>
            Opens on focus and hover after 400ms; <Kbd>Esc</Kbd> dismisses; stays while hovered (WCAG 1.4.13).
          </>,
        ],
        [
          'Semantics',
          <>
            <Token>tooltip</Token> via <Token>aria-describedby</Token>; <Token>mode="label"</Token> skips it when the button's{' '}
            <Token>aria-label</Token> already says the same.
          </>,
        ],
        ['Tokens', <><Token>bg-inverse</Token>, <Token>text-inverse</Token>, <Token>radius-sm</Token>, <Token>shadow-md</Token></>],
      ]}
    >
      <div className="grid gap-6 lg:grid-cols-2">
        <Plate title="Anatomy" note="Static render" bodyClassName="specimen-grid">
          <div inert className="grid place-items-center gap-2 py-6">
            <div className={cx(tooltipSurfaceClass, 'relative')}>
              Copy invoice ID
              <svg viewBox="0 0 10 5" aria-hidden="true" className="absolute start-1/2 top-full w-2.5 -translate-x-1/2 fill-(--color-bg-inverse) rtl:translate-x-1/2">
                <path d="M0 0h10L5 5Z" />
              </svg>
            </div>
            <Button iconOnly size="sm" variant="ghost" aria-label="Copy invoice ID">
              <IconCopy />
            </Button>
          </div>
        </Plate>
        <Plate title="Live" note="Hover or Tab to each control">
          <div className="flex flex-wrap items-center gap-3">
            <Tooltip content="Copy link" mode="label">
              <Button iconOnly variant="secondary" aria-label="Copy link">
                <IconLink />
              </Button>
            </Tooltip>
            <Tooltip content="Download PDF" mode="label">
              <Button iconOnly variant="secondary" aria-label="Download PDF">
                <IconDownload />
              </Button>
            </Tooltip>
            <Tooltip content="Prorated to the day: 17 days of 3 seats at $20.">
              <Button variant="ghost" startIcon={<IconInfo />}>
                Why $412.50?
              </Button>
            </Tooltip>
          </div>
        </Plate>
      </div>
    </Section>
  );
}
