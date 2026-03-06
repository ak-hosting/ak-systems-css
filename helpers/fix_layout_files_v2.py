import os
import re

files = [
    '/Users/ak/dev-cloud/ak-systems-css/demo/layout.html',
    '/Users/ak/dev-cloud/ak-systems-css/demo/layout.de.html',
    '/Users/ak/dev-cloud/ak-systems-css/demo/layout.tr.html'
]

def replace_classes(content):
    # Remove link
    content = content.replace('<link rel="stylesheet" href="demo.css">', '')
    
    # Remove style block
    content = re.sub(r'\s*<style>\s*body\s*{\s*padding-bottom:\s*4rem;\s*}\s*</style>', '', content, flags=re.DOTALL)
    
    # Simple class replacements
    content = content.replace('demo-header', 'ak-w-full ak-bg-surface ak-border-b ak-border-border ak-py-4 ak-mb-8')
    content = content.replace('demo-nav', 'ak-flex ak-items-center ak-gap-4')
    content = content.replace('demo-section', 'ak-mb-12')
    
    # Grid box replacements
    # We replace demo-grid-box-highlight first to handle the override
    # Actually, simpler to just replace the string and let CSS cascade or just accept the verbose classes
    # But to be cleaner:
    
    # Replace demo-grid-box-highlight with specific styles
    content = content.replace('demo-grid-box-highlight', 'ak-bg-primary-subtle ak-text-primary')
    
    # Replace demo-grid-box with base styles
    content = content.replace('demo-grid-box', 'ak-bg-surface-variant ak-p-4 ak-rounded ak-border ak-border-border ak-text-center')
    
    return content

for file_path in files:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r') as f:
        content = f.read()
    
    new_content = replace_classes(content)
        
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
