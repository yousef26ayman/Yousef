from turtle import*
speed(1)
width(6)
penup()
goto(160,-100)
pendown()
begin_fill()
color("red")
fillcolor('red')
left(90)
for i in range(2):
    forward(100)
    circle(50,90)
    forward(200)
    circle(50,90)
end_fill()
goto(-20,0)
begin_fill()
fillcolor('black')
color('white')
left(180)
forward(100)
left(120)
forward(100)
left(120)
forward(100)
end_fill()
done()