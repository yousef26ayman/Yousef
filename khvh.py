import turtle
t = turtle. Turtle()
turtle.bgcolor('cyan')
t.pensize(3)
t.speed(15)
r = 30
for i in range(100):
    t.circle(r)
    t.right(90)
    r += 5
turtle.done()