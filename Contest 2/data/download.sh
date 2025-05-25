#!/bin/bash

# Download Kaggle competition data
COMPETITION="soil-classification-part-2"
TARGET_DIR="./data"

echo "Downloading competition files: $COMPETITION"
mkdir -p "$TARGET_DIR"
kaggle competitions download -c "$COMPETITION" -p "$TARGET_DIR"

# Unzip all files
echo "Unzipping files..."
unzip "$TARGET_DIR/*.zip" -d "$TARGET_DIR"

# Clean up zip files
rm "$TARGET_DIR/*.zip"

echo "Download complete. Files saved to $TARGET_DIR"
