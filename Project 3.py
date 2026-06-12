shop_items = [
    {"name": "keyboard", "price": 100},
    {"name": "mouse", "price": 50},
    {"name": "monitor", "price": 150},
    {"name": "mousepad", "price": 35}
]
inventory = {

}


gold = 300
print("Type 'leave' to stop!")
decision = input("Action: ")
while decision.lower() != "leave":     
    print(f"Gold amount: {gold}")
    print("Inventory")
    for key, value in inventory.items():
        print(f"{key} {value}")
    print("-------------Welcome to the Shop-------------")
    for q in shop_items:
        print(f"{q['name']}: {q['price']} gold")
    print("---------------------------------------------")
    purch = input("What would you like to purchase from the shop?: ")
    if purch == "1" and gold >= 100:
        gold -= 100
        if "keyboard" in inventory:
            inventory["keyboard"] += 1
            for key, value in inventory.items():
                print(f"You now have {value} {key}s!")
        else:
            inventory["keyboard"] = 1
            print("You have just purchased a keyboard!")
    elif gold < 100:
        print("You're broke")
    if purch == "2" and gold >= 50:
        gold -= 50
        if "mouse" in inventory:
            inventory["mouse"] += 1
            for key, value in inventory.items():
                print(f"You have {value} {key}s")
        else:
            inventory["mouse"] = 1
            print("You have just purchase a mousepad!")
    elif gold < 50:
        print("You're broke")

    if purch == "3" and gold >= 150:
        gold -= 150
        if "monitor" in inventory:
            inventory["monitor"] += 1
        for key, value in inventory.items():
            print(f"You have {value} {key}s")
        else:
            inventory["monitor"] = 1
            print(f"You have just purchased a monitor")
    elif gold < 150:
        print("You are broke")

    if purch == "4" and gold >= 35:
        gold -= 35
        if "mousepad" in inventory:
            inventory["mousepad"] += 1
            for key, value in inventory.items():
                print(f"You have {value} {key}s")
        else:
            inventory["mousepad"] = 1
            print("You have just purchased a mousepad!")
    elif gold < 35:
        print("You're broke")
    
    print("Type 'leave' to stop!")
    decision = input("Action: ")

