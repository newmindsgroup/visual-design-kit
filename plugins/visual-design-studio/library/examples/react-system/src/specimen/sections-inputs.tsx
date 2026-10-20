// Version-Timestamp: 2026-10-20 02:52:00 UTC
import { useState, type FocusEvent } from 'react';
import { Badge } from '../components/badge';
import { Checkbox } from '../components/checkbox';
import { IconSearch } from '../components/icons';
import { Radio, RadioCard, RadioGroup, SegmentedControl, SegmentedItem } from '../components/radio-group';
import { Select, SelectGroup, SelectItem, SelectSeparator } from '../components/select';
import { Switch } from '../components/switch';
import { TextField } from '../components/text-field';
import { countries } from '../shared/data';
import { Example, Kbd, Plate, Section, StateMatrix, Token } from './doc';

const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function ValidatedFields() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [touched, setTouched] = useState<Record<string, boolean>>({});
  const blur = (event: FocusEvent<HTMLInputElement>) => setTouched((t) => ({ ...t, [event.target.name]: true }));
  const nameError = touched.workspace && !name.trim() ? 'Enter a workspace name' : undefined;
  const emailError =
    touched.email && !email.trim()
      ? 'Enter a billing email address'
      : touched.email && !emailPattern.test(email)
        ? 'Enter an email address in the correct format, like name@example.com'
        : undefined;
  return (
    <div className="grid gap-5 sm:grid-cols-2">
      <TextField
        label="Workspace name"
        name="workspace"
        required
        necessityIndicator="optional"
        value={name}
        onValueChange={setName}
        onBlur={blur}
        error={nameError}
        autoComplete="organization"
      />
      <TextField
        label="Billing email"
        name="email"
        type="email"
        required
        necessityIndicator="optional"
        hint="Receipts and renewal reminders go here."
        value={email}
        onValueChange={setEmail}
        onBlur={blur}
        error={emailError}
        autoComplete="email"
        spellCheck={false}
        autoCapitalize="none"
      />
      <TextField label="Website" name="website" necessityIndicator="optional" startAdornment="https://" placeholder="harbor.studio" inputMode="url" />
      <TextField label="Seats" name="seats" necessityIndicator="optional" inputMode="numeric" defaultValue="18" endAdornment="seats" inputClassName="tabular-nums" />
    </div>
  );
}

export function TextFieldSection() {
  return (
    <Section
      id="text-field"
      number="02"
      title="Text field"
      summary="Visible label above the input, hint before the field, error below it. Validate on blur, re-validate on every edit once in error."
      contract={[
        ['Keyboard', <>Native text editing, IME composition, paste and autofill are never blocked.</>],
        [
          'Semantics',
          <>
            <Token>label for</Token>; hint and error joined in <Token>aria-describedby</Token>; <Token>aria-invalid</Token> with
            an icon and text, never color alone.
          </>,
        ],
        [
          'Tokens',
          <>
            <Token>--input-*</Token> (border is <Token>border-strong</Token>, 3:1), <Token>--color-danger-fg</Token>, 16px text so
            iOS does not zoom
          </>,
        ],
      ]}
    >
      <Plate title="States" note="Error keeps the focus ring visible on top of the danger border">
        <StateMatrix
          states={['Empty', 'Hover', 'Focus', 'Filled', 'Invalid', 'Disabled', 'Read-only']}
          rows={[
            {
              label: 'Field',
              cells: [
                <TextField label="Company" placeholder="Harbor Studio" />,
                <TextField label="Company" placeholder="Harbor Studio" data-preview-state="hover" />,
                <TextField label="Company" defaultValue="Harbor" data-preview-state="focus" />,
                <TextField label="Company" defaultValue="Harbor Studio" />,
                <TextField label="Company" defaultValue="" error="Enter a company name" />,
                <TextField label="Company" defaultValue="Harbor Studio" disabled />,
                <TextField label="Company" defaultValue="Harbor Studio" readOnly />,
              ],
            },
          ]}
        />
      </Plate>
      <Plate title="Validation, hints and adornments" note="Tab out of a required field to see its error">
        <ValidatedFields />
      </Plate>
      <Plate title="Sizes" note="Shares heights with Button so inputs and buttons align in one row">
        <div className="grid gap-4 sm:grid-cols-3">
          <TextField size="sm" label="Small (dense tools)" placeholder="Search" startAdornment={<IconSearch />} />
          <TextField size="md" label="Medium (default)" placeholder="Search" startAdornment={<IconSearch />} />
          <TextField size="lg" label="Large (touch-first)" placeholder="Search" startAdornment={<IconSearch />} />
        </div>
      </Plate>
    </Section>
  );
}

export function SelectSection() {
  const [country, setCountry] = useState<string>('');
  return (
    <Section
      id="select"
      number="03"
      title="Select"
      summary="One of about 6-15 options. For longer or searchable lists use a combobox; for 2-5 visible options use radios."
      contract={[
        [
          'Keyboard',
          <>
            <Kbd>Space</Kbd>, <Kbd>Enter</Kbd> or <Kbd>↓</Kbd> opens; arrows and typeahead move; <Kbd>Enter</Kbd> selects;{' '}
            <Kbd>Esc</Kbd> closes and returns focus.
          </>,
        ],
        [
          'Semantics',
          <>
            Radix Select: <Token>combobox</Token> trigger with <Token>listbox</Token>; label, hint and error wired like Text field;
            hidden native select submits <Token>name</Token>.
          </>,
        ],
        [
          'Tokens',
          <>
            Trigger reuses <Token>--input-*</Token>; menu <Token>bg-surface-raised</Token>, <Token>shadow-md</Token>,{' '}
            <Token>z-dropdown</Token> (<Token>z-modal</Token> inside dialogs)
          </>,
        ],
      ]}
    >
      <Plate title="States">
        <StateMatrix
          states={['Placeholder', 'Hover', 'Focus', 'Invalid', 'Disabled']}
          rows={[
            {
              label: 'Trigger',
              cells: [
                <Select label="Country" placeholder="Choose a country">
                  <SelectItem value="ie">Ireland</SelectItem>
                </Select>,
                <Select label="Country" placeholder="Choose a country" data-preview-state="hover">
                  <SelectItem value="ie">Ireland</SelectItem>
                </Select>,
                <Select label="Country" defaultValue="ie" data-preview-state="focus">
                  <SelectItem value="ie">Ireland</SelectItem>
                </Select>,
                <Select label="Country" placeholder="Choose a country" error="Choose a country">
                  <SelectItem value="ie">Ireland</SelectItem>
                </Select>,
                <Select label="Country" defaultValue="ie" disabled>
                  <SelectItem value="ie">Ireland</SelectItem>
                </Select>,
              ],
            },
          ]}
        />
      </Plate>
      <Plate title="Live" note="Open with the keyboard and type a letter to jump">
        <div className="grid gap-5 sm:grid-cols-2">
          <Select
            label="Billing country"
            hint="Sets tax and the invoice currency."
            placeholder="Choose a country"
            value={country}
            onValueChange={setCountry}
            required
            necessityIndicator="required"
            autoComplete="country"
            name="country"
          >
            {countries.map((c) => (
              <SelectItem key={c.value} value={c.value}>
                {c.label}
              </SelectItem>
            ))}
          </Select>
          <Select label="Invoice delivery" defaultValue="email">
            <SelectGroup label="Automatic">
              <SelectItem value="email" description="PDF attached, sent on the 1st">
                Email
              </SelectItem>
              <SelectItem value="portal" description="Download from the billing portal">
                Portal only
              </SelectItem>
            </SelectGroup>
            <SelectSeparator />
            <SelectGroup label="Manual">
              <SelectItem value="post" disabled description="Not available on the Team plan">
                Post
              </SelectItem>
            </SelectGroup>
          </Select>
        </div>
      </Plate>
    </Section>
  );
}

function NotificationGroup() {
  const items = [
    { id: 'invoices', label: 'Invoices and receipts' },
    { id: 'renewals', label: 'Renewal reminders' },
    { id: 'usage', label: 'Usage alerts' },
  ];
  const [checked, setChecked] = useState<Record<string, boolean>>({ invoices: true, renewals: false, usage: true });
  const count = Object.values(checked).filter(Boolean).length;
  const all = count === items.length ? true : count === 0 ? false : 'indeterminate';
  return (
    <fieldset className="m-0 grid gap-3 border-0 p-0">
      <legend className="mb-3 text-sm font-medium text-default">Email me about</legend>
      <Checkbox
        label="All billing email"
        checked={all}
        onCheckedChange={(value) => setChecked(Object.fromEntries(items.map((i) => [i.id, value === true])))}
      />
      <div className="grid gap-3 ps-8">
        {items.map((item) => (
          <Checkbox
            key={item.id}
            label={item.label}
            checked={checked[item.id]}
            onCheckedChange={(value) => setChecked((c) => ({ ...c, [item.id]: value === true }))}
          />
        ))}
      </div>
    </fieldset>
  );
}

export function CheckboxSection() {
  return (
    <Section
      id="checkbox"
      number="04"
      title="Checkbox"
      summary="Independent on/off choices, or agreeing to terms. A parent checkbox shows the mixed state when only some children are on."
      contract={[
        [
          'Keyboard',
          <>
            <Kbd>Space</Kbd> toggles. Clicking the label toggles too.
          </>,
        ],
        [
          'Semantics',
          <>
            Radix <Token>checkbox</Token> role with <Token>aria-checked="mixed"</Token>; 20px box in a 24px target (44px on
            touch); description linked.
          </>,
        ],
        [
          'Tokens',
          <>
            Box <Token>--input-border</Token>; checked <Token>bg-accent</Token> with <Token>text-on-accent</Token>; check
            mark is the non-color cue
          </>,
        ],
      ]}
    >
      <Plate title="States">
        <StateMatrix
          states={['Unchecked', 'Checked', 'Mixed', 'Hover', 'Focus', 'Invalid', 'Disabled']}
          rows={[
            {
              label: 'Checkbox',
              cells: [
                <Checkbox label="Option" />,
                <Checkbox label="Option" defaultChecked />,
                <Checkbox label="Option" checked="indeterminate" />,
                <Checkbox label="Option" data-preview-state="hover" />,
                <Checkbox label="Option" defaultChecked data-preview-state="focus" />,
                <Checkbox label="Option" invalid />,
                <Checkbox label="Option" defaultChecked disabled />,
              ],
            },
          ]}
        />
      </Plate>
      <div className="grid gap-6 lg:grid-cols-2">
        <Plate title="Group with a parent">
          <NotificationGroup />
        </Plate>
        <Plate title="With description and error">
          <div className="grid gap-5">
            <Checkbox
              label="Send a copy of every invoice to accounts@harbor.studio"
              description="Copies go out on the same day as the original."
              defaultChecked
            />
            <Checkbox label="I accept the updated Data Processing Agreement" required error="Accept the agreement to continue" />
          </div>
        </Plate>
      </div>
    </Section>
  );
}

export function SwitchSection() {
  return (
    <Section
      id="switch"
      number="05"
      title="Switch"
      summary="A setting that takes effect the moment it changes. Inside a form with a Save button, use a checkbox instead."
      contract={[
        [
          'Keyboard',
          <>
            <Kbd>Space</Kbd> and <Kbd>Enter</Kbd> toggle.
          </>,
        ],
        [
          'Semantics',
          <>
            Radix <Token>switch</Token> role, states on and off; label and description linked; thumb moves with the text
            direction.
          </>,
        ],
        [
          'Tokens',
          <>
            Off: <Token>border-strong</Token> track and thumb; on: <Token>bg-accent</Token> with an{' '}
            <Token>fg-on-accent</Token> thumb and check mark
          </>,
        ],
      ]}
    >
      <Plate title="States">
        <StateMatrix
          states={['Off', 'On', 'Hover', 'Focus', 'Disabled off', 'Disabled on']}
          rows={[
            {
              label: 'Switch',
              cells: [
                <Switch label="Alerts" labelPlacement="end" />,
                <Switch label="Alerts" labelPlacement="end" defaultChecked />,
                <Switch label="Alerts" labelPlacement="end" data-preview-state="hover" />,
                <Switch label="Alerts" labelPlacement="end" defaultChecked data-preview-state="focus" />,
                <Switch label="Alerts" labelPlacement="end" disabled />,
                <Switch label="Alerts" labelPlacement="end" defaultChecked disabled />,
              ],
            },
          ]}
        />
      </Plate>
      <Plate title="Settings list" bodyClassName="p-0 sm:p-0">
        <div className="divide-y divide-subtle">
          <Switch className="px-5 py-4 sm:px-6" label="Renewal reminders" description="Email the billing contact 7 days before each renewal." defaultChecked />
          <Switch className="px-5 py-4 sm:px-6" label="Seat limit alerts" description="Notify admins when 90% of seats are in use." />
          <Switch
            className="px-5 py-4 sm:px-6"
            label="Failed payment alerts"
            description="Always on for workspace owners. Change who is an owner in Members."
            defaultChecked
            disabled
          />
        </div>
      </Plate>
    </Section>
  );
}

export function RadioSection() {
  const [cycle, setCycle] = useState('annual');
  return (
    <Section
      id="radio-group"
      number="06"
      title="Radio group"
      summary="One choice from 2-5 options that people should compare. Radio cards for options that need a sentence; segmented control for views and modes."
      contract={[
        [
          'Keyboard',
          <>
            <Kbd>Tab</Kbd> enters at the checked option; arrows move and select (mirrored in RTL); <Kbd>Tab</Kbd> leaves.
          </>,
        ],
        [
          'Semantics',
          <>
            Radix <Token>radiogroup</Token> named by its visible label, one tab stop, <Token>required</Token> and error
            supported.
          </>,
        ],
        [
          'Tokens',
          <>
            Circle <Token>--input-border</Token>; selected <Token>border-accent</Token> plus dot; card selected{' '}
            <Token>bg-accent-subtle</Token> with a 2px edge
          </>,
        ],
      ]}
    >
      <Plate title="States">
        <StateMatrix
          states={['Unselected', 'Selected', 'Hover', 'Focus', 'Disabled']}
          rows={[
            {
              label: 'Radio',
              cells: [
                <RadioGroup label="State" labelVisible={false} defaultValue="">
                  <Radio value="a" label="Option" />
                </RadioGroup>,
                <RadioGroup label="State" labelVisible={false} defaultValue="a">
                  <Radio value="a" label="Option" />
                </RadioGroup>,
                <RadioGroup label="State" labelVisible={false} defaultValue="">
                  <Radio value="a" label="Option" data-preview-state="hover" />
                </RadioGroup>,
                <RadioGroup label="State" labelVisible={false} defaultValue="a">
                  <Radio value="a" label="Option" data-preview-state="focus" />
                </RadioGroup>,
                <RadioGroup label="State" labelVisible={false} defaultValue="a" disabled>
                  <Radio value="a" label="Option" />
                </RadioGroup>,
              ],
            },
          ]}
        />
      </Plate>
      <div className="grid gap-6 lg:grid-cols-2">
        <Plate title="Vertical with descriptions">
          <RadioGroup label="Payment method" defaultValue="card" hint="You can change this before each renewal.">
            <Radio value="card" label="Card ending 4242" description="Visa, expires 10/2026" />
            <Radio value="invoice" label="Bank transfer on invoice" description="Net 30 terms, available on annual plans" />
            <Radio value="paypal" label="PayPal" description="Not available in your region" disabled />
          </RadioGroup>
        </Plate>
        <Plate title="Horizontal, required, with error">
          <RadioGroup label="Billing cycle" orientation="horizontal" required necessityIndicator="required" error="Choose a billing cycle">
            <Radio value="monthly" label="Monthly" />
            <Radio value="annual" label="Annual" />
          </RadioGroup>
        </Plate>
      </div>
      <div className="grid gap-6 lg:grid-cols-2">
        <Plate title="Radio cards">
          <RadioGroup label="Plan" defaultValue="team">
            <RadioCard value="starter" label="Starter" description="Up to 10 seats, 50 GB storage." meta="$12 / seat" />
            <RadioCard value="team" label="Team" description="Up to 50 seats, SSO and audit log." meta="$20 / seat" badge={<Badge tone="accent" size="sm">Current</Badge>} />
            <RadioCard value="business" label="Business" description="Unlimited seats, SCIM, priority support." meta="$32 / seat" />
          </RadioGroup>
        </Plate>
        <Plate title="Segmented control" note="Same radiogroup semantics, immediate effect">
          <Example>
            <SegmentedControl label="Billing cycle" value={cycle} onValueChange={setCycle}>
              <SegmentedItem value="monthly">Monthly</SegmentedItem>
              <SegmentedItem value="annual">Annual</SegmentedItem>
            </SegmentedControl>
            <p className="text-sm text-muted" aria-live="polite">
              {cycle === 'annual' ? 'Annual billing: $20 per seat per month, billed yearly.' : 'Monthly billing: $24 per seat per month.'}
            </p>
          </Example>
        </Plate>
      </div>
    </Section>
  );
}
