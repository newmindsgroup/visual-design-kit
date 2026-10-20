// Version-Timestamp: 2026-10-20 02:52:00 UTC
/** Static interaction states for documentation and visual tests (see system.css custom variants). */
export type PreviewState = 'hover' | 'focus' | 'active' | 'hover focus';

export type Size = 'sm' | 'md' | 'lg';
export type Tone = 'neutral' | 'accent' | 'info' | 'success' | 'warning' | 'danger';
export type StatusTone = Exclude<Tone, 'accent'>;
