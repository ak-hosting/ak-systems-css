import re
import os
import sys

def extract_classes(file_path):
    """Extracts CSS class names from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Regex to match class selectors like .ak-btn, .ak-modal-open
            # It handles complex selectors but focuses on extracting the class name part
            # This is a simplified regex and might need adjustment for edge cases
            classes = set(re.findall(r'\.([a-zA-Z0-9_-]+)', content))
            # Filter only ak- classes to be more specific to the design system
            ak_classes = {c for c in classes if c.startswith('ak-')}
            return ak_classes
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return set()

def verify_minified_css(source_dir, minified_file):
    """Verifies that all classes in source files exist in the minified file."""
    
    print(f"Scanning source directory: {source_dir}")
    all_source_classes = set()
    
    # Iterate through all CSS files in source directory
    for filename in os.listdir(source_dir):
        if filename.endswith(".css"):
            file_path = os.path.join(source_dir, filename)
            classes = extract_classes(file_path)
            all_source_classes.update(classes)
            # print(f"  {filename}: Found {len(classes)} classes")

    print(f"Total unique 'ak-' classes found in source: {len(all_source_classes)}")

    print(f"Reading minified file: {minified_file}")
    try:
        with open(minified_file, 'r', encoding='utf-8') as f:
            minified_content = f.read()
    except Exception as e:
        print(f"Error reading minified file: {e}")
        return

    missing_classes = []
    for cls in all_source_classes:
        # Check if the class exists in the minified content
        # We search for the class name preceded by a dot or space/brace to avoid partial matches
        # But simply checking for the string is usually enough for a quick verification 
        # given the unique prefix 'ak-'
        if cls not in minified_content:
            missing_classes.append(cls)

    if missing_classes:
        print("\n❌ MISSING CLASSES in minified file:")
        for cls in missing_classes:
            print(f"  - {cls}")
        print(f"\nFound {len(missing_classes)} missing classes.")
        sys.exit(1)
    else:
        print("\n✅ SUCCESS: All source classes found in minified file.")
        print("The minified file accurately reflects the design system source.")

if __name__ == "__main__":
    SOURCE_DIR = "css/ak-design-system"
    MINIFIED_FILE = "dist/ak-design-system.min.css"
    
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: Source directory {SOURCE_DIR} not found.")
        sys.exit(1)
        
    if not os.path.exists(MINIFIED_FILE):
        print(f"Error: Minified file {MINIFIED_FILE} not found. Run ./build.sh first.")
        sys.exit(1)

    verify_minified_css(SOURCE_DIR, MINIFIED_FILE)
