# Framework Analysis: Layout & Structural Components

This document outlines the analysis and implementation of structural components (Hero, Footer) and image utilities within the `ak-design-system` framework.

## 1. Analysis Request
**Objective:** Determine if high-level components like Hero sections, Footers, and Image handling utilities should be part of the core framework to ensure 90-95% CDN coverage.
**Conclusion:** Yes. While these can be built with utilities, standardized classes significantly speed up prototyping and ensure consistency across projects.

## 2. Current State & Implementations

### A. Footer (`.ak-footer`)
*   **Status:** ✅ Existing
*   **Location:** `css/ak-design-system/ak-layout.css`
*   **Features:**
    *   Sticky footer support via `margin-top: auto`
    *   Standardized padding and top border
    *   Responsive behavior
*   **Usage:**
    ```html
    <footer class="ak-footer">
      <div class="ak-container">
        <!-- Content -->
      </div>
    </footer>
    ```

### B. Header (`.ak-header`)
*   **Status:** ✅ Existing
*   **Location:** `css/ak-design-system/ak-layout.css`
*   **Features:**
    *   Sticky positioning (`position: sticky`)
    *   Flexbox layout for brand/nav/actions
    *   Mobile optimization

### C. Hero Section (`.ak-hero`)
*   **Status:** ✨ Newly Implemented
*   **Location:** `css/ak-design-system/ak-layout.css`
*   **Why added:** To provide a standard entry point for landing pages with consistent spacing and typography centering.
*   **Features:**
    *   Centered content layout
    *   Responsive padding (larger on desktop, compact on mobile)
    *   Typography presets for Title and Subtitle
*   **Usage:**
    ```html
    <section class="ak-hero">
      <div class="ak-hero-content">
        <h1 class="ak-hero-title">Welcome to AK Systems</h1>
        <p class="ak-hero-subtitle">Building the future of digital infrastructure.</p>
        <div class="ak-hero-actions">
          <button class="ak-btn ak-btn-primary">Get Started</button>
          <button class="ak-btn ak-btn-outline">Learn More</button>
        </div>
      </div>
    </section>
    ```

### D. Image Utilities (`.ak-img-*`, `.ak-object-*`)
*   **Status:** ✨ Newly Implemented
*   **Location:** `css/ak-design-system/ak-utilities.css`
*   **Why added:** To handle responsive images and object-fit properties without custom CSS.
*   **Features:**
    *   `.ak-img-fluid`: Makes images responsive (max-width: 100%, height: auto)
    *   `.ak-img-thumbnail`: Adds border and padding for gallery-style images
    *   `.ak-object-cover` / `.ak-object-contain`: Controls image aspect ratio behavior
*   **Usage:**
    ```html
    <img src="image.jpg" class="ak-img-fluid ak-rounded" alt="Responsive Image">
    <img src="avatar.jpg" class="ak-w-20 ak-h-20 ak-object-cover ak-rounded-full">
    ```

## 3. Recommendation for Agents
When building new pages using `ak-design-system`:
1.  **Always use** `.ak-header` and `.ak-footer` for the main layout shell.
2.  **Prefer** `.ak-hero` for the top section of landing pages instead of custom flex utilities.
3.  **Always use** `.ak-img-fluid` for content images to prevent overflow issues on mobile.
4.  **Use** `.ak-object-cover` for avatars or card images that need to fill a specific dimension without distortion.

This structure ensures we meet the "95% CDN coverage" goal, reducing the need for custom CSS in individual projects.
