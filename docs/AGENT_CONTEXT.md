# AK Design System - Agent Context & Usage Guide

This document defines the rules, classes, and structures for the **AK Design System**.
AI Agents should use this context to generate compliant HTML/CSS without hallucinating non-existent classes.

## 1. Core Principles
- **Prefix:** All classes use the `ak-` prefix (e.g., `ak-btn`, `ak-card`).
- **No External Frameworks:** Do not use Bootstrap, Tailwind, or Bulma classes.
- **Icons:** Use `lucide` icons with `data-lucide="icon-name"`.
- **Dark Mode:** Supported via `.ak-theme-dark` on `<body>`.

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
```

### Forms (`.ak-form-group`)
```html
<div class="ak-form-group">
  <label class="ak-form-label">Email</label>
  <input type="email" class="ak-input" placeholder="hello@example.com">
  <p class="ak-form-hint">We'll never share your email.</p>
</div>

<!-- Select -->
<select class="ak-select"><option>Option 1</option></select>

<!-- Checkbox -->
<label class="ak-checkbox">
  <input type="checkbox">
  <span>I agree</span>
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

### Badges (`.ak-badge`)
```html
<span class="ak-badge">Default</span>
<span class="ak-badge ak-badge-primary">Primary</span>
<span class="ak-badge ak-badge-success">Success</span>
<span class="ak-badge ak-badge-warning">Warning</span>
<span class="ak-badge ak-badge-destructive">Error</span>
<span class="ak-badge ak-badge-outline">Outline</span>
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
Since this is a CSS-only framework, interactivity (Modals, Dropdowns, Tabs) must be handled by custom JS that toggles:
- `.active` class for Tabs/Modals.
- `.open` class for Dropdowns.
