# generate_dataset.py
import pandas as pd
import random
from faker import Faker

fake = Faker()

# Some sample options for furniture attributes
categories = ["Chair", "Table", "Sofa", "Bed", "Wardrobe", "Bookshelf", "Dining Set"]
materials = ["Wood", "Metal", "Plastic", "Glass", "Leather", "Fabric"]
colors = ["Brown", "Black", "White", "Beige", "Grey", "Blue", "Green"]

brands = ["UrbanLoom", "FurniCraft", "HomeLuxe", "ComfyCasa", "OakStone"]
manufacturers = ["FurniMakers Ltd.", "UrbanWorks", "CasaFurnish", "CraftedCo", "EliteWood"]
countries = ["India", "China", "Vietnam", "Germany", "Italy"]

data = []

for i in range(1, 51):  # 50 items
    category = random.choice(categories)
    brand = random.choice(brands)
    material = random.choice(materials)
    color = random.choice(colors)
    manufacturer = random.choice(manufacturers)
    country = random.choice(countries)
    price = round(random.uniform(2000, 30000), 2)
    
    title = f"{brand} {material} {category}"
    description = f"A stylish {category.lower()} made from premium {material.lower()} in {color.lower()} color. Perfect for modern homes."
    package_dim = f"{random.randint(30, 200)}x{random.randint(30, 200)}x{random.randint(30, 200)} cm"
    image = f"https://picsum.photos/200?random={i}"
    uniq_id = f"PROD-{1000 + i}"

    data.append({
        "uniq_id": uniq_id,
        "title": title,
        "brand": brand,
        "description": description,
        "price": price,
        "categories": category,
        "images": image,
        "manufacturer": manufacturer,
        "package_dimensions": package_dim,
        "country_of_origin": country,
        "material": material,
        "color": color
    })

df = pd.DataFrame(data)
df.to_csv("products.csv", index=False)
print("✅ Dataset generated successfully: products.csv (50 items)")
