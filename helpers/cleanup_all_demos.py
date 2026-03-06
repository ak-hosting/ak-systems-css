import os
import re
import glob

demo_dir = '/Users/ak/dev-cloud/ak-systems-css/demo'
html_files = glob.glob(os.path.join(demo_dir, '*.html'))

def clean_file(content):
    # Remove link
    content = content.replace('<link rel="stylesheet" href="demo.css">', '')
    
    # Remove style block (generic demo styles)
    # Be careful not to remove specific styles needed for specific demos if they are not covered by framework
    # But user wants framework only.
    # The common pattern is:
    # <style>
    #     /* Demo-specific styles */
    #     body { ... }
    #     .demo-header { ... }
    # </style>
    
    # Try to match the specific comment block first
    content = re.sub(r'\s*<style>.*?/\* Demo-specific styles \*/.*?</style>', '', content, flags=re.DOTALL)
    
    # Also try to match blocks defining .demo-header if comment is missing
    # But only if it looks like the standard demo block
    if '.demo-header {' in content and '<style>' in content:
         content = re.sub(r'\s*<style>\s*body\s*\{[^}]*\}\s*\.demo-header\s*\{[^}]*\}\s*\.demo-nav\s*\{[^}]*\}\s*\.demo-section\s*\{[^}]*\}\s*.*?</style>', '', content, flags=re.DOTALL)

    # Replacements
    content = content.replace('class="demo-header"', 'class="ak-w-full ak-bg-surface ak-border-b ak-border-border ak-py-4 ak-mb-8"')
    content = content.replace('class="demo-nav"', 'class="ak-flex ak-items-center ak-gap-4"')
    content = content.replace('class="demo-section"', 'class="ak-mb-12"')
    
    # Also replace if they are just part of a class list (less common in these demos but possible)
    # Simple string replace for class names might be safer if we are sure they don't collide
    # content = content.replace('demo-header', 'ak-w-full ak-bg-surface ak-border-b ak-border-border ak-py-4 ak-mb-8')
    # But replacing "demo-header" might replace it in text content or comments.
    # Using class="..." is safer, but what if there are other classes?
    # e.g. class="demo-header sticky"
    # My previous scripts used simple replacement which worked because the files are consistent.
    # But for robustness, I'll stick to simple replacement of the class name string, assuming it's not used in text.
    
    content = content.replace('demo-header', 'ak-w-full ak-bg-surface ak-border-b ak-border-border ak-py-4 ak-mb-8')
    content = content.replace('demo-nav', 'ak-flex ak-items-center ak-gap-4')
    content = content.replace('demo-section', 'ak-mb-12')
    
    return content

for file_path in html_files:
    with open(file_path, 'r') as f:
        content = f.read()
    
    new_content = clean_file(content)
    
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
