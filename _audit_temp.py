import os, json

# === EN vs NA page comparison ===
en_pages = set()
na_pages = set()

base = 'E:/nauru/src/pages'
for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.astro'):
            continue
        rel = os.path.relpath(root, base).replace(os.sep, '/')
        key = (rel + '/' + f.replace('.astro', '')).lstrip('/')
        if rel.startswith('na'):
            na_pages.add(key[3:])  # strip 'na/'
        else:
            en_pages.add(key)

both = en_pages & na_pages
only_en = en_pages - na_pages

print('EN pages:', len(en_pages))
print('NA pages:', len(na_pages))
print('Translated (both):', len(both))
print('EN only (needs NA):', len(only_en))

# === Dist pages count ===
dist_html = 0
for root, dirs, files in os.walk('E:/nauru/dist'):
    for f in files:
        if f.endswith('.html'):
            dist_html += 1
print('Dist HTML files:', dist_html)

# === Sitemap URL count ===
with open('E:/nauru/dist/sitemap-0.xml') as f:
    urls = f.read().count('<url>')
print('Sitemap URLs:', urls)

# === Generated hero PNGs ===
png_dir = 'E:/nauru/public/assets/images'
generated = [f for f in os.listdir(png_dir) if f.endswith('.png')] if os.path.exists(png_dir) else []
print('Generated hero PNGs:', len(generated))

# === Hero SVGs ===
svg_dir = 'E:/nauru/public/images/hero'
svgs = [f for f in os.listdir(svg_dir) if f.endswith('.svg')] if os.path.exists(svg_dir) else []
print('Hero SVGs:', len(svgs))

# === Check E:/nauru package.json ===
with open('E:/nauru/package.json') as f:
    pkg = json.load(f)
print('Dependencies:', list(pkg.get('dependencies',{}).keys()))
print('DevDependencies:', list(pkg.get('devDependencies',{}).keys()))
