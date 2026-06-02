#!/usr/bin/env python3
"""Check hero images in nauru dist pages."""
import os

pages = []
for root, dirs, files in os.walk('.'):
    rel = os.path.relpath(root, '.')
    if rel.startswith('_astro') or rel.startswith('assets'):
        continue
    for f in files:
        if not f.endswith('.html'):
            continue
        path = os.path.join(root, f)
        # Filter as gremium does
        p = path.replace(os.sep, '/')
        skip_patterns = ['/404.', '/500.', '/admin/', '/dashboard/', '/login/', '/assets/', '/_astro/', '/node_modules/']
        if any(x in p for x in skip_patterns):
            continue
        content = open(path, encoding='utf-8', errors='ignore').read()
        has_hero = 'hero' in content.lower()
        pages.append((path, has_hero))

print(f'Total filtered pages: {len(pages)}')
no_hero = [p for p, h in pages if not h]
print(f'Without hero: {len(no_hero)}')
for p in sorted(no_hero):
    print(f'  NO HERO: {p}')
