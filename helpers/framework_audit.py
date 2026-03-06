import os
import re
import sys
from pathlib import Path

# Configuration
DIST_CSS = "dist/ak-design-system.css"
SEARCH_DIRS = ["demo", "."]
IGNORE_DIRS = [".git", "node_modules", "dist", "css", "src", "helpers", "docs", ".github", "__pycache__"]
IGNORE_FILES = ["index.html"] # Maybe ignore root index if it's just a redirect or similar? No, check it.

def parse_css_classes(css_path):
    if not os.path.exists(css_path):
        print(f"Error: CSS file not found at {css_path}")
        return set()
    
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple regex to capture classes starting with .
    # This is a naive parser but should work for standard CSS
    # It looks for .classname followed by space, comma, :, ., or {
    # It excludes things inside comments (though we should strip comments first)
    
    # Strip comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    
    classes = set()
    # Regex for class selector: \.([a-zA-Z0-9_-]+)
    # We need to be careful not to capture things inside values (e.g. .5em)
    # But usually selectors are at the start of line or after } or ,
    
    # Let's try to match selectors. 
    # A selector is text before {
    selectors = re.findall(r'([^{]+){', content)
    
    for sel in selectors:
        # Split by comma for multiple selectors
        parts = sel.split(',')
        for part in parts:
            # Find all .classnames in the selector part
            # We want to match .ak-something but not 0.5px
            # Valid CSS identifier starts with - or letter/underscore.
            # Modified to handle escaped characters (like \: for responsive prefixes and \/ for fractions)
            # e.g. .ak-md\:ak-block, .ak-w-1\/2
            matches = re.findall(r'\.(-?[_a-zA-Z]+[_a-zA-Z0-9-]*(?:\\:[_a-zA-Z0-9-]+)*(?:\\/[0-9]+)?)', part)
            for m in matches:
                # Remove backslashes for comparison with HTML attributes
                clean_class = m.replace('\\', '')
                classes.add(clean_class)
                
    return classes

def parse_html_classes(root_dirs):
    used_classes = set()
    file_map = {} # class -> list of files
    
    files_to_scan = []
    
    for root_dir in root_dirs:
        if root_dir == ".":
            # Scan files in root
            for f in os.listdir("."):
                if f.endswith(".html") and os.path.isfile(f):
                    files_to_scan.append(f)
        else:
            for root, dirs, files in os.walk(root_dir):
                # Modify dirs in-place to skip ignored
                dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
                
                for file in files:
                    if file.endswith(".html"):
                        files_to_scan.append(os.path.join(root, file))
    
    print(f"Scanning {len(files_to_scan)} HTML files...")
    
    for file_path in files_to_scan:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to find class="..."
        # Handles single and double quotes
        matches = re.findall(r'class=["\']([^"\']*)["\']', content)
        
        for match in matches:
            # Split by whitespace
            cls_list = match.split()
            for cls in cls_list:
                used_classes.add(cls)
                if cls not in file_map:
                    file_map[cls] = []
                if file_path not in file_map[cls]:
                    file_map[cls].append(file_path)
                    
    return used_classes, file_map

def main():
    print("--- Agent 1: Framework Analyzer ---")
    defined_classes = parse_css_classes(DIST_CSS)
    print(f"Found {len(defined_classes)} classes in framework.")
    
    print("\n--- Agent 2: HTML Scanner ---")
    used_classes, file_map = parse_html_classes(SEARCH_DIRS)
    print(f"Found {len(used_classes)} unique classes used in HTML.")
    
    print("\n--- Agent 3: CSS Comparator ---")
    found = set()
    missing = set()
    
    for cls in used_classes:
        if cls in defined_classes:
            found.add(cls)
        else:
            missing.add(cls)
            
    print(f"FOUND: {len(found)}")
    print(f"MISSING: {len(missing)}")
    
    print("\n--- Detailed Report ---")
    if missing:
        print("MISSING CLASSES:")
        for cls in sorted(missing):
            print(f"  {cls} (used in: {', '.join(file_map[cls][:3])}{'...' if len(file_map[cls])>3 else ''})")
    else:
        print("No missing classes found! Great job.")

if __name__ == "__main__":
    main()
