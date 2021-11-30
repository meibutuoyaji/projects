import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


end = len(names)
random_integer = random.randint(0, end -1)

lucky_person = names[random_integer]

print(lucky_person + "  is going to buy the meal today!")
