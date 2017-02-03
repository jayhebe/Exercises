def display_inventory(inventory):
    total_number = 0
    print("Inventory:")
    for k, v in inventory.items():
        print(str(v) + " " + k)
        total_number += v
    print("Total number of items: " + str(total_number))
    
def add_to_inventory(inventory, added_items):
    for each_item in added_items:
        inventory.setdefault(each_item, 0)
        inventory[each_item] += 1
    
inventory = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
added_items = ["torch", "torch", "gold coin", "gold coin", "gold coin", "arrow", "arrow", "rope", "baba"]

add_to_inventory(inventory, added_items)
display_inventory(inventory)