#!/bin/bash

# Download Kaggle competition data
COMPETITION="soil-classification"
TARGET_DIR="./data"

echo "Downloading competition files: $COMPETITION"
mkdir -p "$TARGET_DIR"
kaggle competitions download -c "$COMPETITION" -p "$TARGET_DIR"

# Unzip all downloaded zip files in the target directory
echo "Unzipping files..."
for file in "$TARGET_DIR"/*.zip; do
    unzip -o "$file" -d "$TARGET_DIR"
done

# Clean up zip files
rm "$TARGET_DIR"/*.zip

echo "Download complete. Files saved to $TARGET_DIR"
