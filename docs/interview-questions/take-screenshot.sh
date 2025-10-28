#!/bin/bash
# Quick Screenshot Helper Script
# Usage: ./take-screenshot.sh q01-odoo-dashboard

SCREENSHOT_DIR="docs/interview-questions/junior"
FILENAME="$1.png"

if [ -z "$1" ]; then
    echo "❌ Usage: ./take-screenshot.sh <filename-without-extension>"
    echo "Example: ./take-screenshot.sh q01-odoo-dashboard"
    echo ""
    echo "📋 Available screenshots needed:"
    cat "$SCREENSHOT_DIR/CHECKLIST.md" | grep "q[0-9]" | head -20
    exit 1
fi

echo "📸 Taking screenshot for: $FILENAME"
echo "Click and drag to select area, or press Enter for full screen"
echo "Screenshot will be saved to: $SCREENSHOT_DIR/$FILENAME"
echo ""

# Use flameshot if available, otherwise gnome-screenshot
if command -v flameshot &> /dev/null; then
    flameshot gui -p "$SCREENSHOT_DIR/$FILENAME"
elif command -v gnome-screenshot &> /dev/null; then
    gnome-screenshot -a -f "$SCREENSHOT_DIR/$FILENAME"
else
    echo "❌ No screenshot tool found. Please install flameshot or gnome-screenshot"
    echo "   sudo apt install flameshot"
    exit 1
fi

if [ -f "$SCREENSHOT_DIR/$FILENAME" ]; then
    echo "✅ Screenshot saved: $SCREENSHOT_DIR/$FILENAME"
    
    # Show file size
    SIZE=$(du -h "$SCREENSHOT_DIR/$FILENAME" | cut -f1)
    echo "📊 File size: $SIZE"
    
    # Warn if too large
    SIZE_KB=$(du -k "$SCREENSHOT_DIR/$FILENAME" | cut -f1)
    if [ $SIZE_KB -gt 500 ]; then
        echo "⚠️  Warning: File is larger than 500KB. Consider compressing."
        echo "   You can use: optipng $SCREENSHOT_DIR/$FILENAME"
    fi
else
    echo "❌ Screenshot cancelled or failed"
fi
