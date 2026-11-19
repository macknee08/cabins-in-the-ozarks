// Mobile nav + photo lightbox. No dependencies.
(() => {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
      toggle.textContent = open ? 'Close' : 'Menu';
    });
    nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
      nav.classList.remove('open'); toggle.setAttribute('aria-expanded', false); toggle.textContent = 'Menu';
    }));
  }

  const lb = document.querySelector('.lightbox');
  if (!lb) return;
  const img = lb.querySelector('img');
  const count = lb.querySelector('.lb-count');
  let set = [], i = 0, last = null;
  const show = () => { img.src = set[i].dataset.full; img.alt = set[i].querySelector('img').alt; count.textContent = `${i + 1} of ${set.length}`; };
  document.querySelectorAll('.gallery').forEach(g => {
    const items = [...g.querySelectorAll('button')];
    items.forEach((b, n) => b.addEventListener('click', () => {
      set = items; i = n; last = b; show(); lb.classList.add('open'); lb.querySelector('.lb-close').focus();
    }));
  });
  const close = () => { lb.classList.remove('open'); img.src = ''; last && last.focus(); };
  const step = d => { i = (i + d + set.length) % set.length; show(); };
  lb.querySelector('.lb-close').addEventListener('click', close);
  lb.querySelector('.lb-prev').addEventListener('click', () => step(-1));
  lb.querySelector('.lb-next').addEventListener('click', () => step(1));
  lb.addEventListener('click', e => { if (e.target === lb) close(); });
  document.addEventListener('keydown', e => {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') step(-1);
    if (e.key === 'ArrowRight') step(1);
  });
})();
