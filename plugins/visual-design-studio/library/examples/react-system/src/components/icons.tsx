// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Original 24px stroke icons (MIT, part of this example). Decorative by default (aria-hidden);
// pass `title` only when the icon is the sole carrier of meaning and has no text next to it.
import type { ComponentProps, ReactNode } from 'react';
import { cx } from '../lib/cx';

export type IconSize = 'sm' | 'md' | 'lg';
/** 'custom' applies no size class; pass your own size utility in className. */
export type IconProps = Omit<ComponentProps<'svg'>, 'children'> & { size?: IconSize | 'custom'; title?: string };

const sizeClass: Record<IconSize, string> = {
  sm: 'size-(--size-icon-sm)',
  md: 'size-(--size-icon-md)',
  lg: 'size-(--size-icon-lg)',
};

function createIcon(name: string, paths: ReactNode, options: { mirror?: boolean } = {}) {
  function Icon({ size = 'md', title, className, ...rest }: IconProps) {
    return (
      <svg
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth={1.75}
        strokeLinecap="round"
        strokeLinejoin="round"
        focusable="false"
        data-icon={name}
        aria-hidden={title ? undefined : true}
        role={title ? 'img' : undefined}
        className={cx('shrink-0', size !== 'custom' && sizeClass[size], options.mirror && 'rtl:-scale-x-100', className)}
        {...rest}
      >
        {title ? <title>{title}</title> : null}
        {paths}
      </svg>
    );
  }
  Icon.displayName = `Icon${name}`;
  return Icon;
}

export const IconCheck = createIcon('Check', <path d="m5 12.5 4.5 4.5L19 7.5" />);
export const IconMinus = createIcon('Minus', <path d="M6 12h12" />);
export const IconX = createIcon('X', <path d="M6.5 6.5l11 11m0-11-11 11" />);
export const IconPlus = createIcon('Plus', <path d="M12 5.5v13M5.5 12h13" />);
export const IconChevronDown = createIcon('ChevronDown', <path d="m6.5 9.5 5.5 5.5 5.5-5.5" />);
export const IconChevronUp = createIcon('ChevronUp', <path d="m6.5 14.5 5.5-5.5 5.5 5.5" />);
export const IconChevronRight = createIcon('ChevronRight', <path d="m9.5 6.5 5.5 5.5-5.5 5.5" />, { mirror: true });
export const IconArrowRight = createIcon('ArrowRight', <path d="M5 12h14m-5.5-5.5L19 12l-5.5 5.5" />, { mirror: true });
export const IconArrowUp = createIcon('ArrowUp', <path d="M12 19V5m-5.5 5.5L12 5l5.5 5.5" />);
export const IconArrowDown = createIcon('ArrowDown', <path d="M12 5v14m-5.5-5.5L12 19l5.5-5.5" />);
export const IconSort = createIcon('Sort', <path d="m8 9.5 4-4 4 4m-8 5 4 4 4-4" />);
export const IconInfo = createIcon(
  'Info',
  <>
    <circle cx="12" cy="12" r="8.5" />
    <path d="M12 11v5.5M12 7.75v.01" />
  </>,
);
export const IconCheckCircle = createIcon(
  'CheckCircle',
  <>
    <circle cx="12" cy="12" r="8.5" />
    <path d="m8.25 12.25 2.5 2.5 5-5.25" />
  </>,
);
export const IconWarning = createIcon(
  'Warning',
  <>
    <path d="M10.3 4.6 3.4 16.8A2 2 0 0 0 5.1 19.8h13.8a2 2 0 0 0 1.7-3L13.7 4.6a2 2 0 0 0-3.4 0Z" />
    <path d="M12 9.5v4M12 16.75v.01" />
  </>,
);
export const IconDanger = createIcon(
  'Danger',
  <>
    <path d="M8.6 3.5h6.8l5.1 5.1v6.8l-5.1 5.1H8.6l-5.1-5.1V8.6Z" />
    <path d="M12 8v4.5M12 15.75v.01" />
  </>,
);
export const IconDownload = createIcon('Download', <path d="M12 4.5v10m-4.5-4.5L12 14.5l4.5-4.5M5 19h14" />);
export const IconCopy = createIcon(
  'Copy',
  <>
    <rect x="8.5" y="8.5" width="11" height="11" rx="2" />
    <path d="M15.5 8.5V6.5a2 2 0 0 0-2-2h-7a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h2" />
  </>,
);
export const IconSearch = createIcon(
  'Search',
  <>
    <circle cx="11" cy="11" r="6.5" />
    <path d="m16 16 3.5 3.5" />
  </>,
);
export const IconCard = createIcon(
  'Card',
  <>
    <rect x="3.5" y="5.5" width="17" height="13" rx="2" />
    <path d="M3.5 10h17M7 15h3" />
  </>,
);
export const IconReceipt = createIcon(
  'Receipt',
  <>
    <path d="M6 3.5h12v17l-2.5-1.5-2 1.5-1.5-1.5-1.5 1.5-2-1.5L6 20.5Z" />
    <path d="M9 8.5h6M9 12h6M9 15.5h3.5" />
  </>,
);
export const IconInbox = createIcon(
  'Inbox',
  <>
    <path d="M4 13.5 6.4 6a2 2 0 0 1 1.9-1.5h7.4A2 2 0 0 1 17.6 6l2.4 7.5" />
    <path d="M4 13.5V18a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-4.5h-4.5l-1 2h-5l-1-2Z" />
  </>,
);
export const IconFolder = createIcon(
  'Folder',
  <path d="M3.5 7.5a2 2 0 0 1 2-2h4l2 2h7a2 2 0 0 1 2 2v7.5a2 2 0 0 1-2 2h-13a2 2 0 0 1-2-2Z" />,
);
export const IconUsers = createIcon(
  'Users',
  <>
    <circle cx="9" cy="8.5" r="3.5" />
    <path d="M3 19.5a6 6 0 0 1 12 0M15.5 5.2a3.5 3.5 0 0 1 0 6.6M17.5 14.3a6 6 0 0 1 3.5 5.2" />
  </>,
);
export const IconBell = createIcon(
  'Bell',
  <path d="M6.5 16.5V11a5.5 5.5 0 0 1 11 0v5.5l1.5 2H5Zm3.5 3.5h4" />,
);
export const IconSettings = createIcon(
  'Settings',
  <>
    <circle cx="12" cy="12" r="3" />
    <path d="M12 3.5v2.25M12 18.25v2.25M3.5 12h2.25M18.25 12h2.25M6 6l1.6 1.6M16.4 16.4 18 18M6 18l1.6-1.6M16.4 7.6 18 6" />
  </>,
);
export const IconExternal = createIcon(
  'External',
  <path d="M13.5 4.5h6v6m0-6-8 8M17.5 13.5v5a1 1 0 0 1-1 1h-11a1 1 0 0 1-1-1v-11a1 1 0 0 1 1-1h5" />,
  { mirror: true },
);
export const IconMore = createIcon(
  'More',
  <path d="M6 12h.01M12 12h.01M18 12h.01" strokeWidth={2.75} />,
);
export const IconTrash = createIcon(
  'Trash',
  <path d="M5 7h14M10 4.5h4M7 7l.8 11.2a1.5 1.5 0 0 0 1.5 1.3h5.4a1.5 1.5 0 0 0 1.5-1.3L17 7M10.25 10.5v5.5M13.75 10.5v5.5" />,
);
export const IconLink = createIcon(
  'Link',
  <path d="M10 14a4 4 0 0 0 5.7 0l2.8-2.8a4 4 0 0 0-5.7-5.7L11.5 6.8M14 10a4 4 0 0 0-5.7 0l-2.8 2.8a4 4 0 0 0 5.7 5.7l1.3-1.3" />,
);
export const IconSparkle = createIcon(
  'Sparkle',
  <path d="M12 4.5c.5 3.6 2.4 5.5 6 6-3.6.5-5.5 2.4-6 6-.5-3.6-2.4-5.5-6-6 3.6-.5 5.5-2.4 6-6Z" />,
);
