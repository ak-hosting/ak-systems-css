import os
import re

def check_files():
    demo_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'demo'))
    files = [f for f in os.listdir(demo_dir) if f.endswith('.html')]
    
    issues = []
    
    for file in files:
        path = os.path.join(demo_dir, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Check for drawer
            if '<div id="nav-drawer"' not in content:
                issues.append(f"{file}: Missing nav-drawer")
                
            has_demo_script = bool(re.search(r'<script[^>]+src="js/ak-demo\.js"[^>]*>\s*</script>', content, re.IGNORECASE))
            has_open_modal = 'function openModal(id)' in content or has_demo_script
            if not has_open_modal:
                issues.append(f"{file}: Missing openModal implementation (inline or js/ak-demo.js)")
                 
            # Check for Escape key handler
            has_escape_handler = ("e.key === 'Escape'" in content) or ('e.key === "Escape"' in content) or has_demo_script
            if not has_escape_handler:
                issues.append(f"{file}: Missing Escape key handler (inline or js/ak-demo.js)")
                
    if not issues:
        print("All files passed checks!")
    else:
        for issue in issues:
            print(issue)

if __name__ == '__main__':
    check_files()
