"""Build public HTML from readable content files; no external dependencies."""
from pathlib import Path
import os
from urllib.parse import urlparse
source=Path('content'); output=Path('_site')
base=os.environ.get('SITE_BASE','https://braaapaganda.github.io/braaapaganda-site/').rstrip('/')+'/'
assert urlparse(base).scheme=='https'
for src in source.iterdir():
    if not src.is_file(): continue
    dest=output/src.name.replace('__','/')
    dest.parent.mkdir(parents=True,exist_ok=True)
    text=src.read_text(encoding='utf-8')
    if src.name=='404.html':
        text=text.replace('https://braaapaganda.github.io/braaapaganda-site/',base)
    dest.write_text(text,encoding='utf-8')
print('Built',sum(p.is_file() for p in output.rglob('*')),'public files')
