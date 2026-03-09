# Setup: Ensuring we have our base data from Tasks 2 & 3
products = ["Laptop", "Smartphone", "Monitor", "Keyboard", "Mouse", "Webcam"]
categories = ["Electronics", "Electronics", "Hardware", "Hardware", "Hardware", "Hardware"]
price_dict = {
    "Laptop": 1200.0, "Smartphone": 800.0, "Monitor": 280.0, 
    "Keyboard": 50.0, "Mouse": 25.0, "Webcam": 95.0
}

# 1. Create a list of tuples named 'catalog'
# We use zip() to pair the product and category, then look up the price
catalog = []
for i in range(len(products)):
    name = products[i]
    category = categories[i]
    price = price_dict.get(name, 0.0)
    catalog.append((name, price, category))

print("--- Catalog (List of Tuples) ---")
for item in catalog:
    print(item)

# 2. Create category_to_products dictionary
category_to_products = {}
for name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []  # Initialize list if category is new
    category_to_products[category].append(name)

# 3. Find and print products in the category with the most items
# We find the key (category) that has the longest list of products
max_category = max(category_to_products, key=lambda k: len(category_to_products[k]))

print(f"\n--- Category with most products: {max_category} ---")
for p in category_to_products[max_category]:
    print(f"- {p}")
