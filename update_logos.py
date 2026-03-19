#!/usr/bin/env python3
import os

# Logo SVG inline to embed in navigation - BitWin + 币胜网
LOGO_SVG_NAV = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 50" width="260" height="40">
  <circle cx="25" cy="25" r="22" fill="#f7931a"/>
  <path d="M15 12h10c6 0 10 3 10 8 0 3-2 5-2 5 0 5 2 4 2 6 5 6v2c0 4-2 7-6 7h-10zm8 14c2 0 3-1 3-3v-2c0-2-1-3-3-3h-5v8zm-8-12v8h5c2 0 3-1 3-3v-2c0-2-1-3-3-3z" fill="white"/>
  <text x="55" y="32" font-family="Arial, Helvetica, sans-serif" font-size="28" font-weight="bold" fill="#f7931a">Bit<tspan fill="currentColor">Win</tspan></text>
  <text x="140" y="32" font-family="Arial, Helvetica, sans-serif" font-size="26" font-weight="bold">
    <tspan fill="#f7931a">币</tspan><tspan fill="currentColor">胜网</tspan>
  </text>
</svg>'''

# Footer logo is larger - BitWin + 币胜网
LOGO_SVG_FOOTER = '''<div class="footer-logo">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 75" width="380" height="63">
  <circle cx="38" cy="38" r="33" fill="#f7931a"/>
  <path d="M22 18h15c9 0 15 4.5 15 12 0 4.5-3 7.5-3 7.5 0 7.5 3 6 3 9 9 9v3c0 6-3 10.5-9 10.5h-15zm12 21c3 0 4.5-1.5 4.5-4.5v-3c0-3-1.5-4.5-4.5-4.5h-7.5v12zm-12-18v12h7.5c3 0 4.5-1.5 4.5-4.5v-3c0-3-1.5-4.5-4.5-4.5z" fill="white"/>
  <text x="85" y="48" font-family="Arial, Helvetica, sans-serif" font-size="42" font-weight="bold" fill="#f7931a">Bit<tspan fill="currentColor">Win</tspan></text>
  <text x="220" y="48" font-family="Arial, Helvetica, sans-serif" font-size="40" font-weight="bold">
    <tspan fill="#f7931a">币</tspan><tspan fill="currentColor">胜网</tspan>
  </text>
</svg>
</div>'''

# Old SVG without Chinese text (current in files)
OLD_NAV_LINK_SVG = '''<a href="/" class="nav-brand"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 50" width="160" height="40">
  <circle cx="25" cy="25" r="22" fill="#f7931a"/>
  <path d="M15 12h10c6 0 10 3 10 8 0 3-2 5-2 5 0 5 2 4 2 6 5 6v2c0 4-2 7-6 7h-10zm8 14c2 0 3-1 3-3v-2c0-2-1-3-3-3h-5v8zm-8-12v8h5c2 0 3-1 3-3v-2c0-2-1-3-3-3z" fill="white"/>
  <text x="55" y="32" font-family="Arial, Helvetica, sans-serif" font-size="28" font-weight="bold" fill="#f7931a">Bit<tspan fill="currentColor">Win</tspan></text>
</svg></a>'''
# Already has Chinese but with old wider spacing (165px)
OLD_NAV_SVG_SPACING = '''<a href="/" class="nav-brand"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 50" width="260" height="40">
  <circle cx="25" cy="25" r="22" fill="#f7931a"/>
  <path d="M15 12h10c6 0 10 3 10 8 0 3-2 5-2 5 0 5 2 4 2 6 5 6v2c0 4-2 7-6 7h-10zm8 14c2 0 3-1 3-3v-2c0-2-1-3-3-3h-5v8zm-8-12v8h5c2 0 3-1 3-3v-2c0-2-1-3-3-3z" fill="white"/>
  <text x="55" y="32" font-family="Arial, Helvetica, sans-serif" font-size="28" font-weight="bold" fill="#f7931a">Bit<tspan fill="currentColor">Win</tspan></text>
  <text x="165" y="32" font-family="Arial, Helvetica, sans-serif" font-size="26" font-weight="bold">
    <tspan fill="#f7931a">币</tspan><tspan fill="currentColor">胜网</tspan>
  </text>
</svg></a>'''
OLD_NAV_LINK_TEXT = '<a href="/" class="nav-brand">币胜网</a>'
NEW_NAV_LINK = f'<a href="/" class="nav-brand">{LOGO_SVG_NAV}</a>'

# Old footer without Chinese text
OLD_FOOTER_CONTENT_OLD = '<p>币胜网 © 2026</p>'
OLD_FOOTER_SVG_OLD = '''<div class="footer-logo">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 75" width="250" height="63">
  <circle cx="38" cy="38" r="33" fill="#f7931a"/>
  <path d="M22 18h15c9 0 15 4.5 15 12 0 4.5-3 7.5-3 7.5 0 7.5 3 6 3 9 9 9v3c0 6-3 10.5-9 10.5h-15zm12 21c3 0 4.5-1.5 4.5-4.5v-3c0-3-1.5-4.5-4.5-4.5h-7.5v12zm-12-18v12h7.5c3 0 4.5-1.5 4.5-4.5v-3c0-3-1.5-4.5-4.5-4.5z" fill="white"/>
  <text x="85" y="48" font-family="Arial, Helvetica, sans-serif" font-size="42" font-weight="bold" fill="#f7931a">Bit<tspan fill="currentColor">Win</tspan></text>
</svg>
</div>
  <p>币胜网 © 2026</p>'''
# Already has new SVG with Chinese but may be duplicated - replace the whole thing
OLD_FOOTER_SVG_NEW = '''<div class="footer-logo">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 75" width="380" height="63">
  <circle cx="38" cy="38" r="33" fill="#f7931a"/>
  <path d="M22 18h15c9 0 15 4.5 15 12 0 4.5-3 7.5-3 7.5 0 7.5 3 6 3 9 9 9v3c0 6-3 10.5-9 10.5h-15zm12 21c3 0 4.5-1.5 4.5-4.5v-3c0-3-1.5-4.5-4.5-4.5h-7.5v12zm-12-18v12h7.5c3 0 4.5-1.5 4.5-4.5v-3c0-3-1.5-4.5-4.5-4.5z" fill="white"/>
  <text x="85" y="48" font-family="Arial, Helvetica, sans-serif" font-size="42" font-weight="bold" fill="#f7931a">Bit<tspan fill="currentColor">Win</tspan></text>
  <text x="255" y="48" font-family="Arial, Helvetica, sans-serif" font-size="40" font-weight="bold">
    <tspan fill="#f7931a">币</tspan><tspan fill="currentColor">胜网</tspan>
  </text>
</svg>
</div>
  <p>币胜网 © 2026</p>'''
NEW_FOOTER_CONTENT = f'{LOGO_SVG_FOOTER}\n  <p>币胜网 © 2026</p>'

def clean_duplicate_footers(content):
    # If multiple footer-logo divs exist, remove all and start fresh
    import re
    # Find everything from the opening <div class="container"> in footer to closing </div> before </footer>
    # This captures all footer-logos and the copyright paragraph
    pattern = r'(<footer>\s*<div class="container">).*(?=</div>\s*</footer>)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        # Replace everything inside container with clean version
        replacement = r'\1\n  ' + NEW_FOOTER_CONTENT + '\n'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        return content, True
    return content, False

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace navigation brand
    updated = False
    # Check for old navigation (either text or old SVG without Chinese)
    if OLD_NAV_LINK_SVG in content:
        content = content.replace(OLD_NAV_LINK_SVG, NEW_NAV_LINK)
        updated = True
    elif OLD_NAV_SVG_SPACING in content:
        content = content.replace(OLD_NAV_SVG_SPACING, NEW_NAV_LINK)
        updated = True
    elif OLD_NAV_LINK_TEXT in content:
        content = content.replace(OLD_NAV_LINK_TEXT, NEW_NAV_LINK)
        updated = True

    # Replace footer with logo
    # First check for duplicated logos - clean everything
    content, cleaned = clean_duplicate_footers(content)
    if cleaned:
        updated = True
    elif OLD_FOOTER_SVG_OLD in content:
        content = content.replace(OLD_FOOTER_SVG_OLD, NEW_FOOTER_CONTENT)
        updated = True
    elif OLD_FOOTER_SVG_NEW in content:
        content = content.replace(OLD_FOOTER_SVG_NEW, NEW_FOOTER_CONTENT)
        updated = True
    elif OLD_FOOTER_CONTENT_OLD in content:
        content = content.replace(OLD_FOOTER_CONTENT_OLD, NEW_FOOTER_CONTENT)
        updated = True

    # Add favicon link if not present
    if 'favicon.svg' not in content:
        if '</head>' in content:
            content = content.replace('</head>', '  <link rel="icon" type="image/svg+xml" href="/logo.svg">\n</head>')

    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")
    else:
        print(f"No change: {filepath}")

def main():
    html_files = []

    # Root level HTML
    for f in ['index.html', 'article.html', 'search.html', 'tags.html']:
        if os.path.exists(f):
            html_files.append(f)

    # Articles directory HTML
    articles_dir = 'articles'
    if os.path.exists(articles_dir):
        for f in os.listdir(articles_dir):
            if f.endswith('.html'):
                html_files.append(os.path.join(articles_dir, f))

    print(f"Found {len(html_files)} HTML files to update")

    for html_file in html_files:
        update_file(html_file)

    print("\nDone! All files updated with BitWin logo.")

if __name__ == '__main__':
    main()
