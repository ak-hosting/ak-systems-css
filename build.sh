#!/bin/bash

# Start build timer (with millisecond precision if available)
if command -v gdate &> /dev/null; then
    START_TIME=$(gdate +%s.%N)
    USE_NANOSECONDS=true
elif [ "$(uname)" = "Darwin" ] && command -v python3 &> /dev/null; then
    START_TIME=$(python3 -c "import time; print(time.time())")
    USE_NANOSECONDS=true
else
    START_TIME=$(date +%s)
    USE_NANOSECONDS=false
fi

# Define paths
CSS_DIR="css/ak-design-system"
DIST_DIR="dist"
OUTPUT_FILE="$DIST_DIR/ak-design-system.css"
VERSION=$(cat VERSION)

# Colors for output (if terminal supports it)
if [ -t 1 ]; then
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    BLUE='\033[0;34m'
    NC='\033[0m' # No Color
else
    GREEN=''
    YELLOW=''
    BLUE=''
    NC=''
fi

# Ensure dist directory exists
mkdir -p "$DIST_DIR"

echo -e "${BLUE}Building CSS files...${NC}"

# Add version header
echo "/*! AK Design System v$VERSION | (c) AK Systems */" > "$OUTPUT_FILE"

# Concatenate files in correct order
cat "$CSS_DIR/ak-core.css" \
    "$CSS_DIR/ak-base.css" \
    "$CSS_DIR/ak-layout.css" \
    "$CSS_DIR/ak-components.css" \
    "$CSS_DIR/ak-loaders.css" \
    "$CSS_DIR/ak-utilities.css" \
    "$CSS_DIR/ak-modifiers.css" >> "$OUTPUT_FILE"

# Get file size in human-readable format
if command -v numfmt &> /dev/null; then
    SIZE=$(numfmt --to=iec-i --suffix=B $(stat -f%z "$OUTPUT_FILE" 2>/dev/null || stat -c%s "$OUTPUT_FILE" 2>/dev/null))
else
    SIZE=$(ls -lh "$OUTPUT_FILE" | awk '{print $5}')
fi

echo -e "${GREEN}✓${NC} Build complete: $OUTPUT_FILE (${SIZE})"

# Minify CSS using Python script
MIN_OUTPUT_FILE="$DIST_DIR/ak-design-system.min.css"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if command -v python3 &> /dev/null; then
    python3 "$SCRIPT_DIR/minify_css.py" "$OUTPUT_FILE" "$MIN_OUTPUT_FILE"
    if [ $? -eq 0 ]; then
        if command -v numfmt &> /dev/null; then
            MIN_SIZE=$(numfmt --to=iec-i --suffix=B $(stat -f%z "$MIN_OUTPUT_FILE" 2>/dev/null || stat -c%s "$MIN_OUTPUT_FILE" 2>/dev/null))
        else
            MIN_SIZE=$(ls -lh "$MIN_OUTPUT_FILE" | awk '{print $5}')
        fi
        echo -e "${GREEN}✓${NC} Minification complete: $MIN_OUTPUT_FILE (${MIN_SIZE})"
    else
        echo -e "${YELLOW}⚠${NC} Warning: Minification failed, creating copy as fallback"
        cp "$OUTPUT_FILE" "$MIN_OUTPUT_FILE"
    fi
else
    echo -e "${YELLOW}⚠${NC} Warning: python3 not found, creating copy as fallback"
    cp "$OUTPUT_FILE" "$MIN_OUTPUT_FILE"
fi

# Calculate build time
if [ "$USE_NANOSECONDS" = true ]; then
    if command -v gdate &> /dev/null; then
        END_TIME=$(gdate +%s.%N)
        BUILD_TIME=$(echo "$END_TIME - $START_TIME" | bc)
    else
        END_TIME=$(python3 -c "import time; print(time.time())")
        BUILD_TIME=$(python3 -c "print($END_TIME - $START_TIME)")
    fi
    # Format time nicely
    if (( $(echo "$BUILD_TIME < 1" | bc -l 2>/dev/null || echo "$BUILD_TIME < 1" | awk '{print ($1 < 1)}') )); then
        BUILD_TIME_MS=$(echo "$BUILD_TIME * 1000" | bc | awk '{printf "%.0f", $1}')
        BUILD_TIME_STR="${BUILD_TIME_MS}ms"
    else
        BUILD_TIME_STR=$(echo "$BUILD_TIME" | awk '{printf "%.2f", $1}')"s"
    fi
else
    END_TIME=$(date +%s)
    BUILD_TIME=$((END_TIME - START_TIME))
    BUILD_TIME_STR="${BUILD_TIME}s"
fi

# Calculate compression stats
if [ -f "$OUTPUT_FILE" ] && [ -f "$MIN_OUTPUT_FILE" ]; then
    ORIG_SIZE=$(stat -f%z "$OUTPUT_FILE" 2>/dev/null || stat -c%s "$OUTPUT_FILE" 2>/dev/null)
    MIN_SIZE=$(stat -f%z "$MIN_OUTPUT_FILE" 2>/dev/null || stat -c%s "$MIN_OUTPUT_FILE" 2>/dev/null)
    if [ -n "$ORIG_SIZE" ] && [ -n "$MIN_SIZE" ] && [ "$ORIG_SIZE" -gt 0 ]; then
        COMPRESSION_RATIO=$(echo "scale=1; (1 - $MIN_SIZE / $ORIG_SIZE) * 100" | bc 2>/dev/null || awk "BEGIN {printf \"%.1f\", (1 - $MIN_SIZE / $ORIG_SIZE) * 100}")
        SAVED_BYTES=$((ORIG_SIZE - MIN_SIZE))
        if command -v numfmt &> /dev/null; then
            SAVED_SIZE=$(numfmt --to=iec-i --suffix=B $SAVED_BYTES)
        else
            SAVED_SIZE="${SAVED_BYTES} bytes"
        fi
    fi
fi

# Count source files
SOURCE_FILES=7

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✓ Build completed successfully${NC}"
echo ""
echo -e "  ${BLUE}Files processed:${NC} ${SOURCE_FILES} source files"
echo -e "  ${BLUE}Output files:${NC} 2 (unminified + minified)"
if [ -n "$COMPRESSION_RATIO" ]; then
    echo -e "  ${BLUE}Compression:${NC} ${COMPRESSION_RATIO}% reduction (${SAVED_SIZE} saved)"
fi
echo -e "  ${BLUE}Build time:${NC} ${BUILD_TIME_STR}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
