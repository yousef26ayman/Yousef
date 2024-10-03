
from turtle import *
from random import *
import turtle
import time


setup(800, 500)
title("Turtle Race")
bgcolor("forestgreen")
speed(0)


penup()
goto(-100, 205)
color("white")
write("TURTLE RACE", font=("Arial", 20, "bold"))


goto(-350, 200)
pendown()
color("chocolate")
begin_fill()
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()


gap_size = 20
shape("square")
penup()


color("white")
for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()


for i in range(10):
    goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
    stamp()


color("black")
for i in range(10):
    goto(250, (190 - (i * gap_size * 2)))
    stamp()


for i in range(10):
    goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
    stamp()
    

blue_turtle = Turtle()
blue_turtle.color("cyan")
blue_turtle.shape("turtle")
blue_turtle.shapesize(1.5)
blue_turtle.penup()
blue_turtle.goto(-300, 150)
blue_turtle.pendown()
    

pink_turtle = Turtle()
pink_turtle.color("magenta")
pink_turtle.shape("turtle")
pink_turtle.shapesize(1.5)
pink_turtle.penup()
pink_turtle.goto(-300, 50)
pink_turtle.pendown()    
    

yellow_turtle = Turtle()
yellow_turtle.color("yellow")
yellow_turtle.shape("turtle")
yellow_turtle.shapesize(1.5)
yellow_turtle.penup()
yellow_turtle.goto(-300, -50)
yellow_turtle.pendown()    
  

green_turtle = Turtle()
green_turtle.color("lime")
green_turtle.shape("turtle")
green_turtle.shapesize(1.5)
green_turtle.penup()
green_turtle.goto(-300, -150)
green_turtle.pendown()    


time.sleep(1)



