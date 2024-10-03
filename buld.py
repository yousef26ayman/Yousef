

from turtle import *

speed(0)
bgcolor("black")


penup()
goto(0, 20)
pendown()
color("saddlebrown")
begin_fill()
circle(100)
end_fill()


penup()
goto(-200, -200)
pendown()
begin_fill()
for i in range(2):
    forward(400)
    left(90)
    forward(20)
    left(90)
end_fill()


penup()
goto(-175, -180)
pendown()
color("chocolate")
begin_fill()
for i in range(2):
    forward(350)
    left(90)
    forward(20)
    left(90)
end_fill()


penup()
goto(-150, -160)
pendown()
color("sandybrown")
begin_fill()
for i in range(2):
    forward(300)
    left(90)
    forward(250)
    left(90)
end_fill()


penup()
goto(-175, 90)
pendown()
color("chocolate")
begin_fill()
for i in range(2):
    forward(350)
    left(90)
    forward(20)
    left(90)
end_fill()

penup()
goto(-150, 110)
pendown()
color("sienna")
begin_fill()
for i in range(2):
    forward(300)
    left(90)
    forward(20)
    left(90)
end_fill()


x = -125
y = 30
color("khaki")


def window():
    global x # Ensures that x can be used inside of this function
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    for i in range(4):
        forward(40)
        left(90)
    end_fill()

    x = x + 70 # Moves the next window over 70 steps to the right


for i in range(3): # This loop will draw 3 rows of windows
    for i in range(4): # This loop will draw one row of 4 windows
        window()
    x = -125 # Ensures all rows of windows start from the same x-position
    y = y - 85 # Moves the next row of windows down lower than the previous

hideturtle()
