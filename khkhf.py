import turtle as t
t.tracer(50)
t.setup(1537,865)
t.bgcolor('black')
t.ht()
color=('red','black')
for i in range(180):
    t.width(10)
    t.pencolor(color[i%2])
    t.circle(700)
    t.rt(2)
    
t.done()    