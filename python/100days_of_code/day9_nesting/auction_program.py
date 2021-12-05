from art import logo
print(logo)

#add name and bid into a dictionary as the key and value
dictionary = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    #bidding_record = {"Taka":123, "James":231}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of $ {highest_bid}")


#ask for name and bid price
while not bidding_finished:
    name = input("What is your name?")
    bid_price = int(input("What is your bid?"))
    dictionary[name] = bid_price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(dictionary)
    elif should_continue == "yes":
        print("Let's keep going!")
