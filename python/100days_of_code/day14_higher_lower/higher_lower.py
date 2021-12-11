#import necessary modules
from art import logo, vs
from game_data import data
import random
# print logo
print(logo)

#score starts from zero
score = 0

#flag for loop
should_continue = True

#account b becomes a
account_b = random.choice(data)


#loop
while should_continue:

    #function for random account information

    candidate = random.choice(data)


    def format_data(account):
        """[Takes the account data and returns the printable format.
        """
        candidate_name = candidate["name"]
        candidate_follower_count = candidate["follower_count"]
        candidate_description = candidate["description"]
        candidate_country = candidate["country"]
        return(f"{candidate_name}, {candidate_follower_count}, {candidate_description}, from {candidate_country} ")

    def check_answer(guess, a_follower, b_follower):
        """
        Take the user guess and follower counts and returns if they got it right.
        """
        if a_follower > b_follower:
            return guess == "A"
        else:
            return guess == "B"

    #account

    account_a =  account_b
    account_b =  random.choice(data)


    # print candidate A
    print(f"Compare A: {format_data(account_a)}")

    #VS logo
    print(vs)

    #print candidate B
    print(f"Against B: {format_data(account_b)}")

    #ask user
    guess = input("Who has more followers? Type 'A' or 'B':  ").lower()

    #check if use is correct

    follower_number = candidate["follower_count"]
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower, b_follower)

    #Give user feedback on their guess.
    #Score keeping
    if is_correct:
        score += 1
        print(f"nice. Your score is currently {score}")
    else:
        game_should_continue = False
        print("no. Final score: {score}")
