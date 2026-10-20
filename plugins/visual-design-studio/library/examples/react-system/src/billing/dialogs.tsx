// Version-Timestamp: 2026-10-20 02:52:00 UTC
import { useEffect, useRef, useState } from 'react';
import { Badge } from '../components/badge';
import { Button } from '../components/button';
import { Dialog, DialogBody, DialogClose, DialogContent, DialogFooter } from '../components/dialog';
import { RadioCard, RadioGroup, SegmentedControl, SegmentedItem } from '../components/radio-group';
import { formatAmount, formatCurrency, plans, type Plan } from '../shared/data';

type Cycle = 'monthly' | 'annual';

export function ChangePlanDialog({
  open,
  onOpenChange,
  currentPlan,
  currentCycle,
  seats,
  onConfirm,
}: {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  currentPlan: Plan['id'];
  currentCycle: Cycle;
  seats: number;
  onConfirm: (plan: Plan['id'], cycle: Cycle) => void;
}) {
  const [planId, setPlanId] = useState<Plan['id']>(currentPlan);
  const [cycle, setCycle] = useState<Cycle>(currentCycle);
  const [saving, setSaving] = useState(false);
  const timer = useRef<number | undefined>(undefined);

  useEffect(() => {
    if (open) {
      setPlanId(currentPlan);
      setCycle(currentCycle);
    }
  }, [open, currentPlan, currentCycle]);
  useEffect(() => () => window.clearTimeout(timer.current), []);

  const plan = plans.find((p) => p.id === planId) ?? plans[0];
  const perSeat = cycle === 'annual' ? plan.annual : plan.monthly;
  const total = perSeat * seats * (cycle === 'annual' ? 12 : 1);
  const unchanged = planId === currentPlan && cycle === currentCycle;

  return (
    <Dialog open={open} onOpenChange={(next) => !saving && onOpenChange(next)}>
      <DialogContent
        title="Change plan"
        description={`${seats} seats. The change applies today and the difference is prorated to the day.`}
        data-testid="change-plan-dialog"
      >
        <DialogBody label="Plan options">
          <div className="grid gap-6">
            <SegmentedControl label="Billing cycle" value={cycle} onValueChange={(v) => setCycle(v as Cycle)}>
              <SegmentedItem value="monthly">Monthly</SegmentedItem>
              <SegmentedItem value="annual">Annual · save 16%</SegmentedItem>
            </SegmentedControl>
            <RadioGroup label="Plan" value={planId} onValueChange={(v) => setPlanId(v as Plan['id'])}>
              {plans.map((p) => (
                <RadioCard
                  key={p.id}
                  value={p.id}
                  label={p.name}
                  description={p.summary}
                  meta={`${formatCurrency(cycle === 'annual' ? p.annual : p.monthly)} / seat / mo`}
                  badge={
                    p.id === currentPlan ? (
                      <Badge size="sm" tone="accent" variant="outline">
                        Current
                      </Badge>
                    ) : null
                  }
                />
              ))}
            </RadioGroup>
            <div className="grid gap-1 rounded-md border border-subtle bg-sunken p-4" aria-live="polite">
              <p className="text-sm text-muted">New price</p>
              <p className="font-display text-2xl font-semibold tracking-tight text-default">
                {formatAmount(total)} <span className="font-body text-sm font-regular text-muted">per {cycle === 'annual' ? 'year' : 'month'}</span>
              </p>
              <p className="text-sm text-muted">
                {unchanged ? 'This is your current plan. Choose a different plan or billing cycle to continue.' : 'Charged today, minus the unused part of your current plan.'}
              </p>
            </div>
          </div>
        </DialogBody>
        <DialogFooter>
          <DialogClose asChild>
            <Button variant="secondary" disabled={saving}>
              Cancel
            </Button>
          </DialogClose>
          <Button
            disabled={unchanged}
            loading={saving}
            loadingLabel="Changing plan…"
            onClick={() => {
              setSaving(true);
              timer.current = window.setTimeout(() => {
                setSaving(false);
                onConfirm(planId, cycle);
                onOpenChange(false);
              }, 900);
            }}
          >
            Confirm change
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}

export function CancelDialog({
  open,
  onOpenChange,
  planName,
  onConfirm,
}: {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  planName: string;
  onConfirm: () => void;
}) {
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent
        role="alertdialog"
        size="sm"
        closeButton={false}
        title={`Cancel the ${planName} plan?`}
        description="Harbor Studio keeps every feature until 14 March 2027, then moves to the Free plan. Projects over the Free limit become read-only. You can resume before then."
        data-testid="cancel-dialog"
      >
        <DialogFooter>
          <DialogClose asChild>
            <Button variant="secondary">Keep subscription</Button>
          </DialogClose>
          <DialogClose asChild>
            <Button variant="danger" onClick={onConfirm}>
              Cancel subscription
            </Button>
          </DialogClose>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
