#!/bin/bash
# Gremium EXACT check for first 20 HTML files
cd "/c/HermesPortable/home/scripts/blog-automation/nauru"
hero_count=0
tag_count=0
meta_count=0
jsonld_count=0
total=0

for f in $(find dist -name "*.html" | sort | head -20); do
  content=$(cat "$f")
  total=$((total+1))
  
  # hero check: "hero" in content (case-insensitive) OR "../images/" OR "/images/"
  hero=0
  if echo "$content" | grep -qi "hero"; then hero=1; fi
  if echo "$content" | grep -q "../images/"; then hero=1; fi
  if echo "$content" | grep -q "/images/"; then hero=1; fi
  if [ "$hero" = "1" ]; then hero_count=$((hero_count+1)); fi
  
  # amazon tag
  tag=0
  if echo "$content" | grep -q 'tag=nova079-20'; then
    tag=1
    tag_count=$((tag_count+1))
  fi
  
  # meta description
  meta=0
  if echo "$content" | grep -q '<meta name="description"'; then meta=1; fi
  if echo "$content" | grep -q '<meta name="Description"'; then meta=1; fi
  if [ "$meta" = "1" ]; then meta_count=$((meta_count+1)); fi
  
  # jsonld: "@type" AND one of "BlogPosting"/"WebPage"/"Article"/"WebSite"
  jsonld=0
  if echo "$content" | grep -q '"@type"'; then
    if echo "$content" | grep -q '"BlogPosting"'; then jsonld=1; fi
    if echo "$content" | grep -q '"WebPage"'; then jsonld=1; fi
    if echo "$content" | grep -q '"Article"'; then jsonld=1; fi
    if echo "$content" | grep -q '"WebSite"'; then jsonld=1; fi
  fi
  if [ "$jsonld" = "1" ]; then jsonld_count=$((jsonld_count+1)); fi
  
  echo "$(basename $(dirname $(dirname $f)))/$(basename $(dirname $f))/$(basename $f) | hero=$hero | tag=$tag | meta=$meta | jsonld=$jsonld"
done

echo ""
echo "=== GREMIUM REPORT (first $total pages) ==="
echo "hero_bilder: $hero_count/$total"
echo "amazon_links: $tag_count/$total"
echo "meta_beschreibungen: $meta_count/$total"
echo "jsonld: $jsonld_count/$total"
