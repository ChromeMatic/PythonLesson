from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}): ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
