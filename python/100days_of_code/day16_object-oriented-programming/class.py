# # import modules

# # print(modules.variable)

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)

# my_screen = Screen()
# print(my_screen.canvwidth)

# my_screen.exitonclick()


# timmy.color("coral")

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu"])
table.align = "l"



print(table)
