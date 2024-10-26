from data import MENU, resources

profit = 0

def sufficient_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:  # Change >= to >
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def money_collection():
    """Returns the total coins inserted"""
    print("Insert coins 🪙")
    total = int(input("How many 1's? ")) * 1
    total += int(input("How many 2's? ")) * 2
    total += int(input("How many 5's? ")) * 5
    total += int(input("How many 10's? ")) * 10
    return total

def transaction(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"Here is {change} Rupees in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money.")
        return False

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)🍵: ").lower()
    if choice == "turn off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit} Rupees")
    else:
        drink = MENU.get(choice)
        if drink:
            print(f"Cost = {drink['cost']} Rupees")
            if sufficient_resources(drink["ingredients"]):
                payment = money_collection()
                if transaction(payment, drink['cost']):  # Check if transaction is successful
                    # Deduct resources if transaction was successful
                    for item in drink["ingredients"]:
                        resources[item] -= drink["ingredients"][item]
                    print(f"Here is your {choice} ☕️. Enjoy!")
        else:
            print("Invalid choice. Please choose espresso, latte, or cappuccino.")