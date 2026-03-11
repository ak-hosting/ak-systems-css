# ak-systems CSS Framework

Ein leichtgewichtiges CSS-Framework von ak-systems für schnelle Prototypen.

*Read this in [English](README.md) | [Türkçe](README.tr.md)*

## Installation

### Produktion (CDN) - Empfohlen

Nutzen Sie das jsDelivr CDN, um das CSS einzubinden. Dies ist der zuverlässigste Weg.

```html
<!-- Spezifische Version nutzen (empfohlen für Produktion) -->
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@v2.0.2/dist/ak-design-system.min.css"
/>
```

### Entwicklung (Lokal)

Nur nutzen, wenn Sie am Framework selbst arbeiten.

```html
<link rel="stylesheet" href="dist/ak-design-system.css">
```

### Bleeding Edge (Instabil)

Wenn Sie die absolut neuesten Änderungen vom `main`-Branch benötigen (nicht für Produktion empfohlen):

```html
<!-- Warnung: Kann Breaking Changes enthalten -->
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@main/dist/ak-design-system.min.css"
/>
```

## Versionierung und CDN-Nutzung

- **Empfohlen:** Auf Release-Tags pinnen (z. B. `.../ak-systems-css@v1.3.2/...`), um unbeabsichtigte Updates zu vermeiden. Dies stellt sicher, dass Ihre Seite exakt gleich aussieht, auch wenn wir Änderungen vornehmen.
- **Entwicklung:** Nutzen Sie `.../ak-systems-css@main/...`, um immer die neuesten Änderungen zu erhalten. Beachten Sie, dass dies Ihr Layout brechen kann, wenn wir Klassennamen ändern.
- Siehe [CHANGELOG.md](CHANGELOG.md) für detaillierte Versionshistorie.
- Unterstützte Einstiegspunkte: `dist/ak-design-system.css` für Entwicklung und `dist/ak-design-system.min.css` für Produktion/CDN.

## Build Prozess

Um die Distributionsdateien in `dist/` zu generieren:

```bash
./build-css.sh
```

Wenn die CSS-Dateien in `css/ak-design-system/` bereits aktuell sind und Sie nur bundlen + minifizieren möchten:

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
<div class="ak-grid ak-grid-3 ak-gap-4">
  <div>Spalte 1</div>
  <div>Spalte 2</div>
  <div>Spalte 3</div>
</div>
```

### Buttons

```html
<button class="ak-btn">Standard Button</button>
<button class="ak-btn ak-btn-primary">Primary Button</button>
<button class="ak-btn ak-btn-destructive">Destructive Button</button>

<!-- Moderne Varianten (Soft, Glass, Gradient, Formen) - siehe AGENT_CONTEXT.md für vollständige Liste -->
<button class="ak-btn ak-btn-soft-primary ak-btn-rounded">Modern Rund</button>
```

### Loader / Animationen

```html
<!-- Basis Spinner -->
<div class="ak-loader-spinner ak-loader-primary ak-loader-md"></div>

<!-- Dots Loader -->
<div class="ak-loader-dots ak-loader-primary ak-loader-md">
  <span></span><span></span><span></span>
</div>
```

### Header & Footer Varianten

```html
<!-- Zentrierter Header -->
<header class="ak-header ak-header-centered">
  <div class="ak-header-content">
    <nav class="ak-header-nav">...</nav>
    <div class="ak-header-brand">Logo</div>
    <div class="ak-header-actions">...</div>
  </div>
</header>

<!-- Mehrspaltiger Footer -->
<footer class="ak-footer ak-footer-multi-column">
  <div class="ak-footer-content">
    <div class="ak-footer-column">
      <h5 class="ak-footer-column-title">Unternehmen</h5>
      <a href="#">Über uns</a>
      <a href="#">Kontakt</a>
    </div>
  </div>
</footer>
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

## KI- / MCP-Hinweise

Dieses Projekt enthält ein **Model Context Protocol (MCP)** für KI-Agenten (Codex, Cursor, Claude und andere LLMs). Das MCP stellt Regeln, mentale Modelle und Entscheidungslogik bereit, damit KI-Agenten korrekt mit dem AK Design System arbeiten können, ohne den gesamten Code analysieren zu müssen.

**Dokumentations-Hierarchie:**
- **MCP** ([`docs/ak-design-system.mcp.md`](docs/ak-design-system.mcp.md)): Regeln, mentales Modell und Entscheidungsrahmen
- **AGENT_CONTEXT.md** ([`docs/AGENT_CONTEXT.md`](docs/AGENT_CONTEXT.md)): Technische Referenz mit Klassenlisten und Code-Beispielen
- **demo/index.html**: Source of Truth für HTML-Patterns

Das MCP ist für die externe Nutzung durch KI-Agenten konzipiert und fokussiert sich auf Prinzipien und Struktur, während AGENT_CONTEXT.md spezifische Klassen-Namen und Implementierungsdetails enthält.

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
