import os
from data import MENU, COINS, ingredients


def print_report(money):
    water = ingredients["water"]
    milk = ingredients["milk"]
    coffee = ingredients["coffee"]
    print(
        f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def process_coins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    sum_coins = 0
    sum_coins += quarters * COINS["quarter"]
    sum_coins += dimes * COINS["dime"]
    sum_coins += nickels * COINS["nickel"]
    sum_coins += pennies * COINS["penny"]
    sum_coins_in_dollars = sum_coins / 100
    return sum_coins_in_dollars


def handle_order(order):
    recipe = MENU[order]
    insufficient_ingredients = []
    recipe_ingredients = recipe["ingredients"]
    for key in recipe_ingredients:
        if ingredients[key] < recipe_ingredients[key]:
            insufficient_ingredients.append(key.title())
    if len(insufficient_ingredients) > 0:
        print(
            f"Sorry, not enough ingredients: {', '.join(insufficient_ingredients)}.")
        return 0
    else:
        sum_coins = process_coins()
        if sum_coins < recipe["cost"]:
            short = recipe['cost'] - sum_coins
            print(
                f"Sorry, ${sum_coins} is ${round(short, 2)} short of the ${recipe['cost']} cost for {order}. Coins refunded.")
        else:
            for key in recipe_ingredients:
                ingredients[key] -= recipe_ingredients[key]
            sum_coins -= recipe["cost"]
            if sum_coins > 0:
                print(f"Here is ${round(sum_coins, 2)} in change.")
            print(f"Enjoy your {order} ☕!")
            return recipe["cost"]


def coffee_machine():
    os.system("cls")
    money = 0
    ordering = True
    while ordering:
        order = input(
            "What would you like? (Espresso/Latte/Cappuccino)\n").lower()
        if order == "report":
            print_report(money)
        elif order == "espresso" or order == "latte" or order == "cappuccino":
            money = handle_order(order)
        elif order == "off" or order == "quit" or order == "exit":
            ordering = False
            print("Thank you for using the coffee machine!")
        else:
            print("Invalid input, please try again.")


coffee_machine()
