# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def review():
    print("review")
    print("review")
    print("review")


review()

#functions with inputs

def greet_with_name(name):
    print(f"review {name}")
    print(f"review {name}")
    print(f"review {name}")

greet_with_name("Taka")


#positonal arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"review {location}")

greet_with("Takahiro", "America")

#keyword argument
def greet_with_new(a, b):
    print(f"Hello {a}")
    print(f"review {b}")

greet_with_new(b="location", a="name")
