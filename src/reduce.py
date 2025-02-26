#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths', nargs='+', required=True)
parser.add_argument('--output_path', required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter, defaultdict

# load each of the input paths
total = defaultdict(Counter)
for path in args.input_paths:
    with open(path) as f:
        tmp = json.load(f)
        for hashtag, counts in tmp.items():
            for key, value in counts.items():
                total[hashtag][key] += value  # ✅ Correctly summing nested dictionaries

# write the output path
with open(args.output_path, 'w') as f:
    f.write(json.dumps(total, indent=4))

print(f"Reduced data saved to {args.output_path}")

