#!/bin/bash
cd /e/nauru
for f in $(find dist -name "*.html" | sort | head -20); do
  tag=$(grep -c 'tag=nova079-20' "$f" 2>/dev/null)
  hero=$(grep -c '/images/hero/' "$f" 2>/dev/null)
  meta=$(grep -c 'name="description"' "$f" 2>/dev/null)
  jsonld=$(grep -c '"@context"' "$f" 2>/dev/null)
  echo "$f | tag=$tag hero=$hero meta=$meta jsonld=$jsonld"
done
