// Version-Timestamp: 2026-10-23 20:10:44 UTC
// Minimal RGBA PNG encoder and a flat bar-chart rasterizer (node:zlib only, no canvas dependency).
// Used by --canva-safe mode, which places charts as images because Canva's PPTX import ignores native charts.
import zlib from 'node:zlib';

const crcTable = (() => {
  const table = new Uint32Array(256);
  for (let n = 0; n < 256; n++) {
    let c = n;
    for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
    table[n] = c >>> 0;
  }
  return table;
})();

function crc32(buf) {
  if (typeof zlib.crc32 === 'function') return zlib.crc32(buf) >>> 0;
  let c = 0xffffffff;
  for (const byte of buf) c = crcTable[(c ^ byte) & 0xff] ^ (c >>> 8);
  return (c ^ 0xffffffff) >>> 0;
}

function chunk(type, data) {
  const len = Buffer.alloc(4);
  len.writeUInt32BE(data.length);
  const body = Buffer.concat([Buffer.from(type, 'ascii'), data]);
  const crc = Buffer.alloc(4);
  crc.writeUInt32BE(crc32(body));
  return Buffer.concat([len, body, crc]);
}

export function encodePng(width, height, rgba) {
  const header = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(width, 0);
  ihdr.writeUInt32BE(height, 4);
  ihdr[8] = 8; // bit depth
  ihdr[9] = 6; // RGBA
  const raw = Buffer.alloc((width * 4 + 1) * height);
  for (let y = 0; y < height; y++) {
    raw[y * (width * 4 + 1)] = 0; // filter: none
    rgba.copy(raw, y * (width * 4 + 1) + 1, y * width * 4, (y + 1) * width * 4);
  }
  return Buffer.concat([
    header,
    chunk('IHDR', ihdr),
    chunk('IDAT', zlib.deflateSync(raw, { level: 9 })),
    chunk('IEND', Buffer.alloc(0)),
  ]);
}

const rgb = (hex) => [0, 2, 4].map((i) => parseInt(hex.slice(i, i + 2), 16));

/**
 * Draws a column chart with a baseline and light gridlines on a transparent background.
 * Labels are NOT rasterized: the deck adds them as real text boxes so they stay editable in Canva.
 * Returns { png, bars } where bars holds each column's box as fractions of the image, for label placement.
 */
export function barChartPng({ values, max, width = 1600, height = 900, colors, highlight = values.length - 1, gridColor, baseColor }) {
  const px = Buffer.alloc(width * height * 4); // transparent
  const fill = (x0, y0, x1, y1, hex) => {
    const [r, g, b] = rgb(hex);
    for (let y = Math.max(0, Math.round(y0)); y < Math.min(height, Math.round(y1)); y++) {
      for (let x = Math.max(0, Math.round(x0)); x < Math.min(width, Math.round(x1)); x++) {
        const i = (y * width + x) * 4;
        px[i] = r;
        px[i + 1] = g;
        px[i + 2] = b;
        px[i + 3] = 255;
      }
    }
  };
  const top = height * 0.04;
  const base = height * 0.98;
  for (let step = 1; step <= 4; step++) {
    const y = base - ((base - top) * step) / 4;
    fill(0, y - 1, width, y + 1, gridColor);
  }
  const slot = width / values.length;
  const barW = slot * 0.56;
  const bars = values.map((value, i) => {
    const h = ((base - top) * value) / max;
    const x0 = slot * i + (slot - barW) / 2;
    fill(x0, base - h, x0 + barW, base, i === highlight ? colors.highlight : colors.rest);
    return { x: x0 / width, y: (base - h) / height, w: barW / width, h: h / height, slot: slot / width };
  });
  fill(0, base, width, base + 4, baseColor);
  return { png: encodePng(width, height, px), bars };
}
