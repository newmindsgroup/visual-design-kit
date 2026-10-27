// Visual Design Kit, MIT. Part of a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// The one place that names the token file. Inside the kit it reads the generated
// library/tokens/dist/tokens.resolved.json directly, so brand and mode always match the kit build.
// In a copied project, point this import at your own tokens.resolved.json (same format).
import resolved from '../../../../tokens/dist/tokens.resolved.json';
import type {ResolvedTokens} from './theme.ts';

export const TOKENS = resolved as unknown as ResolvedTokens;
export const BRANDS = Object.keys(TOKENS.values);
export const MODES = Object.keys(TOKENS.modes);
