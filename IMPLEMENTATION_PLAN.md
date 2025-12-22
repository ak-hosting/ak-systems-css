# Implementierungsplan: Fehlende CSS-Klassen zum Design System hinzufügen

## Ziel
Alle in den Demo-Dateien verwendeten Klassen müssen im Design System definiert sein. Keine benutzerdefinierten Styles in Demo-Dateien.

## Systematische Implementierung

### Phase 1: Typography & Base Classes (ak-base.css)

1. `.ak-link` - Link-Styling Klasse
2. `.ak-code` - Inline Code Klasse (existiert als `code`, aber `.ak-code` fehlt)
3. `.ak-blockquote` - Blockquote Klasse (existiert als `blockquote`, aber `.ak-blockquote` fehlt)
4. `.ak-section` - Section Container
5. `.ak-code-block` - Code Block (für `<pre>` mit Klasse)

### Phase 2: Button Varianten (ak-components.css)

6. `.ak-btn-accent` - Accent Button Variante
7. `.ak-btn-link` - Link Button Variante
8. `.ak-btn-outline` - Outline Button Variante
9. `.ak-loading` - Loading State (allgemein, nicht nur für Buttons)
10. `.ak-loading-spinner` - Loading Spinner Element

### Phase 3: Card Komponenten (ak-components.css)

11. `.ak-card-title` - Card Titel
12. `.ak-card-description` - Card Beschreibung
13. `.ak-card-content` - Card Content (Alias für `.ak-card-body` oder separate Klasse)
14. `.ak-card-img` - Card Bild Styling

### Phase 4: Form Komponenten (ak-components.css)

15. `.ak-form` - Form Container
16. `.ak-form-field` - Form Field Container (Alias für `.ak-form-group` oder separate)
17. `.ak-form-hint` - Form Hint Text (Alias für `.ak-form-help` oder separate)
18. `.ak-checkbox-group` - Checkbox Group Container
19. `.ak-checkbox-input` - Checkbox Input Element
20. `.ak-checkbox-label` - Checkbox Label Element
21. `.ak-radio-input` - Radio Input Element
22. `.ak-radio-label` - Radio Label Element

### Phase 5: Alert System (ak-components.css) - NEU

23. `.ak-alert` - Alert Container
24. `.ak-alert-success` - Success Alert
25. `.ak-alert-warning` - Warning Alert
26. `.ak-alert-danger` - Danger Alert
27. `.ak-alert-icon` - Alert Icon
28. `.ak-alert-title` - Alert Titel
29. `.ak-alert-description` - Alert Beschreibung

### Phase 6: Badge System (ak-components.css) - NEU

30. `.ak-badge` - Badge Container
31. `.ak-badge-success` - Success Badge
32. `.ak-badge-warning` - Warning Badge
33. `.ak-badge-danger` - Danger Badge

### Phase 7: Table System (ak-components.css) - NEU

34. `.ak-table` - Table Container
35. `.ak-table-container` - Table Wrapper
36. `.ak-table-header` - Table Header (optional)
37. `.ak-table-body` - Table Body (optional)
38. `.ak-table-footer` - Table Footer (optional)

### Phase 8: Modal Erweiterungen (ak-components.css)

39. `.ak-modal-title` - Modal Titel

### Phase 9: Utility Classes - Width/Height (ak-utilities.css)

40. `.ak-w-4`, `.ak-w-8`, `.ak-w-12`, `.ak-w-16`, `.ak-w-20` - Width Utilities
41. `.ak-h-4`, `.ak-h-8`, `.ak-h-12`, `.ak-h-16`, `.ak-h-20` - Height Utilities
42. `.ak-w-full` - Full Width
43. `.ak-h-full` - Full Height

### Phase 10: Utility Classes - Background (ak-utilities.css)

44. `.ak-bg-primary` - Primary Background
45. `.ak-bg-accent` - Accent Background
46. `.ak-bg-muted` - Muted Background
47. `.ak-bg-card` - Card Background (alias für surface)
48. `.ak-bg-secondary` - Secondary Background
49. `.ak-bg-success` - Success Background
50. `.ak-bg-destructive` - Destructive Background
51. `.ak-bg-surface` - Surface Background

### Phase 11: Utility Classes - Border Radius (ak-utilities.css)

52. `.ak-rounded` - Rounded Border (base radius)
53. `.ak-rounded-sm` - Small Rounded
54. `.ak-rounded-md` - Medium Rounded
55. `.ak-rounded-lg` - Large Rounded
56. `.ak-rounded-full` - Full Rounded
57. `.ak-rounded-none` - No Radius

### Phase 12: Responsive Grid Classes (ak-layout.css)

58. `.ak-grid-cols-1`, `.ak-grid-cols-2`, `.ak-grid-cols-3`, `.ak-grid-cols-4` - Grid Columns
59. `.ak-sm:ak-grid-cols-2` - Small Breakpoint Grid
60. `.ak-md:ak-grid-cols-2`, `.ak-md:ak-grid-cols-3` - Medium Breakpoint Grid
61. `.ak-lg:ak-grid-cols-3`, `.ak-lg:ak-grid-cols-4` - Large Breakpoint Grid
62. `.ak-md:ak-hidden` - Responsive Hide (Medium)
63. `.ak-lg:ak-hidden` - Responsive Hide (Large)

### Phase 13: State Classes (ak-utilities.css)

64. `.ak-active` - Active State Utility

## Dateien zu ändern

1. `css/ak-design-system/ak-base.css` - Typography & Base Classes
2. `css/ak-design-system/ak-components.css` - Komponenten (Buttons, Cards, Forms, Alerts, Badges, Tables, Modals)
3. `css/ak-design-system/ak-utilities.css` - Utility Classes (Width, Height, Background, Border Radius, State)
4. `css/ak-design-system/ak-layout.css` - Responsive Grid Classes

## Demo-Dateien anpassen

Nach Implementierung aller Klassen:
1. Alle `<style>` Tags aus Demo-Dateien entfernen
2. Benutzerdefinierte Klassen durch Design System Klassen ersetzen:
   - `.demo-section` → `.ak-section` oder `.ak-card`
   - `.color-demo` → `.ak-w-20 .ak-h-20 .ak-bg-*`
   - `.spacing-demo` → Utility-Klassen
   - `.modal-overlay` → `.ak-modal`
   - `.toast` → `.ak-toast`
   - `.code-block` → `.ak-code-block`
   - `.language-selector` → Utility-Klassen
   - `.content-section` → `.ak-section`

## Implementierungsreihenfolge

1. Zuerst alle fehlenden Klassen zum Design System hinzufügen
2. Dann Demo-Dateien anpassen und benutzerdefinierte Styles entfernen
3. Testen, dass alles funktioniert
4. Neue Version taggen

