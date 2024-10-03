import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Analog Clock game yousef ayman")
wn.tracer(0)



pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.hideturtle()



def draw_clock(h, m, s):
    global pen

    pen.penup()
    pen.pensize(15)
    pen.setposition(0, 210)
    pen.setheading(180)  
    pen.color("#142164", "#F6F6F6")
    pen.pendown()
    pen.begin_fill()
    pen.circle(210)
    pen.end_fill()

  
    pen.penup()
    pen.setposition(0, 0)
    pen.setheading(90)
    for _ in range(12):
        pen.forward(210)
        pen.pendown()
        pen.backward(20)
        pen.penup()
        pen.setposition(0, 0)
        pen.right(360 / 12)

   
    pen.color("#D92531")
    pen.pensize(12)
    pen.penup()
   
    angle = (h / 12) * 360
    pen.setheading(90)
    pen.right(angle)  
    pen.pendown()
    pen.forward(100)

  
    pen.color("#4A9609")
    pen.pensize(10)
    pen.penup()
    pen.setposition(0, 0)
    
    angle = (m / 60) * 360
    pen.setheading(90)
    pen.right(angle) 
    pen.pendown()
    pen.forward(150)

    
    pen.color("#142164")
    pen.pensize(4)
    pen.penup()
    pen.setposition(0, 0)
    
    angle = (s / 60) * 360
    pen.setheading(90)
    pen.right(angle)  
    pen.pendown()
    pen.forward(170)


while True:
    h = int(time.strftime("%I"))  
    m = int(time.strftime("%M"))  
    s = int(time.strftime("%S"))  

   
    pen.clear()
    time.sleep(1)
    draw_clock(h, m, s)
    wn.update()   
    wn.mainloop()
