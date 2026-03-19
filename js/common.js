// Common shared functions

const ARTICLES_INDEX_URL = '/data/index.json';
const ARTICLE_CONTENT_URL = '/articles/{id}.json';

let articlesCache = null;

// Load articles metadata from JSON index
async function loadArticles() {
  if (articlesCache) {
    return articlesCache;
  }

  try {
    const response = await fetch(ARTICLES_INDEX_URL);
    if (!response.ok) {
      throw new Error('Failed to load articles index');
    }
    articlesCache = await response.json();
    return articlesCache;
  } catch (error) {
    console.error('Error loading articles index:', error);
    return [];
  }
}

// Load single article full content
async function loadArticleContent(articleId) {
  const url = ARTICLE_CONTENT_URL.replace('{id}', articleId);
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error('Failed to load article content');
    }
    const data = await response.json();
    return data.content;
  } catch (error) {
    console.error('Error loading article content:', error);
    return null;
  }
}

// Render article card HTML
function renderArticleCard(article) {
  return `
    <article class="article-card">
      <h2><a href="${article.url}">${article.title}</a></h2>
      <div class="article-meta">
        <span>${article.date}</span>
      </div>
      <div class="article-excerpt">${article.excerpt}</div>
      <div class="tags">
        ${article.tags.map(tag => `<a href="/tags.html#tag=${encodeURIComponent(tag)}" class="tag">${tag}</a>`).join('')}
      </div>
    </article>
  `;
}

// Render article list to container
function renderArticleList(articles, containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  if (articles.length === 0) {
    container.innerHTML = '<div class="no-results">未找到相关文章</div>';
    return;
  }

  const html = articles.map(renderArticleCard).join('');
  container.innerHTML = html;
}

// Build tag index from articles
function buildTagIndex(articles) {
  const tagIndex = {};
  articles.forEach(article => {
    article.tags.forEach(tag => {
      if (!tagIndex[tag]) {
        tagIndex[tag] = [];
      }
      tagIndex[tag].push(article);
    });
  });

  // Sort by article count descending
  return Object.entries(tagIndex)
    .sort((a, b) => b[1].length - a[1].length)
    .reduce((obj, [tag, articles]) => {
      obj[tag] = articles;
      return obj;
    }, {});
}

// Debounce utility
function debounce(func, wait) {
  let timeout;
  return function() {
    const context = this;
    const args = arguments;
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(context, args), wait);
  };
}

// Global header scroll effect and back to top button
function initGlobalEffects() {
  // Header shadow on scroll
  const header = document.querySelector('header');
  if (header) {
    function toggleHeaderShadow() {
      if (window.scrollY > 10) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }
    window.addEventListener('scroll', debounce(toggleHeaderShadow, 10));
    toggleHeaderShadow();
  }

  // Floating back to top button
  if (!document.querySelector('.back-to-top-fixed')) {
    const btn = document.createElement('button');
    btn.className = 'back-to-top back-to-top-fixed';
    btn.innerHTML = '↑';
    btn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    document.body.appendChild(btn);

    function toggleBackToTop() {
      if (window.scrollY > 300) {
        btn.classList.add('visible');
      } else {
        btn.classList.remove('visible');
      }
    }
    window.addEventListener('scroll', debounce(toggleBackToTop, 100));
    toggleBackToTop();
  }
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  initGlobalEffects();
});
