"""Generate a canonical-only sitemap from reviewed public HTML sources."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

ORIGIN = 'https://braaapaganda.com'
# Public transition notices remain available, but aren't search landing pages.
EXCLUDED = {'404.html', '404__index.html', 'ask-the-show__index.html',
            'community__index.html', 'forums__forum__injured-riders-stories__index.html',
            'membership-account__index.html', 'membership-levels__index.html',
            'research__index.html'}


class Metadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonicals = []
        self.noindex = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link' and 'canonical' in attrs.get('rel', '').lower().split():
            self.canonicals.append(attrs.get('href', ''))
        if tag == 'meta' and attrs.get('name', '').lower() in ('robots', 'googlebot'):
            directives = attrs.get('content', '').lower().replace(',', ' ').split()
            self.noindex |= 'noindex' in directives or 'none' in directives


def sitemap_urls(source):
    urls = set()
    for src in sorted(Path(source).glob('*.html')):
        if src.name in EXCLUDED:
            continue
        meta = Metadata()
        meta.feed(src.read_text(encoding='utf-8'))
        if meta.noindex:
            continue
        if len(meta.canonicals) != 1:
            raise ValueError(f'{src.name}: expected exactly one canonical URL')
        canonical = meta.canonicals[0]
        parsed = urlparse(canonical)
        if parsed.scheme != 'https' or parsed.netloc != 'braaapaganda.com' or parsed.query or parsed.fragment:
            raise ValueError(f'{src.name}: invalid canonical URL {canonical}')
        path = '/' + src.name.replace('__', '/')
        if path.endswith('/index.html'):
            path = path[:-len('index.html')]
        # An alias must point to a real canonical source, never create another entry.
        if canonical != ORIGIN + path:
            target = parsed.path.lstrip('/')
            if target.endswith('/') or not target:
                target += 'index.html'
            if not (Path(source) / target.replace('/', '__')).is_file():
                raise ValueError(f'{src.name}: canonical target does not exist')
            continue
        urls.add(canonical)
    return sorted(urls)


def write_sitemap(source, destination):
    namespace = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    ET.register_namespace('', namespace)
    root = ET.Element(f'{{{namespace}}}urlset')
    urls = sitemap_urls(source)
    for url in urls:
        node = ET.SubElement(root, f'{{{namespace}}}url')
        ET.SubElement(node, f'{{{namespace}}}loc').text = url
    ET.indent(root, space='  ')
    ET.ElementTree(root).write(destination, encoding='utf-8', xml_declaration=True)
    return len(urls)
