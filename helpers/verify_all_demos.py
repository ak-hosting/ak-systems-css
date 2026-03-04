import re
import os
import sys

def extract_classes_from_html(file_path):
    """Extracts CSS class names from an HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Find class="..." attributes
            class_attrs = re.findall(r'class="([^"]+)"', content)
            classes = set()
            for attr in class_attrs:
                # Split by space to get individual classes
                for cls in attr.split():
                    if cls.startswith('ak-'):
                        classes.add(cls)
            return classes
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return set()

def verify_all_demos(demo_dir, minified_file):
    """Verifies that all classes used in demo files exist in the minified CSS."""
    
    print(f"Scanning demo directory: {demo_dir}")
    all_demo_classes = set()
    
    for filename in os.listdir(demo_dir):
        if filename.endswith(".html"):
            file_path = os.path.join(demo_dir, filename)
            classes = extract_classes_from_html(file_path)
            all_demo_classes.update(classes)
            # print(f"  {filename}: Found {len(classes)} classes")

    print(f"Total unique 'ak-' classes found in demos: {len(all_demo_classes)}")

    print(f"Reading minified file: {minified_file}")
    try:
        with open(minified_file, 'r', encoding='utf-8') as f:
            minified_content = f.read()
    except Exception as e:
        print(f"Error reading minified file: {e}")
        return

    missing_classes = []
    for cls in all_demo_classes:
        # Handle responsive prefixes with colons
        # HTML: class="ak-md:ak-grid-cols-2"
        # CSS: .ak-md\:ak-grid-cols-2
        css_selector = f".{cls.replace(':', '\\:')}"
        
        # Check if the class exists in the minified content
        if css_selector not in minified_content:
            missing_classes.append(cls)

    if missing_classes:
        print("\n❌ POTENTIALLY MISSING CLASSES in minified file (referenced in demos):")
        for cls in sorted(missing_classes):
            print(f"  - {cls}")
        print(f"\nFound {len(missing_classes)} potentially missing classes.")
    else:
        print("\n✅ SUCCESS: All demo classes found in minified CSS.")

if __name__ == "__main__":
    DEMO_DIR = "demo"
    MINIFIED_FILE = "dist/ak-design-system.min.css"
    
    if not os.path.exists(DEMO_DIR):
        print(f"Error: Demo directory {DEMO_DIR} not found.")
        sys.exit(1)
        
    if not os.path.exists(MINIFIED_FILE):
        print(f"Error: Minified file {MINIFIED_FILE} not found.")
        sys.exit(1)

    verify_all_demos(DEMO_DIR, MINIFIED_FILE)
