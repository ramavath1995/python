from data import *


def resources_sufficient(drink):
    for i in drink:
        if drink[i] >= resources[i]:
            print(f"Sorry not enough {i}")
            return False
        else:
            return True


def transaction_successful(chosen_drink, user_choice):
    global profit
    drink = chosen_drink['cost']
    if user_choice >= drink:
        profit += drink
        change = abs(drink - user_choice)
        print(f"Here your change {change}")
        return True
    else:
        print("Sorry not enough money")
        return False


def make_drink(drink):
    for i in drink:
        resources[i] -= drink[i]


is_finished = False
while not is_finished:
    user = input("What would you like (espresso/latte/cappuccino)? or report: ").lower()
    if user == "off":
        is_finished = True
    elif user == "report":
        for item in resources:
            print(f"Milk = {resources['milk']}ml")
            print(f"Water = {resources['water']}ml")
            print(f"Coffee = {resources['coffee']}grams")
            # noinspection PyUnboundLocalVariable
            print(f"Money = Rs {profit}")

    else:
        choice = MENU[user]
        if resources_sufficient(choice['ingredients']):
            money = int(input(f"Please add enough cash for your drink {user} Rs: "))
            if transaction_successful(choice, money):
                make_drink(choice['ingredients'])
                print(f"Here your drink {user} ☕️")
            else:
                is_finished = True
        else:
            is_finished = True
