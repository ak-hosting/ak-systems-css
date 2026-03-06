import os
import re

DEMO_DIR = os.path.join(os.getcwd(), 'demo')
CDN_LINK = 'https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@v2.0.0/dist/ak-design-system.min.css'
LOCAL_LINK = '../dist/ak-design-system.min.css'

# Regex for "Modal logic" block (found in sections.html)
MODAL_LOGIC_REGEX = re.compile(r'<script>\s*// Modal logic[\s\S]*?</script>', re.MULTILINE)

# Regex for broken script fragments (residue)
# Matches if (openModals.length > 0) ... });
# This catches the residue both inside <script> tags (index.html) and standing alone (cards.html)
BROKEN_FRAGMENT_REGEX = re.compile(r'\s*if \(openModals\.length > 0\) \{[\s\S]*?\}\s*\}\s*\)\s*;\s*', re.MULTILINE)

# Regex for lucide.createIcons() if it stands alone
LUCIDE_REGEX = re.compile(r'\s*lucide\.createIcons\(\);\s*', re.MULTILINE)

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Revert LOCAL link to CDN link
    if LOCAL_LINK in content:
        content = content.replace(LOCAL_LINK, CDN_LINK)
        print(f"Reverted local CSS link to CDN in {os.path.basename(file_path)}")
    
    # 2. Remove "Modal logic" block
    if MODAL_LOGIC_REGEX.search(content):
        content = MODAL_LOGIC_REGEX.sub('', content)
        print(f"Removed inline modal logic from {os.path.basename(file_path)}")
        
    # 3. Remove broken script fragments
    if BROKEN_FRAGMENT_REGEX.search(content):
        content = BROKEN_FRAGMENT_REGEX.sub('', content)
        print(f"Removed broken script fragment from {os.path.basename(file_path)}")
    
    # 4. Remove lucide.createIcons() call
    if LUCIDE_REGEX.search(content):
        content = LUCIDE_REGEX.sub('', content)
        print(f"Removed lucide.createIcons() from {os.path.basename(file_path)}")

    # 5. Clean up empty script tags resulting from removal
    content = re.sub(r'<script>\s*</script>', '', content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    count = 0
    if not os.path.exists(DEMO_DIR):
        print(f"Directory not found: {DEMO_DIR}")
        return

    for filename in os.listdir(DEMO_DIR):
        if filename.endswith('.html'):
            if process_file(os.path.join(DEMO_DIR, filename)):
                count += 1
    print(f"Processed {count} files.")

if __name__ == '__main__':
    main()
