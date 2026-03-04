import os
import re

demo_dir = '/Users/ak/dev-cloud/ak-systems-css/demo'
# The link to add. We use a simple version, indentation might be off but HTML doesn't care much.
# We'll try to match indentation of the previous line if possible, or just use a standard one.
link_to_add = '\n                    <li><a href="selection-controls.html"><i data-lucide="check-square" class="ak-w-4 ak-h-4 ak-mr-2"></i><span>Selection Controls</span></a></li>'
link_to_add_with_data = '\n                    <li><a href="selection-controls.html" data-page="selection"><i data-lucide="check-square" class="ak-w-4 ak-h-4 ak-mr-2"></i><span>Selection Controls</span></a></li>'

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    if 'selection-controls.html' in content:
        print(f"Skipping {filepath} (already present)")
        return

    # Find forms link block
    # Matches <li>...<a href="...forms...">...</a>...</li>
    # Handles multiline with re.DOTALL
    # We look for href containing forms.html, forms.xx.html, or #forms
    pattern = re.compile(r'(<li[^>]*>\s*<a href="[^"]*(?:forms(?:\.[a-z]{2})?\.html|#forms)"[^>]*>.*?</li>)', re.IGNORECASE | re.DOTALL)
    
    match = pattern.search(content)
    if match:
        full_match = match.group(1)
        
        # Decide which link style to use
        if 'data-page' in full_match or 'data-section' in full_match:
             # If using data-section, we might want to stick to data-page for external link?
             # index.html uses data-section for internal anchors but data-page is not used there?
             # Let's check index.html sidebar again. 
             # It uses data-section="overview".
             # But for selection-controls it uses... wait, I need to check index.html again.
             # index.html: <a href="selection-controls.html"> (no data-attribute)
             # So if we are in index.html (indicated by #forms), we might not need data-page.
             # But forms.html uses data-page.
             if '#forms' in full_match:
                 new_link = link_to_add # No data-page for index pages
             else:
                 new_link = link_to_add_with_data
        else:
            new_link = link_to_add
            
        # Insert after
        new_content = content.replace(full_match, full_match + new_link)
        
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Could not find forms link in {filepath}")

for filename in os.listdir(demo_dir):
    if filename.endswith('.html'):
        update_file(os.path.join(demo_dir, filename))
