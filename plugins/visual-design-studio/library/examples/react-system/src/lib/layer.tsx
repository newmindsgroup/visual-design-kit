// Version-Timestamp: 2026-10-20 02:52:00 UTC
import { createContext, useContext } from 'react';

/**
 * Popovers (select menus, tooltips) render in a portal. Inside a modal they must stack above the modal layer,
 * so DialogContent provides "modal" and popovers pick the matching --z-* token.
 */
export type Layer = 'base' | 'modal';
export const LayerContext = createContext<Layer>('base');

export function usePopoverLayerClass(): string {
  return useContext(LayerContext) === 'modal' ? 'z-modal' : 'z-dropdown';
}
