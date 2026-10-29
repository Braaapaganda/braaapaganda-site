"""Build public HTML from readable content files; no external dependencies."""
from pathlib import Path
import os
from urllib.parse import urlparse
source=Path('content'); output=Path('_site')
base=os.environ.get('SITE_BASE','https://braaapaganda.github.io/braaapaganda-site/').rstrip('/')+'/'
parsed=urlparse(base)
assert parsed.scheme in ('http','https') and not parsed.username and not parsed.password
assert (parsed.netloc, parsed.path) in (('braaapaganda.com','/'), ('braaapaganda.github.io','/braaapaganda-site/'))
assert not parsed.query and not parsed.fragment
base=parsed._replace(scheme='https').geturl()
for src in source.iterdir():
    if not src.is_file(): continue
    dest=output/src.name.replace('__','/')
    dest.parent.mkdir(parents=True,exist_ok=True)
    if src.suffix.lower() in ('.ico','.png','.jpg','.jpeg','.webp','.gif'):
        dest.write_bytes(src.read_bytes())
        continue
    text=src.read_text(encoding='utf-8')
    if src.name=='404.html':
        text=text.replace('https://braaapaganda.github.io/braaapaganda-site/',base).replace('https://braaapaganda.com/',base)
    dest.write_text(text,encoding='utf-8')
print('Built',sum(p.is_file() for p in output.rglob('*')),'public files')
