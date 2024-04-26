MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def coins():
    print("Please insert coins")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def sufficient_resource(coffee):
    for key in coffee:
        if coffee[key] > resources[key]:
            print(f"sorry there is not enough {key}.")
            return False
    return True


def transaction(price):
    total_amt = coins()
    if total_amt >= price:
        change = round(total_amt - price, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def coffee_machine():
    on_coffee_machine = True
    while on_coffee_machine:
        coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if coffee == "off":
            on_coffee_machine = False
        elif coffee == "report":
            print(f"Water = {resources['water']}ml")
            print(f"Milk = {resources['milk']}ml")
            print(f"coffee =  {resources['coffee']}g")
            print(f"Balance = Rs.{profit}")
        else:
            drink = MENU[coffee]
            if sufficient_resource(drink["ingredients"]):
                if transaction(drink["cost"]):
                    make_coffee(coffee, drink["ingredients"])


coffee_machine()
