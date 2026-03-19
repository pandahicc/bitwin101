// Search functionality

let allArticles = [];
let searchTimeout = null;

document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('search-input');
  const resultsCount = document.getElementById('search-results-count');
  const resultsContainer = document.getElementById('search-results');

  // Load articles
  loadArticles().then(articles => {
    allArticles = articles;
  });

  // Focus input on page load
  searchInput.focus();

  // Check for query parameter
  const params = new URLSearchParams(window.location.search);
  const queryParam = params.get('q');
  if (queryParam) {
    searchInput.value = queryParam;
    performSearch();
  }

  // Search on input with debounce
  searchInput.addEventListener('input', (e) => {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
      performSearch();
      updateURL(e.target.value);
    }, 150);
  });

  function performSearch() {
    const query = searchInput.value.toLowerCase().trim();
    let results = [];

    if (query.length === 0) {
      resultsCount.textContent = '';
      resultsContainer.innerHTML = '';
      return;
    }

    results = searchArticles(query, allArticles);

    resultsCount.textContent = `找到 ${results.length} 篇相关文章`;
    renderArticleList(results, 'search-results');
  }

  function searchArticles(query, articles) {
    return articles.filter(article => {
      const titleMatch = article.title.toLowerCase().includes(query);
      const excerptMatch = article.excerpt.toLowerCase().includes(query);
      const tagMatch = article.tags.some(tag => tag.toLowerCase().includes(query));
      return titleMatch || excerptMatch || tagMatch;
    });
  }

  function updateURL(query) {
    const url = new URL(window.location);
    if (query) {
      url.searchParams.set('q', query);
    } else {
      url.searchParams.delete('q');
    }
    window.history.replaceState({}, '', url);
  }
});
