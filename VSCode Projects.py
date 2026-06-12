import random

inventory = {
    "Wood": 0,
    "Stone": 0,
    "Planks": 0,
    "Iron Axe": 1,
}

options = input("Pick an option: \n1. View Inventory \n2. Gather Resources \n3. Craft Item\nWhat do you want to do?: ")
while True:
    if options == "1":
        for key, value in inventory.items():
            print(f"{key}: {value}")
    elif options == "2":
        drop = random.randint(1,3)
        if random == 1:
            inventory["Wood"] += 1
        elif random == 2:
            inventory["Stone"] += 1
        elif random == 3:
            inventory["Planks"] += 1
    elif options == "3":
        craft = input("What do you want to craft?: ")
        if craft == "Crafting Table":
            if inventory["Wood"] >= 4:
                inventory["Craft Table"] += 1
        elif craft == "Furnace":
            if inventory["Stone"] >= 8:
                inventory["Furnace"] += 1
        else:
            print("You do not have enough resources for that!")

    else:
        print("Invalid Action!")
    options = input("Pick an option: \n1. View Inventory \n2. Gather Resources \n3. Craft Item\nWhat do you want to do?: ")            
