# ak-systems CSS Framework

A lightweight CSS framework by ak-systems for rapid prototyping.

*Read this in other languages: [Deutsch](README.de.md), [Türkçe](README.tr.md)*

## Installation

Include the CSS framework in your HTML document:

```html
<link rel="stylesheet" href="https://ak-hosting.github.io/ak-systems-css/css/ak-design-system.css">
```

Note: GitHub Pages must be enabled for this repository to serve the CDN link. If not enabled, the link will return 404.

Alternatively, you can download the CSS files and include them locally:

```html
<link rel="stylesheet" href="css/ak-design-system.css">
```

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

### Optional Utility Modules (opt-in)

Load after the core file when you need them:

```html
<link rel="stylesheet" href="css/ak-design-system.css">
<link rel="stylesheet" href="css/ak-utilities-bg.css">
<link rel="stylesheet" href="css/ak-utilities-border.css">
<link rel="stylesheet" href="css/ak-utilities-shadow.css">
<link rel="stylesheet" href="css/ak-utilities-position.css">
<link rel="stylesheet" href="css/ak-utilities-size.css">
<link rel="stylesheet" href="css/ak-layout-helpers.css">
<link rel="stylesheet" href="css/ak-accessibility.css">
```

Modules are independent and optional. Use only what you need.

## Demo

You can find a demo page with all components here: [ak-systems CSS Demo](https://ak-hosting.github.io/ak-systems-css/demo/)

Note: The demo page is available once GitHub Pages is enabled for the repository. Until then, open the local demo at `demo/index.html` via a local server.

## Quick Smoke Test (local)

1. Serve the repo locally (e.g., `python3 -m http.server` from the project root).
2. Open `demo/index.html` (or a localized variant) in the browser.
3. Temporarily include any optional module links you want to test (see above).
4. Verify background, border, shadow, position, size, layout, and accessibility helpers render as expected alongside existing components.

## Versioning and CDN Usage

- Pin to release tags when available to avoid unintentional updates, e.g. `https://ak-hosting.github.io/ak-systems-css/css/ak-design-system.css?v=<tag>`.
- Keep optional modules on the same tag/version as the core file to ensure token compatibility.

## Important Notes

- Developed by [ak-systems](https://ak-pro.com)
- This file must not be modified
- This is not a license to modify the framework
- You may use another CSS, but this framework must not be modified
- We are not liable for any errors or modifications

## License

This project is licensed under the [ak-systems CSS Framework License](LICENSE).
