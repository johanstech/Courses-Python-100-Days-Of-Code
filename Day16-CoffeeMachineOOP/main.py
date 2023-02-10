import os
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    os.system("cls")
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    menu_items = menu.get_items()
    print(menu_items)
    ordering = True
    while ordering:
        order = input(f"What would you like? ({menu_items})\n").lower()
        if order == "report":
            coffee_maker.report()
            money_machine.report()
        elif order == "off" or order == "quit" or order == "exit":
            ordering = False
            print("Thank you for using the coffee machine!")
        else:
            drink = menu.find_drink(order)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(drink):
                    money_machine.make_payment(drink.cost)
                    coffee_maker.make_coffee(drink)


coffee_machine()
