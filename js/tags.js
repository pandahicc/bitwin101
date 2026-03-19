// Tag navigation and filtering

let allArticles = [];
let tagIndex = {};
let activeTag = null;

document.addEventListener('DOMContentLoaded', () => {
  const tagCloudContainer = document.getElementById('tag-cloud');
  const articlesContainer = document.getElementById('filtered-articles');

  // Load articles and build index
  loadArticles().then(articles => {
    allArticles = articles;
    tagIndex = buildTagIndex(articles);
    renderTagCloud();

    // Check URL hash for tag
    checkHashAndFilter();
  });

  // Listen for hash changes
  window.addEventListener('hashchange', checkHashAndFilter);

  function renderTagCloud() {
    const tagCloudContainer = document.getElementById('tag-cloud');
    let html = `<a href="#" class="tag ${activeTag === null ? 'active' : ''}" data-tag="">全部标签</a>`;

    Object.entries(tagIndex).forEach(([tag, articles]) => {
      const isActive = tag === activeTag ? 'active' : '';
      html += `<a href="#tag=${encodeURIComponent(tag)}" class="tag ${isActive}" data-tag="${escapeHtml(tag)}">${tag} (${articles.length})</a>`;
    });

    tagCloudContainer.innerHTML = html;

    // Add click handlers
    tagCloudContainer.querySelectorAll('[data-tag]').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const tag = link.getAttribute('data-tag');
        if (tag === '') {
          window.location.hash = '';
        }
        filterByTag(tag);
      });
    });
  }

  function checkHashAndFilter() {
    const hash = window.location.hash;
    const tagMatch = hash.match(/^#tag=(.*)$/);

    if (tagMatch && tagMatch[1]) {
      const tag = decodeURIComponent(tagMatch[1]);
      filterByTag(tag);
    } else {
      filterByTag(null);
    }
  }

  function filterByTag(tag) {
    activeTag = tag;
    renderTagCloud();

    let articlesToShow;
    if (!tag) {
      // Show all articles sorted by date
      articlesToShow = allArticles.sort((a, b) => b.date.localeCompare(a.date));
    } else {
      articlesToShow = tagIndex[tag] || [];
    }

    renderArticleList(articlesToShow, 'filtered-articles');
  }

  function escapeHtml(text) {
    return text
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }
});
