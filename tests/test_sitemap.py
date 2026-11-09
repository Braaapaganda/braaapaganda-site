import tempfile
import unittest
from pathlib import Path
from sitemap import sitemap_urls, write_sitemap, EXCLUDED
import xml.etree.ElementTree as ET

class SitemapTests(unittest.TestCase):
    def test_public_sources(self):
        urls = sitemap_urls('content')
        self.assertIn('https://braaapaganda.com/', urls)
        self.assertIn('https://braaapaganda.com/where-are-they-now/', urls)
        self.assertIn('https://braaapaganda.com/articles/', urls)
        self.assertEqual(len(urls), len(set(urls)))
        for name in EXCLUDED | {'home__index.html', 'page__2__index.html'}:
            path = '/' + name.replace('__', '/').replace('index.html', '')
            self.assertNotIn('https://braaapaganda.com' + path, urls)

    def test_new_articles_aliases_and_noindex(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory)
            def add(name, url, robots=''):
                (p/name).write_text(f'<link rel="canonical" href="{url}">{robots}')
            add('new__index.html', 'https://braaapaganda.com/new/')
            add('alias__index.html', 'https://braaapaganda.com/new/')
            add('hidden__index.html', 'https://braaapaganda.com/hidden/', '<meta name="robots" content="noindex,follow">')
            self.assertEqual(sitemap_urls(p), ['https://braaapaganda.com/new/'])
            write_sitemap(p, p/'sitemap.xml')
            self.assertEqual(len(ET.parse(p/'sitemap.xml').getroot()), 1)
            add('bad__index.html', 'https://other.example/bad/')
            with self.assertRaises(ValueError):
                sitemap_urls(p)

    def test_missing_canonical_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory)/'new__index.html').write_text('<title>New</title>')
            with self.assertRaises(ValueError):
                sitemap_urls(directory)
