#!/bin/bash
set -e

# Configuration
VERSION=$(cat VERSION)
DIST_DIR="dist"
SRC_DIR="css/ak-design-system"
OUTPUT_CSS="$DIST_DIR/ak-design-system.css"
OUTPUT_MIN_CSS="$DIST_DIR/ak-design-system.min.css"

echo "🏗️  Building AK Design System v$VERSION..."

# Ensure dist directory exists
mkdir -p "$DIST_DIR"

# 1. Bundle CSS files (Concatenation instead of @import)
# Order is critical: core -> base -> layout -> components -> loaders -> utilities
echo "📦 Bundling CSS files..."
cat "$SRC_DIR/ak-core.css" \
    "$SRC_DIR/ak-base.css" \
    "$SRC_DIR/ak-layout.css" \
    "$SRC_DIR/ak-components.css" \
    "$SRC_DIR/ak-loaders.css" \
    "$SRC_DIR/ak-utilities.css" > "$OUTPUT_CSS"

# Note: ak-modifiers.css is empty and skipped

echo "✅ Bundled to $OUTPUT_CSS"

# 2. Minify CSS (Simplified for POSIX sed compatibility)
echo "🗜️  Minifying CSS..."

# Remove comments
cat "$OUTPUT_CSS" | perl -pe 's|/\*.*?\*/||gs' > "$OUTPUT_CSS.tmp"

# Remove newlines and extra spaces
tr -d '\n' < "$OUTPUT_CSS.tmp" | sed 's/  */ /g' | sed 's/ {/{/g' | sed 's/{ /{/g' | sed 's/ }/}/g' | sed 's/} /}/g' | sed 's/; /;/g' | sed 's/: /:/g' > "$OUTPUT_MIN_CSS"

# Cleanup
rm "$OUTPUT_CSS.tmp"

echo "✅ Minified to $OUTPUT_MIN_CSS"

# 3. Create Gzip version for CDN checking
gzip -fk "$OUTPUT_MIN_CSS"
GZIP_SIZE=$(ls -lh "$OUTPUT_MIN_CSS.gz" | awk '{print $5}')
RAW_SIZE=$(ls -lh "$OUTPUT_MIN_CSS" | awk '{print $5}')

echo "🎉 Build complete!"
echo "----------------------------------------"
echo "Version: $VERSION"
echo "Size:    $RAW_SIZE"
echo "Gzipped: $GZIP_SIZE"
echo "----------------------------------------"
