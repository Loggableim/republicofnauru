import os

base = 'E:/nauru/src/pages'
en_pages = set()
na_pages = set()

for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.astro'):
            continue
        rel = os.path.relpath(root, base).replace(os.sep, '/')
        key = (rel + '/' + f.replace('.astro', '')).lstrip('/')
        if rel.startswith('na'):
            na_pages.add(key[3:])
        else:
            en_pages.add(key)

both = en_pages & na_pages
only_en = en_pages - na_pages

print('=== Translated (both EN + NA) ===')
for p in sorted(both):
    print('  ✅', p)

print()
print('=== EN only (missing NA translation) ===')
for p in sorted(only_en):
    print('  ❌', p)
