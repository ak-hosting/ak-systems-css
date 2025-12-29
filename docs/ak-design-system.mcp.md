# AK Design System - Model Context Protocol (MCP)

**Externer, agentenorientierter Kontext für AI-Agenten**

Dieses MCP dient als externer Kontext für AI-Agenten (Codex, Cursor, Claude, andere LLMs), die mit dem AK Design System arbeiten. Es vermittelt ein korrektes mentales Modell, klare Regeln und Entscheidungslogik, ohne dass Agenten den gesamten Code analysieren müssen.

**WICHTIG:** Dieses MCP ergänzt `AGENT_CONTEXT.md` (technische Referenz) und ersetzt es nicht. `demo/index.html` ist die "Source of Truth" für HTML-Patterns.

---

## Zusammenfassung: Warum dieser MCP so aufgebaut ist

1. **Minimaler Ansatz**: MCP fokussiert auf Regeln, Struktur und Entscheidungslogik, nicht auf vollständige Klassenlisten (dafür AGENT_CONTEXT.md)

2. **Externe Nutzbarkeit**: MCP ist als externer Kontext konzipiert, der außerhalb des Repositories genutzt werden kann, ohne Repository-spezifische Pfade zu benötigen

3. **Verschärfte Entscheidungsregeln**: Grundprinzip "Im Zweifel abbrechen statt improvisieren" verhindert Halluzinationen und falsche Annahmen

4. **Klare Trennung der Verantwortlichkeiten**: MCP (mentales Modell) vs. AGENT_CONTEXT.md (technische Referenz) vs. demo/index.html (Patterns)

5. **Stabilität vs. Variabilität**: MCP dokumentiert nur stabile Regeln und Prinzipien, variable Informationen (Klassen-Listen) bleiben in AGENT_CONTEXT.md

6. **Framework-Grenzen respektieren**: MCP macht unmissverständlich klar, was das Framework ist (CSS-only) und was nicht (kein JavaScript, keine Modifikationen)

7. **Legacy-Kontext**: MCP erklärt Legacy-Dateien und deren Vermeidung, ohne detaillierte Mappings (dafür ak-legacy-map.md)

8. **Modul-Hierarchie ohne Details**: MCP erklärt die Struktur und Rollen der Module, aber keine spezifischen Klassen (dafür AGENT_CONTEXT.md)

9. **Versionierung integriert**: MCP berücksichtigt Versionierung und CDN-Nutzung für externe Nutzung

10. **Pflegehinweise enthalten**: MCP dokumentiert selbst, wann es aktualisiert werden muss, um langfristige Wartbarkeit zu gewährleisten

---

## 1. MCP-Zweck

### Probleme, die dieser MCP löst

- **Halluzinationen verhindern**: Agenten erfinden keine nicht existierenden CSS-Klassen
- **Modulstruktur verstehen**: Korrekte Import-Reihenfolge und Modul-Hierarchie
- **Legacy-Verwirrung vermeiden**: Klarheit über veraltete vs. aktuelle Dateien
- **Framework-Grenzen respektieren**: Keine Modifikationen, keine externen Framework-Klassen
- **Entscheidungslogik**: Wann MCP-Wissen reicht, wann weitere Quellen konsultiert werden müssen

### Zielgruppe

- Codex, Cursor, Claude und andere LLMs
- Entwickler, die das Framework außerhalb des Repositories nutzen
- Agenten, die HTML/CSS mit ak-systems-Klassen generieren

### Beziehung zu anderen Dokumenten

- **AGENT_CONTEXT.md**: Technische Referenz mit Klassenlisten und Code-Beispielen
- **demo/index.html**: Source of Truth für korrekte HTML-Patterns
- **ak-legacy-map.md**: Mapping zwischen Legacy-Dateien und aktueller Struktur
- **Dieses MCP**: Mentales Modell, Regeln, Entscheidungslogik (keine Klassenlisten, kein Code)

---

## 2. Projekt-Mentales-Modell

### Korrekte Denkweise

**Das AK Design System ist:**
- Ein **CSS-Framework** (kein JavaScript-Framework)
- **Modular aufgebaut**: 7 Module in definierter Import-Reihenfolge
- **Unveränderlich**: Framework-Code darf nicht modifiziert werden (siehe LICENSE)
- **Präfix-basiert**: Alle Klassen beginnen mit `ak-` (unverhandelbar)
- **CSS-Variablen-basiert**: Theming über CSS-Custom-Properties
- **Mobile-first**: Responsive Design ist integriert
- **Accessibility-orientiert**: Unterstützung für `prefers-reduced-motion`, Keyboard-Navigation

**Das Framework stellt bereit:**
- CSS-Klassen für Layout, Komponenten, Utilities
- CSS-Variablen für Theming und Custom-Styling
- Dark Mode Support via `.ak-theme-dark` auf `<body>`
- Responsive Breakpoints (z.B. `ak-md:`, `ak-lg:`)

**Das Framework stellt NICHT bereit:**
- JavaScript-Funktionalität (Interaktivität muss extern implementiert werden)
- Icons (verwendet Lucide Icons extern)
- Build-Tools oder Bundler (nur CSS-Konkatenation)

### Falsche Annahmen (VERMEIDEN)

**Agenten dürfen NIEMALS annehmen:**
- Das Framework ist ein JavaScript-Framework oder enthält JS
- Klassen ohne `ak-` Präfix existieren oder erlaubt sind
- Bootstrap, Tailwind, Bulma oder andere Framework-Klassen verwendet werden können
- Das Framework kann modifiziert oder erweitert werden
- Legacy-Dateien direkt importiert werden sollten (nur `index.css` verwenden)
- JavaScript-Komponenten sind Teil des Frameworks
- Icons sind Teil des Frameworks (Lucide ist extern)

**Typische Fehlannahmen:**
- Verwendung von `btn-primary` statt `ak-btn ak-btn-primary`
- Import von Legacy-Dateien wie `ak-design-system.css` direkt
- Vorschlag von Framework-Modifikationen oder Erweiterungen
- Annahme, dass Modals/Dropdowns ohne JavaScript funktionieren

---

## 3. Architektur-Leitplanken

### Was Agenten IMMER annehmen dürfen

**Präfix-Regel (unverhandelbar):**
- Alle CSS-Klassen beginnen mit `ak-`
- Keine Ausnahmen, keine Klassen ohne Präfix

**Modulare Struktur:**
- Framework besteht aus 7 Modulen in definierter Reihenfolge
- Import-Reihenfolge ist kritisch: core → base → layout → components → loaders → utilities → modifiers
- Nur `css/ak-design-system/index.css` wird importiert (nicht einzelne Module)

**CSS-Variablen:**
- Theming über CSS-Custom-Properties (z.B. `--ak-color-primary`)
- Variablen sind stabil und können für Custom-Styling verwendet werden
- Dark Mode via `.ak-theme-dark` auf `<body>` aktivieren

**Responsive Design:**
- Mobile-first Ansatz
- Breakpoint-Präfixe: `ak-md:`, `ak-lg:` etc.
- Responsive Utilities sind verfügbar

**Framework-Grenzen:**
- Framework ist CSS-only
- JavaScript-Interaktivität muss extern implementiert werden
- Icons kommen von Lucide (extern), nicht vom Framework

### Was Agenten NIEMALS tun dürfen

**Verbotene Aktionen:**
- Klassen ohne `ak-` Präfix erfinden oder verwenden
- Legacy-Dateien direkt importieren (außer `index.css`)
- Bootstrap, Tailwind, Bulma oder andere Framework-Klassen verwenden
- Framework-Code modifizieren, erweitern oder vorschlagen
- JavaScript-Funktionalität als Teil des Frameworks annehmen
- Icons als Teil des Frameworks behandeln

**Verbotene Annahmen:**
- Framework kann angepasst werden
- Klassen existieren, die nicht dokumentiert sind
- Legacy-Dateien sind aktuelle Best Practice
- Externe Frameworks können kombiniert werden

---

## 4. Struktur & Rollen

### Modul-Hierarchie (Import-Reihenfolge)

Die 7 Module werden in folgender Reihenfolge importiert (via `index.css`):

1. **ak-core.css**: CSS-Variablen, Reset, Grundlagen
   - Rolle: Fundament, Theming-Variablen, Custom-Properties
   - Stabilität: Sehr stabil (nur bei Breaking Changes)

2. **ak-base.css**: Basis-Styles, Typography, Accessibility
   - Rolle: Grundlegende HTML-Elemente, Schriftarten, Accessibility-Features
   - Stabilität: Stabil (seltene Änderungen)

3. **ak-layout.css**: Container, Grid, Flexbox-Utilities, Header/Footer/Sidebar
   - Rolle: Layout-Komponenten und -Utilities
   - Stabilität: Stabil (neue Varianten möglich)

4. **ak-components.css**: Buttons, Cards, Forms, Badges, Modals, etc.
   - Rolle: UI-Komponenten
   - Stabilität: Variabel (neue Komponenten möglich)

5. **ak-loaders.css**: Spinner, Dots, Loading-States
   - Rolle: Loading-Indikatoren
   - Stabilität: Stabil

6. **ak-utilities.css**: Margin, Padding, Display, Text, Width/Height, etc.
   - Rolle: Utility-Klassen
   - Stabilität: Variabel (neue Utilities möglich)

7. **ak-modifiers.css**: Modifier-Klassen für Varianten
   - Rolle: Varianten und Modifikatoren
   - Stabilität: Variabel

**WICHTIG:** Agenten müssen diese Reihenfolge verstehen, aber dürfen einzelne Module nicht direkt importieren. Nur `index.css` verwenden.

### Trennung der Verantwortlichkeiten

**Framework (ak-design-system):**
- CSS-Klassen mit `ak-` Präfix
- CSS-Variablen für Theming
- Layout, Komponenten, Utilities
- **NICHT verantwortlich für:** JavaScript, Icons, Build-Tools

**Custom CSS (Projekt-spezifisch):**
- Eigene Styles, die Framework-Klassen erweitern
- Verwendung von CSS-Variablen für Konsistenz
- **Darf:** Framework-Variablen nutzen, eigene Klassen definieren
- **Darf NICHT:** Framework-Klassen überschreiben oder modifizieren

**Custom JavaScript (Projekt-spezifisch):**
- Interaktivität für Modals, Dropdowns, Tabs
- Toggle von Klassen wie `.active`, `.open`
- **Verantwortlich für:** Alle JavaScript-Funktionalität (Framework ist CSS-only)

**Externe Abhängigkeiten:**
- **Lucide Icons**: Extern, nicht Teil des Frameworks
- **CDN**: Framework kann via CDN geladen werden

### Legacy-Dateien

**WICHTIG:** Legacy-Dateien existieren nur für Rückwärtskompatibilität. Agenten müssen verstehen:

- **Nur `index.css` verwenden** (canonical entry)
- Legacy-Dateien sind deprecated und werden in Phase 4 entfernt
- Mapping zwischen Legacy und aktuellen Modulen ist dokumentiert in `ak-legacy-map.md`
- Agenten dürfen Legacy-Dateien nicht direkt importieren oder empfehlen

---

## 5. Entscheidungsregeln für Agenten

### Grundprinzip: Im Zweifel abbrechen statt improvisieren

Agenten müssen bei Unsicherheit klar kommunizieren und abbrechen, anstatt zu improvisieren oder Klassen zu erfinden.

### Regel 1: Nicht existierende Klassen

**Situation:** Agent ist unsicher, ob eine Klasse existiert.

**Handlung:**
1. Agent MUSS abbrechen
2. Agent MUSS auf `AGENT_CONTEXT.md` oder `demo/index.html` verweisen
3. Agent DARF KEINE Klassen erfinden oder vermuten

**Beispiel:**
- ❌ FALSCH: "Ich verwende `ak-btn-large` (nehme an, dass es existiert)"
- ✅ RICHTIG: "Ich bin unsicher, ob `ak-btn-large` existiert. Bitte konsultieren Sie `AGENT_CONTEXT.md` oder `demo/index.html` für verfügbare Button-Varianten."

### Regel 2: Unklare Patterns

**Situation:** Pattern ist nicht eindeutig aus MCP ableitbar.

**Handlung:**
1. Agent MUSS `AGENT_CONTEXT.md` oder `demo/index.html` konsultieren
2. Falls dort nicht eindeutig: Agent MUSS abbrechen
3. Agent DARF KEINE Patterns erfinden oder vermuten

**Beispiel:**
- ❌ FALSCH: "Ich verwende eine vermutete HTML-Struktur für Modals"
- ✅ RICHTIG: "Bitte konsultieren Sie `demo/index.html` für die korrekte Modal-Struktur. Falls dort nicht eindeutig, kann ich nicht fortfahren."

### Regel 3: Anforderungen außerhalb des Framework-Scopes

**Situation:** Anforderung wird nicht durch Framework abgedeckt.

**Handlung:**
1. Agent MUSS klar kommunizieren, dass Anforderung nicht durch Framework abgedeckt wird
2. Agent DARF KEINE Workarounds oder Erweiterungen vorschlagen
3. Agent DARF KEINE Framework-Modifikationen vorschlagen

**Beispiel:**
- ❌ FALSCH: "Ich erweitere das Framework um eine neue Komponente"
- ✅ RICHTIG: "Diese Anforderung wird nicht durch das AK Design System abgedeckt. Bitte implementieren Sie eine Custom-Lösung mit eigenen CSS-Klassen und Framework-Variablen."

### Regel 4: Wann MCP-Wissen reicht

**MCP-Wissen reicht für:**
- Grundlegende Struktur und Modul-Hierarchie verstehen
- Präfix-Regel (`ak-`) anwenden
- Framework-Grenzen respektieren (CSS-only, keine Modifikationen)
- Legacy-Dateien vermeiden
- CSS-Variablen für Custom-Styling verwenden

**Agent kann direkt handeln, wenn:**
- Nur grundlegende Regeln und Prinzipien benötigt werden
- Framework-Grenzen respektiert werden müssen
- Entscheidung über Legacy vs. aktuelle Struktur getroffen werden muss

### Regel 5: Wann AGENT_CONTEXT.md konsultieren

**AGENT_CONTEXT.md konsultieren für:**
- Spezifische Klassen-Namen und deren Existenz
- Komponenten-Strukturen und HTML-Patterns
- Verfügbare Varianten (z.B. Button-Varianten)
- CSS-Variablen-Namen und Werte
- Utility-Klassen-Namen

**Agent MUSS konsultieren, wenn:**
- Unsicherheit über Klassen-Existenz besteht
- Spezifische Komponenten-Struktur benötigt wird
- Varianten oder Modifikatoren benötigt werden

### Regel 6: Wann gezielte Code-Analyse erlaubt

**Gezielte Code-Analyse erlaubt für:**
- CSS-Implementierungsdetails (z.B. spezifische Selektoren)
- Media-Queries und Breakpoint-Werte
- Spezifische CSS-Regeln für Debugging
- Verständnis von CSS-Spezifität oder Cascade-Problemen

**Agent DARF analysieren, wenn:**
- Nur spezifische CSS-Details benötigt werden
- Debugging von Styling-Problemen erforderlich ist
- Verständnis von CSS-Implementierung notwendig ist

**Agent DARF NICHT analysieren für:**
- Klassen-Existenz (dafür AGENT_CONTEXT.md)
- HTML-Patterns (dafür demo/index.html)
- Framework-Struktur (dafür dieses MCP)

### Regel 7: Wann abbrechen

**Agent MUSS abbrechen, wenn:**
- Unsicherheit über Klassen-Existenz nach Konsultation aller Quellen
- Anforderung außerhalb des Framework-Scopes liegt
- Pattern nach Konsultation von MCP, AGENT_CONTEXT.md und demo/index.html unklar bleibt
- Framework-Modifikation erforderlich wäre
- Externe Framework-Klassen verwendet werden sollen

**Abbrechen bedeutet:**
- Klare Kommunikation, warum nicht fortgefahren werden kann
- Verweis auf relevante Dokumentation
- Keine Improvisation oder Vermutungen

---

## 6. Externe Nutzung & Stabilität

### Stabile Informationen (ändern sich selten)

**Sehr stabil (Breaking Changes nur bei Major-Versionen):**
- Präfix-Regel (`ak-`)
- Modul-Hierarchie und Import-Reihenfolge
- Framework-Grenzen (CSS-only, keine Modifikationen)
- CSS-Variablen-Namen (z.B. `--ak-color-primary`)
- Grundlegende Architektur-Prinzipien

**Stabil (Änderungen möglich, aber selten):**
- Modul-Rollen und Verantwortlichkeiten
- Legacy-Mapping (bis Phase 4)
- Build-Prozess-Struktur
- CDN-URL-Struktur

### Variable Informationen (ändern sich häufiger)

**Variabel (können sich ändern):**
- Verfügbare Komponenten (neue Komponenten möglich)
- Verfügbare Utility-Klassen (neue Utilities möglich)
- Verfügbare Varianten (neue Varianten möglich)
- Spezifische Klassen-Namen (für Details: AGENT_CONTEXT.md)

**Für variable Informationen:**
- Agenten MÜSSEN `AGENT_CONTEXT.md` oder `demo/index.html` konsultieren
- MCP reicht nicht für spezifische Klassen-Listen

### Versionierung

**Version-Information:**
- Framework-Version ist in `VERSION`-Datei dokumentiert
- CDN-URLs enthalten Versions-Tags (z.B. `@v1.3.0`)
- CHANGELOG.md dokumentiert Änderungen zwischen Versionen

**Für externe Nutzung:**
- MCP sollte Framework-Version kennen (aus `VERSION`)
- CDN-URLs sollten mit Versions-Tags verwendet werden
- Breaking Changes werden in CHANGELOG.md dokumentiert

### CDN-Nutzung

**CDN-URL-Struktur:**
- Production: `https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@v{VERSION}/dist/ak-design-system.min.css`
- Development: `https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@main/dist/ak-design-system.min.css`

**Empfehlungen:**
- Spezifische Versionen verwenden (nicht `@main` in Production)
- Version aus `VERSION`-Datei für aktuelle Version

### Externe Nutzbarkeit

**MCP als externer Kontext:**
- MCP kann außerhalb des Repositories genutzt werden
- MCP ist agentenlesbar und strukturiert
- MCP enthält keine Repository-spezifischen Pfade (außer Referenzen zu Dokumentation)

**Stabilität für externe Nutzung:**
- MCP-Struktur ist stabil (6 Abschnitte)
- Stabile Regeln ändern sich selten
- Variable Informationen werden über AGENT_CONTEXT.md aktualisiert

**Synchronisation:**
- MCP muss bei Änderungen an stabilen Regeln aktualisiert werden
- Variable Informationen (Klassen-Listen) bleiben in AGENT_CONTEXT.md
- Version-Information sollte aus `VERSION`-Datei stammen

---

## Pflegehinweise

### Wann MCP aktualisiert werden muss

**Kritische Änderungen (MCP MUSS aktualisiert werden):**
- Änderung der Präfix-Regel
- Änderung der Modul-Hierarchie oder Import-Reihenfolge
- Änderung der Framework-Grenzen (z.B. JavaScript wird hinzugefügt)
- Breaking Changes in der Architektur
- Änderung der Legacy-Strategie

**Wichtige Änderungen (MCP SOLLTE aktualisiert werden):**
- Neue Module werden hinzugefügt
- Modul-Rollen ändern sich
- Neue stabile Prinzipien werden etabliert
- Entscheidungsregeln müssen angepasst werden

**Nicht erforderlich (AGENT_CONTEXT.md reicht):**
- Neue Komponenten werden hinzugefügt
- Neue Utility-Klassen werden hinzugefügt
- Neue Varianten werden hinzugefügt
- CSS-Variablen werden hinzugefügt (außer Breaking Changes)

### Synchronisation mit anderen Dokumenten

**AGENT_CONTEXT.md:**
- Enthält Klassen-Listen und Code-Beispiele
- Wird häufiger aktualisiert (bei neuen Komponenten)
- MCP referenziert AGENT_CONTEXT.md, überschreibt es nicht

**demo/index.html:**
- Source of Truth für HTML-Patterns
- Wird bei neuen Komponenten aktualisiert
- MCP verweist darauf, analysiert es nicht

**VERSION:**
- Enthält aktuelle Framework-Version
- MCP sollte Version kennen, aber nicht duplizieren

**CHANGELOG.md:**
- Dokumentiert Änderungen zwischen Versionen
- MCP verweist darauf für Breaking Changes

---

**Ende des MCP**

Dieses MCP ist ein lebendes Dokument und sollte bei architektonischen Änderungen aktualisiert werden. Für spezifische Klassen-Listen und Code-Beispiele konsultieren Sie `AGENT_CONTEXT.md`. Für HTML-Patterns konsultieren Sie `demo/index.html`.

