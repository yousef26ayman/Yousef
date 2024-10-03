from turtle import *
import colorsys

bgcolor('black')
tracer(40)
h=0


for i in range(400):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    begin_fill()
    forward(i)
    left(19)
    backward(i*0.5)
    circle(i*0.1,180)
    end_fill()
    h += 0.0