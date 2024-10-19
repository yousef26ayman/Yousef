import  tkinter as tk
from tkinter import *
import math


def fresh():
    answer.delete(1.0,END)


class calculation:

    def circleMethod():
        global radius
        valueFrame1 = Frame(root)
        value = Label(valueFrame1,text="Enter value of radius:")
        value.grid(row=0,column=0)
        radius = Entry(valueFrame1)
        radius.grid(row=0,column=1,pady=5,ipadx=5)
        valueFrame1.pack(side=TOP,pady=5,padx=5,ipadx=5)
        result= Button(valueFrame1,text="Get Answer!",bg="green",command=calculation.C_area)
        result.grid(row=0,column=2)
        circle.config(state=DISABLED)

    #====================SQAURE METHOD
    def squareMethod():
        global side
        valueFrame1 = Frame(root)
        value = Label(valueFrame1, text="Enter value of side:")
        value.grid(row=0, column=0)
        side = Entry(valueFrame1)
        side.grid(row=0, column=1, pady=5, ipadx=5)
        valueFrame1.pack(side=TOP, pady=5, padx=5, ipadx=5)
        result = Button(valueFrame1, text="Get Answer!", bg="green",command=calculation.S_area)
        result.grid(row=0, column=2)
        square.config(state=DISABLED)

    # ======================Recatngle Method
    def rectangleMethod():
        global length , breadth
        valueFrame = Frame(root)
        value = Label(valueFrame,text="Length:  ")
        value.grid(row=0, column=0)
        length = Entry(valueFrame)
        length.grid(row=0,column=1,pady=5)
        value = Label(valueFrame, text="Breadth:  ")
        value.grid(row=0, column=2)
        breadth = Entry(valueFrame)
        breadth.grid(row=0, column=3, pady=5)
        result = Button(valueFrame, text="Get Answer!", bg="green", command=calculation.R_area)
        result.grid(row=0, column=4)
        valueFrame.pack(side=TOP,pady=5,padx=5,ipadx=5)
        rectangle.config(state=DISABLED)

    def triangleMethod():
        global side1, side2, side3
        valueFrame = Frame(root)
        value =Label(valueFrame,text= "Side1 :")
        value.grid(row=0,column=0)
        side1 = Entry(valueFrame)
        side1.grid(row=0,column=1)
        value = Label(valueFrame, text="Side2 :")
        value.grid(row=0, column=2)
        side2 = Entry(valueFrame)
        side2.grid(row=0, column=3)
        value = Label(valueFrame, text="Side3 :")
        value.grid(row=0, column=4)
        side3 = Entry(valueFrame)
        side3.grid(row=0, column=5)
        result = Button(valueFrame, text="Get Answer!", bg="green", command=calculation.T_area)
        result.grid(row=0, column=6)
        valueFrame.pack(side=TOP, pady=5, padx=5, ipadx=5)
        triangle.config(state=DISABLED)
    #==========================Area of circle
    def C_area():
        pi = 3.14
        r = radius.get()
        answer.delete(1.0,END)
        areaOfCircle = pi*float(r)*float(r)
        answer.insert(INSERT,"Area of Circle = Pi*r^2\n => 22/7*r^2\n 3.14 X ")
        answer.insert(INSERT, r)
        answer.insert(INSERT, " X ")
        answer.insert(INSERT, r)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT,areaOfCircle)
        answer.insert(INSERT, "Ans.")


    #==================Area of square
    def S_area():
        s = side.get()
        answer.delete(1.0,END)
        areaOfSquare = float(s)*float(s)
        answer.insert(INSERT,"Area of Square = *r^2\n => ")
        answer.insert(INSERT, s)
        answer.insert(INSERT, " X ")
        answer.insert(INSERT, s)
        answer.insert(INSERT, " = ")
        answer.insert(INSERT,areaOfSquare)
        answer.insert(INSERT, "Ans.")

    #=========================rectangle area
    def R_area():
        l = length.get()
        b = breadth.get()

        areaofRectangle = float(l)*float(b)
        answer.delete(1.0,END)
        answer.insert(INSERT,"Area of rectangle = \n => LENGTH x BREATH\n=> ")
        answer.insert(INSERT, l)
        answer.insert(INSERT, " X ")
        answer.insert(INSERT, b)
        answer.insert(INSERT," = ")
        answer.insert(INSERT,areaofRectangle)
        answer.insert(INSERT,"  Ans.")

    #================triangle area
    def T_area():
        s1 = side1.get()
        s2 = side2.get()
        s3 = side3.get()
        s = 1/2*(float(s1)+float(s2)+float(s3))
        areaOfTriangle = math.sqrt(s*(s-float(s1))*(s-float(s2))*(s-float(s3)))
        answer.delete(1.0,END)
        answer.insert(INSERT,"S = 1/2(a+b+c)\n=>")
        answer.insert(INSERT, s)
        answer.insert(INSERT, "\nArea Of Triangle =\n=> "
                              "sqrt(s(s-a)(s-b)(s-c))\n=>")
        answer.insert(INSERT, areaOfTriangle)
        answer.insert(INSERT, " Ans.")

root = tk.Tk()
root.title("Area App")

frame1 = Frame(root)
title =  Label(frame1,text="Calculate Area of Different Shapes",font=("arial",20,"bold"),fg="red")
title.grid(row=0,column=0)
choice = Label(frame1,text="What shape do you have?",font=("arial",10,),fg="blue")
choice.grid(row=1,column=0)
refresh = Button(frame1,text="Clear All",bg="red",fg="black",command=fresh)
refresh.grid(row=1,column=2)
frame1.pack(side=TOP,pady=10,padx=5,ipadx=5)

frame2= Frame(root)
circle = Button(frame2,font=("calibri",15),text="Circle",bg="POWDER BLUE",command=calculation.circleMethod)
circle.grid(row=0,column=0)
square = Button(frame2,font=("calibri",15),text="Square",bg="BROWN",command=calculation.squareMethod)
square.grid(row=0,column=1)
rectangle = Button(frame2,font=("calibri",15),text="Rectangle",bg="POWDER BLUE",command=calculation.rectangleMethod)
rectangle.grid(row=0,column=2)
triangle = Button(frame2,font=("calibri",15),text="Triangle",bg="BROWN",command= calculation.triangleMethod)
triangle.grid(row=0,column=3)
frame2.pack(side=TOP)

frame3 = Frame(root,bg="blue")
answer = Text(frame3,height=10,wrap=WORD)
answer.grid(padx=5,ipadx=5,pady=5,ipady=5)
frame3.pack(side=BOTTOM)
mainloop()