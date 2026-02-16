# 1.Create a list named products containing at least 6 product names (strings).
products = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Keyboard",
    "Mouse",
    "Monitor"
]
print(products)
print(type(products))

# 2.Create a tuple named sample_product that stores (product_name, price, category) for one product.
sample_product = ("Monitor", 25000, "Electronics")
print(sample_product)
print(type(sample_product))

# 3.Print the 2nd and last product from the products list.
print("Second product:", products[1])
print("Last product:", products[5])

# 4.Append two new product names to products and then print the updated list.
products.append("Smartwatch")
products.append("Printer")
print(products)

# Extra (optional): Convert sample_product into a list, change its price, and convert it back to a tuple.
sample_product_list = list(sample_product) #Convert tuple to list to modify price
print(type(sample_product_list))

sample_product_list[1] = 27000   #Change the price (index 1)

sample_product = tuple(sample_product_list)   #Convert back to tuple
print(sample_product)
print(type(sample_product))
