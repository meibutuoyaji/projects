############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#import modules

import random
from art import logo

#Ask user to join

user_will = input("Do you want to join Blackjack? Type 'yes' or 'no' ")

should_continue = True
if user_will == 'yes':
    print(logo)
else:
    should_continue = False


#Create a deal_card() function that uses the List below to *return* a random card.
def deal_card():
    """[Returns a random card from the deck.]
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
#Create a function called calculate_score() that takes a List of cards as input

def calculate_score(cards):
    """[Take a list of cards and return the score calculated from the cards]
    """
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0

#Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
#compare function
def compare(your_score, computer_score):
    if your_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"


    if your_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif your_score == 0:
        return "Win with a Blackjack 😎"
    elif your_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif your_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():

    print(logo)

#Deal the user and computer 2 cards each using deal_card() and append().
your_cards = []
computer_cards = []
#set a end variable
is_game_over = False

for _ in range(2): #loop two times
    your_cards.append(deal_card())
    computer_cards.append(deal_card())



#Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
while not is_game_over:
    your_score = calculate_score(your_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {your_cards}, current score: {your_score} ")
    print(f"Computer's first card: {computer_cards[0]}")

    if your_score == 0 or computer_score == 0 or your_score > 21:
        is_game_over = True
    else:
      another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if another_card == "y":
         your_cards.append(deal_card())
      else:
          is_game_over = True
#Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {your_cards}, final score: {your_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(your_score, computer_score))
