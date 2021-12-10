import random
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")

#ramdom number from 1 and 100
numbers = random.randint(1, 100)

#Difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' :")

#define attempts
end_of_attempts = False
should_continue = True

#function
def check_answer_easy(user_guess, numbers):
 while not end_of_attempts:
            attempts_left = 10
            for guess in range(10):
                print(f"You have {attempts_left} attempts remaining to guess the number ")
                user_guess = int(input("Make a guess"))
                if user_guess == numbers:
                    print("You have got the right one!!")
                    end_of_attempts = True
                else:
                    if user_guess > numbers:
                        print("Too high")
                    elif user_guess < numbers:
                        print("Too low")
                        print(f"guess again")
                    attempts_left -= 1
                    if attempts_left == 0:
                        end_of_attempts = True
                        print("You lose.")

def check_answer_hard(user_guess, numbers):
    while not end_of_attempts:
                attempts_left = 5
                for guess in range(5):
                    print(f"You have {attempts_left} attempts remaining to guess the number ")
                    user_guess = int(input("Make a guess"))
                    if user_guess == numbers:
                        end_of_attempts = True
                    else:
                        if user_guess > numbers:
                            print("Too high")
                        elif user_guess < numbers:
                            print("Too low")
                            print(f"guess again")
                        attempts_left -= 1
                        if attempts_left == 0:
                            end_of_attempts = True
                            print("You lose.")


#Loop
while should_continue:
    if difficulty == "easy":
        check_answer_easy()
    elif difficulty == "hard":
        check_answer_hard()
    else:
        user_choice = input("Please type 'y' to continue 'n' to quit")
        if user_choice == "n":
            should_continue = False
