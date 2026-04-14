inventory = {"apple": 10}

product = "banana"

if product not in inventory:
    inventory[product] = 0

print(inventory)