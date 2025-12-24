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
| `ak-loader-dots` | Pulsierende Punkte | Inline-Text, Lade-Overlay |
| `ak-loader-bar` | Linearer Fortschrittsbalken | Seitenladen, Uploads |

### Varianten (`{variant}`)
| Klasse | Token Mapping | Beschreibung |
|---|---|---|
| `ak-loader-primary` | `--ak-color-primary` | Hauptaktion |
| `ak-loader-secondary` | `--ak-color-secondary` | Sekundäre Aktionen |
| `ak-loader-neutral` | `currentColor` | Passt sich der Textfarbe an |
| `ak-loader-white` | `#ffffff` | Auf dunklen Hintergründen |
| `ak-loader-muted` | `--ak-color-text-muted` | Dezent |

### Größen (`{size}`)
| Klasse | Token | Pixel |
|---|---|---|
| `ak-loader-xs` | `--ak-space-3` | 12px |
| `ak-loader-sm` | `--ak-space-4` | 16px (Default) |
| `ak-loader-md` | `--ak-space-6` | 24px |
| `ak-loader-lg` | `--ak-space-12` | 48px |
| `ak-loader-xl` | `--ak-space-16` | 64px |

## 3. Implementation Details

### CSS Variablen & Tokens
Loader nutzen ausschließlich CSS-Variablen aus `ak-core.css`.

```css
/* Beispiel Definition */
.ak-loader-spinner {
  border: 2px solid currentColor;
  border-right-color: transparent;
  border-radius: 50%;
  animation: ak-spin 1s linear infinite;
}
```

### Motion Standards
- **Animationen:** `ak-spin`, `ak-pulse`, `ak-progress-indeterminate`
- **Dauer:**
  - Spinner: 1s linear
  - Dots: 1.4s ease-in-out both
  - Bar: 2s infinite linear
- **Reduced Motion:**
  ```css
  @media (prefers-reduced-motion: reduce) {
    [class*="ak-loader-"] {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
    }
  }
  ```

## 4. Verwendung

### HTML Struktur

**Spinner (Standard)**
```html
<span class="ak-loader-spinner ak-loader-primary ak-loader-md" role="status" aria-label="Loading..."></span>
```

**Dots**
```html
<div class="ak-loader-dots ak-loader-neutral ak-loader-sm" role="status" aria-label="Loading...">
  <span></span><span></span><span></span>
</div>
```

**Progress Bar**
```html
<div class="ak-loader-bar ak-loader-primary ak-loader-md" role="progressbar">
  <div class="ak-loader-bar-value"></div>
</div>
```

### Integration in Komponenten

**Button mit Loader**
```html
<button class="ak-btn ak-btn-primary" disabled>
  <span class="ak-loader-spinner ak-loader-white ak-loader-sm"></span>
  <span>Speichern...</span>
</button>
```

## 5. Migration & Kompatibilität

Bestehende Klassen wie `.ak-loading-spinner` bleiben vorerst als Alias erhalten, sollten aber mittelfristig durch die neuen `ak-loader-*` Klassen ersetzt werden.

### Legacy Mapping
| Alt | Neu |
|---|---|
| `.ak-loading-spinner` | `.ak-loader-spinner-neutral-sm` |
| `.ak-btn-loading::after` | (Refactor zu explizitem Loader Element empfohlen) |

## 6. Do's and Don'ts

- **Do:** Nutze `aria-label` für Screenreader.
- **Do:** Nutze `neutral` Variante innerhalb von Buttons, um Farbkonflikte zu vermeiden.
- **Don't:** Überschreibe Loader-Farben mit Inline-Styles. Nutze die Varianten.
- **Don't:** Ändere die `border-width` manuell. Sie skaliert mit der Größe.
