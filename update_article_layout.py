#!/usr/bin/env python3
import os

def update_article_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already updated
    if 'article-container' in content:
        print(f"Already updated: {filepath}")
        return False

    # The pattern we need to replace:
    # Original:
    #   <main class="container">
    #     <a href="/" class="back-link">← 返回首页</a>
    #     <article>
    #       ...
    #     </article>
    #   </main>
    #
    # New:
    #   <div class="container article-container">
    #     <aside class="article-sidebar">
    #       <nav class="sidebar-nav">
    #         <a href="/" class="sidebar-home">← 返回首页</a>
    #         <h4>文章目录</h4>
    #         <ul class="toc">
    #           <!-- JS auto-generated -->
    #         </ul>
    #         <h4>标签</h4>
    #         <div class="sidebar-tags">
    #           {existing tags go here}
    #         </div>
    #         <button class="back-to-top">↑ 回到顶部</button>
    #       </nav>
    #     </aside>
    #     <main class="article-main">
    #       <article>
    #         ...
    #       </article>
    #     </main>
    #   </div>
    #   <button class="back-to-top back-to-top-fixed">↑</button>

    # Extract the part after <main class="container"> and before </main>
    start_tag = '  <main class="container">\n'
    end_tag = '\n  </main>'

    if start_tag not in content:
        print(f"Structure not found in: {filepath}")
        return False

    # Split content
    before = content.split(start_tag)[0]
    after_start = content.split(start_tag)[1]
    main_content = after_start.split(end_tag)[0]
    after = end_tag + after_start.split(end_tag)[1]

    # Extract back-link (it's the first line)
    lines = main_content.strip().split('\n')
    back_link = lines[0].strip()
    rest_of_content = '\n'.join(lines[1:]).strip()

    # Extract tags from article-header
    # Find the tags div
    import re
    tags_match = re.search(r'<div class="tags"[^>]*>.*?</div>', rest_of_content, re.DOTALL)
    tags_html = ''
    if tags_match:
        tags_html = tags_match.group(0)

    # Build new structure
    new_content = before + '''  <div class="container article-container">
    <aside class="article-sidebar">
      <nav class="sidebar-nav">
        <a href="/" class="sidebar-home">← 返回首页</a>
        <h4>文章目录</h4>
        <ul class="toc">
          <!-- JS will auto-generate table of contents -->
        </ul>
'''
    if tags_html:
        new_content += '''        <h4>标签</h4>
        <div class="sidebar-tags">
          {tags}
        </div>
'''.format(tags=tags_html)

    new_content += '''        <button class="back-to-top">↑ 回到顶部</button>
      </nav>
    </aside>
    <main class="article-main">
''' + rest_of_content + '''
    </main>
  </div>
  <button class="back-to-top back-to-top-fixed">↑</button>
''' + after

    # Add script tag at the end before </body>
    if '</body>' in new_content and 'article.js' not in new_content:
        new_content = new_content.replace('</body>', '  <script src="/js/article.js"></script>\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Updated: {filepath}")
    return True

def main():
    html_files = []

    # Articles directory HTML
    articles_dir = 'articles'
    if os.path.exists(articles_dir):
        for f in os.listdir(articles_dir):
            if f.endswith('.html'):
                html_files.append(os.path.join(articles_dir, f))

    print(f"Found {len(html_files)} article HTML files to update\n")

    updated = 0
    for html_file in html_files:
        if update_article_file(html_file):
            updated += 1

    print(f"\nDone! Updated {updated} files.")

if __name__ == '__main__':
    main()
