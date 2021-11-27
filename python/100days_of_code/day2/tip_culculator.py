print("Welcome to the tip calculator")

bill = input("what was the total bill?")

bill_float = float(bill)

tip = input("How much tip would you like to give? 10, 12 or 15?")

tip_int = int(tip)

people = input("How many people to split the bill?")

people_int = int(people)

tip_percent = tip_int / 100

total_tip_amount = bill_float * tip_percent

total_bill = bill_float + total_tip_amount

bill_per_person = total_bill / people_int

final_amount = "{:.2f}".format(bill_per_person)

print("Each person should pay " + str(final_amount))
