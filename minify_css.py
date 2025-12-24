#!/usr/bin/env python3
"""
CSS Minifier - Removes comments, unnecessary whitespace, and compresses CSS
"""

import re
import sys

def minify_css(css_content):
    """
    Minify CSS by removing comments, unnecessary whitespace, and compressing
    """
    # Remove CSS comments (/* ... */) but preserve /*! ... */ (important comments)
    css_content = re.sub(r'/\*(?!\!)[^*]*\*+(?:[^/*][^*]*\*+)*/', '', css_content)
    
    # Remove leading/trailing whitespace from each line
    css_content = '\n'.join(line.strip() for line in css_content.split('\n'))
    
    # Remove empty lines
    css_content = re.sub(r'\n\s*\n', '\n', css_content)
    
    # Remove whitespace around certain characters
    css_content = re.sub(r'\s*{\s*', '{', css_content)
    css_content = re.sub(r'\s*}\s*', '}', css_content)
    css_content = re.sub(r'\s*:\s*', ':', css_content)
    css_content = re.sub(r'\s*;\s*', ';', css_content)
    css_content = re.sub(r'\s*,\s*', ',', css_content)
    
    # Remove whitespace before certain characters
    css_content = re.sub(r'\s+([{}:;,)])', r'\1', css_content)
    
    # Remove whitespace after certain characters
    css_content = re.sub(r'([{}:;,(])\s+', r'\1', css_content)
    
    # Remove whitespace around operators in calc() and similar
    css_content = re.sub(r'\s*([+\-*/=])\s*', r'\1', css_content)
    
    # Remove last semicolon before closing brace
    css_content = re.sub(r';}', '}', css_content)
    
    # Remove whitespace between selectors and {
    css_content = re.sub(r'\s+{', '{', css_content)
    
    # Compress multiple spaces to single space (but preserve in strings)
    css_content = re.sub(r' +', ' ', css_content)
    
    # Remove all remaining newlines and unnecessary spaces
    css_content = re.sub(r'\n', '', css_content)
    css_content = re.sub(r'\s+', ' ', css_content)
    
    # Final cleanup: remove spaces around certain patterns
    css_content = re.sub(r'\s*>\s*', '>', css_content)
    css_content = re.sub(r'\s*\+\s*', '+', css_content)
    css_content = re.sub(r'\s*~\s*', '~', css_content)
    
    return css_content.strip()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: minify_css.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        minified = minify_css(css_content)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(minified)
        
        # Calculate compression ratio
        original_size = len(css_content.encode('utf-8'))
        minified_size = len(minified.encode('utf-8'))
        ratio = (1 - minified_size / original_size) * 100 if original_size > 0 else 0
        
        print(f"Minified: {original_size:,} bytes → {minified_size:,} bytes ({ratio:.1f}% reduction)")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

