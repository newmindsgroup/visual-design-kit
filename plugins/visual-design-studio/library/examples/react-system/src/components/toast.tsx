// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Toast: transient confirmation of the user's own action, optionally with one action such as Undo.
// Never for errors that need action (use an inline Alert). Radix Toast: live-region announcement,
// pauses on hover, focus and window blur, F8 jumps to the viewport, swipe or Escape dismisses.
import { useDirection } from '@radix-ui/react-direction';
import * as RadixToast from '@radix-ui/react-toast';
import { createContext, useCallback, useContext, useMemo, useRef, useState, type ReactNode } from 'react';
import { cx } from '../lib/cx';
import { Button, closeButtonClass } from './button';
import { IconCheckCircle, IconDanger, IconInfo, IconWarning, IconX } from './icons';

export type ToastTone = 'neutral' | 'info' | 'success' | 'warning' | 'danger';

export interface ToastAction {
  label: string;
  /** Describes how to do the same thing without the toast (Radix announces it), e.g. "Undo from the History panel". */
  altText: string;
  onAction: () => void;
}

export interface ToastOptions {
  title: ReactNode;
  description?: ReactNode;
  tone?: ToastTone;
  action?: ToastAction;
  /** Milliseconds. Default 6000, or 10000 when there is an action (never under 5000 with an action). */
  duration?: number;
}

interface ToastRecord extends ToastOptions {
  id: string;
  open: boolean;
}

interface ToastApi {
  toast: (options: ToastOptions) => string;
  dismiss: (id: string) => void;
}

const ToastContext = createContext<ToastApi | null>(null);

export function useToast(): ToastApi {
  const api = useContext(ToastContext);
  if (!api) throw new Error('useToast must be used inside <ToastProvider>.');
  return api;
}

const toneIcon: Record<ToastTone, ReactNode> = {
  neutral: null,
  info: <IconInfo className="text-info" />,
  success: <IconCheckCircle className="text-success" />,
  warning: <IconWarning className="text-warning" />,
  danger: <IconDanger className="text-danger" />,
};

export const toastSurfaceClass = cx(
  'pointer-events-auto relative flex w-full items-start gap-3 rounded-lg border border-default bg-surface-raised p-4 text-default shadow-lg',
);

/** The visual body shared by live toasts and static previews. */
function ToastBody({ tone = 'neutral', title, description, live }: { tone?: ToastTone; title: ReactNode; description?: ReactNode; live: boolean }) {
  const Title = live ? RadixToast.Title : 'p';
  const Description = live ? RadixToast.Description : 'p';
  return (
    <>
      {toneIcon[tone] ? <span className="mt-0.5 flex">{toneIcon[tone]}</span> : null}
      <div className="grid min-w-0 flex-1 gap-0.5 py-0.5">
        <Title className="text-sm font-semibold leading-snug text-default">{title}</Title>
        {description ? <Description className="text-sm leading-snug text-muted">{description}</Description> : null}
      </div>
    </>
  );
}

export function ToastProvider({ children, label = 'Notifications' }: { children: ReactNode; label?: string }) {
  const [toasts, setToasts] = useState<ToastRecord[]>([]);
  const counter = useRef(0);
  const dir = useDirection();

  const toast = useCallback((options: ToastOptions) => {
    counter.current += 1;
    const id = `toast-${counter.current}`;
    // Keep at most three on screen; older ones close first.
    setToasts((list) => [...list.map((t, i) => (i < list.length - 2 ? { ...t, open: false } : t)), { ...options, id, open: true }]);
    return id;
  }, []);

  const dismiss = useCallback((id: string) => {
    setToasts((list) => list.map((t) => (t.id === id ? { ...t, open: false } : t)));
  }, []);

  const remove = useCallback((id: string) => setToasts((list) => list.filter((t) => t.id !== id)), []);
  const api = useMemo(() => ({ toast, dismiss }), [toast, dismiss]);

  return (
    <ToastContext.Provider value={api}>
      <RadixToast.Provider swipeDirection={dir === 'rtl' ? 'left' : 'right'} label={label}>
        {children}
        {toasts.map((t) => (
          <RadixToast.Root
            key={t.id}
            open={t.open}
            onOpenChange={(open) => {
              if (!open) dismiss(t.id);
            }}
            onAnimationEnd={(event) => {
              if (!t.open && event.target === event.currentTarget) remove(t.id);
            }}
            duration={t.duration ?? (t.action ? 10000 : 6000)}
            type={t.tone === 'danger' || t.tone === 'warning' ? 'foreground' : 'background'}
            data-slot="toast"
            data-tone={t.tone ?? 'neutral'}
            className={cx(
              toastSurfaceClass,
              'data-[state=open]:animate-toast-in data-[state=closed]:animate-toast-out',
              'data-[swipe=move]:translate-x-(--radix-toast-swipe-move-x) data-[swipe=cancel]:translate-x-0 data-[swipe=cancel]:transition-transform data-[swipe=end]:animate-toast-swipe-out',
            )}
          >
            <ToastBody tone={t.tone} title={t.title} description={t.description} live />
            {t.action ? (
              <RadixToast.Action altText={t.action.altText} asChild>
                <Button size="sm" variant="secondary" onClick={t.action.onAction}>
                  {t.action.label}
                </Button>
              </RadixToast.Action>
            ) : null}
            <RadixToast.Close className={cx(closeButtonClass, '-me-1 -mt-1')} aria-label="Dismiss notification">
              <IconX size="sm" />
            </RadixToast.Close>
          </RadixToast.Root>
        ))}
        <RadixToast.Viewport
          data-slot="toast-viewport"
          className="fixed bottom-0 end-0 z-toast m-0 flex w-full list-none flex-col gap-3 p-4 outline-none sm:max-w-104 sm:p-6"
        />
      </RadixToast.Provider>
    </ToastContext.Provider>
  );
}

/** Static render of a toast for documentation. Not a live region; use useToast() in product code. */
export function ToastPreview({ tone, title, description, actionLabel }: ToastOptions & { actionLabel?: string }) {
  return (
    <div className={toastSurfaceClass} data-slot="toast-preview" data-tone={tone ?? 'neutral'}>
      <ToastBody tone={tone} title={title} description={description} live={false} />
      {actionLabel ? (
        <Button size="sm" variant="secondary" tabIndex={-1}>
          {actionLabel}
        </Button>
      ) : null}
      <span className={cx(closeButtonClass, '-me-1 -mt-1')} aria-hidden="true">
        <IconX size="sm" />
      </span>
    </div>
  );
}
