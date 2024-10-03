

from turtle import *

speed(0)
bgcolor("skyblue")

penup()
goto(-250, -100)
pendown()

color("black", "gray")
begin_fill()


forward(30)
left(88)
forward(300)
right(88)
forward(50)
right(88)
forward(300)


left(88)
forward(40)
left(90)
forward(100)
right(120)
forward(200)


left(120)
forward(100)
right(120)
forward(200)


right(60)
forward(200)
right(90)
forward(487)
right(90)
forward(200)

end_fill()


penup()
goto(-200, -250)
pendown()

color("black", "white")
begin_fill()
for i in range(4):
    forward(100)
    right(90)
end_fill()


penup()
goto(-50, -250)
pendown()

color("black", "white")
begin_fill()
for i in range(4):
    forward(100)
    right(90)
end_fill()


penup()
goto(100, -250)
pendown()

color("black", "white")
begin_fill()
for i in range(4):
    forward(100)
    right(90)
end_fill()


penup()
goto(-150, 230)
pendown()

color("gray")
begin_fill()
circle(20)
end_fill()

penup()
goto(-120, 250)
pendown()

begin_fill()
circle(25)
end_fill()

penup()
goto(-90, 270)
pendown()

begin_fill()
circle(30)
end_fill()

hideturtle()
