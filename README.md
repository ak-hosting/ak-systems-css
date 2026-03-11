# ak-systems CSS Framework

A lightweight CSS framework by ak-systems for rapid prototyping.

*Read this in other languages: [Deutsch](README.de.md), [Türkçe](README.tr.md)*

## Installation

### Production (CDN) - Recommended

Use the jsDelivr CDN to include the minified CSS. This is the most reliable way to use the framework.

```html
<!-- Use a specific version (recommended for production) -->
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@v2.0.2/dist/ak-design-system.min.css"
/>
```

### Development (Local)

Only use this if you are contributing to the framework itself.

```html
<link rel="stylesheet" href="dist/ak-design-system.css">
```

### Bleeding Edge (Unstable)

If you need the absolute latest changes from the `main` branch (not recommended for production):

```html
<!-- Warning: This may include breaking changes without notice -->
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@main/dist/ak-design-system.min.css"
/>
```

## Build Process

The project now uses a robust build pipeline with SCSS compilation and minification.

To generate the distribution files in `dist/`, run the build script:

```bash
./build-css.sh
```

This will:
1. Compile SCSS modules (in `src/scss`) to `css/ak-design-system/*.css`
2. Bundle all CSS files into `dist/ak-design-system.css`
3. Minify the bundle to `dist/ak-design-system.min.css`

If you already have up-to-date CSS files in `css/ak-design-system/` and only want to bundle + minify:

```bash
./build.sh
```

## Architecture (v2.0+)

Version 2.0 introduces a modern SCSS-based architecture for utilities, removing `!important` and enabling easy overrides.

- **Core**: Variables & Reset (`ak-core.css`, `ak-base.css`)
- **Layout**: Grid, Containers (`ak-layout.css`)
- **Components**: Buttons, Cards, etc. (`ak-components.css`, `ak-components-extended.css`)
- **Backgrounds**: Patterns and decorative backgrounds (`ak-backgrounds.css`)
- **Utilities**: Generated from SCSS modules (`ak-utilities.css`)
  - Spacing (`m-4`, `p-2`)
  - Layout (`block`, `absolute`)
  - Flexbox (`flex`, `justify-center`)
  - Typography (`text-center`, `font-bold`)
  - Sizing (`w-full`, `h-screen`)
  - Accessibility, print, pointer-events, user-select, whitespace/break, min-size, flex item, and aspect-ratio helpers

All utilities now support responsive prefixes (e.g. `ak-md:flex`) and use CSS variables internally.

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

<!-- Modern Variants (Soft, Glass, Gradient, Shapes) - see AGENT_CONTEXT.md for full list -->
<button class="ak-btn ak-btn-soft-primary ak-btn-rounded">Modern Round</button>
```

### Loaders / Spinners

```html
<!-- Basic Spinner -->
<div class="ak-loader-spinner ak-loader-primary ak-loader-md"></div>

<!-- Dots Loader -->
<div class="ak-loader-dots ak-loader-primary ak-loader-md">
  <span></span><span></span><span></span>
</div>
```

### Header & Footer Variants

```html
<!-- Centered Header -->
<header class="ak-header ak-header-centered">
  <div class="ak-header-content">
    <nav class="ak-header-nav">...</nav>
    <div class="ak-header-brand">Logo</div>
    <div class="ak-header-actions">...</div>
  </div>
</header>

<!-- Multi-Column Footer -->
<footer class="ak-footer ak-footer-multi-column">
  <div class="ak-footer-content">
    <div class="ak-footer-column">
      <h5 class="ak-footer-column-title">Company</h5>
      <a href="#">About</a>
      <a href="#">Contact</a>
    </div>
  </div>
</footer>
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

## AI / MCP Guidance

This project includes a **Model Context Protocol (MCP)** for AI agents (Codex, Cursor, Claude, and other LLMs). The MCP provides rules, mental models, and decision logic to help AI agents work correctly with the AK Design System without requiring full code analysis.

**Documentation hierarchy:**
- **MCP** ([`docs/ak-design-system.mcp.md`](docs/ak-design-system.mcp.md)): Rules, mental model, and decision framework
- **AGENT_CONTEXT.md** ([`docs/AGENT_CONTEXT.md`](docs/AGENT_CONTEXT.md)): Technical reference with class lists and code examples
- **demo/index.html**: Source of truth for HTML patterns

The MCP is designed for external use by AI agents and focuses on principles and structure, while AGENT_CONTEXT.md contains specific class names and implementation details.

## Quick Smoke Test (local)

1. Serve the repo locally (e.g., `python3 -m http.server` from the project root).
2. Open `demo/index.html` (or a localized variant) in the browser.
3. Verify background, border, shadow, position, size, layout, and accessibility helpers render as expected alongside existing components.

## Versioning and CDN Usage

- **Recommended:** Pin to release tags (e.g., `.../ak-systems-css@v1.3.1/...`) to avoid unintentional updates. This ensures your site looks exactly the same, even if we release major changes.
- **Development:** Use `.../ak-systems-css@main/...` to always get the latest changes. Be aware that this might break your layout if we change class names.
- See [CHANGELOG.md](CHANGELOG.md) for detailed version history.
- Supported entries only: `dist/ak-design-system.css` for development and `dist/ak-design-system.min.css` for production/CDN.

## Important Notes

- Developed by [ak-systems](https://ak-pro.com)
- This file must not be modified
- This is not a license to modify the framework
- You may use another CSS, but this framework must not be modified
- We are not liable for any errors or modifications

## License

This project is licensed under the [ak-systems CSS Framework License](LICENSE).
