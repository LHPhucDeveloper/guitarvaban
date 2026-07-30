import json, os, html, re

def build_all():
    with open('bqt_data.json', 'r', encoding='utf-8') as f:
        bqt_data = json.load(f)

    with open('sec6_data.json', 'r', encoding='utf-8') as f:
        sec6_data = json.load(f)

    with open('stories_data.json', 'r', encoding='utf-8') as f:
        stories_data = json.load(f)

    with open('gallery_data.json', 'r', encoding='utf-8') as f:
        gallery_data = json.load(f)

    print("Generating updated styles.css...")
    generate_styles_css()

    print("Generating updated script.js...")
    generate_script_js()

    print("Generating updated index.html...")
    generate_index_html(bqt_data, sec6_data, stories_data, gallery_data)

    print("Generating updated README.md...")
    generate_readme_md()

    print("All files updated successfully!")

def generate_styles_css():
    css_content = """/* ----------------------------------------------------
   YEARBOOK DESIGN SYSTEM & EDITORIAL STYLES (APPLE SCROLL & VIETNAMESE TYPO)
   CLB Guitar và Bạn - 5th Anniversary (2021 - 2026)
   ---------------------------------------------------- */

:root {
  /* Color Tokens - Default Dark Warm Editorial Theme */
  --bg-primary: #0b090e;
  --bg-secondary: #131019;
  --bg-card: #1b1724;
  --bg-paper: #221d2e;
  --text-main: #f7f6f9;
  --text-muted: #ad07bf; /* replaced later with clean muted */
  --text-muted: #aa9ebc;
  --text-dim: #7f7494;
  
  --accent-gold: #d4af37;
  --accent-gold-light: #f7e7b4;
  --accent-gold-dark: #aa8825;
  --accent-warm: #e07a5f;
  --accent-coral: #f4a261;
  --accent-emerald: #2a9d8f;
  
  --border-light: rgba(212, 175, 55, 0.18);
  --border-subtle: rgba(255, 255, 255, 0.08);
  --shadow-soft: 0 12px 35px rgba(0, 0, 0, 0.4);
  --shadow-glow: 0 0 30px rgba(212, 175, 55, 0.25);

  /* Vietnamese Typography System */
  --font-serif: 'Cormorant Garamond', 'Lora', Georgia, serif;
  --font-sans: 'Be Vietnam Pro', 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-signature: 'Caveat', cursive;
  
  /* Spacing & Sizing */
  --radius-sm: 8px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-full: 9999px;
  --apple-ease: cubic-bezier(0.16, 1, 0.3, 1);
  --transition: all 0.4s var(--apple-ease);
}

/* Light Magazine Theme Overrides */
[data-theme="light"] {
  --bg-primary: #fdfbf7;
  --bg-secondary: #f6f1ea;
  --bg-card: #ffffff;
  --bg-paper: #fcf9f4;
  --text-main: #1c1a22;
  --text-muted: #575266;
  --text-dim: #8b849b;
  
  --border-light: rgba(170, 136, 37, 0.22);
  --border-subtle: rgba(0, 0, 0, 0.06);
  --shadow-soft: 0 10px 30px rgba(0, 0, 0, 0.06);
  --shadow-glow: 0 0 20px rgba(212, 175, 55, 0.18);
}

/* Base Resets */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  font-size: 16px;
  background-color: var(--bg-primary);
  color: var(--text-main);
}

body {
  font-family: var(--font-sans);
  line-height: 1.85;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
  overflow-x: hidden;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
  object-fit: cover;
}

a {
  color: inherit;
  text-decoration: none;
  transition: var(--transition);
}

button {
  font-family: inherit;
  cursor: pointer;
  border: none;
  background: none;
}

/* Typographic Hierarchy */
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-serif);
  font-weight: 700;
  line-height: 1.25;
  color: var(--text-main);
}

h1 { font-size: clamp(2.5rem, 5.5vw, 4.8rem); letter-spacing: -0.02em; }
h2 { font-size: clamp(2rem, 3.8vw, 3.2rem); letter-spacing: -0.01em; }
h3 { font-size: clamp(1.4rem, 2.2vw, 2.1rem); }
h4 { font-size: clamp(1.15rem, 1.6vw, 1.4rem); }

.subtitle {
  font-family: var(--font-sans);
  font-size: 0.95rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: var(--accent-gold);
  margin-bottom: 0.5rem;
}

.text-gold { color: var(--accent-gold); }
.text-warm { color: var(--accent-warm); }

/* Text Justification & Alignment for Magazine Feel */
.editorial-body p,
.story-content p,
.foreword-section p,
.about-cards p,
.closing-card p {
  text-align: justify;
  text-justify: inter-word;
  hyphens: auto;
  margin-bottom: 1.5rem;
  font-size: 1.05rem;
  color: var(--text-main);
  line-height: 1.85;
}

/* Drop Caps for Editorial Stories & Foreword */
.editorial-body p:first-of-type::first-letter,
.story-content p:first-of-type::first-letter {
  font-family: var(--font-serif);
  font-size: 4.2rem;
  float: left;
  line-height: 0.75;
  padding-top: 4px;
  padding-right: 14px;
  padding-bottom: 4px;
  color: var(--accent-gold);
  font-weight: 700;
}

/* Pull Quotes */
.pull-quote {
  font-family: var(--font-serif);
  font-size: 1.4rem;
  font-style: italic;
  color: var(--accent-gold-light);
  border-left: 4px solid var(--accent-gold);
  padding: 1.25rem 1.75rem;
  margin: 2.25rem 0;
  background: rgba(212, 175, 55, 0.06);
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  text-align: left !important;
}

[data-theme="light"] .pull-quote {
  color: #7a5c0d;
}

/* Layout Containers */
.container {
  width: 90%;
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 1rem;
}

.section {
  padding: 7rem 0;
  position: relative;
}

.section-header {
  text-align: center;
  max-width: 800px;
  margin: 0 auto 4.5rem auto;
}

.section-header p {
  color: var(--text-muted);
  font-size: 1.15rem;
  margin-top: 1rem;
  text-align: center !important;
}

/* ----------------------------------------------------
   APPLE-STYLE SCROLL REVEAL ANIMATIONS
   ---------------------------------------------------- */
.reveal {
  opacity: 0;
  transform: translateY(45px) scale(0.97);
  transition: opacity 0.85s var(--apple-ease), transform 0.85s var(--apple-ease);
  will-change: opacity, transform;
}

.reveal.active {
  opacity: 1;
  transform: translateY(0) scale(1);
}

.reveal-delay-1 { transition-delay: 0.15s; }
.reveal-delay-2 { transition-delay: 0.3s; }
.reveal-delay-3 { transition-delay: 0.45s; }

/* ----------------------------------------------------
   APPLE-STYLE PROGRESS HEADER (REPLACED OLD MENU)
   ---------------------------------------------------- */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  padding: 0.85rem 0;
  background: rgba(11, 9, 14, 0.88);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-subtle);
  transition: var(--transition);
}

[data-theme="light"] .navbar {
  background: rgba(253, 251, 247, 0.9);
}

.navbar .nav-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo-brand {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  font-family: var(--font-serif);
  font-weight: 700;
  font-size: 1.3rem;
}

.logo-brand img {
  width: 44px;
  height: 44px;
  object-fit: contain;
  border-radius: 50%;
}

/* Center Section Reading Tracker */
.reading-tracker {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--text-muted);
  background: rgba(255, 255, 255, 0.04);
  padding: 0.4rem 1.2rem;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-subtle);
}

.reading-tracker .dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent-gold);
  box-shadow: 0 0 10px var(--accent-gold);
  animation: pulse-dot 2s infinite;
}

@keyframes pulse-dot {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.4); opacity: 0.6; }
}

.reading-title {
  color: var(--accent-gold-light);
  font-weight: 600;
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 0.85rem;
}

.btn-icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-card);
  color: var(--text-main);
  border: 1px solid var(--border-subtle);
  transition: var(--transition);
}

.btn-icon:hover {
  background: var(--accent-gold);
  color: #000;
  transform: translateY(-2px);
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.65rem 1.5rem;
  background: linear-gradient(135deg, var(--accent-gold), var(--accent-gold-dark));
  color: #000;
  font-weight: 600;
  font-size: 0.9rem;
  border-radius: var(--radius-full);
  transition: var(--transition);
  box-shadow: var(--shadow-glow);
}

.btn-primary:hover {
  transform: translateY(-2px);
  filter: brightness(1.1);
}

/* TOP PROGRESS BAR */
.progress-bar-container {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: rgba(255, 255, 255, 0.05);
}

.progress-bar-fill {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, var(--accent-warm), var(--accent-gold), var(--accent-gold-light));
  box-shadow: 0 0 12px var(--accent-gold);
  transition: width 0.1s ease-out;
}

/* SECTION 1: COVER HERO */
.hero-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  padding-top: 6rem;
  background: radial-gradient(circle at center, rgba(212, 175, 55, 0.14) 0%, rgba(11, 9, 14, 1) 78%),
              url('assets/images/gallery/image2.jpeg') center/cover no-repeat;
  background-blend-mode: overlay;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, rgba(11, 9, 14, 0.4), rgba(11, 9, 14, 0.96));
}

.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  max-width: 900px;
  padding: 2rem;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.55rem 1.65rem;
  border-radius: var(--radius-full);
  background: rgba(212, 175, 55, 0.15);
  border: 1px solid var(--border-light);
  color: var(--accent-gold-light);
  font-size: 0.95rem;
  letter-spacing: 0.12em;
  margin-bottom: 2rem;
}

.hero-title {
  font-size: clamp(3.2rem, 7.5vw, 5.8rem);
  font-weight: 900;
  letter-spacing: -0.02em;
  margin-bottom: 1.5rem;
  background: linear-gradient(135deg, #ffffff 25%, var(--accent-gold-light) 65%, var(--accent-gold) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtitle {
  font-size: clamp(1.15rem, 2vw, 1.55rem);
  color: var(--text-muted);
  font-weight: 300;
  max-width: 720px;
  margin: 0 auto 3rem auto;
  text-align: center !important;
}

.hero-stats-banner {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  background: rgba(255, 255, 255, 0.03);
  backdrop-filter: blur(25px);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 2rem;
  margin-top: 2rem;
}

.hero-stat-item h3 {
  font-size: 2.6rem;
  color: var(--accent-gold);
}

.hero-stat-item p {
  font-size: 0.85rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  text-align: center !important;
}

/* SECTION 1.2: FOREWORD */
.foreword-section {
  background: var(--bg-secondary);
}

.foreword-grid {
  display: grid;
  grid-template-columns: 1fr 1.25fr;
  gap: 4.5rem;
  align-items: center;
}

.foreword-image-frame {
  position: relative;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-soft);
  border: 1px solid var(--border-light);
}

.foreword-image-frame img {
  width: 100%;
  height: 560px;
  object-fit: cover;
  transition: transform 0.8s var(--apple-ease);
}

.foreword-image-frame:hover img {
  transform: scale(1.04);
}

.foreword-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 1.5rem;
  background: linear-gradient(to top, rgba(0,0,0,0.92), transparent);
  color: #fff;
}

.signature-card {
  margin-top: 2.25rem;
  padding: 1.5rem;
  background: var(--bg-card);
  border-radius: var(--radius-md);
  border-left: 4px solid var(--accent-gold);
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.signature-card img {
  width: 65px;
  height: 65px;
  border-radius: 50%;
  border: 2px solid var(--accent-gold);
}

.signature-name {
  font-family: var(--font-signature);
  font-size: 1.8rem;
  color: var(--accent-gold-light);
  line-height: 1;
  margin-top: 0.2rem;
}

/* SECTION 1.3: TABLE OF CONTENTS */
.toc-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.75rem;
}

.toc-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 2.25rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: var(--transition);
}

.toc-card:hover {
  border-color: var(--accent-gold);
  transform: translateY(-6px);
  box-shadow: var(--shadow-soft);
}

.toc-number {
  font-family: var(--font-serif);
  font-size: 2.8rem;
  font-weight: 900;
  color: var(--accent-gold);
  opacity: 0.85;
  margin-bottom: 1rem;
}

.toc-card h3 {
  font-size: 1.3rem;
  margin-bottom: 0.5rem;
}

.toc-card p {
  color: var(--text-muted);
  font-size: 0.95rem;
  text-align: left !important;
}

/* SECTION 1.4: ABOUT & CORE VALUES */
.about-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.75rem;
  margin-top: 3.5rem;
}

.value-card {
  background: var(--bg-card);
  padding: 2.25rem 1.75rem;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-subtle);
  text-align: center;
  transition: var(--transition);
}

.value-card:hover {
  border-color: var(--accent-gold);
  transform: translateY(-5px);
}

.value-icon {
  font-size: 2.8rem;
  color: var(--accent-gold);
  margin-bottom: 1rem;
}

.value-card p {
  text-align: center !important;
  font-size: 0.95rem;
}

/* SECTION 2: TIMELINE & STATS */
.timeline-track {
  position: relative;
  max-width: 920px;
  margin: 3.5rem auto 0 auto;
  padding: 2rem 0;
}

.timeline-track::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  width: 2px;
  background: var(--border-light);
  transform: translateX(-50%);
}

.timeline-item {
  position: relative;
  width: 50%;
  padding: 0 2.75rem 3.5rem 2.75rem;
}

.timeline-item:nth-child(odd) {
  left: 0;
  text-align: right;
}

.timeline-item:nth-child(even) {
  left: 50%;
  text-align: left;
}

.timeline-node {
  position: absolute;
  top: 0;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--accent-gold);
  border: 4px solid var(--bg-primary);
  box-shadow: var(--shadow-glow);
  z-index: 2;
}

.timeline-item:nth-child(odd) .timeline-node { right: -11px; }
.timeline-item:nth-child(even) .timeline-node { left: -11px; }

.timeline-card {
  background: var(--bg-card);
  padding: 2rem;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-subtle);
}

.timeline-card p {
  font-size: 0.95rem;
}

.timeline-year {
  display: inline-block;
  padding: 0.3rem 0.9rem;
  background: var(--accent-gold);
  color: #000;
  font-weight: 700;
  font-size: 0.85rem;
  border-radius: var(--radius-full);
  margin-bottom: 0.85rem;
}

/* SECTION 3: BQT */
.bqt-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
  gap: 2.25rem;
}

.bqt-card {
  background: var(--bg-card);
  border-radius: var(--radius-lg);
  overflow: hidden;
  border: 1px solid var(--border-subtle);
  transition: var(--transition);
}

.bqt-card:hover {
  border-color: var(--accent-gold);
  transform: translateY(-8px);
  box-shadow: var(--shadow-soft);
}

.bqt-photo-wrapper {
  position: relative;
  height: 350px;
  overflow: hidden;
}

.bqt-photo-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.7s var(--apple-ease);
}

.bqt-card:hover .bqt-photo-wrapper img {
  transform: scale(1.06);
}

.bqt-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: rgba(11, 9, 14, 0.88);
  backdrop-filter: blur(8px);
  color: var(--accent-gold);
  padding: 0.4rem 0.95rem;
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 600;
  border: 1px solid var(--border-light);
}

.bqt-content {
  padding: 1.85rem;
}

.bqt-role {
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--accent-warm);
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.bqt-name {
  font-size: 1.45rem;
  margin-bottom: 0.25rem;
}

.bqt-nickname {
  font-size: 0.925rem;
  color: var(--accent-gold);
  margin-bottom: 1rem;
}

.bqt-info-list {
  list-style: none;
  font-size: 0.88rem;
  color: var(--text-muted);
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
  margin-bottom: 1.25rem;
}

.bqt-quote-box {
  background: var(--bg-paper);
  padding: 0.95rem 1.15rem;
  border-radius: var(--radius-sm);
  font-size: 0.88rem;
  font-style: italic;
  border-left: 3px solid var(--accent-gold);
}

/* SECTION 4: SPONSORS */
.sponsor-tier {
  margin-bottom: 4.5rem;
}

.sponsor-tier-title {
  text-align: center;
  font-size: 1.55rem;
  color: var(--accent-gold);
  margin-bottom: 2.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
}

.sponsor-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
  gap: 1.75rem;
}

.sponsor-card {
  background: var(--bg-card);
  padding: 2.25rem;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-light);
  text-align: center;
  box-shadow: var(--shadow-soft);
  transition: var(--transition);
}

.sponsor-card:hover {
  transform: translateY(-5px);
  border-color: var(--accent-gold);
}

/* SECTION 5: GALLERY MASONRY */
.gallery-filter {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 3.5rem;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 0.55rem 1.65rem;
  border-radius: var(--radius-full);
  background: var(--bg-card);
  color: var(--text-muted);
  border: 1px solid var(--border-subtle);
  font-size: 0.925rem;
  transition: var(--transition);
}

.filter-btn.active,
.filter-btn:hover {
  background: var(--accent-gold);
  color: #000;
  font-weight: 600;
}

.gallery-masonry {
  column-count: 3;
  column-gap: 1.75rem;
}

.gallery-item {
  break-inside: avoid;
  margin-bottom: 1.75rem;
  position: relative;
  border-radius: var(--radius-md);
  overflow: hidden;
  cursor: pointer;
  border: 1px solid var(--border-subtle);
}

.gallery-item img {
  width: 100%;
  display: block;
  transition: transform 0.7s var(--apple-ease);
}

.gallery-item:hover img {
  transform: scale(1.06);
}

.gallery-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, transparent 65%);
  opacity: 0;
  transition: opacity 0.4s ease;
  display: flex;
  align-items: flex-end;
  padding: 1.5rem;
  color: #fff;
}

.gallery-item:hover .gallery-overlay {
  opacity: 1;
}

/* SECTION 6: MEMBER SPOTLIGHT GRID */
.search-filter-bar {
  max-width: 620px;
  margin: 0 auto 3.5rem auto;
  position: relative;
}

.search-input {
  width: 100%;
  padding: 1.1rem 1.75rem 1.1rem 3.25rem;
  border-radius: var(--radius-full);
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  color: var(--text-main);
  font-size: 1.05rem;
  outline: none;
  transition: var(--transition);
}

.search-input:focus {
  border-color: var(--accent-gold);
  box-shadow: var(--shadow-glow);
}

.search-icon {
  position: absolute;
  left: 1.35rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
}

.members-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(270px, 1fr));
  gap: 2rem;
}

.member-card {
  background: var(--bg-card);
  border-radius: var(--radius-md);
  overflow: hidden;
  border: 1px solid var(--border-subtle);
  transition: var(--transition);
  display: flex;
  flex-direction: column;
}

.member-card:hover {
  border-color: var(--accent-gold);
  transform: translateY(-5px);
  box-shadow: var(--shadow-soft);
}

.member-photo {
  height: 290px;
  width: 100%;
  object-fit: cover;
}

.member-body {
  padding: 1.35rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.member-name {
  font-size: 1.2rem;
  margin-bottom: 0.2rem;
}

.member-nickname {
  font-size: 0.88rem;
  color: var(--accent-gold);
  margin-bottom: 0.85rem;
  font-weight: 500;
}

.member-meta {
  font-size: 0.825rem;
  color: var(--text-muted);
  margin-bottom: 0.85rem;
}

.member-quote {
  font-size: 0.85rem;
  font-style: italic;
  color: var(--text-main);
  background: var(--bg-paper);
  padding: 0.85rem;
  border-radius: var(--radius-sm);
  margin-top: auto;
  border-left: 3px solid var(--accent-gold);
}

/* SECTION 7: STORIES */
.story-article {
  background: var(--bg-card);
  border-radius: var(--radius-lg);
  padding: 3.75rem;
  margin-bottom: 4.5rem;
  border: 1px solid var(--border-subtle);
  box-shadow: var(--shadow-soft);
}

.story-header {
  margin-bottom: 2.75rem;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 1.75rem;
}

.story-author-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.story-title {
  font-size: clamp(1.85rem, 3.2vw, 2.7rem);
  margin-bottom: 1rem;
}

/* SECTION 8: CLOSING */
.closing-section {
  background: radial-gradient(circle at center, rgba(212, 175, 55, 0.16) 0%, rgba(11, 9, 14, 1) 80%),
              url('assets/images/gallery/image35.jpeg') center/cover no-repeat;
  background-blend-mode: overlay;
  text-align: center;
  padding: 9rem 0;
}

.closing-card {
  max-width: 820px;
  margin: 0 auto;
  background: rgba(19, 16, 25, 0.88);
  backdrop-filter: blur(25px);
  padding: 4.5rem 2.5rem;
  border-radius: var(--radius-lg);
  border: 1px solid var(--border-light);
}

.qr-box {
  margin-top: 2.75rem;
  display: inline-block;
  padding: 1.75rem;
  background: #ffffff;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-glow);
}

.qr-box img {
  width: 170px;
  height: 170px;
}

.qr-box p {
  color: #000;
  font-weight: 700;
  font-size: 0.9rem;
  margin-top: 0.6rem;
}

/* LIGHTBOX MODAL */
.lightbox-modal {
  display: none;
  position: fixed;
  inset: 0;
  z-index: 2000;
  background: rgba(0,0,0,0.94);
  backdrop-filter: blur(12px);
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.lightbox-modal.active {
  display: flex;
}

.lightbox-content {
  max-width: 90vw;
  max-height: 85vh;
  border-radius: var(--radius-md);
  overflow: hidden;
  position: relative;
}

.lightbox-content img {
  max-width: 100%;
  max-height: 80vh;
  object-fit: contain;
}

.lightbox-close {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  color: #fff;
  font-size: 2.2rem;
  cursor: pointer;
}

/* RESPONSIVE DESIGN */
@media (max-width: 1024px) {
  .foreword-grid { grid-template-columns: 1fr; }
  .gallery-masonry { column-count: 2; }
  .timeline-track::before { left: 20px; }
  .timeline-item { width: 100%; padding-left: 3rem; text-align: left !important; }
  .timeline-item:nth-child(even) { left: 0; }
  .timeline-node { left: 9px !important; }
}

@media (max-width: 768px) {
  .reading-tracker { display: none; }
  .hero-stats-banner { grid-template-columns: 1fr; }
  .gallery-masonry { column-count: 1; }
  .story-article { padding: 2.25rem 1.5rem; }
}

/* ----------------------------------------------------
   PRINT STYLES FOR A4 PDF EXPORT
   ---------------------------------------------------- */
@media print {
  @page {
    size: A4 portrait;
    margin: 12mm 10mm 12mm 10mm;
  }

  body {
    background-color: #ffffff !important;
    color: #111111 !important;
    font-size: 11pt;
    line-height: 1.5;
  }

  .navbar,
  .btn-icon,
  .btn-primary,
  .search-filter-bar,
  .gallery-filter,
  .lightbox-modal,
  .no-print {
    display: none !important;
  }

  .reveal {
    opacity: 1 !important;
    transform: none !important;
  }

  .section {
    padding: 2rem 0 !important;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  .hero-section {
    min-height: auto !important;
    padding: 3rem 0 !important;
    background: #ffffff !important;
    color: #000000 !important;
  }

  .hero-title {
    background: none !important;
    -webkit-text-fill-color: initial !important;
    color: #000000 !important;
  }

  .bqt-card,
  .member-card,
  .story-article,
  .toc-card,
  .timeline-card,
  .sponsor-card {
    background: #ffffff !important;
    border: 1px solid #ddd !important;
    box-shadow: none !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    color: #000000 !important;
  }

  .story-article {
    page-break-before: always;
    break-before: page;
  }

  .bqt-grid,
  .members-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 1rem !important;
  }

  .gallery-masonry {
    column-count: 2 !important;
  }

  a { text-decoration: none !important; color: #000 !important; }
}
"""
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css_content)

def generate_script_js():
    js_content = """/* ----------------------------------------------------
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
"""
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

def generate_index_html(bqt_data, sec6_data, stories_data, gallery_data):
    # Render BQT HTML
    bqt_html = ""
    for idx, m in enumerate(bqt_data):
        quote_html = f'<div class="bqt-quote-box">"{html.escape(m["quote"])}"</div>' if m["quote"] else ""
        delay_class = f"reveal-delay-{(idx % 3) + 1}"
        bqt_html += f"""
        <article class="bqt-card js-member-card reveal {delay_class}" data-name="{html.escape(m['name'].lower())}" data-nickname="{html.escape(m['nickname'].lower())}" data-song="{html.escape(m['song'].lower())}">
          <div class="bqt-photo-wrapper">
            <img src="{m['photo']}" alt="{html.escape(m['name'])}" loading="lazy">
            <span class="bqt-badge">BQT #{m['bqt']}</span>
          </div>
          <div class="bqt-content">
            <div class="bqt-role">{html.escape(m['role'] or 'Ban Quản Trị')}</div>
            <h3 class="bqt-name">{html.escape(m['name'])}</h3>
            <div class="bqt-nickname">{html.escape(m['nickname'] or '')}</div>
            <ul class="bqt-info-list">
              <li>📅 Tham gia: {html.escape(m['join_date'] or '01/08/2021')}</li>
              <li>🎵 Bài hát yêu thích: <strong>{html.escape(m['song'] or 'N/A')}</strong></li>
            </ul>
            {quote_html}
          </div>
        </article>
        """

    # Render Sec6 HTML
    sec6_html = ""
    for idx, m in enumerate(sec6_data):
        quote_html = f'<div class="member-quote">"{html.escape(m["quote"])}"</div>' if m["quote"] else ""
        delay_class = f"reveal-delay-{(idx % 3) + 1}"
        sec6_html += f"""
        <article class="member-card js-member-card reveal {delay_class}" data-name="{html.escape(m['name'].lower())}" data-nickname="{html.escape(m['nickname'].lower())}" data-song="{html.escape(m['song'].lower())}">
          <img class="member-photo" src="{m['photo']}" alt="{html.escape(m['name'])}" loading="lazy">
          <div class="member-body">
            <h4 class="member-name">{html.escape(m['name'])}</h4>
            <div class="member-nickname">{html.escape(m['nickname'] or '')}</div>
            <div class="member-meta">
              <div>📅 Tham gia: {html.escape(m['join_date'] or 'N/A')}</div>
              <div>🎵 Bài hát: {html.escape(m['song'] or 'N/A')}</div>
            </div>
            {quote_html}
          </div>
        </article>
        """

    # Render Stories HTML
    stories_html = ""
    for idx, s in enumerate(stories_data):
        content_paras = s['content'].split('\n')
        paras_html = ""
        for p in content_paras:
            if p.strip():
                paras_html += f"<p>{html.escape(p.strip())}</p>\n"

        stories_html += f"""
        <article class="story-article reveal" id="story-{idx+1}">
          <header class="story-header">
            <div class="story-author-badge">
              <span class="text-gold font-bold">📖 Tác giả:</span>
              <span class="font-semibold">{html.escape(s['author'])}</span>
            </div>
            <h3 class="story-title">{html.escape(s['title'])}</h3>
          </header>
          <div class="story-content">
            {paras_html}
          </div>
        </article>
        """

    # Render Gallery HTML
    gallery_html = ""
    for idx, g in enumerate(gallery_data):
        delay_class = f"reveal-delay-{(idx % 3) + 1}"
        gallery_html += f"""
        <div class="gallery-item js-gallery-item js-lightbox-trigger reveal {delay_class}" data-category="{g['category'].lower()}" data-src="{g['src']}" data-caption="{html.escape(g['caption'])}">
          <img src="{g['src']}" alt="{html.escape(g['caption'])}" loading="lazy">
          <div class="gallery-overlay">
            <span>🔍 Xem ảnh lớn</span>
          </div>
        </div>
        """

    html_full = f"""<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kỷ Yếu Điện Tử - Chúng Ta Của Những Năm Ấy (2021 - 2026)</title>
  <meta name="description" content="Kỷ yếu 05 năm thành lập CLB Guitar và Bạn (01/08/2021 - 01/08/2026). Nơi lưu giữ những ký ức, câu chuyện và tình bạn đẹp nhất.">
  
  <!-- High-Quality Vietnamese Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Caveat:wght@600;700&display=swap" rel="stylesheet">
  
  <!-- Main Stylesheet -->
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <!-- Apple-Style Progress & Tracker Header -->
  <header class="navbar">
    <div class="container nav-inner">
      <a href="#cover" class="logo-brand">
        <img src="assets/images/logo.png" alt="CLB Guitar và Bạn Logo">
        <span>Guitar & Bạn</span>
      </a>
      
      <!-- Section Reading Tracker -->
      <div class="reading-tracker">
        <span class="dot"></span>
        <span>Đang xem:</span>
        <span id="reading-section-title" class="reading-title">Bìa Kỷ Yếu</span>
      </div>
      
      <div class="nav-actions">
      </div>
    </div>
    
    <!-- Top Progress Bar Fill -->
    <div class="progress-bar-container">
      <div id="progress-bar-fill" class="progress-bar-fill"></div>
    </div>
  </header>

  <main>
    <!-- SECTION 1: COVER HERO -->
    <section id="cover" class="hero-section" data-section-title="Phần I: Bìa Kỷ Yếu">
      <div class="hero-overlay"></div>
      <div class="hero-content reveal">
        <div class="hero-badge">
          <span>🎸 KỶ NIỆM 05 NĂM THÀNH LẬP CLB GUITAR VÀ BẠN</span>
        </div>
        <h1 class="hero-title">CHÚNG TA CỦA NHỮNG NĂM ẤY</h1>
        <p class="hero-subtitle">
          Một hành trình âm nhạc, tình bạn và những ký ức rực rỡ từ ngày 01 tháng 8 năm 2021 đến 01 tháng 8 năm 2026.
        </p>

        <div class="hero-stats-banner reveal reveal-delay-1">
          <div class="hero-stat-item">
            <h3>05</h3>
            <p>Năm Hành Trình</p>
          </div>
          <div class="hero-stat-item">
            <h3>10,000+</h3>
            <p>Thành Viên</p>
          </div>
          <div class="hero-stat-item">
            <h3>1,000+</h3>
            <p>Bản Cover Lan Tỏa</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 1.2: FOREWORD -->
    <section id="foreword" class="section foreword-section" data-section-title="Phần I: Lời Ngỏ Ban Quản Trị">
      <div class="container">
        <div class="foreword-grid">
          <div class="foreword-image-frame reveal">
            <img src="assets/images/gallery/image3.jpeg" alt="Tập thể CLB Guitar và Bạn">
            <div class="foreword-caption">
              <h4>Mái nhà chung của những tâm hồn yêu tiếng đàn</h4>
            </div>
          </div>

          <div class="editorial-body reveal reveal-delay-1">
            <div class="subtitle">LỜI NGỎ BAN QUẢN TRỊ</div>
            <h2>Gửi những tâm hồn đồng điệu</h2>
            <div class="pull-quote">
              "Điều gì khiến một cộng đồng có thể đi cùng nhau suốt 5 năm? Có lẽ đơn giản là vì giữa hàng triệu người, chúng ta đã tìm thấy nhau nhờ một niềm yêu thích rất bình dị: Âm Nhạc."
            </div>
            <p>
              Từ một nhóm nhỏ những người yêu guitar, CLB Guitar và Bạn đã dần trở thành một mái nhà chung, nơi có những buổi offline rộn ràng, những bản cover đầy cảm xúc, những chương trình thiện nguyện, những mini game vui vẻ và trên hết là rất nhiều tình bạn được bắt đầu từ đây.
            </p>
            <p>
              Cuốn kỷ yếu điện tử "Chúng ta của những năm ấy" không được tạo nên để kể về những thành tích hay những con số. Chúng tôi muốn lưu giữ những điều giản dị hơn: một bức ảnh, một nụ cười, một lần gặp gỡ, hay chỉ đơn giản là một cái tên đã từng xuất hiện trong hành trình 5 năm ấy.
            </p>

            <div class="signature-card reveal reveal-delay-2">
              <img src="assets/images/members/6.jpeg" alt="Mai Nguyễn">
              <div>
                <h4 class="text-gold">Mai Nguyễn (Cô Cô)</h4>
                <div class="signature-name">Mai Nguyễn</div>
                <p style="font-size:0.85rem; color:var(--text-muted);">Người sáng lập CLB Guitar và Bạn</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 1.3: TABLE OF CONTENTS -->
    <section class="section" data-section-title="Phần I: Mục Lục Kỷ Yếu">
      <div class="container">
        <div class="section-header reveal">
          <div class="subtitle">MỤC LỤC KỶ YẾU</div>
          <h2>Các phần nội dung chính</h2>
        </div>
        <div class="toc-grid">
          <a href="#cover" class="toc-card reveal reveal-delay-1">
            <div class="toc-number">01</div>
            <h3>Phần I. Mở Đầu</h3>
            <p>Bìa kỷ yếu, Lời ngỏ Ban Quản trị, Giới thiệu & Sứ mệnh CLB</p>
          </a>
          <a href="#journey" class="toc-card reveal reveal-delay-1">
            <div class="toc-number">02</div>
            <h3>Phần II. Hành Trình 05 Năm</h3>
            <p>Mốc thời gian 2021-2026, Con số ấn tượng & Dấu ấn phát triển</p>
          </a>
          <a href="#bqt" class="toc-card reveal reveal-delay-2">
            <div class="toc-number">03</div>
            <h3>Phần III. Những Người Giữ Lửa</h3>
            <p>11 Thành viên Ban Quản trị & Tri ân thế hệ tiền nhiệm</p>
          </a>
          <a href="#sponsors" class="toc-card reveal reveal-delay-2">
            <div class="toc-number">04</div>
            <h3>Phần IV. Tri Ân Đồng Hành</h3>
            <p>Tôn vinh các nhà tài trợ, mạnh thường quân & người đồng hành</p>
          </a>
          <a href="#gallery" class="toc-card reveal reveal-delay-3">
            <div class="toc-number">05</div>
            <h3>Phần V. Khoảnh Khắc Đáng Nhớ</h3>
            <p>Bộ sưu tập hình ảnh offline, giao lưu, guitar & thiện nguyện</p>
          </a>
          <a href="#members" class="toc-card reveal reveal-delay-3">
            <div class="toc-number">06</div>
            <h3>Phần VI. Chúng Ta Của Những Năm Ấy</h3>
            <p>Trang thông tin cá nhân & hình ảnh của gần 40 thành viên</p>
          </a>
          <a href="#stories" class="toc-card reveal reveal-delay-3">
            <div class="toc-number">07</div>
            <h3>Phần VII. Những Câu Chuyện Còn Mãi</h3>
            <p>7 Bài viết cảm xúc, hồi ký & trải nghiệm cá nhân đặc sắc</p>
          </a>
          <a href="#farewell" class="toc-card reveal reveal-delay-3">
            <div class="toc-number">08</div>
            <h3>Phần VIII. Hẹn Gặp Lại</h3>
            <p>Lời kết, thông điệp hướng tới tương lai & Mã QR kết nối</p>
          </a>
        </div>
      </div>
    </section>

    <!-- SECTION 1.4: ABOUT & VALUES -->
    <section class="section" style="background: var(--bg-secondary);" data-section-title="Phần I: Giới Thiệu CLB">
      <div class="container">
        <div class="section-header reveal">
          <div class="subtitle">GIỚI THIỆU CLB</div>
          <h2>Quá trình hình thành & Sứ mệnh</h2>
          <p>
            Ngày 01/08/2021, giữa những ngày phong tỏa nghiêm ngặt của đại dịch COVID-19 tại Quận Gò Vấp (TP.HCM), CLB Guitar và Bạn được ra đời nhằm mang lại một không gian âm nhạc chữa lành và kết nối những tâm hồn đồng điệu.
          </p>
        </div>

        <div class="about-cards">
          <div class="value-card reveal reveal-delay-1">
            <div class="value-icon">🎶</div>
            <h3>Tự Do & Sáng Tạo</h3>
            <p>Không phân biệt trình độ, tuổi tác; tôn trọng phong cách âm nhạc cá nhân của mỗi thành viên.</p>
          </div>
          <div class="value-card reveal reveal-delay-1">
            <div class="value-icon">🤝</div>
            <h3>Kết Nối & Sẻ Chia</h3>
            <p>Đồng hành cùng nhau qua âm nhạc, tạo dựng những tình bạn chân thành ngoài đời thực.</p>
          </div>
          <div class="value-card reveal reveal-delay-2">
            <div class="value-icon">🌿</div>
            <h3>Tôn Trọng & Văn Minh</h3>
            <p>Xây dựng môi trường giao lưu văn minh, luôn khuyến khích và cổ vũ lẫn nhau tiến bộ.</p>
          </div>
          <div class="value-card reveal reveal-delay-2">
            <div class="value-icon">❤️</div>
            <h3>Âm Nhạc Cho Cộng Đồng</h3>
            <p>Lan tỏa tinh thần nhân văn qua các chương trình thiện nguyện và trao tặng đàn guitar.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2: JOURNEY & TIMELINE -->
    <section id="journey" class="section" data-section-title="Phần II: Hành Trình 05 Năm">
      <div class="container">
        <div class="section-header reveal">
          <div class="subtitle">PHẦN II. HÀNH TRÌNH 05 NĂM</div>
          <h2>Dấu ấn thời gian (2021 – 2026)</h2>
        </div>

        <div class="timeline-track">
          <div class="timeline-item reveal">
            <div class="timeline-node"></div>
            <div class="timeline-card">
              <span class="timeline-year">01/08/2021</span>
              <h3>Khởi Đầu Giữa Mùa Dịch</h3>
              <p>Thành lập nhóm trực tuyến kết nối những người yêu guitar trong bối cảnh đại dịch COVID-19 bùng phát.</p>
            </div>
          </div>

          <div class="timeline-item reveal reveal-delay-1">
            <div class="timeline-node"></div>
            <div class="timeline-card">
              <span class="timeline-year">2022</span>
              <h3>Offline & Mở Rộng Cộng Đồng</h3>
              <p>Chuyển từ hoạt động online sang các buổi offline rộn ràng, đón nhận hàng nghìn thành viên mới trên khắp cả nước.</p>
            </div>
          </div>

          <div class="timeline-item reveal reveal-delay-2">
            <div class="timeline-node"></div>
            <div class="timeline-card">
              <span class="timeline-year">2023 - 2024</span>
              <h3>Âm Nhạc Sẻ Chia & Thiện Nguyện</h3>
              <p>Tổ chức các sự kiện trao tặng đàn cho trẻ em nghèo, các chương trình giao lưu nghệ sĩ chuyên nghiệp.</p>
            </div>
          </div>

          <div class="timeline-item reveal reveal-delay-3">
            <div class="timeline-node"></div>
            <div class="timeline-card">
              <span class="timeline-year">01/08/2026</span>
              <h3>Cột Mốc 05 Năm Rực Rỡ</h3>
              <p>Ra mắt kỷ yếu điện tử "Chúng Ta Của Những Năm Ấy", khẳng định một cộng đồng bền chặt và giàu cảm xúc.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: BQT -->
    <section id="bqt" class="section" style="background: var(--bg-secondary);" data-section-title="Phần III: Những Người Giữ Lửa">
      <div class="container">
        <div class="section-header reveal">
          <div class="subtitle">PHẦN III. NHỮNG NGƯỜI GIỮ LỬA</div>
          <h2>Ban Quản Trị Đương Nhiệm (11 Trang)</h2>
          <p>Những con người âm thầm cống hiến thời gian, công sức và tâm huyết để gìn giữ không gian ấm áp cho CLB.</p>
        </div>

        <div class="bqt-grid">
          {bqt_html}
        </div>

        <div class="story-article reveal" style="margin-top: 4.5rem;">
          <h3 class="text-gold">Tri Ân Những Người Đã Từng Giữ Lửa</h3>
          <p>
            Một chặng đường 5 năm không thể được viết nên bởi một vài con người. Trước Ban Quản trị hôm nay, đã có những anh chị và các bạn từng dành thời gian, tâm huyết và cả những ngày cuối tuần của mình để góp phần xây dựng CLB Guitar và Bạn (Anh Hổ Ca và các cựu thành viên BQT).
          </p>
        </div>
      </div>
    </section>

    <!-- SECTION 4: SPONSORS -->
    <section id="sponsors" class="section" data-section-title="Phần IV: Tri Ân Đồng Hành">
      <div class="container">
        <div class="section-header reveal">
          <div class="subtitle">PHẦN IV. TRI ÂN NHỮNG NGƯỜI ĐỒNG HÀNH</div>
          <h2>Nhà Tài Trợ & Mạnh Thường Quân</h2>
          <p>Xin trân trọng ghi nhận và cảm ơn những tấm lòng sẻ chia đã giúp đỡ CLB trong suốt 05 năm qua.</p>
        </div>

        <div class="sponsor-tier reveal">
          <div class="sponsor-tier-title">
            <span>💛 Đồng Hành Xuyên Suốt</span>
          </div>
          <div class="sponsor-cards-grid">
            <div class="sponsor-card">
              <h3 class="text-gold">Nhà Tài Trợ Vàng</h3>
              <p style="color:var(--text-muted); font-size:0.9rem; margin-top:0.5rem; text-align:center !important;">Sát cánh cùng CLB qua nhiều năm liền, tạo nền tảng vững chắc cho mọi hoạt động.</p>
            </div>
            <div class="sponsor-card">
              <h3 class="text-gold">Đơn Vị Đồng Hành Cốt Lõi</h3>
              <p style="color:var(--text-muted); font-size:0.9rem; margin-top:0.5rem; text-align:center !important;">Hỗ trợ kinh phí & thiết bị âm thanh cho các chương trình kỷ niệm lớn.</p>
            </div>
          </div>
        </div>

        <div class="sponsor-tier reveal reveal-delay-1">
          <div class="sponsor-tier-title">
            <span>💛 Đồng Hành Nhiều Năm & Theo Chương Trình</span>
          </div>
          <div class="sponsor-cards-grid">
            <div class="sponsor-card">
              <h4>Mạnh Thường Quân Thiện Nguyện</h4>
              <p style="color:var(--text-muted); font-size:0.85rem; text-align:center !important;">Tài trợ các suất quà và đàn guitar cho trẻ em có hoàn cảnh khó khăn.</p>
            </div>
            <div class="sponsor-card">
              <h4>Đối Tác Quà Tặng & Mini Game</h4>
              <p style="color:var(--text-muted); font-size:0.85rem; text-align:center !important;">Tài trợ phần thưởng cho các giải đấu và trò chơi âm nhạc trực tuyến.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: GALLERY -->
    <section id="gallery" class="section" style="background: var(--bg-secondary);" data-section-title="Phần V: Khoảnh Khắc Đáng Nhớ">
      <div class="container">
        <div class="section-header reveal">
          <div class="subtitle">PHẦN V. KHOẢNH KHẮC ĐÁNG NHỚ</div>
          <h2>Bộ Sưu Tập Hình Ảnh Kỷ Niệm</h2>
        </div>

        <div class="gallery-filter reveal">
          <button class="filter-btn js-gallery-filter active" data-category="all">Tất Cả</button>
          <button class="filter-btn js-gallery-filter" data-category="offline">Offline</button>
          <button class="filter-btn js-gallery-filter" data-category="jamming">Giao Lưu</button>
          <button class="filter-btn js-gallery-filter" data-category="charity">Thiện Nguyện</button>
          <button class="filter-btn js-gallery-filter" data-category="events">Sự Kiện</button>
        </div>

        <div class="gallery-masonry">
          {gallery_html}
        </div>
      </div>
    </section>

    <!-- SECTION 6: MEMBERS SPOTLIGHT -->
    <section id="members" class="section" data-section-title="Phần VI: Chúng Ta Của Những Năm Ấy">
      <div class="container">
        <div class="section-header reveal">
          <div class="subtitle">PHẦN VI. CHÚNG TA CỦA NHỮNG NĂM ẤY</div>
          <h2>Gương Mặt Thành Viên (29 Trang)</h2>
        </div>

        <div class="search-filter-bar reveal">
          <span class="search-icon">🔍</span>
          <input type="text" id="member-search" class="search-input" placeholder="Tìm theo tên thành viên, biệt danh hoặc bài hát yêu thích...">
        </div>

        <div class="members-grid">
          {sec6_html}
        </div>
      </div>
    </section>

    <!-- SECTION 7: STORIES -->
    <section id="stories" class="section" style="background: var(--bg-secondary);" data-section-title="Phần VII: Những Câu Chuyện Còn Mãi">
      <div class="container">
        <div class="section-header reveal">
          <div class="subtitle">PHẦN VII. NHỮNG CÂU CHUYỆN CÒN MÃI</div>
          <h2>Hồi Ký & Trải Nghiệm Cá Nhân</h2>
        </div>

        {stories_html}
      </div>
    </section>

    <!-- SECTION 8: CLOSING -->
    <section id="farewell" class="section closing-section" data-section-title="Phần VIII: Hẹn Gặp Lại">
      <div class="container">
        <div class="closing-card reveal">
          <div class="subtitle">PHẦN VIII. HẸN GẶP LẠI</div>
          <h2 style="font-size: clamp(2.2rem, 4.5vw, 3.8rem); margin-bottom: 1.5rem;">HẸN GẶP LẠI...</h2>
          <div class="pull-quote" style="border:none; background:none; font-size: 1.3rem;">
            "Có người nói rằng, điều đẹp nhất của một cuộc gặp gỡ không phải là chúng ta đã ở bên nhau bao lâu, mà là sau nhiều năm nhìn lại, vẫn còn nhớ mình đã từng mỉm cười vì nhau."
          </div>
          <p style="color:var(--text-muted); font-size:1.15rem; max-width:720px; margin: 0 auto 2rem auto; text-align:center !important;">
            Mỗi người là một giai điệu. Cùng nhau, chúng ta đã tạo nên một bản hòa ca mang tên CLB Guitar và Bạn.
          </p>
          
          <div class="qr-box reveal reveal-delay-1">
            <img src="assets/images/logo.png" alt="QR Code Facebook Group">
            <p>Tham Gia Group Facebook</p>
          </div>

          <div style="margin-top: 2rem; color: var(--accent-gold); font-weight: 600;">
            Tháng 8 Năm 2026
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- LIGHTBOX MODAL -->
  <div id="lightbox-modal" class="lightbox-modal">
    <span class="lightbox-close">&times;</span>
    <div class="lightbox-content">
      <img id="lightbox-img" src="" alt="Zoomed view">
      <div id="lightbox-caption" style="color:#fff; padding:1rem; text-align:center;"></div>
    </div>
  </div>

  <!-- JavaScript -->
  <script src="script.js"></script>
</body>
</html>
"""
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_full)

def generate_readme_md():
    readme_content = """# Kỷ Yếu Điện Tử - "CHÚNG TA CỦA NHỮNG NĂM ẤY"
### Kỷ niệm 05 năm thành lập CLB Guitar và Bạn (01/08/2021 – 01/08/2026)

---

## 🌟 Cải Tiến Mới Nhất

1. **Phông Chữ Tiếng Việt Cao Cấp**:
   - Sử dụng `Be Vietnam Pro` cho phần thân văn bản (cực kỳ rõ nét, chuẩn tiếng Việt).
   - Sử dụng `Cormorant Garamond` & `Lora` cho tiêu đề và tạp chí nghệ thuật.
   - Thêm font chữ ký `Caveat` cho phần chữ ký của Founder.

2. **Căn Đều Văn Bản (Text Justification)**:
   - Tất cả các đoạn văn thư ngỏ, hồi ký, câu chuyện đều được căn đều 2 bên (`text-align: justify; text-justify: inter-word;`) mang lại trải nghiệm đọc tạp chí in ấn cao cấp.

3. **Hiệu Ứng Cuộn Trang Apple Smooth Reveal**:
   - Các phần tử mượt mà trượt nhẹ từ dưới lên và mờ dần (Fade-in & Scale) khi cuộn trang, sử dụng đường cong gia tốc chuẩn Apple `cubic-bezier(0.16, 1, 0.3, 1)`.

4. **Thanh Tiến Trình Cuộn Apple Progress Header**:
   - Rút gọn menu điều hướng cũ thành thanh tiến trình cuộn đọc tinh tế ở mép trên cùng.
   - Hiển thị phần đang đọc trực tiếp (ví dụ: `Đang xem: Phần III: Những Người Giữ Lửa`).

---

## 📁 Cấu Trúc Thư Mục Project

```
/
├── index.html              # Trang chủ chứa toàn bộ 8 Phần Kỷ yếu
├── styles.css              # Hệ thống CSS Design System & Style cho A4 PDF Print
├── script.js               # Đổi giao diện, Tìm kiếm thành viên, Lightbox modal
├── assets/
│   ├── images/
│   │   ├── logo.png        # Logo chính thức của CLB
│   │   ├── members/        # Ảnh 40 thành viên (1.jpeg .. 40.jpeg)
│   │   └── gallery/        # Ảnh hoạt động, offline & giao lưu
└── README.md               # Hướng dẫn sử dụng & xuất PDF A4
```

---

## 🖨️ Hướng Dẫn Xuất File PDF A4 Để In Ấn

1. Mở file `index.html` bằng trình duyệt **Google Chrome** hoặc **Safari**.
2. Nhấn nút **"🖨️ Xuất PDF A4"** ở góc phải thanh menu navigation (hoặc nhấn phím tắt `Cmd + P` trên Mac / `Ctrl + P` trên Windows).
3. Trong cửa sổ xem trước in:
   - **Máy in (Destination)**: Chọn *Save as PDF* (Lưu dưới dạng PDF).
   - **Khổ giấy (Paper size)**: Chọn *A4*.
   - **Tỷ lệ (Scale)**: Chọn *Default* hoặc *100%*.
   - **Đồ họa nền (Background graphics)**: Tích chọn ✅ (Bắt buộc để hiển thị khung nền và màu sắc chuẩn).
4. Nhấn **Save** để tải file PDF kỷ yếu đẹp mắt hoàn chỉnh!
"""
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == '__main__':
    build_all()
