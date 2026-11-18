/* Plate theme behaviour: develop toggle, click-to-enlarge, click-to-expand. No dependencies. */
(function () {
  'use strict';
  var body = document.body;

  // "Develop all plates": remembered between pages.
  var dev = document.getElementById('develop');
  function setDeveloped(on) {
    body.classList.toggle('developed', on);
    if (dev) {
      dev.setAttribute('aria-pressed', on ? 'true' : 'false');
      dev.textContent = on ? 'Return to negatives' : 'Develop all plates';
    }
  }
  var stored = false;
  try { stored = localStorage.getItem('developed') === '1'; } catch (e) {}
  setDeveloped(stored);
  if (dev) dev.addEventListener('click', function () {
    var on = !body.classList.contains('developed');
    setDeveloped(on);
    try { localStorage.setItem('developed', on ? '1' : '0'); } catch (e) {}
  });

  // Lightbox: plates, pinned charts and images inside long-form pages.
  var box = document.getElementById('lightbox');
  if (box && typeof box.showModal === 'function') {
    var img = box.querySelector('img'), cap = box.querySelector('figcaption');
    var prev = box.querySelector('.prev'), next = box.querySelector('.next');
    var items = [], at = 0;
    document.querySelectorAll('.plate, .chart, .prose img').forEach(function (el) {
      var im = el.tagName === 'IMG' ? el : el.querySelector('img');
      if (!im || (el.tagName === 'IMG' && el.closest('a'))) return;
      var fc = el.tagName === 'IMG' ? null : el.querySelector('figcaption');
      var text = fc ? (fc.querySelector('.hand') || fc).textContent : im.alt;
      var i = items.push({ src: im.currentSrc || im.src, alt: im.alt, text: text.trim(), photo: !el.classList.contains('chart') && el.tagName !== 'IMG' || body.classList.contains('negatives') }) - 1;
      if (el.tagName !== 'IMG' && !el.hasAttribute('tabindex')) el.setAttribute('tabindex', '0');
      el.setAttribute('role', 'button');
      el.setAttribute('aria-label', 'Enlarge: ' + (im.alt || text));
      el.addEventListener('click', function (e) { if (!e.target.closest('a')) show(i); });
      el.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); show(i); } });
    });
    function show(i) {
      at = (i + items.length) % items.length;
      var it = items[at];
      img.src = it.src; img.alt = it.alt; img.className = it.photo ? 'photo' : '';
      cap.textContent = it.text;
      prev.hidden = next.hidden = items.length < 2;
      if (!box.open) box.showModal();
    }
    prev.addEventListener('click', function () { show(at - 1); });
    next.addEventListener('click', function () { show(at + 1); });
    box.querySelector('.x').addEventListener('click', function () { box.close(); });
    box.addEventListener('click', function (e) { if (e.target === box || e.target.classList.contains('frame')) box.close(); });
    box.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') show(at - 1);
      if (e.key === 'ArrowRight') show(at + 1);
    });
  }

  // Index cards and research topics: a click anywhere on them opens the detail.
  document.querySelectorAll('[data-expand]').forEach(function (el) {
    var d = el.querySelector('details');
    if (!d) return;
    d.addEventListener('toggle', function () { el.classList.toggle('open', d.open); });
    el.addEventListener('click', function (e) {
      if (e.target.closest('a, summary, .more')) return;
      d.open = !d.open;
    });
  });

  // Publication list filter.
  var list = document.getElementById('publist');
  if (list) {
    var count = document.getElementById('pubcount');
    document.querySelectorAll('.filters button[data-filter]').forEach(function (b) {
      b.addEventListener('click', function () {
        var first = b.dataset.filter === 'first';
        list.classList.toggle('only-first', first);
        document.querySelectorAll('.filters button[data-filter]').forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
        list.querySelectorAll('.yr').forEach(function (y) {
          var n = y.nextElementSibling, any = false;
          while (n && n.classList.contains('pub')) { if (n.classList.contains('first')) any = true; n = n.nextElementSibling; }
          y.classList.toggle('empty', !any);
        });
        if (count) count.textContent = list.querySelectorAll(first ? 'li.pub.first' : 'li.pub').length + ' entries';
      });
    });
  }
})();
