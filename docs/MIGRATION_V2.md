# Migration Guide to AK Design System v2.0

## ⚠️ Breaking Changes

Version 2.0 introduces significant architectural improvements that may require changes to your code if you were relying on implementation details or `!important` overrides.

### 1. Removal of `!important` from Utilities

**Old Behavior (v1.x):**
All utility classes used `!important` to force overrides.
```css
.ak-m-4 { margin: 16px !important; }
```

**New Behavior (v2.0):**
Utilities use standard CSS specificity and CSS variables.
```css
.ak-m-4 { margin: var(--ak-space-4, 16px); }
```

**Impact:**
- Utilities can now be overridden by custom CSS without needing `!important`.
- If you were relying on utilities to brute-force override other styles, check your layouts.

### 2. CSS Variables for Spacing

Utilities now use CSS variables (`--ak-space-*`) internally. This allows for runtime theming of spacing scales.

### 3. Reduced Specificity

By removing `!important`, the specificity of utility classes is lower. Ensure your custom CSS is loaded *after* the framework CSS if you intend to override it.

## Upgrade Steps

1. **Update CSS Link:**
   Point to the new v2 distribution file (once released).
   
2. **Check Overrides:**
   Search your codebase for `!important` usage that was fighting against framework utilities. You can likely remove your `!important` now.

3. **Verify Layouts:**
   Check complex layouts where utilities might have been used to force positioning.
