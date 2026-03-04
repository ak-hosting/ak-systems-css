
import os
import re

def check_active_links():
    demo_dir = '/Users/ak/dev-cloud/ak-systems-css/demo'
    files = [f for f in os.listdir(demo_dir) if f.endswith('.html')]
    
    files_missing_active = []
    
    print("Checking active links...")
    
    for file in files:
        # Determine expected href
        # If file is index.html, index.de.html, etc., we might look for data-page="index"
        # But generally the href points to the file itself.
        
        path = os.path.join(demo_dir, file)
        
        # Mapping file to expected href/data-page logic
        # Simple heuristic: Look for the filename in the href attribute OF AN ACTIVE LINK
        
        expected_href = file
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Pattern: <a href="FILENAME" class="ak-active"
            # OR class="ak-active" ... href="FILENAME"
            # We can just check if the specific string exists, or use regex for flexibility
            
            # Regex to find an anchor tag that has both href="expected_href" AND class="...ak-active..."
            # Note: The class might be "ak-nav-link ak-active" or just "ak-active"
            
            # Simplification: Check if the line containing the href also contains "ak-active"
            
            lines = content.split('\n')
            found = False
            for line in lines:
                if f'href="{expected_href}"' in line and 'ak-active' in line:
                    found = True
                    break
                # Special case for index pages which might have href="index.html" or href="#overview"
                if 'index' in file:
                     if 'href="index.html"' in line and 'ak-active' in line: # Fallback
                         found = True
                         break
                     if 'data-page="index"' in line and 'ak-active' in line:
                         found = True
                         break
            
            if not found:
                files_missing_active.append(file)

    if files_missing_active:
        print(f"Found {len(files_missing_active)} files missing active link:")
        for f in files_missing_active:
            print(f"- {f}")
    else:
        print("All files have correct active links!")

if __name__ == "__main__":
    check_active_links()
