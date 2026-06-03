#!/bin/bash
cd "/c/HermesPortable/home/scripts/blog-automation/nauru"
missing_meta=0
missing_jsonld=0
total=0
for f in $(find dist -name "*.html" | sort); do
  # Skip 404/500/admin/dashboard/login/assets/_astro/node_modules
  f_clean="${f//\\//}"
  skip=0
  for skip_pattern in "404." "500." "/admin/" "/dashboard/" "/login/" "/assets/" "/_astro/" "/node_modules/"; do
    if echo "$f_clean" | grep -q "$skip_pattern"; then skip=1; break; fi
  done
  [ "$skip" = "1" ] && continue
  
  content=$(cat "$f")
  total=$((total+1))
  
  has_meta=0
  echo "$content" | grep -q 'name="description"' && has_meta=1
  
  has_jsonld=0
  if echo "$content" | grep -q '"@type"'; then
    echo "$content" | grep -q '"BlogPosting"' && has_jsonld=1
    echo "$content" | grep -q '"WebPage"' && has_jsonld=1
    echo "$content" | grep -q '"Article"' && has_jsonld=1
    echo "$content" | grep -q '"WebSite"' && has_jsonld=1
  fi
  
  if [ "$has_meta" = "0" ]; then
    echo "MISSING META: $f"
    missing_meta=$((missing_meta+1))
  fi
  if [ "$has_jsonld" = "0" ]; then
    echo "MISSING JSONLD: $f"
    missing_jsonld=$((missing_jsonld+1))
  fi
  
  # Only first 20 for amazon
  if [ "$total" -le 20 ]; then
    has_tag=0
    echo "$content" | grep -q 'tag=nova079-20' && has_tag=1
    if [ "$has_tag" = "0" ]; then
      echo "MISSING TAG ($total): $f"
    fi
  fi
done
echo ""
echo "Total pages: $total"
echo "Missing meta: $missing_meta"
echo "Missing jsonld: $missing_jsonld"
