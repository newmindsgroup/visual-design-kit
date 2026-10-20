// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Type-level tests, checked by `npm run typecheck` (part of `npm test`). Each @ts-expect-error must stay an error.
import { Button } from '../src/components/button';
import { Checkbox } from '../src/components/checkbox';
import { IconCopy } from '../src/components/icons';
import { TextField } from '../src/components/text-field';

export const iconButton = (
  <Button iconOnly aria-label="Copy invoice ID">
    <IconCopy />
  </Button>
);

export const iconButtonWithoutName = (
  // @ts-expect-error icon-only buttons must have an aria-label
  <Button iconOnly>
    <IconCopy />
  </Button>
);

// @ts-expect-error variant is a closed set: primary, secondary, ghost, danger
export const unknownVariant = <Button variant="tertiary">Save</Button>;

// @ts-expect-error size is a closed set: sm, md, lg
export const unknownSize = <Button size="xl">Save</Button>;

// @ts-expect-error a checkbox needs a visible label or an aria-label
export const unnamedCheckbox = <Checkbox />;

export const tableCheckbox = <Checkbox aria-label="Select INV-2048" />;

// @ts-expect-error text fields always have a visible label prop
export const unlabeledField = <TextField placeholder="Email" />;
