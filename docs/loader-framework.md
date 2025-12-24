# AK Design System – Loader & Spinner Framework

## 1. Übersicht
Das Loader-Framework stellt standardisierte Ladeindikatoren bereit, die sich nahtlos in das AK Design System integrieren. Es vermeidet Duplikate, nutzt bestehende Design-Tokens und ist vollständig über das CDN steuerbar.

### Ziele
- **Konsistenz:** Einheitliches Aussehen über alle Applikationen hinweg.
- **Performance:** CSS-only Implementationen ohne JavaScript-Abhängigkeiten.
- **Flexibilität:** Unterstützung verschiedener Größen, Farben und Typen.
- **Barrierefreiheit:** Standardmäßige Unterstützung für `prefers-reduced-motion`.

## 2. Architektur & Namenskonventionen

Wir folgen dem im System etablierten **Composable Class Pattern** (ähnlich wie `ak-btn` oder `ak-icon`). Dies ermöglicht maximale Flexibilität und Konsistenz.

**Schema:**
`<element class="ak-loader-{type} ak-loader-{size} ak-loader-{variant}">`

### Typen (`{type}`)
| Klasse | Beschreibung | Anwendungsfall |
|---|---|---|
| `ak-loader-spinner` | Rotierender Ring | Buttons, Cards, kleine Bereiche |
| `ak-loader-track` | Spinner mit Hintergrundring | Heller Hintergrund, besserer Kontrast |
| `ak-loader-dots` | Pulsierende Punkte | Inline-Text, Lade-Overlay |
| `ak-loader-bar` | Linearer Fortschrittsbalken | Seitenladen, Uploads |
| `ak-loader-wave` | 5 wellenförmige Balken | Audio, Aktivität, Sprachverarbeitung |
| `ak-loader-grid` | 3x3 pulsierendes Raster | Galerien, Datentabellen, Dashboards |
| `ak-loader-flip` | Rotierendes 3D-Quadrat | Splash Screens, Zentrales Laden |
| `ak-skeleton` | Shimmer-Effekt | Platzhalter für noch nicht geladenen Content |

### Varianten (`{variant}`)
| Klasse | Token Mapping | Beschreibung |
|---|---|---|
| `ak-loader-primary` | `--ak-color-primary` | Hauptaktion |
| `ak-loader-secondary` | `--ak-color-secondary` | Sekundäre Aktionen |
| `ak-loader-neutral` | `currentColor` | Passt sich der Textfarbe an |
| `ak-loader-white` | `#ffffff` | Auf dunklen Hintergründen |
| `ak-loader-muted` | `--ak-color-text-muted` | Dezent |
| `ak-loader-destructive` | `--ak-color-destructive` | Fehlerzustände oder Warnungen |

### Größen (`{size}`)
| Klasse | Token | Pixel |
|---|---|---|
| `ak-loader-xs` | `--ak-space-3` | 12px |
| `ak-loader-sm` | `--ak-space-4` | 16px (Default) |
| `ak-loader-md` | `--ak-space-6` | 24px |
| `ak-loader-lg` | `--ak-space-12` | 48px |
| `ak-loader-xl` | `--ak-space-16` | 64px |

## 3. Verwendung

### HTML Struktur

**Spinner (Standard)**
```html
<span class="ak-loader-spinner ak-loader-primary ak-loader-md" role="status" aria-label="Loading..."></span>
```

**Track Spinner (mit Ring)**
```html
<span class="ak-loader-spinner ak-loader-track ak-loader-primary ak-loader-md" role="status" aria-label="Loading..."></span>
```

**Dots**
```html
<div class="ak-loader-dots ak-loader-neutral ak-loader-sm" role="status" aria-label="Loading...">
  <span></span><span></span><span></span>
</div>
```

**Wave (Activity)**
```html
<div class="ak-loader-wave ak-loader-primary" role="status" aria-label="Processing...">
  <span></span><span></span><span></span><span></span><span></span>
</div>
```

**Grid (Data)**
```html
<div class="ak-loader-grid ak-loader-primary" role="status" aria-label="Loading data...">
  <span></span><span></span><span></span>
  <span></span><span></span><span></span>
  <span></span><span></span><span></span>
</div>
```

**Flip (Plane)**
```html
<div class="ak-loader-flip ak-loader-primary" role="status" aria-label="Loading..."></div>
```

**Progress Bar**
```html
<div class="ak-loader-bar ak-loader-primary ak-loader-md" role="progressbar" aria-valuenow="45" aria-valuemin="0" aria-valuemax="100">
  <div class="ak-loader-bar-value" style="width: 45%"></div>
</div>

<!-- Indeterminate State -->
<div class="ak-loader-bar ak-loader-primary ak-loader-md ak-loader-bar-indeterminate" role="progressbar">
  <div class="ak-loader-bar-value"></div>
</div>
```

**Skeleton Loading**
```html
<!-- Textzeile -->
<div class="ak-skeleton ak-skeleton-text"></div>

<!-- Kreis (Avatar) -->
<div class="ak-skeleton ak-skeleton-circle"></div>

<!-- Rechteck (Card/Image) -->
<div class="ak-skeleton ak-skeleton-rect"></div>
```

## 4. Implementation Details

### CSS Variablen & Tokens
Loader nutzen ausschließlich CSS-Variablen aus `ak-core.css`.

### Motion Standards
- **Animationen:** `ak-spin`, `ak-pulse`, `ak-wave`, `ak-grid`, `ak-flip`, `ak-shimmer`
- **Reduced Motion:**
  Wird global unterstützt. Wenn der User `prefers-reduced-motion: reduce` aktiviert hat, werden Animationen verlangsamt oder gestoppt.

```css
@media (prefers-reduced-motion: reduce) {
  [class*="ak-loader-"] {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
  }
}
```

## 5. Migration & Kompatibilität

Bestehende Klassen wie `.ak-loading-spinner` bleiben vorerst als Alias erhalten, sollten aber mittelfristig durch die neuen `ak-loader-*` Klassen ersetzt werden.

### Legacy Mapping
| Alt | Neu |
|---|---|
| `.ak-loading-spinner` | `.ak-loader-spinner-neutral-sm` |
| `.ak-btn-loading::after` | (Refactor zu explizitem Loader Element empfohlen) |

## 6. Do's and Don'ts

- **Do:** Nutze `aria-label` oder `aria-labelledby` für Screenreader.
- **Do:** Nutze `neutral` Variante innerhalb von Buttons, um Farbkonflikte zu vermeiden.
- **Don't:** Überschreibe Loader-Farben mit Inline-Styles. Nutze die Varianten.
- **Don't:** Ändere die `border-width` manuell. Sie skaliert mit der Größe.
