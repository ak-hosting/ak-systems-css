
import os

def check_files():
    demo_dir = '/Users/ak/dev-cloud/ak-systems-css/demo'
    files = [f for f in os.listdir(demo_dir) if f.endswith('.html')]
    
    files_with_old_script = []
    files_perfect = []
    
    print("Checking files for strict script compliance...")
    
    for file in files:
        path = os.path.join(demo_dir, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            has_strict_escape = "querySelectorAll('.ak-modal.ak-modal-open')" in content
            has_strict_click = "e.target.classList.contains('ak-modal')" in content
            
            if not has_strict_escape or not has_strict_click:
                files_with_old_script.append(file)
            else:
                files_perfect.append(file)
                
    if files_with_old_script:
        print(f"Found {len(files_with_old_script)} files with old script:")
        for f in files_with_old_script:
            print(f"- {f}")
    else:
        print("All files have strict script compliance!")

if __name__ == "__main__":
    check_files()
