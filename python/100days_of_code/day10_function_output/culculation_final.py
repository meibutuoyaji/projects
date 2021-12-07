from art import logo

#add
def add(n1, n2):
    return n1 + n2
#substract
def subtract(n1, n2):
    return n1 - n2
#multiply
def multiply(n1, n2):
    return n1 * n2
#divide
def divide(n1, n2):
    return n1 / n2

operations = {

    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    num1 = float(input("what's the first number?:"))

    for symbol in operations:
        print(symbol)


    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above")
        num2 = float(input("what's the second number?:"))
        culculation_function = operations[operation_symbol]
        answer = culculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        should_continue = input("Do you want to continue? Type 'yes' or 'no' ")
        if should_continue == "yes":
            num1 = answer
        else:
            should_continue = False

calculator()
