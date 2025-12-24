# ak-systems CSS Framework

Ein leichtgewichtiges CSS-Framework von ak-systems für schnelle Prototypen.

*Read this in [English](README.md) | [Türkçe](README.tr.md)*

## Installation

Einziger unterstützter Einstieg (Entwicklung):

```html
<link rel="stylesheet" href="css/ak-design-system/index.css">
```

Production/CDN-Einstieg:

```html
<!-- Spezifische Version nutzen (empfohlen) -->
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@v1.1.0/dist/ak-design-system.min.css"
/>

<!-- Oder neueste Version vom Main-Branch (nur für Entwicklung) -->
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@main/dist/ak-design-system.min.css"
/>
```

## Build Prozess

Um die Distributionsdateien in `dist/` zu generieren:

```bash
./build.sh
```

## Nutzung

### Container

```html
<div class="ak-container">
  <!-- Inhalt hier -->
</div>
```

### Grid-System

```html
<div class="ak-row">
  <div class="ak-col">Spalte 1</div>
  <div class="ak-col">Spalte 2</div>
  <div class="ak-col">Spalte 3</div>
</div>
```

### Buttons

```html
<button class="ak-btn">Standard Button</button>
<button class="ak-btn ak-btn-primary">Primary Button</button>
<button class="ak-btn ak-btn-danger">Danger Button</button>
```

## Mobile- & Touch-Best-Practices

- Empfohlener Viewport-Meta-Tag:
  ```html
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  ```
  Stellt responsive Breakpoints und ein mobile-first Verhalten sicher.
- Mobil-optimierte Komponenten:
  - Buttons und Icon-Buttons mit Touch-gerechter Größe
  - Responsives Grid- und Layout-Verhalten
  - Sidebar- und Footer-Navigation auf Mobilgeräten
- Accessibility & Motion:
  - Unterstützung für `prefers-reduced-motion`
  - Tastatur- und Focus-Visible-Unterstützung

**Empfehlung:** Für eigene Komponenten (z. B. Checkboxen, Radios, Links) Touch-Targets von mindestens 24×24px vorsehen. Dies entspricht Accessibility-Best-Practices und ist eine Nutzungsempfehlung, nicht vom Framework erzwungen.

## Demo

Eine Demo-Seite mit allen Komponenten findest du hier: [ak-systems CSS Demo](https://ak-hosting.github.io/ak-systems-css/demo/)

Hinweis: Die Demo-Seite ist verfügbar, sobald GitHub Pages für das Repository aktiviert ist. Bis dahin öffne die lokale Demo unter `demo/index.html` über einen lokalen Server.

## Wichtige Hinweise

- Entwickelt von ak-systems (Website: [ak-pro.com](https://ak-pro.com))
- Dieses Framework darf nicht modifiziert werden
- Keine Unterlizenzierung für Änderungen erlaubt
- Keine Haftung für Fehler oder Schäden

## Lizenz

Dieses Projekt ist unter der [ak-systems CSS Framework License](LICENSE) lizenziert.
- Es handelt sich nicht um eine Lizenz zum Ändern des Frameworks
- Sie können gerne eine andere CSS einbauen, aber dieses Framework darf nicht geändert werden
- Wir haften nicht für Fehler oder Änderungen
