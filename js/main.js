document.addEventListener('DOMContentLoaded', () => {
  initPageLoader();
  initScrollProgress();
  initHeaderScroll();
  initScrollReveal();
  initPageTransitions();
  initMobileNav();
  initBackToTop();
  initContactForm();
  initHeroParallax();
});

/* ── Loading Progress Helper ── */
function animateLoaderProgress(fill, from, to, duration, onDone) {
  if (!fill) { if (onDone) onDone(); return; }
  const start = performance.now();
  const step = (now) => {
    const t = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - t, 3);
    fill.style.width = `${from + (to - from) * eased}%`;
    if (t < 1) {
      requestAnimationFrame(step);
    } else if (onDone) {
      onDone();
    }
  };
  requestAnimationFrame(step);
}

function showLoader() {
  const loader = document.querySelector('.page-loader');
  const fill = document.querySelector('.loader-bar-fill');
  if (loader) loader.classList.remove('hidden');
  if (fill) fill.style.width = '0%';
  document.body.classList.add('is-loading');
  return { loader, fill };
}

function hideLoader(loader, fill) {
  animateLoaderProgress(fill, parseFloat(fill?.style.width) || 90, 100, 200, () => {
    setTimeout(() => {
      if (loader) loader.classList.add('hidden');
      document.body.classList.remove('is-loading');
    }, 250);
  });
}

/* ── Page Loader ── */
function initPageLoader() {
  const { loader, fill } = showLoader();
  document.body.classList.add('page-enter');

  let progress = 0;
  const tick = setInterval(() => {
    if (progress < 85) {
      progress += Math.random() * 12 + 4;
      if (fill) fill.style.width = `${Math.min(progress, 85)}%`;
    }
  }, 180);

  const finish = () => {
    clearInterval(tick);
    hideLoader(loader, fill);
  };

  window.addEventListener('load', () => setTimeout(finish, 300));
  setTimeout(finish, 3000);
}

/* ── Scroll Progress Bar ── */
function initScrollProgress() {
  const bar = document.querySelector('.scroll-progress');
  if (!bar) return;

  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    bar.style.width = `${progress}%`;
  }, { passive: true });
}

/* ── Header shrink on scroll ── */
function initHeaderScroll() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  const onScroll = () => {
    header.classList.toggle('scrolled', window.scrollY > 40);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* ── Scroll Reveal (loading skeleton) ── */
function initScrollReveal() {
  const selectors = [
    '.reveal', '.reveal-left', '.reveal-right', '.reveal-scale',
    'article', '.card', '.section', '.mission-block',
    '.step', '.benefit', '.point', '.job-card', '.industry-item',
    '.info-table', '.access-box', '.contact-card', '.hero-content',
    'h1',
  ];

  const seen = new Set();
  document.querySelectorAll(selectors.join(',')).forEach((el) => {
    if (seen.has(el)) return;
    seen.add(el);
    if (!el.classList.contains('reveal') &&
        !el.classList.contains('reveal-left') &&
        !el.classList.contains('reveal-right') &&
        !el.classList.contains('reveal-scale')) {
      el.classList.add('reveal');
    }
    if (el.classList.contains('card') && !el.dataset.delay) {
      const cards = [...el.parentElement?.querySelectorAll('.card') || []];
      const idx = cards.indexOf(el);
      if (idx >= 0) el.dataset.delay = String(Math.min(idx + 1, 8));
    }
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const delay = parseInt(el.dataset.delay || '0', 10) * 120;
        setTimeout(() => {
          el.classList.add('revealed');
        }, delay + 300);
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });

  document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale')
    .forEach(el => observer.observe(el));
}

/* ── Page Transitions (loading screen) ── */
function initPageTransitions() {
  const isInternal = (href) => {
    if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) return false;
    try {
      const url = new URL(href, window.location.href);
      return url.origin === window.location.origin && url.pathname.endsWith('.html');
    } catch { return false; }
  };

  document.querySelectorAll('a[href]').forEach(link => {
    if (!isInternal(link.getAttribute('href'))) return;

    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (e.metaKey || e.ctrlKey || e.shiftKey) return;

      e.preventDefault();
      const { loader, fill } = showLoader();
      document.body.classList.remove('page-enter');

      animateLoaderProgress(fill, 0, 70, 350);
      setTimeout(() => {
        animateLoaderProgress(fill, 70, 100, 300, () => {
          setTimeout(() => { window.location.href = href; }, 150);
        });
      }, 350);
    });
  });
}

/* ── Mobile Nav ── */
function initMobileNav() {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.main-nav');
  if (!toggle || !nav) return;

  toggle.addEventListener('click', () => {
    nav.classList.toggle('open');
    toggle.textContent = nav.classList.contains('open') ? '✕' : '☰';
  });

  nav.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      nav.classList.remove('open');
      toggle.textContent = '☰';
    });
  });
}

/* ── Back to Top ── */
function initBackToTop() {
  const btn = document.querySelector('.back-to-top');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    btn.classList.toggle('visible', window.scrollY > 400);
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* ── Contact Form ── */
function initContactForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const msg = document.getElementById('form-success');
    if (msg) {
      msg.style.display = 'block';
      msg.classList.add('reveal', 'revealed');
      form.reset();
      msg.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  });
}

/* ── Hero subtle parallax ── */
function initHeroParallax() {
  const hero = document.querySelector('.hero');
  if (!hero) return;

  const observer = new IntersectionObserver(([entry]) => {
    hero.classList.toggle('in-view', entry.isIntersecting);
  }, { threshold: 0.1 });
  observer.observe(hero);

  window.addEventListener('scroll', () => {
    const img = hero.querySelector('.hero-image');
    if (!img) return;
    const rect = hero.getBoundingClientRect();
    if (rect.bottom > 0 && rect.top < window.innerHeight) {
      const offset = rect.top * 0.15;
      img.style.transform = `scale(1.05) translateY(${offset}px)`;
    }
  }, { passive: true });
}
