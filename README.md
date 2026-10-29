# Braaapaganda public site

Readable public HTML and CSS are in `content/`. `build_site.py` copies them into URL directories for GitHub Pages. Double underscores in a filename represent directory separators: `about__index.html` becomes `/about/index.html`. `index.html`, `404.html` and `robots.txt` stay at the site root. No dependencies or ZIP extraction are required.

## Publish a daily article

Copy an existing article HTML file in `content/` to `your-article-slug__index.html`. Edit the title, heading, date, canonical URL and article body. Keep the relative stylesheet and navigation links. Add the article card/link to `index.html`, `home__index.html`, `articles__index.html` and `page__2__index.html`. Keep home and archive aliases equivalent. Preserve existing article filenames/URLs when editing.

Run `python build_site.py`, then `python -m http.server 8766 --directory _site` and review the article, links and mobile layout. Commit public source changes; Actions builds and publishes them.

## Privacy boundary and launch

Never add member data, paid archives, private evidence, credentials or WordPress exports. Published investigations live under `/investigations/`. The original investigation repository and URL remain available for compatibility; no private evidence was copied. Contact uses the publicly listed braaapaganda@gmail.com email. Voluntary donations link to the verified existing Ko-fi page at https://ko-fi.com/braaapaganda; no paid benefits are offered.

The approved launch source permits indexing; preserve canonical URLs and the robots policy when publishing new articles. The 404 base URL comes from GitHub Pages configuration during deployment and adapts to the project URL or future custom domain. DNS and billing are separate tasks. Keep the original hosting and private backup available for rollback until domain verification is complete. public-site.zip is an obsolete historical artifact and is not used by the readable-source workflow.

## Publish an investigation

Each case has its own directory: `investigations__case-slug__index.html` and optional `investigations__case-slug__report.html`. Copy the existing case shell, preserve shared navigation, and add a card to `investigations__index.html`. Use the shared site design and scoped `assets__investigation.css`; preserve source links, evidence labels, limitations, and publication dates. Publish only reviewed public material, never private evidence files. Main navigation points to the index so future cases need no navigation rewrite.

The main custom domain is launched and indexable. Ko-fi is a voluntary external support link, not paid access. Private WordPress backups and DNS rollback records stay outside this public repository; old hosting and domain registration remain intact.
