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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#resource
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

def check_sufficient(order_ingredients):
    """
Returns True when order can be made, False if ingredients are insufficient.
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True



# #espresso order
# def espresso():
#     menu_water = MENU["espresso"]["ingredients"]["water"]
#     menu_coffee = MENU["espresso"]["ingredients"]["coffee"]
#     cost =  float(MENU["espresso"]["cost"])
#     current_water = water - menu_water
#     current_coffee = coffee - menu_coffee
#     current_cost = float(int(money) + cost)
#     if current_water < 0:
#         return(f"Sorry there is not enough water")
#     if current_coffee < 0:
#         return(f"Sorry there is not enough coffee")

# #latte order
# def latte():
#     menu_water = MENU["latte"]["ingredients"]["water"]
#     menu_milk = MENU["latte"]["ingredients"]["milk"]
#     menu_coffee = MENU["latte"]["ingredients"]["coffee"]
#     cost =  float(MENU["latte"]["cost"])
#     current_water = water - menu_water
#     current_milk = milk - menu_milk
#     current_coffee = coffee - menu_coffee
#     current_cost = float(int(money) + cost)
#     if current_water < 0:
#         return(f"Sorry there is not enough water")
#     if current_milk < 0:
#         return(f"Sorry there is not enough milk")
#     if current_coffee < 0:
#         return(f"Sorry there is not enough coffee")
# #cappuccino order
# def cappuccino():
#     menu_water = MENU["cappuccino"]["ingredients"]["water"]
#     menu_milk = MENU["latte"]["ingredients"]["milk"]
#     menu_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
#     cost =  float(MENU["cappuccino"]["cost"])
#     current_water = water - menu_water
#     current_milk = milk - menu_milk
#     current_coffee = coffee - menu_coffee
#     current_cost = float(int(money) + cost)
#     if current_water < 0:
#             return(f"Sorry there is not enough water")
#     if current_milk < 0:
#         return(f"Sorry there is not enough milk")
#     if current_coffee < 0:
#         return(f"Sorry there is not enough coffee")

#total amount
def coins():
    print("Please insert coins.")
    quarters = float(input("How many quarters?\n"))
    dimes = float(input("How many dimes?\n"))
    nickles = float(input("How many nickles?\n"))
    pennies = float(input("How many pennies?\n"))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    final_total = round(total, 1)
    return final_total

#check transaction
def check_transaction(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False

#make coffee
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}, Enjoy!")



    #     change = round(final_total - float(MENU["espresso"]["cost"]), 2)
    #
    #     print(f"Here is your {request}, Enjoy!")
    #     change = round(final_total - float(MENU["latte"]["cost"]), 2)
    #     print(f"Here is ${change} in change")
    #     print(f"Here is your {request}, Enjoy!")
    # if request == "cappuccino" and cappuccino() and final_total > float(MENU["cappuccino"]["cost"]):
    #     change =round (final_total - float(MENU["cappuccino"]["cost"]), 2)
    #     print(f"Here is ${change} in change")
    #     print(f"Here is your {request}, Enjoy!")



# continue
should_continue = True




while should_continue:
#ask user
    request = input("What would you like? (espresso/latte/cappuccino):")
    if request == "off":
        should_continue = False
    elif request == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money} ")
    else:
        drink = MENU[request]
        if check_sufficient(drink["ingredients"]):
            payments = coins()
            if check_transaction(payments, drink["cost"]):
                make_coffee(request, drink["ingredients"])
