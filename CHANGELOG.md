# Changelog

All notable changes to the ak-systems CSS Framework will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.0.0] - 2026-03-05

### Added
- **SCSS Architecture**: Complete rewrite of the utility system using modern SCSS modules (`@use`) and loops.
- **Responsive Utilities**: All utilities (Spacing, Layout, Flex, Typography, Sizing) now support responsive prefixes (e.g. `ak-md:flex`, `ak-lg:w-full`).
- **CSS Variables**: Utilities now use CSS variables internally (e.g. `var(--ak-space-4)`), allowing for runtime theming.
- **Migration Guide**: Comprehensive guide (`docs/MIGRATION_V2.md`) for upgrading from v1 to v2.

### Changed
- **Breaking Change**: Removed `!important` from all utility classes. Utilities now respect standard CSS specificity and can be overridden by custom styles.
- **Build System**: Updated `build-css.sh` to compile SCSS before bundling.

## [1.4.0] - 2026-03-05

### Added
- **Build System**: New `build-css.sh` script to bundle and minify CSS files, replacing runtime `@import` for better performance.
- **Performance**: Significant reduction in CSS file size and HTTP requests.

### Changed
- **Architecture**: Refactored Button component to use a single base class `.ak-btn` with variants, reducing redundancy by ~100 lines.
- **Cleanup**: Removed duplicate definitions for Badges and Selection Cards in `ak-components.css`.
- **Optimization**: Removed empty `ak-modifiers.css` from the build bundle.

## [1.3.2] - 2026-03-05

### Added
- **Selection Controls**: Native support for `ak-selection-grid`, `ak-selection-card`, `ak-segmented-control`, and toggle switches in core framework
- **Navigation**: Added consistent `ak-modal` based navigation drawer to `selection-controls.html` matching other components
- **Demo Pages**: New dedicated Selection Controls page with localized variants (DE/TR)

### Fixed
- **Sidebar**: Fixed sidebar links on index pages to correctly anchor to internal sections
- **Consistency**: Resolved CSS framework conflict by including selection control classes in stable release

## [1.3.1] - 2026-03-03

### Added
- **Localization**: Added full German (DE) and Turkish (TR) localization for all demo pages (Buttons, Modals, Typography, Loaders, Upload, Layout, Cards, Alerts, Tables, Forms)
- **Navigation**: Consistent "View All Variants" / "Alle Varianten" / "Tüm Varyantlar" links across all index pages and languages

### Changed
- **Demo Pages**: Harmonized structure and navigation for all component demos across EN, DE, and TR
- **Index Pages**: Updated index.html, index.de.html, and index.tr.html to include direct links to all localized component demos

## [1.3.0] - 2025-12-30

### Added
- **Model Context Protocol (MCP)**: New `docs/ak-design-system.mcp.md` providing rules, mental models, and decision logic for AI agents working with the framework
- **MCP Documentation**: Added MCP guidance sections to all README files (README.md, README.de.md, README.tr.md)
- **Release Process**: Updated release checklist to include MCP review for major releases

### Changed
- **Documentation**: Enhanced README files with clear documentation hierarchy (MCP, AGENT_CONTEXT.md, demo/index.html)
- **Release Checklist**: Added step to review MCP for breaking changes in major releases

## [1.2.0] - 2025-12-24

### Added
- **Popover Component**: New `.ak-popover` component with multiple positions (top, bottom, left, right), size variants (sm, default, lg), and interactive support
- **Component Documentation**: Comprehensive documentation for all components in `docs/framework_analysis.md`
- **Coverage Analysis**: New `docs/COMPONENT_COVERAGE.md` documenting component coverage status and gaps
- **Archive System**: Created `docs/Archiv/` for outdated documentation

### Changed
- **Build Process**: Improved build script with real CSS minification (19-20% reduction)
- **Documentation**: Extended framework analysis with all implemented components
- **Demo Pages**: Added Hero section and Image utilities examples to demo pages

### Fixed
- **Documentation**: Moved outdated documentation to archive (CSS_Analysis_Report.md, CSS_CLEANUP_PLAN.md)

### Documentation
- Added comprehensive component usage patterns and best practices
- Updated coverage assessment to 90-93%
- Documented all 20+ components with code examples

## [1.1.0] - Previous Release

### Added
- Hero component (`.ak-hero`)
- Image utilities (`.ak-img-fluid`, `.ak-img-thumbnail`, `.ak-object-cover`, `.ak-object-contain`)

## [1.0.3] - Previous Release

### Added
- Badge, Progress, Switch, and Dropdown components

## [1.0.2] - Previous Release

### Added
- Extended components section with avatars, navigation, and tooltips

## [1.0.1] - Previous Release

### Initial release with core components

## [1.0.0] - Initial Release

### Added
- Core design system
- Layout components (Header, Footer, Sidebar)
- Form components
- Card components
- Modal components
- Alert components
- Table components
- Navigation components (Breadcrumbs, Tabs, Pagination)
- Loader/Spinner framework
- Utility classes

[1.3.0]: https://github.com/ak-hosting/ak-systems-css/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/ak-hosting/ak-systems-css/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/ak-hosting/ak-systems-css/compare/v1.0.3...v1.1.0
[1.0.3]: https://github.com/ak-hosting/ak-systems-css/compare/v1.0.2...v1.0.3
[1.0.2]: https://github.com/ak-hosting/ak-systems-css/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/ak-hosting/ak-systems-css/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/ak-hosting/ak-systems-css/releases/tag/v1.0.0

