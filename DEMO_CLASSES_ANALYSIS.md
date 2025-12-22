# Demo-Klassen Analyse - Fehlende CSS-Klassen

## Analyse der verwendeten Klassen in Demo-Dateien

### Fehlende Klassen (müssen zum Design System hinzugefügt werden)

#### 1. Typography & Text
- `.ak-link` - Link-Styling
- `.ak-blockquote` - Blockquote-Styling  
- `.ak-code` - Inline Code-Styling
- `.ak-section` - Section-Container

#### 2. Buttons
- `.ak-btn-accent` - Accent Button Variante
- `.ak-btn-link` - Link Button Variante
- `.ak-btn-outline` - Outline Button Variante
- `.ak-loading` - Loading State (existiert als `.ak-btn-loading`, aber `.ak-loading` fehlt)
- `.ak-loading-spinner` - Loading Spinner

#### 3. Cards
- `.ak-card-title` - Card Titel
- `.ak-card-description` - Card Beschreibung
- `.ak-card-content` - Card Content (existiert als `.ak-card-body`, aber `.ak-card-content` wird verwendet)
- `.ak-card-img` - Card Bild

#### 4. Forms
- `.ak-form` - Form Container
- `.ak-form-field` - Form Field Container
- `.ak-form-hint` - Form Hint Text
- `.ak-checkbox-group` - Checkbox Group
- `.ak-checkbox-input` - Checkbox Input
- `.ak-checkbox-label` - Checkbox Label
- `.ak-radio-input` - Radio Input
- `.ak-radio-label` - Radio Label

#### 5. Alerts
- `.ak-alert` - Alert Container
- `.ak-alert-success` - Success Alert
- `.ak-alert-warning` - Warning Alert
- `.ak-alert-danger` - Danger Alert
- `.ak-alert-icon` - Alert Icon
- `.ak-alert-title` - Alert Titel
- `.ak-alert-description` - Alert Beschreibung

#### 6. Badges
- `.ak-badge` - Badge Container
- `.ak-badge-success` - Success Badge
- `.ak-badge-warning` - Warning Badge
- `.ak-badge-danger` - Danger Badge

#### 7. Tables
- `.ak-table` - Table Container
- `.ak-table-container` - Table Wrapper

#### 8. Modals
- `.ak-modal-title` - Modal Titel

#### 9. Utility Classes - Width/Height
- `.ak-w-4`, `.ak-w-8`, `.ak-w-12` - Width Utilities
- `.ak-h-4`, `.ak-h-8`, `.ak-h-12`, `.ak-h-20` - Height Utilities

#### 10. Utility Classes - Background
- `.ak-bg-primary` - Primary Background
- `.ak-bg-accent` - Accent Background
- `.ak-bg-muted` - Muted Background
- `.ak-bg-card` - Card Background

#### 11. Utility Classes - Border Radius
- `.ak-rounded` - Rounded Border
- `.ak-rounded-full` - Full Rounded Border

#### 12. Responsive Grid Classes
- `.ak-grid-cols-1`, `.ak-grid-cols-2`, `.ak-grid-cols-3`, `.ak-grid-cols-4` - Grid Columns
- `.ak-md:ak-grid-cols-2`, `.ak-md:ak-grid-cols-3` - Responsive Grid (Medium)
- `.ak-lg:ak-grid-cols-3` - Responsive Grid (Large)
- `.ak-sm:ak-grid-cols-2` - Responsive Grid (Small)
- `.ak-md:ak-hidden` - Responsive Hide (Medium)

#### 13. State Classes
- `.ak-active` - Active State (wird verwendet, aber nicht als Utility definiert)

### Benutzerdefinierte Demo-Klassen (sollten durch Design System ersetzt werden)

Diese Klassen sind nur in den Demo-Dateien definiert und sollten durch Design System Klassen ersetzt werden:

- `.demo-section` → sollte durch `.ak-card` oder neue `.ak-section` ersetzt werden
- `.color-demo` → sollte durch Utility-Klassen ersetzt werden
- `.spacing-demo` → sollte durch Utility-Klassen ersetzt werden
- `.modal-overlay` → sollte durch `.ak-modal` ersetzt werden
- `.toast` → sollte durch `.ak-toast` ersetzt werden (existiert bereits!)
- `.code-block` → sollte durch neue `.ak-code-block` ersetzt werden
- `.language-selector` → sollte durch Utility-Klassen ersetzt werden
- `.content-section` → sollte durch `.ak-section` ersetzt werden

### Empfehlung

1. Alle fehlenden Klassen zum Design System hinzufügen
2. Demo-Dateien anpassen, um benutzerdefinierte Styles zu entfernen
3. Alle Klassen sollten mit `ak-` Präfix beginnen
4. Responsive Utilities sollten konsistent implementiert werden

