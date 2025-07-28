import sys
import re

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) == 2:
        rating, text = parts
        try:
            rating = float(rating)
        except ValueError:
            continue
        if rating <= 2.0:
            words = re.findall(r"\b\w+\b", text)
            for word in words:
                print(f"{word}\t1")