# Program a system to manage inventory of a small warehouse. Track items, quantities, and categories.
# Practice Skills: Use dictionaries to store item details and quantities. 
# Lists can be used to store categories or item names. 
# Updating inventory (add, remove items), retrieve items based on e.g. category or quantity. 
# String methods can be used for input validation and formatting.
# Using sets: checking for duplicates and easy access if a particular item is in stock. 

# building a dictionary structured in dict: categories subdict: Items : Quantities
inventory = {"tools":"", "cutlery":"", "towels":"", "kitchenware":"",}
keys = ["tools", "cutlery", "towels", "kitchenware"]
items = ["cutlery", "knife", "tools", "hammer","kitchenware", "toaster", "towels", "cotton towel","towels", "satin towel", "tools", "screwdriver", "cutlery", "fork", "cutlery", "spoon", "cutlery", "teaspoon"]
quantities = [2, 4, 1, 5, 2, 8, 5, 3, 2]



# def type_item_quantity():
#     return list(zip(items[0::2], tuple(zip(items[1::2], quantities))))

# for i, d in type_item_quantity():
#     inventory[i] = d

print(inventory)

# def create_entries():
#     inventory = dict(zip(type_item_quantity[0::2] type_item_quantity()))
#     print(inventory)

# create_entries()
