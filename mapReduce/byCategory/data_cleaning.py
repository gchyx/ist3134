import json
import html
import re

# File paths
review = "/Users/gladys/Documents/IST31434/Amazon_Fashion.jsonl"
category = "/Users/gladys/Documents/IST31434/byCategory/data/categories.txt"
output = "/Users/gladys/Documents/IST31434/byCategory/data/category_reviews.txt"

# Load ASIN 
asin_to_category = {}
with open(category, 'r', encoding='utf-8') as catfile:
    for line in catfile:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            asin, category = parts
            asin_to_category[asin] = category

# Process reviews and add category
with open(review, 'r', encoding='utf-8') as infile, open(output, 'w', encoding='utf-8') as outfile:
    for line in infile:
        try:
            review = json.loads(line)
            asin = review.get("asin", "UNKNOWN")
            rating = review.get("rating")
            text = review.get("text", "")

            # clean text
            text = html.unescape(text)
            text = text.strip().replace("\n", " ")
            text = text.lower()
            text = re.sub(r"[!?.]{2,}", '', text)
            text = re.sub(r"[^\w\s/'\"]", '', text)
            text = text.strip('"').strip("'")

            # match asin to category
            category = asin_to_category.get(asin, "Unknown")

            if rating and text:
                outfile.write(f"{rating}\t{category}\t{text}\n")
        except json.JSONDecodeError:
            continue
