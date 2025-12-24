# ak-systems CSS Framework

A lightweight CSS framework by ak-systems for rapid prototyping.

*Read this in other languages: [Deutsch](README.de.md), [Türkçe](README.tr.md)*

## Installation

Use the canonical CSS entry (development):

```html
<link rel="stylesheet" href="css/ak-design-system/index.css">
```

Production/CDN entry:

```html
<!-- Use a specific version (recommended) -->
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@v1.1.0/dist/ak-design-system.min.css"
/>

<!-- Or use the latest version from main branch (development only) -->
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@main/dist/ak-design-system.min.css"
/>
```

## Build Process

To generate the distribution files in `dist/`, run the build script:

```bash
./build.sh
```

This will concatenate all source files into `dist/ak-design-system.css` and create a placeholder minified file.

## Usage

### Container

```html
<div class="ak-container">
  <!-- Content here -->
</div>
```

### Grid System

```html
<div class="ak-grid ak-grid-3 ak-gap-4">
  <div>Column 1</div>
  <div>Column 2</div>
  <div>Column 3</div>
</div>
```

### Buttons

```html
<button class="ak-btn">Standard Button</button>
<button class="ak-btn ak-btn-primary">Primary Button</button>
<button class="ak-btn ak-btn-destructive">Destructive Button</button>
```

## Mobile & Touch Best Practices

- Recommended viewport meta tag:
  ```html
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  ```
  Ensures responsive breakpoints and mobile-first behavior.
- Mobile-optimized components:
  - Buttons and icon buttons sized for touch
  - Responsive grid and layout behavior
  - Sidebar and footer navigation behavior on mobile
- Accessibility & motion:
  - Support for `prefers-reduced-motion`
  - Keyboard and focus-visible support

**Recommendations:** For custom components (e.g., checkboxes, radios, links), use touch targets of at least 24×24px. This aligns with accessibility best practices and is a usage recommendation, not enforced by the framework.

## Demo

You can find a demo page with all components here: [ak-systems CSS Demo](https://ak-hosting.github.io/ak-systems-css/demo/)

Note: The demo page is available once GitHub Pages is enabled for the repository. Until then, open the local demo at `demo/index.html` via a local server.

## Quick Smoke Test (local)

1. Serve the repo locally (e.g., `python3 -m http.server` from the project root).
2. Open `demo/index.html` (or a localized variant) in the browser.
3. Temporarily include any optional module links you want to test (see above).
4. Verify background, border, shadow, position, size, layout, and accessibility helpers render as expected alongside existing components.

## Versioning and CDN Usage

- Pin to release tags when available to avoid unintentional updates, e.g. `https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@v1.0.3/dist/ak-design-system.min.css`.
- Supported entries only: `css/ak-design-system/index.css` for development and `dist/ak-design-system.min.css` for production/CDN.

## Important Notes

- Developed by [ak-systems](https://ak-pro.com)
- This file must not be modified
- This is not a license to modify the framework
- You may use another CSS, but this framework must not be modified
- We are not liable for any errors or modifications

## License

This project is licensed under the [ak-systems CSS Framework License](LICENSE).
