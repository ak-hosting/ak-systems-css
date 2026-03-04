import os
import re

def check_files():
    demo_dir = '/Users/ak/dev-cloud/ak-systems-css/demo'
    files = [f for f in os.listdir(demo_dir) if f.endswith('.html')]
    
    issues = []
    
    for file in files:
        path = os.path.join(demo_dir, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Check for drawer
            if '<div id="nav-drawer"' not in content:
                issues.append(f"{file}: Missing nav-drawer")
                
            # Check for openModal function with null check
            if 'function openModal(id)' not in content:
                issues.append(f"{file}: Missing openModal function")
            elif 'if (modal)' not in content: # Simple check, might match elsewhere but good enough for now
                 issues.append(f"{file}: Missing null check in script (likely)")
                 
            # Check for Escape key handler
            if "e.key === 'Escape'" not in content and 'e.key === "Escape"' not in content:
                issues.append(f"{file}: Missing Escape key handler")
                
    if not issues:
        print("All files passed checks!")
    else:
        for issue in issues:
            print(issue)

if __name__ == '__main__':
    check_files()
