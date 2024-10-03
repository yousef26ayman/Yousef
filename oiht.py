from turtle import *
import colorsys
bgcolor('black')
pensize (5)
speed (0)
h=0
for i in range(800):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.90
    pencolor(c)
    up()
    down()
    goto (0,0)
    fd(i)
    rt(89)
    circle(i/4,70)
done()













