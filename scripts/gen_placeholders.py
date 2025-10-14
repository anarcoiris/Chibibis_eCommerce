#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from faker import Faker
import json, random
import argparse

OUT_DIR = Path("backend/backend/static/placeholders")  # note backend package path
OUT_DIR.mkdir(parents=True, exist_ok=True)
fake = Faker("es_ES")

def make_img(name, size=(800,800), bg=(245,244,250)):
    img = Image.new("RGB", size, color=bg)
    d = ImageDraw.Draw(img)
    text = name
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 40)
    except Exception:
        font = ImageFont.load_default()
    w,h = d.textsize(text, font=font)
    d.text(((size[0]-w)/2,(size[1]-h)/2), text, fill=(30,30,30), font=font)
    filename = OUT_DIR / f"{name.replace(' ','_')}.png"
    img.save(filename)
    return str(filename)

def gen_products(n=12):
    products = []
    for i in range(n):
        title = fake.sentence(nb_words=3).rstrip(".")
        price = round(random.uniform(5,250),2)
        img = make_img(f"{title}", size=(800,800))
        prod = {
            "id": i+1,
            "title": title,
            "description": fake.paragraph(nb_sentences=2),
            "price": price,
            "currency": "EUR",
            "image": f"/static/placeholders/{Path(img).name}",
            "slug": title.lower().replace(" ", "-")
        }
        products.append(prod)
    with open("backend/backend/static/placeholders/products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    print(f"Generated {n} products and images in {OUT_DIR}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=20)
    args = parser.parse_args()
    gen_products(args.count)
