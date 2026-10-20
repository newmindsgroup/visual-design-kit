// Version-Timestamp: 2026-10-20 02:52:00 UTC
import { useEffect, useRef, useState } from 'react';
import { Button, type ButtonVariant } from '../components/button';
import { IconArrowRight, IconCopy, IconDownload, IconMore, IconPlus, IconTrash } from '../components/icons';
import { Tooltip } from '../components/tooltip';
import { Example, Kbd, Plate, Section, StateMatrix, Token } from './doc';

const buttonVariants: Array<{ variant: ButtonVariant; label: string; text: string }> = [
  { variant: 'primary', label: 'Primary', text: 'Save' },
  { variant: 'secondary', label: 'Secondary', text: 'Export' },
  { variant: 'ghost', label: 'Ghost', text: 'Preview' },
  { variant: 'danger', label: 'Danger', text: 'Delete' },
];

function AsyncSave() {
  const [state, setState] = useState<'idle' | 'saving' | 'saved'>('idle');
  const timer = useRef<number | undefined>(undefined);
  useEffect(() => () => window.clearTimeout(timer.current), []);
  return (
    <div className="flex flex-wrap items-center gap-3">
      <Button
        loading={state === 'saving'}
        loadingLabel="Saving…"
        onClick={() => {
          setState('saving');
          timer.current = window.setTimeout(() => setState('saved'), 1600);
        }}
      >
        Save changes
      </Button>
      <p role="status" className="text-sm text-muted">
        {state === 'saving' ? 'Saving your changes…' : state === 'saved' ? 'All changes saved.' : ''}
      </p>
    </div>
  );
}

export function ButtonSection() {
  return (
    <Section
      id="button"
      number="01"
      title="Button"
      summary="One command per button, labeled verb plus object. One primary per region; danger only on the final destructive confirmation."
      contract={[
        [
          'Keyboard',
          <>
            <Kbd>Enter</Kbd> and <Kbd>Space</Kbd> activate. Nothing fires on pointer-down.
          </>,
        ],
        [
          'Semantics',
          <>
            Native <Token>button</Token>, <Token>type="button"</Token> by default. <Token>loading</Token> sets{' '}
            <Token>aria-busy</Token> and <Token>aria-disabled</Token>, keeps focus and width, ignores clicks.
          </>,
        ],
        [
          'Tokens',
          <>
            <Token>--button-*</Token> (aliases accent, surface, danger roles), <Token>--focus-ring-*</Token>,{' '}
            <Token>--duration-fast</Token>
          </>,
        ],
      ]}
    >
      <Plate title="States" note="Static renders; hover, focus and pressed forced with data-preview-state">
        <StateMatrix
          states={['Rest', 'Hover', 'Focus', 'Pressed', 'Disabled', 'Loading']}
          rows={buttonVariants.map(({ variant, label, text }) => ({
            label,
            cells: [
              <Button variant={variant}>{text}</Button>,
              <Button variant={variant} data-preview-state="hover">
                {text}
              </Button>,
              <Button variant={variant} data-preview-state="focus">
                {text}
              </Button>,
              <Button variant={variant} data-preview-state="active">
                {text}
              </Button>,
              <Button variant={variant} disabled>
                {text}
              </Button>,
              <Button variant={variant} loading>
                {text}
              </Button>,
            ],
          }))}
        />
      </Plate>

      <div className="grid gap-6 lg:grid-cols-2">
        <Plate title="Sizes" note="sm 32 · md 40 · lg 48px; 44px hit area on touch">
          <div className="grid gap-5">
            <div className="flex flex-wrap items-center gap-3">
              <Button size="sm">Small</Button>
              <Button size="md">Medium</Button>
              <Button size="lg">Large</Button>
            </div>
            <div className="flex flex-wrap items-center gap-3">
              <Button size="sm" variant="secondary" startIcon={<IconPlus />}>
                Add seat
              </Button>
              <Button variant="secondary" startIcon={<IconDownload />}>
                Download
              </Button>
              <Button size="lg" endIcon={<IconArrowRight />}>
                Continue
              </Button>
            </div>
          </div>
        </Plate>
        <Plate title="Icon-only" note="aria-label is required by the type; the tooltip shows it">
          <div className="flex flex-wrap items-center gap-3">
            <Tooltip content="Copy invoice ID" mode="label">
              <Button iconOnly size="sm" variant="ghost" aria-label="Copy invoice ID">
                <IconCopy />
              </Button>
            </Tooltip>
            <Tooltip content="Download PDF" mode="label">
              <Button iconOnly variant="secondary" aria-label="Download PDF">
                <IconDownload />
              </Button>
            </Tooltip>
            <Tooltip content="More actions" mode="label">
              <Button iconOnly variant="ghost" aria-label="More actions">
                <IconMore />
              </Button>
            </Tooltip>
            <Tooltip content="Delete project" mode="label">
              <Button iconOnly size="lg" variant="danger" aria-label="Delete project">
                <IconTrash />
              </Button>
            </Tooltip>
          </div>
        </Plate>
      </div>

      <div className="grid gap-6 lg:grid-cols-2">
        <Plate title="Busy" note="Spinner replaces the start icon, width is locked, status is announced next to it">
          <AsyncSave />
        </Plate>
        <Plate title="As a link" note="asChild keeps the styles on an <a> for navigation">
          <Example>
            <div className="flex flex-wrap items-center gap-3">
              <Button asChild variant="secondary" endIcon={<IconArrowRight />}>
                <a href="./billing.html">Open the billing screen</a>
              </Button>
            </div>
          </Example>
        </Plate>
      </div>
    </Section>
  );
}
