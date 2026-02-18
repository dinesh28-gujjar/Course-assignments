# 1.From your products list, create a set of categories called categories_set. (If product names do not contain categories, create a short parallel list categories = [..] with matching length and use that.)
products = ["Laptop", "Smartphone", "Headphones", "Keyboard", "Mouse", "Monitor"]
categories_list = ["Electronics", "Electronics", "Hardware", "Hardware", "Hardware","Hardware"]    #Create a parallel list of categories matching a hypothetical product list

categories_set = set(categories_list)    #Create categories_set from the list
print(f"Initial set: {categories_set}")



# 2.Demonstrate adding a new category to the set and show that duplicates are ignored.
categories_set.add("Software")
print(f"After adding 'Software': {categories_set}")

categories_set.add("Electronics")          # Adding 'Electronics' again won't change the set
print(f"After trying to add 'Electronics' again: {categories_set}")



# 3.Show how to check whether a category exists in the set (print a boolean result).
search = "Hardware"
exists = search in categories_set
print(f"Does '{search}' exist in the set? {exists}")



# Extra (optional): Show how to get the total number of unique categories using a set.
unique = len(categories_set)
print(f"Total number of unique categories: {unique}")
