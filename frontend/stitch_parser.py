import json
import re
from bs4 import BeautifulSoup

def process_stitch():
    with open('stitch_ui/code.html', 'r') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 1. Extract Tailwind Config
    script_tag = soup.find('script', id='tailwind-config')
    tailwind_config_str = script_tag.string if script_tag else ""
    
    # Clean up the config string to valid JS export
    if tailwind_config_str:
        # Extract everything after 'tailwind.config ='
        config_match = re.search(r'tailwind\.config\s*=\s*({.*})', tailwind_config_str, re.DOTALL)
        if config_match:
            config_json = config_match.group(1)
            js_config = f"""/** @type {{import('tailwindcss').Config}} */
export default {{
    content: [
        "./index.html",
        "./src/**/*.{{js,ts,jsx,tsx}}",
    ],
    {config_json[1:]}"""
            
            with open('tailwind.config.js', 'w') as f:
                f.write(js_config)
    
    # 2. Extract CSS
    style_tags = soup.find_all('style')
    css_content = "@tailwind base;\n@tailwind components;\n@tailwind utilities;\n\n"
    for style in style_tags:
        css_content += style.string + "\n"
    
    with open('src/index.css', 'w') as f:
        f.write(css_content)
        
    # 3. Create PostCSS Config
    with open('postcss.config.js', 'w') as f:
        f.write("""export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}""")
    
    # 4. Extract Body and convert to JSX
    body_tag = soup.find('body')
    # Remove script tags from body
    for s in body_tag.find_all('script'):
        s.decompose()
        
    body_html = str(body_tag)
    # Basic HTML to JSX conversion
    body_html = body_html.replace('class=', 'className=')
    body_html = body_html.replace('for=', 'htmlFor=')
    # Fix self-closing tags
    body_html = re.sub(r'<img(.*?)(?<!/)>', r'<img\1/>', body_html)
    body_html = re.sub(r'<input(.*?)(?<!/)>', r'<input\1/>', body_html)
    body_html = re.sub(r'<br(.*?)(?<!/)>', r'<br\1/>', body_html)
    body_html = re.sub(r'<hr(.*?)(?<!/)>', r'<hr\1/>', body_html)
    
    # Style attributes to object
    def style_replacer(match):
        style_str = match.group(1)
        styles = {}
        for rule in style_str.split(';'):
            if ':' in rule:
                key, val = rule.split(':', 1)
                key = key.strip()
                val = val.strip()
                # kebab-case to camelCase
                key = re.sub(r'-([a-z])', lambda m: m.group(1).upper(), key)
                styles[key] = val
        return f"style={{{json.dumps(styles)}}}"
    
    body_html = re.sub(r'style="([^"]*)"', style_replacer, body_html)
    body_html = re.sub(r"style='([^']*)'", style_replacer, body_html)
    
    # Create App.jsx
    jsx_content = f"""import React from 'react';
import './index.css';

function App() {{
    return (
        {body_html}
    );
}}

export default App;
"""
    with open('src/App.jsx', 'w') as f:
        f.write(jsx_content)
        
    print("Files successfully generated.")

if __name__ == "__main__":
    process_stitch()
