import turtle
from turtle import Turtle

tim = Turtle()

for _ in range(4):
    tim.forward(100)
    tim.left(90)

screen = turtle.Screen()
screen.exitonclick()