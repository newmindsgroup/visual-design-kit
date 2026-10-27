// Visual Design Kit, MIT. Part of a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// Safe areas, copied from the kit so the example stays self-contained:
// - 9:16 boxes: skills/print-packaging-social/references/social-formats.md "Safe areas for 9:16"
//   (organic baseline; paid follows Meta Reels ads guidance). Platform overlays change: verify
//   against each platform's current safe-zone template before delivery.
// - 16:9 title-safe 90% and action-safe 93% (SMPTE ST 2046-1), from
//   skills/motion/references/video-and-motion-graphics.md "Safe areas".

export interface Box {
  x: number;
  y: number;
  width: number;
  height: number;
}

export const VERTICAL_SAFE: Record<'organic' | 'paid', Box> = {
  organic: {x: 60, y: 220, width: 880, height: 1280},
  paid: {x: 65, y: 269, width: 855, height: 980},
};

/** A centered box covering `fraction` of the frame width and height. */
export function centeredSafe(width: number, height: number, fraction: number): Box {
  const w = Math.round(width * fraction);
  const h = Math.round(height * fraction);
  return {x: Math.round((width - w) / 2), y: Math.round((height - h) / 2), width: w, height: h};
}

export const titleSafe = (width: number, height: number) => centeredSafe(width, height, 0.9);
export const actionSafe = (width: number, height: number) => centeredSafe(width, height, 0.93);

/** Scale a 1080x1920 safe box to another 9:16 canvas size. */
export function scaleVerticalSafe(box: Box, width: number, height: number): Box {
  const sx = width / 1080;
  const sy = height / 1920;
  return {x: Math.round(box.x * sx), y: Math.round(box.y * sy), width: Math.round(box.width * sx), height: Math.round(box.height * sy)};
}

export function contains(outer: Box, inner: Box): boolean {
  return (
    inner.x >= outer.x &&
    inner.y >= outer.y &&
    inner.x + inner.width <= outer.x + outer.width &&
    inner.y + inner.height <= outer.y + outer.height
  );
}
