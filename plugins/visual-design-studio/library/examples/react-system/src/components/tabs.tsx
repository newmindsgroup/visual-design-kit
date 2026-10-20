// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Tabs: switch between views of the same object. Radix Tabs: tablist/tab/tabpanel, one tab stop,
// Left/Right (mirrored in RTL), Home and End; automatic activation by default (set activationMode="manual"
// when a panel is slow to render).
import * as RadixTabs from '@radix-ui/react-tabs';
import type { ComponentProps, ReactNode } from 'react';
import { cx } from '../lib/cx';

export type TabsProps = ComponentProps<typeof RadixTabs.Root>;

export function Tabs({ className, ...rest }: TabsProps) {
  return <RadixTabs.Root data-slot="tabs" className={cx('flex min-w-0 flex-col', className)} {...rest} />;
}

export type TabsListProps = Omit<ComponentProps<typeof RadixTabs.List>, 'aria-label'> & {
  /** Names the tab list when no visible heading does (pass aria-labelledby instead if one does). */
  'aria-label'?: string;
};

export function TabsList({ className, ...rest }: TabsListProps) {
  return (
    <RadixTabs.List
      data-slot="tabs-list"
      className={cx('flex min-w-0 gap-1 overflow-x-auto border-b border-subtle', className)}
      {...rest}
    />
  );
}

export type TabsTriggerProps = ComponentProps<typeof RadixTabs.Trigger> & {
  /** Optional count shown after the label, e.g. 12 open items. Included in the accessible name. */
  count?: ReactNode;
  icon?: ReactNode;
};

export function TabsTrigger({ className, children, count, icon, ...rest }: TabsTriggerProps) {
  return (
    <RadixTabs.Trigger
      data-slot="tabs-trigger"
      className={cx(
        'group relative inline-flex h-11 shrink-0 cursor-pointer items-center gap-2 whitespace-nowrap rounded-t-sm px-3 text-sm font-medium text-muted outline-none',
        'transition-colors duration-fast ease-standard hover:text-default focus-visible:focus-ring-inset',
        'after:absolute after:inset-x-2 after:bottom-0 after:h-0.5 after:rounded-full after:bg-transparent after:transition-colors after:duration-fast',
        'data-[state=active]:text-default data-[state=active]:after:bg-accent',
        'hover:after:bg-(--color-border-default) data-[state=active]:hover:after:bg-accent',
        'disabled:cursor-not-allowed disabled:text-subtle disabled:hover:after:bg-transparent',
        '[&>svg]:size-(--size-icon-sm)',
        className,
      )}
      {...rest}
    >
      {icon}
      <span>{children}</span>
      {count !== undefined ? (
        <span className="inline-flex h-5 min-w-5 items-center justify-center rounded-full bg-sunken px-1.5 text-xs font-semibold tabular-nums text-muted group-data-[state=active]:bg-accent-subtle group-data-[state=active]:text-accent">
          {count}
        </span>
      ) : null}
    </RadixTabs.Trigger>
  );
}

export function TabsContent({ className, ...rest }: ComponentProps<typeof RadixTabs.Content>) {
  return (
    <RadixTabs.Content
      data-slot="tabs-content"
      className={cx('min-w-0 rounded-sm pt-6 outline-none focus-visible:focus-ring', className)}
      {...rest}
    />
  );
}
