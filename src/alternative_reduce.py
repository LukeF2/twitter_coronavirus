#!/usr/bin/env python3

# command line args
import argparse
import json
import os
import re
import matplotlib.pyplot as plt
from collections import defaultdict

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags', nargs='+', required=True, help="List of hashtags to track")
parser.add_argument('--output_path', default="output/alternative_reduce.png", help="Output plot file")
args = parser.parse_args()

# Initialize data storage
data = defaultdict(lambda: defaultdict(int))  # {hashtag: {day_of_year: count}}

# Regular expression to extract day of the year from filenames
date_pattern = re.compile(r'geoTwitter20-(\d{2})-(\d{2})')

# Scan through all files in the output directory
output_dir = "output"
for filename in os.listdir(output_dir):
    if filename.endswith(".lang"):  # Only process .lang files
        match = date_pattern.search(filename)
        if match:
            month, day = match.groups()
            day_of_year = int(month) * 31 + int(day)  # Approximate day-of-year calculation

            file_path = os.path.join(output_dir, filename)
            with open(file_path, 'r') as f:
                data_json = json.load(f)

            for hashtag in args.hashtags:
                if hashtag in data_json:
                    data[hashtag][day_of_year] = sum(data_json[hashtag].values())  # Sum all languages

# Sort data for plotting
for hashtag in data:
    data[hashtag] = dict(sorted(data[hashtag].items()))  # Ensure sorted by day_of_year

# Plot the data
plt.figure(figsize=(10, 6))

for hashtag, counts in data.items():
    days = list(counts.keys())
    values = list(counts.values())
    plt.plot(days, values, marker='o', label=hashtag)

# Configure plot labels
plt.xlabel("Day of the Year (Approximate)")
plt.ylabel("Tweet Count")
plt.title("Hashtag Popularity Over Time")
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig(args.output_path, bbox_inches="tight")
print(f"Saved alternative reduce plot to {args.output_path}")

# Show the plot (optional)
# plt.show()

