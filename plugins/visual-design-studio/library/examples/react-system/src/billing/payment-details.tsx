// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Billing details form: labels above, optional fields marked, validation on blur, error summary on submit
// (focus moves to it, links jump to each field), busy Save, success toast.
import { useEffect, useRef, useState, type FormEvent, type RefObject } from 'react';
import { Alert } from '../components/alert';
import { Badge } from '../components/badge';
import { Button } from '../components/button';
import { Card, CardDescription } from '../components/card';
import { Checkbox } from '../components/checkbox';
import { IconCard, IconWarning } from '../components/icons';
import { Select, SelectItem } from '../components/select';
import { TextField } from '../components/text-field';
import { useToast } from '../components/toast';
import { countries } from '../shared/data';

type FieldName = 'company' | 'email' | 'taxId' | 'country' | 'address' | 'city' | 'postcode';
type Values = Record<FieldName, string>;

const initial: Values = {
  company: 'Harbor Studio Ltd',
  email: 'accounts@harbor',
  taxId: '',
  country: 'ie',
  address: '14 Grand Canal Quay',
  city: 'Dublin',
  postcode: '',
};

const labels: Record<FieldName, string> = {
  company: 'Company name',
  email: 'Billing email',
  taxId: 'Tax ID',
  country: 'Country',
  address: 'Address',
  city: 'City',
  postcode: 'Postal code',
};

function validate(name: FieldName, value: string): string | undefined {
  const v = value.trim();
  switch (name) {
    case 'company':
      return v ? undefined : 'Enter the company name shown on invoices';
    case 'email':
      if (!v) return 'Enter a billing email address';
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) ? undefined : 'Enter an email address in the correct format, like name@example.com';
    case 'country':
      return v ? undefined : 'Choose a country';
    case 'address':
      return v ? undefined : 'Enter the first line of the address';
    case 'city':
      return v ? undefined : 'Enter a city or town';
    case 'postcode':
      return v ? undefined : 'Enter a postal code (Eircode in Ireland)';
    default:
      return undefined;
  }
}

const order: FieldName[] = ['company', 'email', 'taxId', 'country', 'address', 'city', 'postcode'];

export function PaymentDetails({ replaceCardRef }: { replaceCardRef: RefObject<HTMLButtonElement | null> }) {
  const { toast } = useToast();
  const [values, setValues] = useState<Values>(initial);
  const [errors, setErrors] = useState<Partial<Record<FieldName, string>>>({});
  const [summary, setSummary] = useState<FieldName[]>([]);
  const [saving, setSaving] = useState(false);
  const baseTitle = useRef(document.title);

  useEffect(() => {
    document.title = summary.length ? `Error: ${baseTitle.current}` : baseTitle.current;
  }, [summary]);
  useEffect(() => () => {
    document.title = baseTitle.current;
  }, []);

  const set = (name: FieldName) => (value: string) => {
    setValues((v) => ({ ...v, [name]: value }));
    // Once a field is in error, re-validate on every edit so the message clears as soon as it is fixed.
    if (errors[name]) setErrors((e) => ({ ...e, [name]: validate(name, value) }));
  };
  const blur = (name: FieldName) => () => setErrors((e) => ({ ...e, [name]: validate(name, values[name]) }));

  const onSubmit = (event: FormEvent) => {
    event.preventDefault();
    if (saving) return;
    const next: Partial<Record<FieldName, string>> = {};
    for (const name of order) next[name] = validate(name, values[name]);
    setErrors(next);
    const failing = order.filter((name) => next[name]);
    setSummary(failing);
    if (failing.length) {
      window.requestAnimationFrame(() => document.getElementById('billing-error-summary')?.focus());
      return;
    }
    setSaving(true);
    window.setTimeout(() => {
      setSaving(false);
      toast({ tone: 'success', title: 'Billing details saved', description: 'They appear on invoices from the next one.' });
    }, 1100);
  };

  const field = (name: FieldName) => ({
    id: `billing-${name}`,
    name,
    value: values[name],
    onValueChange: set(name),
    onBlur: blur(name),
    error: errors[name],
  });

  return (
    <div className="grid max-w-(--container-sm) gap-12">
      <section aria-labelledby="payment-method-title" className="grid content-start gap-4">
        <div>
          <h2 id="payment-method-title" className="font-display text-lg font-semibold tracking-tight text-default">
            Payment method
          </h2>
          <p className="mt-1 text-sm text-muted">Charged automatically on each renewal.</p>
        </div>
        <Card padding="sm">
          <div className="flex flex-wrap items-center gap-4">
            <span className="grid size-10 shrink-0 place-items-center rounded-md bg-sunken text-muted" aria-hidden="true">
              <IconCard />
            </span>
            <div className="grid min-w-0 flex-1 gap-0.5">
              <p className="font-semibold text-default">Visa ending 4242</p>
              <CardDescription>Expires 10/2026</CardDescription>
            </div>
            <Badge tone="warning" icon={<IconWarning />}>
              Expires soon
            </Badge>
          </div>
        </Card>
        <div className="flex flex-wrap items-center gap-3">
          <Button ref={replaceCardRef} variant="secondary" startIcon={<IconCard />}>
            Replace card
          </Button>
          <p className="text-sm text-muted">Cards are stored by the payment provider, not by Harbor.</p>
        </div>
      </section>

      <section aria-labelledby="billing-details-title" className="border-t border-subtle pt-10">
        <h2 id="billing-details-title" className="font-display text-lg font-semibold tracking-tight text-default">
          Billing details
        </h2>
        <p className="mt-1 text-sm text-muted">Shown on every invoice. All fields are required unless marked optional.</p>
        <form noValidate onSubmit={onSubmit} className="mt-6 grid gap-5" aria-describedby={summary.length ? 'billing-error-summary' : undefined}>
          {summary.length ? (
            <Alert id="billing-error-summary" tabIndex={-1} tone="danger" title="There is a problem">
              <ul className="mt-1 grid list-disc gap-1 ps-5">
                {summary.map((name) => (
                  <li key={name}>
                    <a
                      href={`#billing-${name}`}
                      className="font-medium text-danger underline"
                      onClick={(event) => {
                        event.preventDefault();
                        document.getElementById(`billing-${name}`)?.focus();
                      }}
                    >
                      {errors[name] ?? labels[name]}
                    </a>
                  </li>
                ))}
              </ul>
            </Alert>
          ) : null}
          <TextField label={labels.company} necessityIndicator="optional" required autoComplete="organization" {...field('company')} />
          <TextField
            label={labels.email}
            hint="Receipts and renewal reminders go here."
            type="email"
            necessityIndicator="optional"
            required
            autoComplete="email"
            spellCheck={false}
            autoCapitalize="none"
            {...field('email')}
          />
          <TextField
            label={labels.taxId}
            hint="VAT, GST or ABN number. Shown on invoices."
            necessityIndicator="optional"
            autoComplete="off"
            className="sm:max-w-80"
            {...field('taxId')}
          />
          <Select
            label={labels.country}
            id="billing-country"
            name="country"
            required
            necessityIndicator="optional"
            value={values.country}
            onValueChange={(v) => {
              set('country')(v);
              setErrors((e) => ({ ...e, country: validate('country', v) }));
            }}
            error={errors.country}
            placeholder="Choose a country"
            className="sm:max-w-80"
            autoComplete="country"
          >
            {countries.map((c) => (
              <SelectItem key={c.value} value={c.value}>
                {c.label}
              </SelectItem>
            ))}
          </Select>
          <TextField label={labels.address} necessityIndicator="optional" required autoComplete="address-line1" {...field('address')} />
          <div className="grid gap-5 sm:grid-cols-2">
            <TextField label={labels.city} necessityIndicator="optional" required autoComplete="address-level2" {...field('city')} />
            <TextField
              label={labels.postcode}
              necessityIndicator="optional"
              required
              autoComplete="postal-code"
              className="sm:max-w-48"
              {...field('postcode')}
            />
          </div>
          <Checkbox label="Email a copy of each invoice to the billing email" defaultChecked name="emailCopy" />
          <div className="flex flex-wrap items-center gap-3 pt-2">
            <Button type="submit" loading={saving} loadingLabel="Saving…">
              Save billing details
            </Button>
            <Button
              variant="ghost"
              onClick={() => {
                setValues(initial);
                setErrors({});
                setSummary([]);
              }}
            >
              Reset
            </Button>
          </div>
        </form>
      </section>
    </div>
  );
}
