# Braaapaganda public site

Readable public HTML and CSS are in `content/`. `build_site.py` copies them into URL directories for GitHub Pages. Double underscores in a filename represent directory separators: `about__index.html` becomes `/about/index.html`. `index.html`, `404.html` and `robots.txt` stay at the site root. No dependencies or ZIP extraction are required.

## Publish a daily article

Copy an existing article HTML file in `content/` to `your-article-slug__index.html`. Edit the title, heading, date, canonical URL and article body. Keep the relative stylesheet and navigation links. Add the article card/link to `index.html`, `home__index.html`, `articles__index.html` and `page__2__index.html`. Keep home and archive aliases equivalent. Preserve existing article filenames/URLs when editing.

Run `python build_site.py`, then `python -m http.server 8766 --directory _site` and review the article, links and mobile layout. Commit public source changes; Actions builds and publishes them.

## Privacy boundary and launch

Never add member data, paid archives, private evidence, credentials or WordPress exports. The investigation remains in its separate repository. Contact uses the publicly listed braaapaganda@gmail.com email. No donation checkout is enabled.

Keep all 35 HTML pages' noindex,nofollow metadata and robots.txt Disallow until approved launch. Remove both only at launch. The 404 base URL comes from GitHub Pages configuration during deployment and adapts to the project URL or future custom domain. DNS and billing are separate tasks. The original WordPress backend must remain until paid access and private records are handled. public-site.zip is an obsolete historical artifact and is not used by the readable-source workflow.
