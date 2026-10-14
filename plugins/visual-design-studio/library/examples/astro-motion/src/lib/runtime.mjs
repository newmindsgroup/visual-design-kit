// Version-Timestamp: 2026-10-14 11:06:44 AST
export function clamp(value, min, max) {
  return Number.isFinite(value) ? Math.min(max, Math.max(min, value)) : min;
}
export function progress(offset, total, viewport) {
  return total > viewport ? clamp(offset / (total - viewport), 0, 1) : 0;
}
export function canAnimate({ playing = false, visible = false, reduced = false, hidden = false } = {}) {
  return playing && visible && !reduced && !hidden;
}
export function createScope() {
  let disposed = false;
  const cleanups = [];
  return {
    get disposed() { return disposed; },
    add(cleanup) { if (disposed) cleanup(); else cleanups.push(cleanup); return cleanup; },
    listen(target, event, listener, options) {
      target.addEventListener(event, listener, options);
      this.add(() => target.removeEventListener(event, listener, options));
    },
    dispose() {
      if (disposed) return [];
      disposed = true;
      const errors = [];
      for (const cleanup of cleanups.reverse()) { try { cleanup(); } catch (error) { errors.push(error); } }
      cleanups.length = 0;
      return errors;
    },
  };
}

export function frameDelta(now, last) { return clamp((now-last)/1000, 0, .05); }
