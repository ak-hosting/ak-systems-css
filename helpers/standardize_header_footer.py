import os
import re

DEMO_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "demo"))
VERSION_FILE = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "VERSION"))


def get_version_tag() -> str:
    try:
        with open(VERSION_FILE, "r", encoding="utf-8") as f:
            version = f.read().strip()
        if version:
            return f"v{version}"
    except OSError:
        pass
    return "main"


CDN_DESIGN_SYSTEM_MIN = f"https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@{get_version_tag()}/dist/ak-design-system.min.css"


def filename_to_lang(filename: str) -> str:
    if filename.endswith(".de.html"):
        return "de"
    if filename.endswith(".tr.html"):
        return "tr"
    if filename.endswith(".en.html"):
        return "en"
    return "en"


def filename_to_base(filename: str) -> str:
    if filename.endswith(".de.html") or filename.endswith(".tr.html") or filename.endswith(".en.html"):
        return filename[:-8]
    if filename.endswith(".html"):
        return filename[:-5]
    return filename


def is_index_file(filename: str) -> bool:
    return filename_to_base(filename) == "index"


def get_lang_switcher(base: str, lang: str) -> str:
    base_for_links = "index" if base == "index" else base

    def btn(href: str, label: str, active: bool) -> str:
        cls = "ak-btn ak-btn-sm ak-btn-primary" if active else "ak-btn ak-btn-sm ak-btn-ghost"
        return f'<a href="{href}" class="{cls}">{label}</a>'

    return "\n                    ".join(
        [
            btn(f"{base_for_links}.html", "EN", lang == "en"),
            btn(f"{base_for_links}.de.html", "DE", lang == "de"),
            btn(f"{base_for_links}.tr.html", "TR", lang == "tr"),
        ]
    )


def get_header_template(title: str, base: str, lang: str, index_lang_href: str) -> str:
    back_link = ""
    if base != "index":
        back_link = f"""
                    <a href="{index_lang_href}" class="ak-btn ak-btn-ghost ak-btn-sm">
                        <i data-lucide="arrow-left" class="ak-w-4 ak-h-4 ak-mr-2"></i>
                        Back to Index
                    </a>"""

    title_html = f'<h1 class="ak-text-xl ak-font-bold">{title}</h1>'
    lang_links = get_lang_switcher(base, lang)

    return f"""<header class="ak-header">
        <div class="ak-header-content">
            <div class="ak-flex ak-items-center ak-gap-4">
                <button class="ak-btn ak-btn-ghost ak-btn-sm ak-mr-2" onclick="openModal('nav-drawer')">
                    <i data-lucide="menu"></i>
                </button>{back_link}
                {title_html}
            </div>
            <div class="ak-header-actions">
                <div class="ak-flex ak-gap-2">
                    {lang_links}
                </div>
            </div>
        </div>
    </header>"""


def get_drawer_title(lang: str) -> str:
    if lang == "tr":
        return "Gezinme"
    return "Navigation"


def get_nav_labels(lang: str) -> dict:
    if lang == "de":
        return {
            "index": "Übersicht",
            "typography": "Typografie",
            "sections": "Sektionen",
            "colors": "Farben",
            "backgrounds": "Hintergründe",
            "buttons": "Buttons",
            "loaders": "Loaders",
            "forms": "Formulare",
            "selection-controls": "Auswahl",
            "upload": "Upload",
            "cards": "Cards",
            "alerts": "Alerts",
            "modals": "Modals",
            "tables": "Tabellen",
            "extended": "Erweitert",
            "layout": "Layout",
            "headers": "Header & Footer",
            "utilities": "Utilities",
        }
    if lang == "tr":
        return {
            "index": "Genel Bakış",
            "typography": "Tipografi",
            "sections": "Bölümler",
            "colors": "Renkler",
            "backgrounds": "Arka Planlar",
            "buttons": "Butonlar",
            "loaders": "Yükleyiciler",
            "forms": "Formlar",
            "selection-controls": "Seçim Kontrolleri",
            "upload": "Yükleme",
            "cards": "Kartlar",
            "alerts": "Uyarılar",
            "modals": "Modallar",
            "tables": "Tablolar",
            "extended": "Genişletilmiş",
            "layout": "Düzen",
            "headers": "Header & Footer",
            "utilities": "Utility Classes",
        }
    return {
        "index": "Overview",
        "typography": "Typography",
        "sections": "Sections",
        "colors": "Colors",
        "backgrounds": "Backgrounds",
        "buttons": "Buttons",
        "loaders": "Loaders",
        "forms": "Forms",
        "selection-controls": "Selection Controls",
        "upload": "Upload",
        "cards": "Cards",
        "alerts": "Alerts",
        "modals": "Modals",
        "tables": "Tables",
        "extended": "Extended",
        "layout": "Layout",
        "headers": "Header & Footer",
        "utilities": "Utility Classes",
    }


def get_drawer_template(lang: str, active_key: str, index_lang_href: str) -> str:
    labels = get_nav_labels(lang)

    def li(href: str, key: str, icon: str) -> str:
        cls = " class=\"ak-active\"" if key == active_key else ""
        return f'<li><a href="{href}"{cls} data-page="{key}"><i data-lucide="{icon}" class="ak-w-4 ak-h-4 ak-mr-2"></i><span>{labels[key]}</span></a></li>'

    suffix = ""
    if lang == "de":
        suffix = ".de"
    elif lang == "tr":
        suffix = ".tr"

    return f"""
    <div id="nav-drawer" class="ak-modal ak-drawer-left" data-testid="sidebar">
        <div class="ak-modal-content">
            <div class="ak-modal-header">
                <h2 class="ak-modal-title">{get_drawer_title(lang)}</h2>
                <button id="close-sidebar" class="ak-btn ak-btn-ghost ak-btn-sm" onclick="closeModal('nav-drawer')">
                    <i data-lucide="x"></i>
                </button>
            </div>
            <div class="ak-modal-body">
                <ul class="ak-nav ak-flex-col ak-gap-2 ak-sidebar-nav">
                    {li(index_lang_href, "index", "home")}
                    {li(f"typography{suffix}.html", "typography", "type")}
                    {li(f"sections{suffix}.html", "sections", "layers")}
                    {li(f"{index_lang_href}#colors", "colors", "palette")}
                    {li(f"backgrounds{suffix}.html", "backgrounds", "image")}
                    {li(f"buttons{suffix}.html", "buttons", "mouse-pointer-click")}
                    {li(f"loaders{suffix}.html", "loaders", "loader")}
                    {li(f"forms{suffix}.html", "forms", "form-input")}
                    {li(f"selection-controls{suffix}.html", "selection-controls", "check-square")}
                    {li(f"upload{suffix}.html", "upload", "cloud-upload")}
                    {li(f"cards{suffix}.html", "cards", "credit-card")}
                    {li(f"alerts{suffix}.html", "alerts", "alert-circle")}
                    {li(f"modals{suffix}.html", "modals", "layout-dashboard")}
                    {li(f"tables{suffix}.html", "tables", "table")}
                    {li(f"extended{suffix}.html", "extended", "layout-grid")}
                    {li(f"layout{suffix}.html", "layout", "layout-dashboard")}
                    {li(f"headers{suffix}.html", "headers", "layout-header")}
                    {li(f"{index_lang_href}#utilities", "utilities", "wrench")}
                </ul>
            </div>
        </div>
    </div>
"""


def find_matching_closing_tag_end(content: str, start_idx: int, tag: str) -> int | None:
    pattern = re.compile(rf"<{tag}\b[^>]*>|</{tag}\s*>", re.IGNORECASE)
    depth = 0
    for m in pattern.finditer(content, start_idx):
        token = m.group(0).lower()
        if token.startswith(f"</{tag}"):
            depth -= 1
            if depth == 0:
                return m.end()
        else:
            depth += 1
    return None


def find_matching_div_end(content: str, start_idx: int) -> int | None:
    pattern = re.compile(r"<div\b[^>]*>|</div\s*>", re.IGNORECASE)
    depth = 0
    for m in pattern.finditer(content, start_idx):
        token = m.group(0).lower()
        if token.startswith("</div"):
            depth -= 1
            if depth == 0:
                return m.end()
        else:
            depth += 1
    return None


def remove_page_footer_after_main(content: str) -> str:
    main_end = content.rfind("</main>")
    if main_end == -1:
        return content

    drawer_start = content.find('<div id="nav-drawer"', main_end)
    if drawer_start == -1:
        drawer_start = len(content)

    footer_matches = list(
        re.finditer(r'<footer\b[^>]*class="[^"]*\bak-footer\b[^"]*"[^>]*>', content[main_end:drawer_start], re.IGNORECASE)
    )
    if not footer_matches:
        return content

    footer_open = footer_matches[-1]
    footer_start = main_end + footer_open.start()
    footer_end = find_matching_closing_tag_end(content, footer_start, "footer")
    if footer_end is None:
        return content

    return content[:footer_start] + content[footer_end:]


def replace_page_header(content: str, new_header: str) -> str:
    body_match = re.search(r"<body\b[^>]*>", content, re.IGNORECASE)
    if not body_match:
        return content

    main_match = re.search(r"<main\b", content, re.IGNORECASE)
    search_end = main_match.start() if main_match else len(content)

    header_start = content.find("<header", body_match.end(), search_end)
    if header_start == -1:
        return content[:body_match.end()] + "\n" + new_header + content[body_match.end():]

    header_end = find_matching_closing_tag_end(content, header_start, "header")
    if header_end is None:
        return content

    return content[:header_start] + new_header + content[header_end:]


def replace_or_insert_drawer(content: str, drawer_html: str) -> str:
    drawer_start = content.rfind('<div id="nav-drawer"')
    if drawer_start != -1:
        drawer_end = find_matching_div_end(content, drawer_start)
        if drawer_end is None:
            return content
        return content[:drawer_start] + drawer_html + content[drawer_end:]

    insert_before = content.rfind("</body>")
    if insert_before == -1:
        return content + drawer_html
    return content[:insert_before] + drawer_html + content[insert_before:]


def remove_theme_toggle_button_from_header(content: str) -> str:
    return re.sub(r'\s*<button[^>]*\bid="theme-toggle"[^>]*>.*?</button>\s*', "\n", content, flags=re.IGNORECASE | re.DOTALL)


def use_cdn_css_in_head(content: str) -> str:
    return re.sub(
        r'(<link\b[^>]*\brel="stylesheet"[^>]*\bhref=")(?:\.\./dist/ak-design-system(?:\.min)?\.css|https://cdn\.jsdelivr\.net/gh/ak-hosting/ak-systems-css@[^"]+/dist/ak-design-system(?:\.min)?\.css)(")',
        rf"\1{CDN_DESIGN_SYSTEM_MIN}\2",
        content,
        flags=re.IGNORECASE,
    )

def normalize_cdn_urls(content: str) -> str:
    return re.sub(
        r"https://cdn\.jsdelivr\.net/gh/ak-hosting/ak-systems-css@[^/]+/dist/ak-design-system(?:\.min)?\.css",
        CDN_DESIGN_SYSTEM_MIN,
        content,
        flags=re.IGNORECASE,
    )


def process_file(file_path: str, filename: str) -> None:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    content = normalize_cdn_urls(content)
    content = use_cdn_css_in_head(content)

    lang = filename_to_lang(filename)
    base = filename_to_base(filename)
    active_key = base
    if base == "index":
        active_key = "index"

    suffix = ""
    if lang == "de":
        suffix = ".de"
    elif lang == "tr":
        suffix = ".tr"

    index_lang_href = f"index{suffix}.html"

    title_match = re.search(r"<header\b[\s\S]*?<h1[^>]*>(.*?)</h1>", content, re.IGNORECASE)
    if title_match:
        title = title_match.group(1).strip()
    else:
        title_tag = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE | re.DOTALL)
        title = "AK Design System"
        if title_tag:
            title = re.sub(r"\s+-\s+AK Design System\s*$", "", title_tag.group(1).strip())

    content = remove_theme_toggle_button_from_header(content)
    new_header = get_header_template(title=title, base=base, lang=lang, index_lang_href=index_lang_href)
    content = replace_page_header(content, new_header)

    drawer_html = get_drawer_template(lang=lang, active_key=active_key, index_lang_href=index_lang_href)
    content = replace_or_insert_drawer(content, drawer_html)

    content = remove_page_footer_after_main(content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated {filename}")


def main() -> None:
    for filename in sorted(os.listdir(DEMO_DIR)):
        if filename.endswith(".html"):
            process_file(os.path.join(DEMO_DIR, filename), filename)


if __name__ == "__main__":
    main()
