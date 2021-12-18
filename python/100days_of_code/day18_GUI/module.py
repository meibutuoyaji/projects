from turtle import Turtle, Screen
import turtle

#moving forward

screen = Screen

tur = turtle.Turtle()
tur.fillcolor("red")

tur.forward(100)
tur.bicolor("orange")
#draw line between two points

x = (10, 140)
y = (100, 240)

tur.penup()
tur.goto(x)
tur.pendown()
tur.goto(y)
