#!/bin/bash

# Define paths
CSS_DIR="css/ak-design-system"
DIST_DIR="dist"
OUTPUT_FILE="$DIST_DIR/ak-design-system.css"

# Ensure dist directory exists
mkdir -p "$DIST_DIR"

# Concatenate files in correct order
cat "$CSS_DIR/ak-core.css" \
    "$CSS_DIR/ak-base.css" \
    "$CSS_DIR/ak-layout.css" \
    "$CSS_DIR/ak-components.css" \
    "$CSS_DIR/ak-loaders.css" \
    "$CSS_DIR/ak-utilities.css" \
    "$CSS_DIR/ak-modifiers.css" > "$OUTPUT_FILE"

echo "Build complete: $OUTPUT_FILE"

# Note: Minification would require external tools. 
# For now, we copy the file to .min.css as a placeholder or use a simple sed/tr if strictly necessary, 
# but usually minification implies a real tool like cssnano.
# Since we cannot install packages, we just copy it to allow the CDN links to work if they point to min.
cp "$OUTPUT_FILE" "$DIST_DIR/ak-design-system.min.css"

echo "Created placeholder min file: $DIST_DIR/ak-design-system.min.css"
