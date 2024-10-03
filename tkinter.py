import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mbox

win = tk.Tk()

win.title("Window")



win.geometry('300x300')

def press(event):
    print('you pressed the button')
    
def exit_win():
    ans = mbox.askyesno('Exit','Are you sure?')
    if ans:
        win.destroy()
        
button = ttk.Button(win,text='Press')       
button.bind('<Button-1>',press)
button.bind('<Return>',press)   
button.bind('<Control_L>e',press) 


button_exit = ttk.Button(win,text='Exit',command=exit_win)

button.pack()
button_exit.pack()
#
label = ttk.Label(win,text="Hello World")

label.pack()

win.mainloop()