import os
import re

DEMO_DIR = '/Users/ak/dev-cloud/ak-systems-css/demo'
REFERENCE_FOOTER = """
    <footer class="ak-footer">
        <div class="ak-container">
            <p class="ak-text-sm">&copy; 2025 ak-systems. All rights reserved.</p>
        </div>
    </footer>
"""

def get_header_template(title, lang_links, theme_toggle="", is_index=False):
    # Standardize Language Links
    # If lang_links is empty or malformed, we might need to regenerate them based on filename
    # But for now, let's assume we can extract them or use a default set if missing.
    
    back_link = ""
    if not is_index:
        back_link = """
                    <a href="index.html" class="ak-btn ak-btn-ghost ak-btn-sm">
                        <i data-lucide="arrow-left" class="ak-w-4 ak-h-4 ak-mr-2"></i>
                        Back to Index
                    </a>"""
    
    # Ensure title is wrapped correctly
    title_html = f'<h1 class="ak-text-xl ak-font-bold">{title}</h1>'
    
    # If lang_links are passed as list/string, insert them.
    # Default to generic if not found (though we should try to preserve existing hrefs)
    
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
                    {theme_toggle}
                </div>
            </div>
        </div>
    </header>"""

def process_file(file_path, filename):
    with open(file_path, 'r') as f:
        content = f.read()
    
    is_index = 'index' in filename
    
    # 1. Extract Title
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', content)
    title = title_match.group(1) if title_match else "AK Design System"
    
    # 2. Extract Language Links
    # Extract links that look like language switchers (EN/DE/TR)
    lang_links_list = re.findall(r'<a href="[^"]+"[^>]*class="[^"]*ak-btn[^"]*"[^>]*>\s*(?:EN|DE|TR)\s*</a>', content)
    
    if lang_links_list:
        lang_links = "\n                    ".join(lang_links_list)
    else:
        # Fallback if no lang links found (e.g. maybe different structure)
        # Try to guess based on filename
        base_name = filename.split('.')[0]
        lang_links = f"""<a href="{base_name}.html" class="ak-btn ak-btn-sm ak-btn-primary">EN</a>
                    <a href="{base_name}.de.html" class="ak-btn ak-btn-sm ak-btn-ghost">DE</a>
                    <a href="{base_name}.tr.html" class="ak-btn ak-btn-sm ak-btn-ghost">TR</a>"""
        # Adjust active state based on lang
        if '.de.' in filename:
            lang_links = lang_links.replace('ak-btn-primary">EN', 'ak-btn-ghost">EN').replace('ak-btn-ghost">DE', 'ak-btn-primary">DE')
        elif '.tr.' in filename:
            lang_links = lang_links.replace('ak-btn-primary">EN', 'ak-btn-ghost">EN').replace('ak-btn-ghost">TR', 'ak-btn-primary">TR')

    # 3. Extract Theme Toggle
    theme_toggle_match = re.search(r'<button[^>]*id="theme-toggle"[^>]*>.*?</button>', content, re.DOTALL)
    theme_toggle = theme_toggle_match.group(0) if theme_toggle_match else ""

    # 4. Replace Header
    # Match existing header block (greedy or non-greedy? We need to be careful not to eat too much)
    # Most headers seem to start with <header and end with </header>
    # We will replace the entire FIRST header block found.
    
    new_header = get_header_template(title, lang_links, theme_toggle, is_index)
    
    # Regex to find the header.
    # Note: index.html has a comment <!-- Header --> before it.
    
    header_pattern = re.compile(r'<header.*?>.*?</header>', re.DOTALL)
    
    if header_pattern.search(content):
        content = header_pattern.sub(new_header, content, count=1)
    else:
        # If no header found, insert after <body ...>
        body_match = re.search(r'<body[^>]*>', content)
        if body_match:
            content = content[:body_match.end()] + '\n' + new_header + content[body_match.end():]
    
    # 4. Replace/Add Footer
    # Find existing footer (the page footer, not example footers inside code blocks or containers)
    # This is tricky because there might be multiple footers in examples.
    # We should look for the footer at the very end of the body, before scripts.
    
    # Strategy: Check if the LAST footer is likely the page footer.
    # Or check if there is a footer that is a direct child of body (hard to tell with regex).
    # But in our demo files, the page footer should be near the end.
    
    # If we find a footer that looks like the page footer (class="ak-footer" and possibly containing copyright), replace it.
    # If not, append it.
    
    # Let's try to find a footer that is NOT inside a `div class="ak-bg-surface-subtle..."` (which are examples).
    # But regex is weak for this.
    
    # Alternative: Look for the specific footer structure we want to replace OR append if missing.
    # If we assume the page footer is the last element before scripts/modals?
    
    # Let's just append the footer before the `nav-drawer` or `scripts` if it doesn't exist.
    # If it exists (e.g. in index.html), we might want to replace it.
    
    # In index.html, the footer is `<footer class="ak-footer">\n    </footer>`.
    # We can match that specific pattern.
    
    footer_pattern = re.compile(r'<footer class="ak-footer">\s*(<div class="ak-container">.*?</div>)?\s*</footer>', re.DOTALL)
    
    # Find all footers
    footers = list(footer_pattern.finditer(content))
    
    replaced_footer = False
    if footers:
        # Check if the last footer is the main one.
        # In index.html, there are many footers. The last one is the empty one.
        last_footer = footers[-1]
        # We can try to replace the last footer if it looks like a page footer.
        # But for safety, let's only replace if it's explicitly the one we identified or if it's missing.
        
        # Actually, let's just insert our footer before the nav-drawer (if present) or scripts.
        # And REMOVE any "page footer" that we identify as the old one (if it exists).
        pass
        
    # Simplified approach:
    # 1. Remove any existing "Page Footer" (we define this as a footer at the root level, usually near end).
    #    In index.html it's `<footer class="ak-footer"></footer>` at the end.
    #    In buttons.html it's missing.
    
    # Let's remove the specific footer pattern found in index.html
    content = re.sub(r'<footer class="ak-footer">\s*</footer>', '', content) # Remove empty footer
    content = re.sub(r'<footer class="ak-footer">\s*<div class="ak-container">\s*<p class="ak-text-sm">&copy;.*?</p>\s*</div>\s*</footer>', '', content, flags=re.DOTALL) # Remove existing correct footer to re-add it
    
    # Now append the new footer
    # Insert before <div id="nav-drawer" ...> OR <script> OR </body>
    
    insertion_point = -1
    
    nav_drawer_match = re.search(r'<div id="nav-drawer"', content)
    if nav_drawer_match:
        insertion_point = nav_drawer_match.start()
    else:
        script_match = re.search(r'<script', content)
        if script_match:
            insertion_point = script_match.start()
        else:
            body_end_match = re.search(r'</body>', content)
            if body_end_match:
                insertion_point = body_end_match.start()
    
    if insertion_point != -1:
        content = content[:insertion_point] + REFERENCE_FOOTER + '\n' + content[insertion_point:]
    
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"Updated {filename}")

def main():
    for filename in os.listdir(DEMO_DIR):
        if filename.endswith('.html') and 'headers' not in filename:
            process_file(os.path.join(DEMO_DIR, filename), filename)

if __name__ == "__main__":
    main()
