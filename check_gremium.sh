#!/bin/bash
cd /e/nauru
for f in $(find dist -name "*.html" | sort | head -20); do
  content=$(cat "$f")
  # Gremium criteria
  if echo "$content" | grep -qi "hero" || echo "$content" | grep -q "../images/" || echo "$content" | grep -q "/images/"; then
    hero=1
  else
    hero=0
  fi
  tag=$(echo "$content" | grep -c 'tag=nova079-20')
  meta=$(echo "$content" | grep -c 'name="description"')
  jsonld=$(echo "$content" | grep -c '"@type"')
  echo "$f | hero=$hero tag=$tag meta=$meta jsonld=$jsonld"
done
