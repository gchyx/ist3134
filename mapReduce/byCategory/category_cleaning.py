import json

CATEGORY_KEYWORDS = {
    # Clothing
    "dress": "Clothing > Dresses",
    "blouse": "Clothing > Tops, Tees & Blouses",
    "tee": "Clothing > Tops, Tees & Blouses",
    "t-shirt": "Clothing > Tops, Tees & Blouses",
    "sweater": "Clothing > Sweaters",
    "hoodie": "Clothing > Fashion Hoodies & Sweatshirts",
    "sweatshirt": "Clothing > Fashion Hoodies & Sweatshirts",
    "jeans": "Clothing > Jeans",
    "pants": "Clothing > Pants",
    "trousers": "Clothing > Pants",
    "skirt": "Clothing > Skirts",
    "shorts": "Clothing > Shorts",
    "active": "Clothing > Active",
    "swimsuit": "Clothing > Swimsuits & Cover Ups",
    "bikini": "Clothing > Swimsuits & Cover Ups",
    "cover up": "Clothing > Swimsuits & Cover Ups",
    "lingerie": "Clothing > Lingerie, Sleep & Lounge",
    "sleepwear": "Clothing > Lingerie, Sleep & Lounge",
    "lounge": "Clothing > Lingerie, Sleep & Lounge",
    "jumpsuit": "Clothing > Jumpsuits, Rompers & Overalls",
    "romper": "Clothing > Jumpsuits, Rompers & Overalls",
    "overall": "Clothing > Jumpsuits, Rompers & Overalls",
    "coat": "Clothing > Coats, Jackets & Vests",
    "jacket": "Clothing > Coats, Jackets & Vests",
    "vest": "Clothing > Coats, Jackets & Vests",
    "blazer": "Clothing > Suiting & Blazers",
    "suit": "Clothing > Suiting & Blazers",
    "sock": "Clothing > Socks & Hosiery",
    "hosiery": "Clothing > Socks & Hosiery",
    "clothing set": "Clothing > Clothing Sets",
    "bodysuit": "Clothing > Bodysuits",

    # Shoes
    "sandal": "Shoes > Sandals",
    "slipper": "Shoes > Slippers",
    "boot": "Shoes > Boots",
    "sneaker": "Shoes > Fashion Sneakers",
    "flat": "Shoes > Flats",
    "loafer": "Shoes > Loafers & Slip-Ons",
    "slip-on": "Shoes > Loafers & Slip-Ons",
    "mule": "Shoes > Mules & Clogs",
    "clog": "Shoes > Mules & Clogs",
    "oxford": "Shoes > Oxfords",
    "pump": "Shoes > Pumps",
    "work shoe": "Shoes > Work & Safety",
    "safety shoe": "Shoes > Work & Safety",
    "athletic shoe": "Shoes > Athletic",
    "running shoe": "Shoes > Athletic",

    # Jewelry
    "anklet": "Jewelry > Anklets",
    "bracelet": "Jewelry > Bracelets",
    "brooch": "Jewelry > Brooches & Pins",
    "pin": "Jewelry > Brooches & Pins",
    "earring": "Jewelry > Earrings",
    "jewelry set": "Jewelry > Jewelry Sets",
    "necklace": "Jewelry > Necklaces",
    "pendant": "Jewelry > Pendants & Coins",
    "ring": "Jewelry > Rings",
    "wedding": "Jewelry > Wedding & Engagement",
    "engagement": "Jewelry > Wedding & Engagement",
    "smart jewelry": "Jewelry > Smart Jewelry",
    "body jewelry": "Jewelry > Body Jewelry",

    # Watches
    "watch": "Watches > Wrist Watches",
    "smartwatch": "Watches > Smartwatches",
    "pocket watch": "Watches > Pocket Watches",
    "watch band": "Watches > Watch Bands",

    # Handbags & Wallets
    "clutch": "Handbags & Wallets > Clutches & Evening Bags",
    "crossbody": "Handbags & Wallets > Crossbody Bags",
    "backpack": "Handbags & Wallets > Fashion Backpacks",
    "hobo": "Handbags & Wallets > Hobo Bags",
    "satchel": "Handbags & Wallets > Satchels",
    "shoulder bag": "Handbags & Wallets > Shoulder Bags",
    "top-handle": "Handbags & Wallets > Top-Handle Bags",
    "tote": "Handbags & Wallets > Totes",
    "wallet": "Handbags & Wallets > Wallets",
    "wristlet": "Handbags & Wallets > Wristlets",

    # Accessories
    "belt": "Accessories > Belts",
    "fashion headband": "Accessories > Fashion Headbands",
    "glove": "Accessories > Gloves & Mittens",
    "mitten": "Accessories > Gloves & Mittens",
    "hand fan": "Accessories > Hand Fans",
    "handbag accessory": "Accessories > Handbag Accessories",
    "hat": "Accessories > Hats & Caps",
    "cap": "Accessories > Hats & Caps",
    "keyring": "Accessories > Keyrings, Keychains & Charms",
    "keychain": "Accessories > Keyrings, Keychains & Charms",
    "charm": "Accessories > Keyrings, Keychains & Charms",
    "scarf": "Accessories > Scarves & Wraps",
    "wrap": "Accessories > Scarves & Wraps",
    "special occasion": "Accessories > Special Occasion Accessories",
    "sport headband": "Accessories > Sport Headbands",
    "sunglasses": "Accessories > Sunglasses & Eyewear Accessories",
    "eyewear": "Accessories > Sunglasses & Eyewear Accessories",
    "card case": "Accessories > Wallets, Card Cases & Money Organizers",
    "money organizer": "Accessories > Wallets, Card Cases & Money Organizers"
}

input = '/Users/gladys/Documents/IST31434/meta_Amazon_Fashion.jsonl'
output = '/Users/gladys/Documents/IST31434/byCategory/data/categories.txt'

def extract_category_and_asin(product_json):
    try:
        product = json.loads(product_json)
        title = product.get("title", "").lower()
        asin = product.get("parent_asin", "UNKNOWN")

        for keyword, category_path in CATEGORY_KEYWORDS.items():
            if keyword in title:
                top_level = category_path.split(" > ")[0]  # Extract 'Clothing' from 'Clothing > Dresses'
                return f"{asin}\t{top_level}"
        return f"{asin}\tUnknown"
    except Exception as e:
        return f"ERROR\t{str(e)}"

with open(input, "r", encoding="utf-8") as infile, open(output, "w", encoding="utf-8") as outfile:
    for line in infile:
        result = extract_category_and_asin(line.strip())
        outfile.write(result + "\n")

