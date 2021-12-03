print("Welcome to Treasure Island. Your mission is to find the treasure. ")

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n ')
lower_choice1 = choice1.lower()

if lower_choice1 == "left":

    choice2 = input('You\'re in front of swamp, where do you want to go? Type "swim" or "wait".\n ')
    lower_choice2 = choice2.lower()
    if lower_choice2 == "wait":

        choice3 = input('You\'re in front of door, where do you want to go? Type "red" or "blue" or "yellow".\n ')
        lower_choice3 = choice3.lower()
        if lower_choice3 == "red":
            print("Burned by fire")

        if lower_choice3 == "yellow":
            print("You are winner")

        else:
            print("Game over")

    else:
        print("Game over.")

else:
    print("Game over.")
