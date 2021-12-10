#Global scope
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

##Local scope

def drink_position():
    potion_strength = 2
    print(potion_strength)

#drink_position()
#print(potion_strength)


display = 7
for _ in range(7):
    display = - 1
    print(display)
