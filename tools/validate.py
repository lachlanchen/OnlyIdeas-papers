#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
for directory in sorted((root / 'papers').iterdir()):
    if not directory.is_dir():
        continue
    metadata = json.loads((directory / 'metadata.json').read_text())
    text = (directory / 'paper.mmd').read_bytes()
    assert metadata['id'] == directory.name
    assert metadata['revision'] == hashlib.sha256(text).hexdigest()
    assert metadata['license'] in ('CC0-1.0', 'CC-BY-4.0', 'CC-BY-SA-4.0', 'author-permission')
    assert metadata['visibility'] == 'public'
    assert 'owner' not in metadata
    for asset in metadata['assets']:
        path = directory / asset['path']
        assert path.resolve().is_relative_to(directory.resolve())
        assert path.is_file(), f'Missing figure: {path}'
    assert not list(directory.rglob('*.pdf')), 'Original PDFs do not belong in this library.'
    print('Valid:', directory.name)
