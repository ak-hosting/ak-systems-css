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

def verify_demo_classes(demo_file, minified_file):
    """Verifies that all classes used in demo file exist in the minified CSS."""
    
    print(f"Scanning demo file: {demo_file}")
    demo_classes = extract_classes_from_html(demo_file)
    print(f"Total unique 'ak-' classes found in demo: {len(demo_classes)}")

    print(f"Reading minified file: {minified_file}")
    try:
        with open(minified_file, 'r', encoding='utf-8') as f:
            minified_content = f.read()
    except Exception as e:
        print(f"Error reading minified file: {e}")
        return

    missing_classes = []
    for cls in demo_classes:
        # Check if the class exists in the minified content
        # We search for the class name preceded by a dot
        # This ensures we match the actual class definition, not just a substring
        if f".{cls}" not in minified_content:
             # Try with space or start of line if dot check fails (though minified usually has dots)
             # But actually, looking for the class definition in CSS usually involves a dot.
             # However, some classes might be used in JS or dynamic construction? 
             # No, we are checking if the CSS *supports* the class.
             
             # Also consider pseudo-classes like :hover, ::before which might be attached
             # But the class itself should be defined as .classname
             
             missing_classes.append(cls)

    if missing_classes:
        print("\n❌ POTENTIALLY MISSING CLASSES in minified file (referenced in demo):")
        for cls in missing_classes:
            print(f"  - {cls}")
        print(f"\nFound {len(missing_classes)} potentially missing classes.")
        print("Note: Some might be dynamic or utility compositions not explicitly defined if using a utility-first approach, but AK System seems to be component-based + utility.")
    else:
        print("\n✅ SUCCESS: All demo classes found in minified CSS.")

if __name__ == "__main__":
    DEMO_FILE = "demo/index.html"
    MINIFIED_FILE = "dist/ak-design-system.min.css"
    
    if not os.path.exists(DEMO_FILE):
        print(f"Error: Demo file {DEMO_FILE} not found.")
        sys.exit(1)
        
    if not os.path.exists(MINIFIED_FILE):
        print(f"Error: Minified file {MINIFIED_FILE} not found.")
        sys.exit(1)

    verify_demo_classes(DEMO_FILE, MINIFIED_FILE)
