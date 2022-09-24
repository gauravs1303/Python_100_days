from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = Menu()
make_that_coffee = CoffeeMaker()
pay = MoneyMachine()
while input('Do you want to turn off machine : ').strip().upper() != 'OFF':
    order = input(f'What do you want ({coffee.get_items()}) : ').strip().lower()
    drink = coffee.find_drink(order)
    if order == 'report':
        make_that_coffee.report()
        pay.report()
    elif drink is not None:
        if make_that_coffee.is_resource_sufficient(drink) and pay.make_payment(drink.cost):
            make_that_coffee.make_coffee(drink)