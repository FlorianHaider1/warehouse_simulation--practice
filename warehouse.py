# Program a system to manage inventory of a small warehouse. Track items, quantities, and categories.
# Practice Skills: Use dictionaries to store item details and quantities. 
# Lists can be used to store categories or item names. 
# Updating inventory (add, remove items), retrieve items based on e.g. category or quantity. 
# String methods can be used for input validation and formatting.
# Using sets: checking for duplicates and easy access if a particular item is in stock. 

# building a dictionary structured in dict: categories subdict: Items : Quantities
from prettytable import PrettyTable

inventory = {"tools":{}, "cutlery":{}, "towels":{}, "kitchenware":{},}
items = ["cutlery", "knife", "tools", "hammer","kitchenware", "toaster", "towels", "cotton towel","towels", "satin towel", "tools", "screwdriver", "cutlery", "fork", "cutlery", "spoon", "cutlery", "teaspoon"]
quantities = [2, 4, 1, 5, 2, 8, 5, 3, 2]

def type_item_quantity():
    return list(zip(items[0::2], items[1::2], quantities))

def entries_dictionary(overview):
    for category, item, quantity in overview:
        inventory[category][item] = quantity
    return inventory

table_inventory = PrettyTable(entries_dictionary(type_item_quantity()))

print(table_inventory)

# def import_to_inventory():
#     for items in type_item_quantity():
#         if inventory[keys] == keys:
#             inventory.values == values
#         print(inventory)

# import_to_inventory()


# import_to_inventory()
# print(inventory)
# for i, d in type_item_quantity():
#     if inventory[] == i:
#         inventory[i] = d


# def create_entries():
#     inventory = dict(zip(type_item_quantity[0::2] type_item_quantity()))
#     print(inventory)

# create_entries()
