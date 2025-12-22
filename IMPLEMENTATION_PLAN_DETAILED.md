# Detaillierter Implementierungsplan: Fehlende CSS-Klassen

## Übersicht
Systematische Hinzufügung aller 64+ fehlenden Klassen zum Design System, damit die Demo-Dateien ausschließlich Design System Klassen verwenden.

## Implementierungsreihenfolge

### Phase 1: Typography & Base (ak-base.css)
**Datei:** `css/ak-design-system/ak-base.css` (am Ende hinzufügen)

1. `.ak-link` - Link-Styling
2. `.ak-code` - Inline Code
3. `.ak-blockquote` - Blockquote
4. `.ak-section` - Section Container
5. `.ak-code-block` - Code Block (für `<pre>`)

### Phase 2: Button Varianten (ak-components.css)
**Datei:** `css/ak-design-system/ak-components.css` (nach `.ak-btn-destructive`)

6. `.ak-btn-accent` - Accent Button
7. `.ak-btn-link` - Link Button
8. `.ak-btn-outline` - Outline Button
9. `.ak-loading` - Loading State
10. `.ak-loading-spinner` - Loading Spinner

### Phase 3: Card Erweiterungen (ak-components.css)
**Datei:** `css/ak-design-system/ak-components.css` (nach `.ak-card-footer`)

11. `.ak-card-title` - Card Titel
12. `.ak-card-description` - Card Beschreibung
13. `.ak-card-content` - Card Content (Alias für body)
14. `.ak-card-img` - Card Bild

### Phase 4: Form Erweiterungen (ak-components.css)
**Datei:** `css/ak-design-system/ak-components.css` (nach `.ak-form-error`)

15. `.ak-form` - Form Container
16. `.ak-form-field` - Form Field (Alias für group)
17. `.ak-form-hint` - Form Hint (Alias für help)
18. `.ak-checkbox-group` - Checkbox Group
19. `.ak-checkbox-input` - Checkbox Input
20. `.ak-checkbox-label` - Checkbox Label
21. `.ak-radio-input` - Radio Input
22. `.ak-radio-label` - Radio Label

### Phase 5: Alert System (ak-components.css) - NEU
**Datei:** `css/ak-design-system/ak-components.css` (nach Forms, vor Modals)

23. `.ak-alert` - Alert Container
24. `.ak-alert-success` - Success Alert
25. `.ak-alert-warning` - Warning Alert
26. `.ak-alert-danger` - Danger Alert
27. `.ak-alert-icon` - Alert Icon
28. `.ak-alert-title` - Alert Titel
29. `.ak-alert-description` - Alert Beschreibung

### Phase 6: Badge System (ak-components.css) - NEU
**Datei:** `css/ak-design-system/ak-components.css` (nach Alerts)

30. `.ak-badge` - Badge Container
31. `.ak-badge-success` - Success Badge
32. `.ak-badge-warning` - Warning Badge
33. `.ak-badge-danger` - Danger Badge

### Phase 7: Table System (ak-components.css) - NEU
**Datei:** `css/ak-design-system/ak-components.css` (nach Badges)

34. `.ak-table` - Table Container
35. `.ak-table-container` - Table Wrapper
36. `.ak-table-header` - Table Header
37. `.ak-table-body` - Table Body
38. `.ak-table-footer` - Table Footer

### Phase 8: Modal Erweiterungen (ak-components.css)
**Datei:** `css/ak-design-system/ak-components.css` (in Modal-Bereich)

39. `.ak-modal-title` - Modal Titel

### Phase 9: Width/Height Utilities (ak-utilities.css)
**Datei:** `css/ak-design-system/ak-utilities.css` (am Ende hinzufügen)

40-43. Width/Height Utilities (`.ak-w-*`, `.ak-h-*`, `.ak-w-full`, `.ak-h-full`)

### Phase 10: Background Utilities (ak-utilities.css)
**Datei:** `css/ak-design-system/ak-utilities.css` (nach Width/Height)

44-51. Background Utilities (`.ak-bg-*`)

### Phase 11: Border Radius Utilities (ak-utilities.css)
**Datei:** `css/ak-design-system/ak-utilities.css` (nach Background)

52-57. Border Radius Utilities (`.ak-rounded-*`)

### Phase 12: Responsive Grid (ak-layout.css)
**Datei:** `css/ak-design-system/ak-layout.css` (nach Grid-Bereich)

58-63. Responsive Grid Classes (`.ak-grid-cols-*`, `.ak-md:*`, `.ak-lg:*`)

### Phase 13: State Utilities (ak-utilities.css)
**Datei:** `css/ak-design-system/ak-utilities.css` (am Ende)

64. `.ak-active` - Active State

## Demo-Dateien Anpassung (nach Implementierung)

**Dateien:** `demo/index.html`, `demo/index.de.html`, `demo/index.en.html`, `demo/index.tr.html`

1. `<style>` Tags komplett entfernen
2. Benutzerdefinierte Klassen ersetzen:
   - `.demo-section` → `.ak-section` oder `.ak-card`
   - `.color-demo` → `.ak-w-20 .ak-h-20 .ak-bg-primary` etc.
   - `.spacing-demo` → Utility-Klassen
   - `.modal-overlay` → `.ak-modal`
   - `.toast` → `.ak-toast`
   - `.code-block` → `.ak-code-block`
   - `.language-selector` → Utility-Klassen
   - `.content-section` → `.ak-section`
   - `active` → `.ak-active` (wo nötig)

## Test & Validierung

1. Alle Demo-Dateien lokal testen
2. Prüfen, dass keine benutzerdefinierten Styles mehr vorhanden sind
3. Prüfen, dass alle Klassen im CSS definiert sind
4. Neue Version taggen (v1.1.0)

