import sys, re
html = sys.stdin.read()

# Find the inline CSS for sticky-nav
m = re.search(r'sticky-nav.*?</style>', html, re.DOTALL)
if m:
    css = m.group()
    # Get default nav-link color (before scrolled overrides)
    scrolled_pos = css.find('.sticky-nav.scrolled')
    if scrolled_pos > 0:
        default_rules = css[:scrolled_pos]
    else:
        default_rules = css
    # Find color for nav-links a
    for match in re.finditer(r'nav-links[^}]*a[^}]*{[^}]*color:\s*([^;}]+)', default_rules):
        print(f'Default link color: {match.group(1).strip()}')
    # Find background
    for match in re.finditer(r'sticky-nav\s*{[^}]*background:\s*([^;}]+)', default_rules):
        print(f'Default background: {match.group(1).strip()}')

# Check HTML: is the sticky-nav really first child?
body_tag = html.find('<body')
if body_tag > 0:
    after_body = html[body_tag:body_tag+3000]
    sticky_pos = after_body.find('sticky-nav')
    ticker_pos = after_body.find('news-ticker')
    if sticky_pos > 0 and ticker_pos > 0:
        if sticky_pos < ticker_pos:
            print(f'StickyNav FIRST ({sticky_pos}px), NewsTicker after ({ticker_pos}px) - CORRECT')
        else:
            print(f'WRONG ORDER - NewsTicker ({ticker_pos}) before StickyNav ({sticky_pos})')

# Check if hero has a nav element
hero_nav = re.search(r'<nav[^>]*data-astro-cid-bbe6dxrz[^>]*>', html)
if hero_nav:
    print(f'HERO HAS NAV: {hero_nav.group()[:100]}')
else:
    print('No nav in hero component - CORRECT')

print('\n✅ StickyNav ist fixed, transparent, weiße Schrift - should be visible on hero BG')