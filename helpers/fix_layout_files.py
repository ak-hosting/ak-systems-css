import os
import re

files = [
    '/Users/ak/dev-cloud/ak-systems-css/demo/layout.html',
    '/Users/ak/dev-cloud/ak-systems-css/demo/layout.de.html',
    '/Users/ak/dev-cloud/ak-systems-css/demo/layout.tr.html'
]

replacements = {
    '<link rel="stylesheet" href="demo.css">': '',
    'class="demo-header"': 'class="ak-w-full ak-bg-surface ak-border-b ak-border-border ak-py-4 ak-mb-8"',
    'class="demo-nav"': 'class="ak-flex ak-items-center ak-gap-4"',
    'class="demo-section"': 'class="ak-mb-12"',
    'class="demo-grid-box"': 'class="ak-bg-surface-variant ak-p-4 ak-rounded ak-border ak-border-border ak-text-center"',
    'class="demo-grid-box ak-col-span-8 demo-grid-box-highlight"': 'class="ak-bg-primary-subtle ak-text-primary ak-p-4 ak-rounded ak-border ak-border-border ak-text-center ak-col-span-8"',
    'class="demo-grid-box ak-col-span-4"': 'class="ak-bg-surface-variant ak-p-4 ak-rounded ak-border ak-border-border ak-text-center ak-col-span-4"',
    'class="demo-grid-box-highlight"': 'class="ak-bg-primary-subtle ak-text-primary ak-p-4 ak-rounded ak-border ak-border-border ak-text-center"'
}

# Regex for removing the style block
style_pattern = re.compile(r'\s*<style>\s*body\s*{\s*padding-bottom:\s*4rem;\s*}\s*</style>', re.DOTALL)

for file_path in files:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r') as f:
        content = f.read()
    
    new_content = content
    
    # Apply string replacements
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
    
    # Remove style block
    new_content = style_pattern.sub('', new_content)
        
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
