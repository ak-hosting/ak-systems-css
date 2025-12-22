# Fehlende CSS-Klassen in Demo-Dateien - Vollständiger Report

## Zusammenfassung

Die Demo-Dateien verwenden **viele CSS-Klassen, die nicht im Design System definiert sind**. Diese müssen entweder:
1. Zum Design System hinzugefügt werden, ODER
2. Durch existierende Klassen ersetzt werden

## Kategorisierte Liste der fehlenden Klassen

### ✅ EXISTIERENDE Klassen (werden korrekt verwendet)
- `.ak-btn`, `.ak-btn-primary`, `.ak-btn-secondary`, `.ak-btn-ghost`, `.ak-btn-destructive`
- `.ak-btn-sm`, `.ak-btn-lg`
- `.ak-card`, `.ak-card-header`, `.ak-card-body`, `.ak-card-footer`
- `.ak-container`
- `.ak-flex`, `.ak-flex-between`, `.ak-items-center`, `.ak-gap-*`
- `.ak-grid`, `.ak-grid-2`, `.ak-grid-3`, `.ak-grid-4`
- `.ak-header`, `.ak-sidebar`, `.ak-sidebar-header`, `.ak-sidebar-nav`
- `.ak-main` (existiert in ak-layout.css)
- `.ak-modal`, `.ak-modal-header`, `.ak-modal-body`, `.ak-modal-footer`, `.ak-modal-content`
- `.ak-input`, `.ak-textarea`, `.ak-select`
- `.ak-form-group`, `.ak-form-label`, `.ak-form-help`, `.ak-form-error`
- `.ak-checkbox`, `.ak-radio`, `.ak-switch`
- `.ak-toast` (existiert bereits!)
- Alle Spacing-Utilities (`.ak-m-*`, `.ak-p-*`, `.ak-gap-*`)
- Alle Text-Utilities (`.ak-text-*`, `.ak-font-*`)

### ❌ FEHLENDE Klassen (müssen hinzugefügt werden)

#### Typography & Text
1. `.ak-link` - Link-Styling (wird verwendet: `<a class="ak-link">`)
2. `.ak-blockquote` - Blockquote (wird verwendet, aber nur `blockquote` ohne Klasse existiert)
3. `.ak-code` - Inline Code (wird verwendet: `<code class="ak-code">`)
4. `.ak-section` - Section Container (wird verwendet: `<section class="ak-section">`)

#### Buttons
5. `.ak-btn-accent` - Accent Button Variante
6. `.ak-btn-link` - Link Button Variante  
7. `.ak-btn-outline` - Outline Button Variante
8. `.ak-loading` - Loading State (`.ak-btn-loading` existiert, aber `.ak-loading` fehlt)
9. `.ak-loading-spinner` - Loading Spinner Element

#### Cards
10. `.ak-card-title` - Card Titel (wird verwendet, aber nicht definiert)
11. `.ak-card-description` - Card Beschreibung (wird verwendet)
12. `.ak-card-content` - Card Content (`.ak-card-body` existiert, aber `.ak-card-content` wird verwendet)
13. `.ak-card-img` - Card Bild Styling

#### Forms
14. `.ak-form` - Form Container (wird verwendet: `<form class="ak-form">`)
15. `.ak-form-field` - Form Field Container (wird verwendet statt `.ak-form-group`)
16. `.ak-form-hint` - Form Hint Text (`.ak-form-help` existiert, aber `.ak-form-hint` wird verwendet)
17. `.ak-checkbox-group` - Checkbox Group Container
18. `.ak-checkbox-input` - Checkbox Input Element
19. `.ak-checkbox-label` - Checkbox Label Element
20. `.ak-radio-input` - Radio Input Element
21. `.ak-radio-label` - Radio Label Element

#### Alerts (komplett fehlend!)
22. `.ak-alert` - Alert Container
23. `.ak-alert-success` - Success Alert
24. `.ak-alert-warning` - Warning Alert
25. `.ak-alert-danger` - Danger Alert
26. `.ak-alert-icon` - Alert Icon
27. `.ak-alert-title` - Alert Titel
28. `.ak-alert-description` - Alert Beschreibung

#### Badges (komplett fehlend!)
29. `.ak-badge` - Badge Container
30. `.ak-badge-success` - Success Badge
31. `.ak-badge-warning` - Warning Badge
32. `.ak-badge-danger` - Danger Badge

#### Tables (komplett fehlend!)
33. `.ak-table` - Table Container
34. `.ak-table-container` - Table Wrapper

#### Modals
35. `.ak-modal-title` - Modal Titel (wird verwendet, aber nicht definiert)

#### Utility Classes - Width/Height (fehlend!)
36. `.ak-w-4`, `.ak-w-8`, `.ak-w-12` - Width Utilities
37. `.ak-h-4`, `.ak-h-8`, `.ak-h-12`, `.ak-h-20` - Height Utilities

#### Utility Classes - Background (fehlend!)
38. `.ak-bg-primary` - Primary Background
39. `.ak-bg-accent` - Accent Background
40. `.ak-bg-muted` - Muted Background
41. `.ak-bg-card` - Card Background

#### Utility Classes - Border Radius (fehlend!)
42. `.ak-rounded` - Rounded Border
43. `.ak-rounded-full` - Full Rounded Border

#### Responsive Grid Classes (fehlend!)
44. `.ak-grid-cols-1`, `.ak-grid-cols-2`, `.ak-grid-cols-3`, `.ak-grid-cols-4` - Grid Columns
45. `.ak-md:ak-grid-cols-2`, `.ak-md:ak-grid-cols-3` - Responsive Grid (Medium)
46. `.ak-lg:ak-grid-cols-3` - Responsive Grid (Large)
47. `.ak-sm:ak-grid-cols-2` - Responsive Grid (Small)
48. `.ak-md:ak-hidden` - Responsive Hide (Medium)

#### State Classes
49. `.ak-active` - Active State Utility (wird verwendet, aber nicht als Utility definiert)

### 🟡 BENUTZERDEFINIERTE Demo-Klassen (sollten durch Design System ersetzt werden)

Diese Klassen sind nur in `<style>` Tags der Demo-Dateien definiert:

1. `.demo-section` → sollte durch `.ak-card` oder neue `.ak-section` ersetzt werden
2. `.color-demo` → sollte durch Utility-Klassen (`.ak-w-20`, `.ak-h-20`, `.ak-bg-*`) ersetzt werden
3. `.spacing-demo` → sollte durch Utility-Klassen ersetzt werden
4. `.modal-overlay` → sollte durch `.ak-modal` ersetzt werden (bereits vorhanden!)
5. `.toast` → sollte durch `.ak-toast` ersetzt werden (bereits vorhanden!)
6. `.code-block` → sollte durch neue `.ak-code-block` ersetzt werden
7. `.language-selector` → sollte durch Utility-Klassen ersetzt werden
8. `.content-section` → sollte durch `.ak-section` ersetzt werden

## Prioritäten

### HOCH (wird häufig verwendet)
- `.ak-section`
- `.ak-link`
- `.ak-code`
- `.ak-btn-outline`
- `.ak-card-title`, `.ak-card-description`, `.ak-card-content`
- `.ak-form`, `.ak-form-field`, `.ak-form-hint`
- `.ak-alert-*` (komplettes Alert-System)
- `.ak-badge-*` (komplettes Badge-System)
- `.ak-table-*` (komplettes Table-System)
- Responsive Grid-Klassen
- Width/Height Utilities
- Background Utilities
- Border Radius Utilities

### MITTEL (wird gelegentlich verwendet)
- `.ak-btn-accent`, `.ak-btn-link`
- `.ak-loading`, `.ak-loading-spinner`
- `.ak-blockquote`
- `.ak-modal-title`
- `.ak-checkbox-*`, `.ak-radio-*` (wenn nicht bereits vorhanden)

### NIEDRIG (kann durch existierende ersetzt werden)
- `.ak-active` (kann durch existierende Utilities ersetzt werden)

## Nächste Schritte

1. Alle fehlenden Klassen zum Design System hinzufügen
2. Demo-Dateien anpassen, um benutzerdefinierte `<style>` Tags zu entfernen
3. Alle Klassen sollten mit `ak-` Präfix beginnen
4. Responsive Utilities konsistent implementieren

