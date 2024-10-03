from turtle import *

setup(800, 500)
bgcolor("#01411C")
speed(0)


penup()
goto(-400, 250)
pendown()
color("white")
begin_fill()
for i in range(2):
    forward(200)
    right(90)
    forward(500)
    right(90)
end_fill()


penup()
goto(50, -135)
pendown()
begin_fill()
circle(150)
end_fill()

penup()
goto(90, -80)
pendown()
color("#01411C")
begin_fill()
circle(130)
end_fill()


penup()
goto(110, 90)
pendown()
color("white")
begin_fill()
for i in range(5):
    forward(90)
    left(144)
end_fill()

hideturtle()