// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Modal dialog for decisions and short focused tasks. Spec: component-specs/dialog.md (DLG-S1 to DLG-S5).
// Radix Dialog: focus moves in, Tab is trapped, Escape closes, focus returns to the trigger, background is inert.
import * as RadixDialog from '@radix-ui/react-dialog';
import { useRef, type ComponentProps, type ReactNode, type RefObject } from 'react';
import { cx, variants } from '../lib/cx';
import { LayerContext } from '../lib/layer';
import { useOverflow } from '../lib/use-overflow';
import { closeButtonClass } from './button';
import { IconX } from './icons';

export interface DialogProps {
  open?: boolean;
  defaultOpen?: boolean;
  onOpenChange?: (open: boolean) => void;
  children: ReactNode;
}

export function Dialog(props: DialogProps) {
  return <RadixDialog.Root {...props} />;
}

/** Wrap your own Button: <DialogTrigger asChild><Button>Open</Button></DialogTrigger>. */
export const DialogTrigger = RadixDialog.Trigger;
/** Any element that closes the dialog: <DialogClose asChild><Button variant="secondary">Cancel</Button></DialogClose>. */
export const DialogClose = RadixDialog.Close;

export const dialogSurfaceStyles = variants({
  base: [
    'relative flex max-h-full w-full flex-col overflow-hidden rounded-(--dialog-radius) border border-(--dialog-border)',
    'bg-(--dialog-bg) text-default shadow-(--dialog-shadow) outline-none',
  ],
  variants: {
    size: {
      sm: 'max-w-104',
      md: 'max-w-(--dialog-max-width)',
      lg: 'max-w-(--container-md)',
    },
  },
  defaultVariants: { size: 'md' },
});

export type DialogContentProps = Omit<ComponentProps<typeof RadixDialog.Content>, 'title' | 'role'> & {
  /** Visible title; it names the dialog (aria-labelledby). */
  title: ReactNode;
  /** Short supporting text; it describes the dialog (aria-describedby). */
  description?: ReactNode;
  /** sm 416px, md 640px (--dialog-max-width), lg 768px. */
  size?: 'sm' | 'md' | 'lg';
  /**
   * 'alertdialog' for confirmations of destructive or consequential actions: pointer-down outside does not
   * dismiss, and initial focus lands on the first action in the footer (put the safe action first in DOM).
   */
  role?: 'dialog' | 'alertdialog';
  /** Show the close button in the header (default true). Confirmations usually rely on Cancel instead. */
  closeButton?: boolean;
  closeLabel?: string;
  /** Element to focus on open (for example the first field). Default: the first focusable element. */
  initialFocusRef?: RefObject<HTMLElement | null>;
};

export function DialogContent({
  title,
  description,
  size = 'md',
  role = 'dialog',
  closeButton = true,
  closeLabel = 'Close',
  initialFocusRef,
  className,
  children,
  onOpenAutoFocus,
  onCloseAutoFocus,
  onPointerDownOutside,
  ...rest
}: DialogContentProps) {
  const contentRef = useRef<HTMLDivElement | null>(null);
  // Element that had focus when the dialog opened. Radix returns focus to <DialogTrigger>; dialogs opened
  // from state (a menu item, a banner action) have no trigger, so focus goes back here instead (DLG-S4).
  const returnFocus = useRef<HTMLElement | null>(null);
  return (
    <RadixDialog.Portal>
      <RadixDialog.Overlay
        data-slot="dialog-overlay"
        className={cx(
          'fixed inset-0 z-(--dialog-z) grid place-items-center overflow-y-auto bg-(--dialog-scrim) p-4 sm:p-6',
          'data-[state=open]:animate-scrim-in data-[state=closed]:animate-scrim-out',
        )}
      >
        <RadixDialog.Content
          ref={contentRef}
          role={role}
          {...(description ? {} : { 'aria-describedby': undefined })}
          aria-modal="true"
          data-slot="dialog"
          onOpenAutoFocus={(event) => {
            const opener = document.activeElement;
            returnFocus.current = opener instanceof HTMLElement && opener !== document.body ? opener : null;
            onOpenAutoFocus?.(event);
            if (event.defaultPrevented) return;
            const target =
              initialFocusRef?.current ??
              (role === 'alertdialog' ? contentRef.current?.querySelector<HTMLElement>('[data-slot="dialog-footer"] button') : null);
            if (target) {
              event.preventDefault();
              target.focus();
            }
          }}
          onCloseAutoFocus={(event) => {
            onCloseAutoFocus?.(event);
            if (event.defaultPrevented) return;
            const target = returnFocus.current;
            if (target?.isConnected) {
              event.preventDefault();
              target.focus();
            }
          }}
          onPointerDownOutside={(event) => {
            onPointerDownOutside?.(event);
            if (role === 'alertdialog') event.preventDefault();
          }}
          className={cx(
            dialogSurfaceStyles({ size }),
            'data-[state=open]:animate-dialog-in data-[state=closed]:animate-dialog-out',
            className,
          )}
          {...rest}
        >
          <LayerContext.Provider value="modal">
            <div className="flex items-start gap-4 px-(--dialog-padding) pt-(--dialog-padding) pb-4" data-slot="dialog-header">
              <div className="grid min-w-0 flex-1 gap-1">
                <RadixDialog.Title className="font-display text-xl font-semibold leading-snug tracking-tight text-default">
                  {title}
                </RadixDialog.Title>
                {description ? (
                  <RadixDialog.Description className="text-sm leading-normal text-muted">{description}</RadixDialog.Description>
                ) : null}
              </div>
              {closeButton ? (
                <RadixDialog.Close className={cx(closeButtonClass, '-me-2 -mt-1')} aria-label={closeLabel}>
                  <IconX size="md" />
                </RadixDialog.Close>
              ) : null}
            </div>
            {children}
          </LayerContext.Provider>
        </RadixDialog.Content>
      </RadixDialog.Overlay>
    </RadixDialog.Portal>
  );
}

/**
 * The dialog's content area. When it overflows (long content, zoom, small screens) it becomes a named,
 * keyboard-focusable scroll region while the header and footer stay in place (DLG-OVERFLOW).
 */
export function DialogBody({ children, className, label = 'Dialog content' }: { children: ReactNode; className?: string; label?: string }) {
  const ref = useRef<HTMLDivElement | null>(null);
  const overflowing = useOverflow(ref, 'y');
  return (
    <div
      ref={ref}
      data-slot="dialog-body"
      role={overflowing ? 'region' : undefined}
      aria-label={overflowing ? label : undefined}
      tabIndex={overflowing ? 0 : undefined}
      className={cx('min-h-0 flex-1 overflow-y-auto px-(--dialog-padding) pb-(--dialog-padding) outline-none focus-visible:focus-ring-inset', className)}
    >
      {children}
    </div>
  );
}

/** Actions row. Order in DOM: safe action first, confirming action last (it sits at the inline end). */
export function DialogFooter({ children, className }: { children: ReactNode; className?: string }) {
  return (
    <div
      data-slot="dialog-footer"
      className={cx(
        'flex flex-col-reverse gap-3 border-t border-subtle bg-surface px-(--dialog-padding) py-4 sm:flex-row sm:items-center sm:justify-end',
        className,
      )}
    >
      {children}
    </div>
  );
}
