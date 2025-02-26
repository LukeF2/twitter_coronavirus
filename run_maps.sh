#!/bin/bash

# Define input and output directories
INPUT_DIR="/data/Twitter dataset"
OUTPUT_DIR="output"

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Loop over each .zip file in the dataset
for file in "$INPUT_DIR"/geoTwitter20-*-*.zip; do
    echo "Processing $file..."
    
    # Correct the path to `map.py`
    nohup python3 src/map.py --input_path="$file" --output_folder="$OUTPUT_DIR" > "$OUTPUT_DIR/$(basename "$file").log" 2>&1 &

done

echo "All mapping jobs started in parallel."

