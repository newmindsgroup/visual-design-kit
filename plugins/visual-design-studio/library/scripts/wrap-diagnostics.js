// Version-Timestamp: 2026-09-11T19:34:00-04:00
// Run in the target page; read-only inspection, no network or mutation.
window.inspectTextWrapping = async function(selector = '[data-wrap]') {
  await document.fonts.ready;
  return [...document.querySelectorAll(selector)].map((element, index) => {
    const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT);
    const lines = new Map(); let node;
    while ((node = walker.nextNode())) {
      for (const match of node.textContent.matchAll(/\S+/gu)) {
        const range = document.createRange();
        range.setStart(node, match.index); range.setEnd(node, match.index + match[0].length);
        for (const rect of range.getClientRects()) {
          if (!rect.width || !rect.height) continue;
          const key = Math.round(rect.top / 2) * 2;
          if (!lines.has(key)) lines.set(key, []);
          lines.get(key).push(match[0]);
        }
      }
    }
    const ordered = [...lines.entries()].sort((a,b)=>a[0]-b[0]);
    return {index, text:element.textContent.trim(), lines:ordered.map(x=>x[1]),
      orphanCandidate:ordered.length>1 && ordered.at(-1)[1].length===1,
      overflow:element.scrollWidth>element.clientWidth+1,
      scope:'Whitespace-based review candidates, not typographic acceptance'};
  });
};
