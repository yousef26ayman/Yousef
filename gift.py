from turtle import *

speed(0)


penup()
goto(0, -300)
pendown()
color("green")
begin_fill()
circle(300)
end_fill()


penup()
goto(-180, 20)
pendown()
color("red")
begin_fill()
for i in range(2):
    forward(360)
    left(90)
    forward(60)
    left(90)
end_fill()


penup()
goto(-160, 0)
pendown()
begin_fill()
for i in range(2):
    forward(320)
    right(90)
    forward(210)
    right(90)
end_fill()


penup()
goto(-10, 80)
pendown()
color("green")
begin_fill()
for i in range(2):
    forward(20)
    right(90)
    forward(290)
    right(90)
end_fill()


penup()
goto(10, 100)
pendown()
pensize(10)
color("red")
for i in range(90):
    forward(1)
    left(0.4)
for i in range(90):
    forward(1)
    left(2)
for i in range(90):
    forward(1)
    left(0.4)




penup()
goto(-10, 100)
pendown()
right(70)
for i in range(90):
    forward(1)
    right(0.4)
for i in range(90):
    forward(1)
    right(2)
for i in range(90):
    forward(1)
    right(0.4)


penup()
goto(-160, 210)
pendown()
color("white")
write("SEASONS GREETINGS", font=("Arial", 22, "bold"))

hideturtle()