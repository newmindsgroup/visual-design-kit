// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Tooltip: short supplementary text or the visible name of an icon-only button.
// Radix Tooltip: opens on hover and keyboard focus after a delay, Escape dismisses, hoverable (WCAG 1.4.13).
// Never put essential information or interactive content in a tooltip, and never attach one to a disabled control.
import * as RadixTooltip from '@radix-ui/react-tooltip';
import type { ReactElement, ReactNode } from 'react';
import { cx } from '../lib/cx';
import { usePopoverLayerClass } from '../lib/layer';

export function TooltipProvider({ children, delayDuration = 400 }: { children: ReactNode; delayDuration?: number }) {
  return (
    <RadixTooltip.Provider delayDuration={delayDuration} skipDelayDuration={300}>
      {children}
    </RadixTooltip.Provider>
  );
}

export const tooltipSurfaceClass =
  'max-w-64 rounded-sm bg-inverse px-2 py-1 text-sm font-medium leading-snug text-inverse shadow-md';

export interface TooltipProps {
  content: ReactNode;
  /** A single focusable element (Button, link). It receives the hover and focus listeners. */
  children: ReactElement;
  side?: 'top' | 'right' | 'bottom' | 'left';
  align?: 'start' | 'center' | 'end';
  open?: boolean;
  defaultOpen?: boolean;
  onOpenChange?: (open: boolean) => void;
  delayDuration?: number;
  /**
   * 'description' (default) links the text to the trigger with aria-describedby.
   * 'label' is for icon-only buttons whose aria-label already says the same thing: no duplicate announcement.
   */
  mode?: 'description' | 'label';
}

export function Tooltip({ content, children, side = 'top', align = 'center', mode = 'description', ...rootProps }: TooltipProps) {
  const layer = usePopoverLayerClass();
  return (
    <RadixTooltip.Root {...rootProps}>
      <RadixTooltip.Trigger asChild {...(mode === 'label' ? { 'aria-describedby': undefined } : {})}>
        {children}
      </RadixTooltip.Trigger>
      <RadixTooltip.Portal>
        <RadixTooltip.Content
          side={side}
          align={align}
          sideOffset={6}
          collisionPadding={8}
          data-slot="tooltip"
          className={cx(layer, tooltipSurfaceClass, 'data-[state=delayed-open]:animate-popover-in data-[state=instant-open]:animate-popover-in data-[state=closed]:animate-popover-out')}
        >
          {content}
          <RadixTooltip.Arrow className="fill-(--color-bg-inverse)" width={10} height={5} />
        </RadixTooltip.Content>
      </RadixTooltip.Portal>
    </RadixTooltip.Root>
  );
}
