from turtle import *

turtle = Turtle()

turtle.speed(0)
turtle.left(90)
turtle.forward(10)

for i, colour in zip(range(10), 50 * ["blue", "red"]):
    turtle.color(colour)
    fillcolor('yellow')
    turtle.forward(500 + i)
    turtle.left(120 + i)
