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
<!-- Use a specific version (recommended for production) -->
<!-- This version is immutable and will not change -->
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@v1.3.1/dist/ak-design-system.min.css"
/>

<!-- Or use the latest version from main branch (always up-to-date) -->
<!-- Warning: This may include breaking changes without notice -->
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
3. Temporarily include any optional module links you want to test (see above).
4. Verify background, border, shadow, position, size, layout, and accessibility helpers render as expected alongside existing components.

## Versioning and CDN Usage

- **Recommended:** Pin to release tags (e.g., `.../ak-systems-css@v1.3.1/...`) to avoid unintentional updates. This ensures your site looks exactly the same, even if we release major changes.
- **Development:** Use `.../ak-systems-css@main/...` to always get the latest changes. Be aware that this might break your layout if we change class names.
- See [CHANGELOG.md](CHANGELOG.md) for detailed version history.
- Supported entries only: `css/ak-design-system/index.css` for development and `dist/ak-design-system.min.css` for production/CDN.

## Important Notes

- Developed by [ak-systems](https://ak-pro.com)
- This file must not be modified
- This is not a license to modify the framework
- You may use another CSS, but this framework must not be modified
- We are not liable for any errors or modifications

## License

This project is licensed under the [ak-systems CSS Framework License](LICENSE).
