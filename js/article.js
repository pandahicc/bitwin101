// Article sidebar navigation - TOC generation and scroll highlighting
(function() {
  document.addEventListener('DOMContentLoaded', function() {
    // Generate Table of Contents from h2/h3 headings
    function generateTOC() {
      const articleContent = document.querySelector('.article-content');
      const tocContainer = document.querySelector('.toc');

      if (!articleContent || !tocContainer) return;

      const headings = articleContent.querySelectorAll('h2, h3');
      if (headings.length === 0) {
        document.querySelector('.sidebar-nav h4:first-of-type').style.display = 'none';
        return;
      }

      headings.forEach((heading, index) => {
        // Add id if not present
        if (!heading.id) {
          heading.id = `heading-${index}`;
        }

        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = `#${heading.id}`;
        a.textContent = heading.textContent;
        a.classList.add(heading.tagName.toLowerCase() === 'h3' ? 'toc-h3' : 'toc-h2');

        a.addEventListener('click', function(e) {
          e.preventDefault();
          const target = document.getElementById(this.getAttribute('href').substring(1));
          if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            // Update URL without reload
            history.pushState(null, null, this.getAttribute('href'));
          }
        });

        li.appendChild(a);
        tocContainer.appendChild(li);
      });

      // Highlight current section on scroll
      highlightCurrentSection(headings);
    }

    function highlightCurrentSection(headings) {
      const tocLinks = document.querySelectorAll('.toc a');
      let currentId = null;

      function highlight() {
        const scrollPosition = window.scrollY;

        for (let i = headings.length - 1; i >= 0; i--) {
          const heading = headings[i];
          if (heading.offsetTop - 120 <= scrollPosition) {
            currentId = heading.id;
            break;
          }
        }

        tocLinks.forEach(link => {
          link.classList.toggle('active', link.getAttribute('href') === `#${currentId}`);
        });
      }

      window.addEventListener('scroll', debounce(highlight, 50));
      highlight();
    }

    // Back to top functionality
    function initBackToTop() {
      const btn = document.querySelector('.back-to-top');
      if (!btn) return;

      btn.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });

      // Show/hide based on scroll position
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

    // Header scroll effect for backdrop blur
    function initHeaderScroll() {
      const header = document.querySelector('header');
      if (!header) return;

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

    // Initialize everything
    generateTOC();
    initBackToTop();
    initHeaderScroll();
  });
})();
