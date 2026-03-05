# AK Design System - Agent Context & Usage Guide

This document defines the rules, classes, and structures for the **AK Design System**.
AI Agents should use this context to generate compliant HTML/CSS without hallucinating non-existent classes.

## 0. Quick References (Source of Truth)
If you need to verify implementation details or download source files:
- **Repository:** [github.com/ak-hosting/ak-systems-css](https://github.com/ak-hosting/ak-systems-css)
- **Live Examples (HTML):** [demo/index.html](https://github.com/ak-hosting/ak-systems-css/blob/v1.3.2/demo/index.html) (Best for copying patterns)
- **CDN (CSS):** `https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@v1.3.2/dist/ak-design-system.min.css`
- **Icons (Lucide):** `https://unpkg.com/lucide@latest/dist/umd/lucide.js`

## 1. Core Principles
- **Prefix:** All classes use the `ak-` prefix (e.g., `ak-btn`, `ak-card`).
- **No External Frameworks:** Do not use Bootstrap, Tailwind, or Bulma classes.
- **Icons:** Use `lucide` icons with `data-lucide="icon-name"`.
- **Dark Mode:** Supported via `.ak-theme-dark` on `<body>`.
- **Reset:** Uses a custom reset; do not rely on browser defaults.

## 2. CSS Variables (Theming)
Use these variables for custom styles to maintain consistency.

### Colors
- Primary: `--ak-color-primary` (Blue)
- Secondary: `--ak-color-secondary` (Dark Blue)
- Accent: `--ak-color-accent` (Green)
- Destructive: `--ak-color-destructive` (Red)
- Background: `--ak-color-bg`, `--ak-color-bg-subtle`
- Surface: `--ak-color-surface` (Cards, Modals)
- Text: `--ak-color-text`, `--ak-color-text-muted`
- Border: `--ak-color-border`

### Spacing & Radius
- Spacing: `--ak-space-1` to `--ak-space-12` (0.25rem steps)
- Radius: `--ak-radius-sm`, `--ak-radius-md`, `--ak-radius-lg`, `--ak-radius-full`

## 3. Component Reference

### Layout Structure (Header/Sidebar/Main)
```html
<body class="ak-theme-dark">
  <header class="ak-header">
    <div class="ak-flex ak-flex-between ak-items-center">
       <div class="ak-flex ak-items-center ak-gap-4">
         <button class="ak-btn ak-btn-ghost" onclick="openModal('nav-drawer')">
           <i data-lucide="menu"></i>
         </button>
         <h1 class="ak-text-xl ak-font-bold">App Name</h1>
       </div>
       <button class="ak-btn ak-btn-ghost"><i data-lucide="sun"></i></button>
    </div>
  </header>

  <!-- Left Drawer (Sidebar) -->
  <div id="nav-drawer" class="ak-modal ak-drawer-left">
    <div class="ak-modal-content">
      <div class="ak-modal-header">
        <h2 class="ak-modal-title">Navigation</h2>
        <button class="ak-btn ak-btn-ghost ak-btn-sm" onclick="closeModal('nav-drawer')">
          <i data-lucide="x"></i>
        </button>
      </div>
      <div class="ak-modal-body">
        <ul class="ak-nav ak-flex-col ak-gap-2">
          <li>
            <a href="#" class="ak-active">
              <i data-lucide="home" class="ak-w-4 ak-h-4 ak-mr-2"></i>
              <span>Home</span>
            </a>
          </li>
          <li>
            <a href="#">
              <i data-lucide="settings" class="ak-w-4 ak-h-4 ak-mr-2"></i>
              <span>Settings</span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>

  <main class="ak-main">
    <div class="ak-container">
      <!-- Page Content -->
    </div>
  </main>

  <footer class="ak-footer">
    <div class="ak-footer-content ak-flex ak-flex-between">
      <p>&copy; 2026 AK Systems</p>
      <ul class="ak-footer-links">
        <li><a href="#" class="ak-text-muted">Privacy</a></li>
        <li><a href="#" class="ak-text-muted">Terms</a></li>
      </ul>
    </div>
  </footer>
</body>
```

### Buttons (`.ak-btn`)
```html
<button class="ak-btn">Default</button>
<button class="ak-btn ak-btn-primary">Primary</button>
<button class="ak-btn ak-btn-secondary">Secondary</button>
<button class="ak-btn ak-btn-accent">Accent</button>
<button class="ak-btn ak-btn-ghost">Ghost</button>
<button class="ak-btn ak-btn-destructive">Destructive</button>
<button class="ak-btn ak-btn-link">Link</button>
<!-- Sizes -->
<button class="ak-btn ak-btn-sm">Small</button>
<button class="ak-btn ak-btn-lg">Large</button>
<button class="ak-btn ak-btn-xl">Extra Large</button>
<button class="ak-btn ak-btn-xs">Extra Small</button>

<!-- Shapes & Effects (Modern Variants) -->
<button class="ak-btn ak-btn-rounded">Rounded</button>
<button class="ak-btn ak-btn-pill">Pill</button>
<button class="ak-btn ak-btn-square"><i data-lucide="x"></i></button>
<button class="ak-btn ak-btn-circle"><i data-lucide="user"></i></button>
<button class="ak-btn ak-btn-soft-primary">Soft Primary</button>
<button class="ak-btn ak-btn-glass">Glass</button>
<button class="ak-btn ak-btn-gradient">Gradient</button>
<button class="ak-btn ak-btn-glow">Glow Effect</button>

<!-- Loading -->
<button class="ak-btn ak-loading"><span class="ak-loading-spinner"></span></button>
```

### Cards (`.ak-card`)
```html
<div class="ak-card">
  <div class="ak-card-header">
    <h3 class="ak-card-title">Card Title</h3>
  </div>
  <div class="ak-card-content">
    <p>Card content goes here.</p>
  </div>
  <div class="ak-card-footer">
    <button class="ak-btn">Action</button>
  </div>
</div>

<!-- Modern Card Variants -->
<div class="ak-card ak-card-hover-lift">Hover Lift</div>
<div class="ak-card ak-card-hover-glow">Hover Glow</div>
<div class="ak-card ak-card-glass">Glass Card</div>
<div class="ak-card ak-card-gradient">Gradient Card</div>
<div class="ak-card ak-card-stats">Stats Card</div>
<div class="ak-card ak-card-horizontal">Horizontal Layout</div>
<div class="ak-card ak-card-overlay">Image Overlay</div>
```

### Forms (`.ak-form-group`)
```html
<div class="ak-form-group">
  <label class="ak-form-label">Email</label>
  <input type="email" class="ak-input" placeholder="hello@example.com">
  <p class="ak-form-hint">We'll never share your email.</p>
</div>

<!-- Modern Input Variants -->
<input type="text" class="ak-input ak-input-filled" placeholder="Filled">
<input type="text" class="ak-input ak-input-material" placeholder="Material (Underline)">
<input type="text" class="ak-input ak-input-glass" placeholder="Glass">
<input type="text" class="ak-input ak-input-pill" placeholder="Pill Shape">
<input type="text" class="ak-input ak-input-flush" placeholder="Flush (No Border)">

<!-- Select -->
<select class="ak-select"><option>Option 1</option></select>

<!-- Checkbox -->
<label class="ak-checkbox">
  <input type="checkbox" class="ak-checkbox-input">
  <span class="ak-checkbox-label">I agree</span>
</label>

<!-- Radio -->
<label class="ak-radio">
  <input type="radio" name="options" class="ak-radio-input">
  <span class="ak-radio-label">Option 1</span>
</label>
<label class="ak-radio">
  <input type="radio" name="options" class="ak-radio-input">
  <span class="ak-radio-label">Option 2</span>
</label>

<!-- Switch -->
<label class="ak-switch">
  <input type="checkbox" class="ak-switch-input">
  <span class="ak-switch-track"><span class="ak-switch-thumb"></span></span>
  <span class="ak-switch-label">Toggle me</span>
</label>

<!-- File Upload -->
<div class="ak-upload">
  <input type="file" class="ak-upload-input">
  <i data-lucide="cloud-upload" class="ak-upload-icon"></i>
  <p class="ak-upload-text">Drop files here</p>
</div>
```

### Selection Controls (Advanced)
Use these for richer selection experiences.

#### Selection Cards (`.ak-selection-card`)
Great for pricing plans or complex options.
```html
<div class="ak-selection-grid">
  <label class="ak-selection-card">
    <input type="radio" name="plan" checked>
    <div class="ak-selection-card-content">
      <div class="ak-flex ak-items-center ak-gap-2 ak-mb-1">
        <i data-lucide="zap" class="ak-text-accent"></i>
        <span class="ak-selection-card-title">Starter</span>
      </div>
      <span class="ak-selection-card-description">Description here.</span>
    </div>
  </label>
</div>
```

#### Segmented Controls (`.ak-segmented-control`)
Linear set of exclusive options.
```html
<div class="ak-segmented-control">
  <label class="ak-segmented-item">
    <input type="radio" name="view" checked>
    <span class="ak-segmented-label">Daily</span>
  </label>
  <label class="ak-segmented-item">
    <input type="radio" name="view">
    <span class="ak-segmented-label">Weekly</span>
  </label>
</div>
```

### Badges (`.ak-badge`)
```html
<span class="ak-badge">Default</span>
<span class="ak-badge ak-badge-primary">Primary</span>
<span class="ak-badge ak-badge-success">Success</span>
<span class="ak-badge ak-badge-warning">Warning</span>
<span class="ak-badge ak-badge-destructive">Error</span>
<span class="ak-badge ak-badge-outline">Outline</span>

<!-- Modern Badge Variants -->
<span class="ak-badge ak-badge-soft-primary">Soft</span>
<span class="ak-badge ak-badge-dot">Dot</span>
<span class="ak-badge ak-badge-square">Square</span>
<span class="ak-badge ak-badge-pill">Pill</span>
```

### Avatars (`.ak-avatar`)
```html
<div class="ak-avatar">
  <img src="user.jpg" alt="User">
</div>
<div class="ak-avatar ak-avatar-sm">SM</div>
<div class="ak-avatar ak-avatar-lg">LG</div>
<div class="ak-avatar ak-avatar-xl">XL</div>

<!-- Modern Avatar Variants -->
<div class="ak-avatar ak-avatar-soft-primary">Soft</div>
<div class="ak-avatar ak-avatar-bordered">Bordered</div>
<div class="ak-avatar ak-avatar-squircle">Squircle</div>
<div class="ak-avatar ak-avatar-hexagon">Hexagon</div>
```

### Loaders (`.ak-loader-*`)
```html
<!-- Spinner -->
<div class="ak-loader-spinner"></div>
<div class="ak-loader-spinner ak-text-primary"></div>

<!-- Dots -->
<div class="ak-loader-dots">
  <span></span><span></span><span></span>
</div>

<!-- Progress Bar -->
<div class="ak-loader-bar ak-loader-indeterminate">
  <div class="ak-loader-bar-value"></div>
</div>
```

### Hero Section (`.ak-hero`)
```html
<section class="ak-hero">
  <div class="ak-hero-content">
    <h1 class="ak-hero-title">Welcome to AK Systems</h1>
    <p class="ak-hero-subtitle">Powerful, modular, and CSS-only.</p>
    <div class="ak-hero-actions">
      <button class="ak-btn ak-btn-primary">Get Started</button>
      <button class="ak-btn ak-btn-outline">Learn More</button>
    </div>
  </div>
</section>
```

### Layout & Grid
```html
<!-- Container -->
<div class="ak-container">...</div>

<!-- Grid System -->
<div class="ak-grid ak-grid-cols-1 ak-md:ak-grid-cols-2 ak-lg:ak-grid-cols-3 ak-gap-4">
  <div>Col 1</div>
  <div>Col 2</div>
  <div>Col 3</div>
</div>

<!-- Flex Utilities -->
<div class="ak-flex ak-flex-col ak-items-center ak-justify-between ak-gap-2">...</div>
```

### Typography
- Headings: `.ak-text-4xl`, `.ak-text-3xl`, ..., `.ak-text-lg`
- Weights: `.ak-font-bold`, `.ak-font-semibold`, `.ak-font-medium`
- Colors: `.ak-text-primary`, `.ak-text-muted`, `.ak-text-destructive`

## 4. Utility Classes (Subset)
- **Margins/Padding:** `ak-m-1` to `ak-m-12`, `ak-p-1` to `ak-p-12` (also `mt`, `mb`, `px`, `py`).
- **Width/Height:** `ak-w-full`, `ak-h-screen`, `ak-w-1/2`.
- **Display:** `ak-block`, `ak-inline-block`, `ak-hidden`, `ak-md:ak-flex`.
- **Text Align:** `ak-text-left`, `ak-text-center`, `ak-text-right`.

## 5. JavaScript Interactions
Since this is a CSS-only framework, interactivity must be handled by external JS.
The `demo/index.html` includes a reference implementation for:

- **Modals & Drawers:**
  - Functions: `openModal(id)` and `closeModal(id)`
  - Toggles `.ak-modal-open` class on the target element.
  - Handles `Escape` key and click-outside to close.
- **Dropdowns:** Toggles `.open` class.
- **Tabs:** Toggles `.active` class.

### Generic Modal Script Pattern
```javascript
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) modal.classList.add('ak-modal-open');
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) modal.classList.remove('ak-modal-open');
}

// Close on Escape or Click Outside
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        document.querySelectorAll('.ak-modal.ak-modal-open').forEach(modal => {
            modal.classList.remove('ak-modal-open');
        });
    }
});

document.addEventListener('click', (e) => {
    if (e.target.classList.contains('ak-modal')) {
        e.target.classList.remove('ak-modal-open');
    }
});
```
