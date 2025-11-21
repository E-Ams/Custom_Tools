import re
import os

def convert_wiki_links(content):
    """Convert wiki-style links to absolute GitHub wiki URLs"""
    
    # Pattern to match [text](link) where link doesn't start with http
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    def replace_link(match):
        text = match.group(1)
        link = match.group(2)
        
        # Don't convert absolute URLs or anchor links
        if link.startswith(('http://', 'https://', '#', '/')):
            return match.group(0)
        
        # Convert wiki page links
        base_url = "https://github.com/E-Ams/Custom_Tools/wiki"
        return f'[{text}]({base_url}/{link})'
    
    return re.sub(pattern, replace_link, content)

def main():
    # Read the README.md file
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convert the links
    converted_content = convert_wiki_links(content)
    
    # Write back to README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(converted_content)

if __name__ == '__main__':
    main()