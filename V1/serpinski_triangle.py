from turtle import *
from random import randint
tracer(0)
def triangle():
    #A = 1 or 2
    #B = 3 or 4
    #C = 5 or 6

    #turtle setting
    title("serpinski triangle")
    up()
    hideturtle()
    speed(0)
    pensize(0.1)

    #screen setting
    #If you have another screen, pls change RANDINT setting "goto(randint(***, ***), randint(***, ***))"
    screensize(1920, 1080)


    home()
    goto(randint(-950, 950), randint(-530, 530))
    a_x = xcor()
    a_y = ycor()
    write("A")
    dot()

    home()
    goto(randint(-950, 950), randint(-530, 530))
    b_x = xcor()
    b_y = ycor()
    write("B")
    dot()

    home()
    goto(randint(-950, 950), randint(-530, 530))
    c_x = xcor()
    c_y = ycor()
    write("C")
    dot()

    home()
    goto(randint(-950, 950), randint(-530, 530))
    d_x = xcor()
    d_y = ycor()
    write("D")
    dot()

    while True:
        x = randint(1, 6)
        if x == 1 or x == 2:
            dis = distance(a_x, a_y)
            tow = towards(a_x, a_y)
            setheading(tow)
            forward(dis//2)
            dot()

        elif x == 3 or x ==4:
            dis = distance(b_x, b_y)
            tow = towards(b_x, b_y)
            setheading(tow)
            forward(dis//2)
            dot()

        elif x == 5 or x ==6:
            dis = distance(c_x, c_y)
            tow = towards(c_x, c_y)
            setheading(tow)
            forward(dis//2)
            dot()
        update()

    done()

if __name__ == "__main__":
    triangle()
