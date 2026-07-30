/* ----------------------------------------------------
   YEARBOOK INTERACTIVE SCRIPT (APPLE SCROLL & PROGRESS HEADER)
   CLB Guitar và Bạn - 5th Anniversary (2021 - 2026)
   ---------------------------------------------------- */

document.addEventListener('DOMContentLoaded', () => {
  initMemberSearch();
  initGalleryFilter();
  initLightbox();
  initScrollProgressAndSectionTracker();
  initAppleScrollReveal();
});

/* Member Search & Filter */
function initMemberSearch() {
  const searchInput = document.getElementById('member-search');
  if (!searchInput) return;

  const memberCards = document.querySelectorAll('.js-member-card');

  searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase().trim();

    memberCards.forEach(card => {
      const name = card.getAttribute('data-name') || '';
      const nickname = card.getAttribute('data-nickname') || '';
      const song = card.getAttribute('data-song') || '';

      if (name.includes(query) || nickname.includes(query) || song.includes(query)) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  });
}

/* Gallery Category Filter */
function initGalleryFilter() {
  const filterBtns = document.querySelectorAll('.js-gallery-filter');
  const galleryItems = document.querySelectorAll('.js-gallery-item');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const cat = btn.getAttribute('data-category');
      galleryItems.forEach(item => {
        const itemCat = item.getAttribute('data-category');
        if (cat === 'all' || itemCat === cat) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
}

/* Lightbox Modal */
function initLightbox() {
  const lightbox = document.getElementById('lightbox-modal');
  const lightboxImg = document.getElementById('lightbox-img');
  const lightboxCaption = document.getElementById('lightbox-caption');
  const closeBtn = document.querySelector('.lightbox-close');

  if (!lightbox) return;

  document.querySelectorAll('.js-lightbox-trigger').forEach(item => {
    item.addEventListener('click', () => {
      const src = item.getAttribute('data-src');
      const caption = item.getAttribute('data-caption') || '';
      lightboxImg.src = src;
      lightboxCaption.textContent = caption;
      lightbox.classList.add('active');
    });
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', () => {
      lightbox.classList.remove('active');
    });
  }

  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) {
      lightbox.classList.remove('active');
    }
  });
}

/* Scroll Progress Fill & Current Section Indicator in Header */
function initScrollProgressAndSectionTracker() {
  const progressFill = document.getElementById('progress-bar-fill');
  const sectionTitleEl = document.getElementById('reading-section-title');
  const sections = document.querySelectorAll('section[id]');

  window.addEventListener('scroll', () => {
    // Fill Progress Bar
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progressPercent = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    if (progressFill) {
      progressFill.style.width = progressPercent.toFixed(2) + '%';
    }

    // Update Current Section Title
    let currentSectionName = 'Bìa Kỷ Yếu';
    const scrollPos = scrollTop + 250;

    sections.forEach(sec => {
      if (scrollPos >= sec.offsetTop && scrollPos < sec.offsetTop + sec.offsetHeight) {
        const titleAttr = sec.getAttribute('data-section-title');
        if (titleAttr) {
          currentSectionName = titleAttr;
        }
      }
    });

    if (sectionTitleEl) {
      sectionTitleEl.textContent = currentSectionName;
    }
  });
}

/* Apple-Style Smooth Intersection Observer Scroll Reveal */
function initAppleScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal');

  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -80px 0px',
    threshold: 0.12
  };

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      }
    });
  }, observerOptions);

  revealElements.forEach(el => observer.observe(el));
}
