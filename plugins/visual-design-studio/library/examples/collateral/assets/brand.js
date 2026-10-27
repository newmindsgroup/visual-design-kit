// Version-Timestamp: 2026-10-23 20:38:00 UTC
// Browser preview only: ?brand=ember or ?brand=meridian sets data-brand on <html>. Printing never needs this file;
// render_collateral.mjs sets the attribute itself and WeasyPrint reads the attribute written in the HTML.
(function () {
  try {
    var brand = new URLSearchParams(window.location.search).get('brand');
    if (brand === 'ember' || brand === 'meridian') document.documentElement.setAttribute('data-brand', brand);
  } catch (error) {
    /* keep the brand written in the HTML */
  }
})();
