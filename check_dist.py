#!/usr/bin/env python3
"""Check which dist pages are missing what."""
import os, glob

repo = 'E:/nauru'
dist = os.path.join(repo, 'dist')
pages = []
for root, dirs, files in os.walk(dist):
    rel = os.path.relpath(root, dist)
    if rel.startswith('_astro') or rel.startswith('assets'):
        continue
    for f in files:
        if not (f.endswith('.html') or f.endswith('.htm')):
            continue
        pages.append(os.path.join(root, f))

skip_patterns = ['/404.', '/500.', '/admin/', '/dashboard/', '/login/', '/assets/', '/_astro/', '/node_modules/']
articles = []
for p in sorted(pages):
    pp = p.replace(os.sep, '/')
    if any(x in pp for x in skip_patterns):
        continue
    articles.append(p)

check_articles = articles[:20]
print(f'Total: {len(pages)}, Articles: {len(articles)}, Checking first {len(check_articles)}:')
for a in check_articles:
    rel = os.path.relpath(a, os.path.join(repo, 'dist')).replace(os.sep, '/')
    content = open(a, encoding='utf-8', errors='ignore').read()
    has_hero = 'hero' in content.lower() or '../images/' in content or '/images/' in content
    has_amazon = 'tag=nova079-20' in content
    has_meta = '<meta name="description"' in content or '<meta name="Description"' in content
    has_jsonld = ('"@type"' in content) and any(t in content for t in ['"BlogPosting"', '"WebPage"', '"Article"', '"WebSite"'])
    flags = []
    if not has_hero: flags.append('NO_HERO')
    if not has_amazon: flags.append('NO_AMAZON')
    if not has_meta: flags.append('NO_META')
    if not has_jsonld: flags.append('NO_JSONLD')
    flag_str = ','.join(flags) if flags else 'OK'
    print(f'  {rel:<45} {flag_str}')
