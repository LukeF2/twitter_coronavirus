#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True, help="Path to the JSON file")
parser.add_argument('--key', required=True, help="Hashtag to visualize")
args = parser.parse_args()

# imports
import json
import os
import matplotlib.pyplot as plt

# Load the data from JSON file
with open(args.input_path, 'r') as f:
    data = json.load(f)

# Extract the relevant hashtag data
if args.key not in data:
    print(f"Error: Hashtag '{args.key}' not found in {args.input_path}")
    exit(1)

hashtag_data = data[args.key]

# Sort data from low to high and take top 10
sorted_data = sorted(hashtag_data.items(), key=lambda x: x[1])[:10]
keys, values = zip(*sorted_data)  # Unpack keys and values

# Create a bar chart
plt.figure(figsize=(10, 5))
plt.barh(keys, values, color="skyblue")  # Horizontal bar chart
plt.xlabel("Count")
plt.ylabel("Keys")
plt.title(f"Top 10 Counts for {args.key}")
plt.grid(axis='x', linestyle="--", alpha=0.7)

# Save the figure
output_filename = f"output/{args.key.replace('#', '')}_{os.path.basename(args.input_path)}.png"
plt.savefig(output_filename, bbox_inches="tight")
print(f"Saved visualization to {output_filename}")

# Show the plot (optional)
# plt.show()

