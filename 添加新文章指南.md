# 添加新文章指南

本文档说明如何在这个静态网站中添加新文章。

## 当前架构

网站采用 **独立静态HTML文件 + 元数据索引** 架构：

- `articles/{id}.html` - 每篇文章一个独立HTML文件（SEO友好）
- `data/index.json` - 所有文章的元数据索引（供搜索和标签过滤使用）
- `sitemap.xml` - 站点地图，供搜索引擎收录

## 添加新文章步骤

### 第一步：创建文章HTML文件

1. 在 `articles/` 目录下新建文件，文件名格式：`YYYYMMDD.html` 或 `YYYYMMDDNN.html`（NN为序号，同一天多篇时使用）。

   例如：`articles/20260320.html`

2. 复制下面的模板，替换占位符内容：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{文章标题} - 币胜网</title>
  <meta name="description" content="{文章摘要（100-150字）}">
  <meta property="og:title" content="{文章标题}">
  <meta property="og:description" content="{文章摘要}">
  <meta property="og:url" content="/articles/{id}.html">
  <meta property="og:type" content="article">
  <meta property="article:published_time" content="{YYYY-MM-DD}">
  <link rel="stylesheet" href="/css/style.css">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
</head>
<body>
  <header>
    <div class="container">
      <nav class="nav">
        <a href="/" class="nav-brand">币胜网</a>
        <div class="nav-links">
          <a href="/">首页</a>
          <a href="/tags.html">标签</a>
          <a href="/search.html">搜索</a>
        </div>
      </nav>
    </div>
  </header>

  <main class="container">
    <a href="/" class="back-link">← 返回首页</a>
    <article>
      <div class="article-header">
        <h1>{文章标题}</h1>
        <div class="article-meta">
          <span>{YYYY-MM-DD}</span>
        </div>
        <div class="tags" style="margin-top: 1rem;">
          <a href="/tags.html#tag=币安" class="tag">币安</a>
          <!-- 更多标签 -->
        </div>
      </div>
      <div class="article-content">
        <!-- 文章HTML内容 -->
      </div>
    </article>
  </main>

  <footer>
    <div class="container">
      <p>币胜网 © 2026</p>
    </div>
  </footer>
</body>
</html>
```

**需要替换的占位符：**

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{文章标题}` | 文章完整标题 | `2026 币安新用户活动指南` |
| `{文章摘要}` | 文章摘要，用于meta description和OG | `本文介绍币安最新的新用户活动，如何参与获得最高奖金...` |
| `{id}` | 文章ID（即文件名，不含.html） | `20260320` |
| `{YYYY-MM-DD}` | 发布日期 | `2026-03-20` |
| 标签部分 | 添加对应的标签，每个标签一行 | `<a href="/tags.html#tag=新用户" class="tag">新用户</a>` |
| 文章内容 | 填入文章完整HTML内容 | 保留原始p/h2/ul等标签 |

### 第二步：在元数据索引中添加条目

编辑 `data/index.json`，在数组中添加一条新记录：

```json
{
  "id": "20260320",
  "title": "2026 币安新用户活动指南",
  "date": "2026-03-20",
  "excerpt": "本文介绍币安最新的新用户活动，如何参与获得最高奖金...",
  "tags": ["币安", "新用户", "活动"],
  "url": "/articles/20260320.html"
}
```

**注意：**
- `id` 必须和HTML文件名一致（不含.html）
- `date` 格式为 `YYYY-MM-DD`
- `url` 格式为 `/articles/{id}.html`
- `tags` 是数组，填入相关标签

### 第三步：更新 sitemap.xml

编辑 `sitemap.xml`，在 `</urlset>` 之前添加：

```xml
  <url>
    <loc>https://bitwin101.com/articles/20260320.html</loc>
    <lastmod>2026-03-20</lastmod>
  </url>
```

## 完成！

添加完成后，刷新网站就可以看到新文章：

- 首页会按日期排序自动显示新文章
- 标签页会自动添加新标签（如果是新标签）并统计计数
- 搜索功能可以搜索到新文章的标题、摘要、标签
- 搜索引擎可以通过 sitemap 发现新文章

## 验证

添加后可以验证：

1. 打开首页 http://localhost:8000/ - 确认新文章出现在列表中
2. 点击文章链接，确认能正常打开并显示完整内容
3. 打开标签页，确认标签显示正确，点击能过滤出文章
4. 在搜索页搜索新文章标题中的关键词，确认能搜到

## 总结

添加一篇新文章总共三步：
1. ✅ 创建 `articles/{id}.html` - 文章HTML
2. ✅ 在 `data/index.json` 添加元数据
3. ✅ 在 `sitemap.xml` 添加URL

**不需要修改任何其他文件！** 所有功能（首页列表、搜索、标签过滤）都是动态读取元数据，自动生效。
