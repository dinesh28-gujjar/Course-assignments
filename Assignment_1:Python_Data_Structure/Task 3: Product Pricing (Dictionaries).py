# 1. Create a dictionary with at least 6 entries
price_dict = {
    "Laptop": 1200.00,
    "Smartphone": 800.00,
    "Monitor": 300.00,
    "Keyboard": 50.00,
    "Mouse": 25.00,
    "Headphones": 150.00
}
print(price_dict)

# 2. Code blocks for management
# Add a new product
price_dict["Webcam"] = 95.00

# Update the price of an existing product
price_dict["Monitor"] = 280.00

# Remove a product by name (handling non-existent cases)
product_to_remove = "Headphones"

print(price_dict)
# .pop(key, default) prevents a KeyError if the item isn't there
removed_price = price_dict.pop(product_to_remove, None)

if removed_price:
    print(f"Removed {product_to_remove} which cost ${removed_price}")

# 3. Print the average price
# Using only dictionary operations and basic arithmetic
total_price = sum(price_dict.values())
count = len(price_dict)
average = total_price / count

print(f"\nAverage Price: ${average:.2f}")

# Extra: Print product with Max and Min prices
# We use the 'key' argument to find the name associated with the max/min value
max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print(f"Most expensive: {max_product} (${price_dict[max_product]})")
print(f"Least expensive: {min_product} (${price_dict[min_product]})")
else:
    print(f"Product '{product_to_remove}' not found.")
