import os
import re

modal_files = [
    '/Users/ak/dev-cloud/ak-systems-css/demo/modals.html',
    '/Users/ak/dev-cloud/ak-systems-css/demo/modals.de.html',
    '/Users/ak/dev-cloud/ak-systems-css/demo/modals.tr.html'
]

section_files = [
    '/Users/ak/dev-cloud/ak-systems-css/demo/sections.html',
    '/Users/ak/dev-cloud/ak-systems-css/demo/sections.de.html',
    '/Users/ak/dev-cloud/ak-systems-css/demo/sections.tr.html'
]

def clean_modals(content):
    # Remove link if present (it wasn't in modals.html but checking anyway)
    content = content.replace('<link rel="stylesheet" href="demo.css">', '')
    
    # Remove style block (lines 16-77 roughly)
    # Using regex to match style block containing demo-specific styles
    content = re.sub(r'\s*<style>.*?/* Demo-specific styles */.*?</style>', '', content, flags=re.DOTALL)
    
    # Also catch if the comment is slightly different or missing
    content = re.sub(r'\s*<style>\s*\.demo-header.*?</style>', '', content, flags=re.DOTALL)
    
    # Replacements
    content = content.replace('demo-header', 'ak-w-full ak-bg-surface ak-border-b ak-border-border ak-py-4 ak-mb-8')
    content = content.replace('demo-nav', 'ak-flex ak-items-center ak-gap-4')
    content = content.replace('demo-section', 'ak-mb-12')
    
    return content

def clean_sections(content):
    # Remove link
    content = content.replace('<link rel="stylesheet" href="demo.css">', '')
    
    # Remove style block
    content = re.sub(r'\s*<style>.*?/* Demo-specific styles */.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*<style>\s*\.demo-header.*?</style>', '', content, flags=re.DOTALL)
    
    # Replacements
    content = content.replace('demo-header', 'ak-w-full ak-bg-surface ak-border-b ak-border-border ak-py-4 ak-mb-8')
    content = content.replace('demo-nav', 'ak-flex ak-items-center ak-gap-4')
    content = content.replace('demo-section', 'ak-mb-12')
    
    # Custom class replacements
    content = content.replace('ak-company-name', 'ak-font-bold ak-text-primary')
    content = content.replace('ak-copyright-year', 'ak-text-sm ak-text-muted')
    
    return content

for file_path in modal_files:
    if not os.path.exists(file_path):
        continue
    with open(file_path, 'r') as f:
        content = f.read()
    new_content = clean_modals(content)
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {file_path}")

for file_path in section_files:
    if not os.path.exists(file_path):
        continue
    with open(file_path, 'r') as f:
        content = f.read()
    new_content = clean_sections(content)
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
