# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

import csv


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
added_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
order = ""

# Displays the inventory.
def display_inventory(inventory):
    for k, v in inventory.items():
        print(v, k)
    print("Total number of items:", sum(inventory.values()))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item]+= 1
        else:
            inventory[item] = 1


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    max_len_name = max([len(v) for v in inventory.keys()])
    max_len_count = max([len(str(v)) for v in inventory.values()])
    sorted_inventory = inventory.items()
    if order == "count,desc":
        sorted_inventory = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    if order == "count,asc":
        sorted_inventory = sorted(inventory.items(), key=lambda x: x[1], reverse=False)
    if order == "name,desc":
        sorted_inventory = sorted(inventory.items(), key=lambda x: x[0], reverse=True)
    if order == "name,asc":
        sorted_inventory = sorted(inventory.items(), key=lambda x: x[0], reverse=False)
    print("Inventory count:\tItem name")
    for i in sorted_inventory:
        pformat = "{:" + str(max_len_count) + "}\t{:>" + str(max_len_name) + "}";
        print(pformat.format(i[1], i[0]))
    print("Total number of items:", sum(inventory.values()))


filename = ""
# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    path = "/home/codeorgo/Documents/2nd_SI_Week/pbwp-1st-si-game-inventory-weiliya/import_inventory.csv"
    file = open(path, newline='')
    reader = csv.reader(file)
    data = [row for row in reader]
    print(data)

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    returns_path = "/home/codeorgo/Documents/2nd_SI_Week/pbwp-1st-si-game-inventory-weiliya/import_inventory.csv"
    file = open(returns_path, 'w')
    writer = csv.writer(file)
    writer.writerow(["ruby", "arrow"])
    
export_inventory(inventory, filename)