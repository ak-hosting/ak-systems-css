import os

files = [
    '/Users/ak/dev-cloud/ak-systems-css/demo/cards.html',
    '/Users/ak/dev-cloud/ak-systems-css/demo/cards.de.html',
    '/Users/ak/dev-cloud/ak-systems-css/demo/cards.tr.html'
]

replacements = {
    '<link rel="stylesheet" href="demo.css">': '',
    'class="demo-header"': 'class="ak-w-full ak-bg-surface ak-border-b ak-border-border ak-py-4 ak-mb-8"',
    'class="demo-nav"': 'class="ak-flex ak-items-center ak-gap-4"',
    'class="demo-section"': 'class="ak-mb-12"',
    'class="demo-grid"': 'class="ak-grid ak-grid-cols-1 ak-md-grid-cols-2 ak-lg-grid-cols-3 ak-gap-6"',
    'class="demo-description"': 'class="ak-text-muted ak-mb-6"'
}

for file_path in files:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r') as f:
        content = f.read()
    
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
        
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
