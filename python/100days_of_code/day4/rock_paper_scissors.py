

user_choice = input("Type 0 for Rock, 1 for Paper or 2 for Scissors.")

import random

computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")

if int(user_choice) >= 3 or int(user_choice) < 0:
    print("You have entered invalid value")
elif computer_choice == 2 and int(user_choice) == 0:
    print("User wins")
elif computer_choice == 0 and int(user_choice) == 2:
    print("Computer wins")
elif computer_choice > int(user_choice):
    print("Computer wins")
elif int(user_choice) > computer_choice:
    print("User wins")
elif computer_choice == int(user_choice):
    print("draw")
