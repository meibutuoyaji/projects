
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        FizzBuzz = number
        print("FizzBuzz")
    elif number % 5 == 0:
        Buzz = number
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
