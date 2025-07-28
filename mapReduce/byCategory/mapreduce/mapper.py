import sys
import re

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) != 3:
        continue
    rating, category, text = parts
    text = text.lower()
    words = re.findall(r"\b\w+\b", text) 
    for word in words:
        print(f"{category}#{word}\t1")