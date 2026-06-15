import sys, re
html = sys.stdin.read()

# Parse sticky nav link colors from CSS inline
m = re.search(r'sticky-nav.*?</style>', html, re.DOTALL)
if m:
    css = m.group()
    parts = css.split('.sticky-nav.scrolled')
    default_section = parts[0] if len(parts) > 0 else ''
    links_section = default_section[default_section.find('nav-links a'):]
    color_match = re.search(r'color:\s*([^;]+)', links_section)
    if color_match:
        print(f'StickyNav default link color: {color_match.group(1).strip()}')

print()
if 'data-astro-cid-bbe6dxrz' in html:
    print('Hero Nav: PRESENT')
else:
    print('Hero Nav: MISSING')

ticker_pos = html.find('news-ticker')
sticky_pos = html.find('sticky-nav')
if ticker_pos > 0 and sticky_pos > 0:
    if sticky_pos > ticker_pos:
        print('ORDER: NewsTicker BEFORE StickyNav OK')
    else:
        print('ORDER: StickyNav BEFORE NewsTicker')

feats = ['Hero' if 'data-astro-cid-bbe6dxrz' in html else 'No Hero',
         'Features' if 'features-grid' in html else 'No Features',
         'Stats' if 'stats-strip' in html else 'No Stats',
         'StickyNav' if 'sticky-nav' in html else 'No Sticky',
         'NewsTicker' if 'news-ticker' in html else 'No Ticker']
print(f'Features: {feats}')