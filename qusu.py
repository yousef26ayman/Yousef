from turtle import *

fave_colour = input("What is your favourite colour: ")

color(fave_colour)
begin_fill()
for i in range(4):
    forward(200)
    right(90)
end_fill()

hideturtle()
