from turtle import Turtle,Screen
import random 
s = Screen()
s.bgcolor("black")
t = Turtle()
t.speed(2)



colors =[
    
    "red","green","cyan","maroon","lime","magenta","yellow","violet","orange","violet","gray","white" 
    
]
angle = [0,90,180,270]
t.pensize(15)
t.speed("fastest")
for i in range(200):
    t.color(random.choice(colors))
    t.setheading(random.choice(angle))
    t.fd(30)