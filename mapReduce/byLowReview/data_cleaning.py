import json
import html
import re

input = "/Users/gladys/Documents/IST31434/Amazon_Fashion.jsonl"
output = "/Users/gladys/Documents/IST31434/Amazon_Fashion.txt"

with open(input, 'r', encoding='utf-8') as infile, open(output, 'w', encoding='utf-8') as outfile:
    for line in infile:
        try:
            review = json.loads(line)
            rating = review.get("rating")
            text = review.get("text", "")

            # cleaning text
            text = html.unescape(text) 
            text = text.strip().replace("\n", " ") 
            text = text.lower()
            text = re.sub(r"[!?.]{2,}", '', text)
            text = re.sub(r"[^\w\s/'\"]", '', text)          
            text = text.strip('"').strip("'")                   

            if rating and text:
                outfile.write(f"{rating}\t{text}\n")
        except json.JSONDecodeError:
            continue
