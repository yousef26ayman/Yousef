from turtle import *

speed(0)
bgcolor('lightgray')
title('Fidget Spinner Game')

spinner_radius = 250  # Increased radius
spinner_speed = 0
spinner_colors = ['red', 'green', 'blue']

def create_spinner():
    penup()
    goto(0, 0)  # Center the spinner
    pendown()

    for color in spinner_colors:
        fillcolor(color)
        begin_fill()
        circle(spinner_radius/len(spinner_colors))
        end_fill()
        right(360 / len(spinner_colors))

def spin_spinner(x, y):
    global spinner_speed
    spinner_speed += 10

def stop_spinner(x, y):
    global spinner_speed
    spinner_speed = max(0, spinner_speed - 5)

def animate_spinner():
    global spinner_speed
    clear()
    create_spinner()
    right(spinner_speed)
    update()
    ontimer(animate_spinner, 20)

def main():
    setup(600, 600)
    hideturtle()
    tracer(False)
    
    create_spinner()

    onscreenclick(spin_spinner, 1)
    onscreenclick(stop_spinner, 3)

    animate_spinner()

    done()

if __name__ == "__main__":
    main()