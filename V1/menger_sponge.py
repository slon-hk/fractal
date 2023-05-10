from turtle import *

def gubka():
    # turtle setting
    speed(-1)
    pensize(0.1)
    hideturtle()

    # screen setting
    # If you have another screen, pls change RANDINT setting "goto(randint(***, ***), randint(***, ***))"
    screensize(1920, 1080)

    up()
    forward(530)
    right(90)
    forward(530)
    down()

    def mini_kvadrat():
        tracer(0)
        for i in range(3):
            begin_fill()
            for i in range(3):
                forward(13.08641975308642)
                left(90)
            end_fill()
            left(90)

        for i in range(2):
            forward(13.08641975308642)
            begin_fill()
            for i in range(4):
                forward(13.08641975308642)
                right(90)
            end_fill()

        forward(13.08641975308642)
        right(90)
        forward(13.08641975308642)
        for i in range(2):
            begin_fill()
            for i in range(4):
                forward(13.08641975308642)
                right(90)
            forward(13.08641975308642)
            end_fill()

        right(90)
        forward(13.08641975308642)
        begin_fill()
        for i in range(4):
            forward(13.08641975308642)
            right(90)
        end_fill()

        forward(13.08641975308642)
        forward(13.08641975308642)

    def mini_kvadrat_stor():
        for i in range(3):
            begin_fill()
            for i in range(4):
                right(90)
                forward(13.08641975308642)
            end_fill()
            right(90)
            forward(13.08641975308642)
            left(90)
        right(180)
        forward(13.08641975308642)

        for i in range(2):
            begin_fill()
            for i in range(4):
                forward(13.08641975308642)
                right(90)
            end_fill()
            forward(13.08641975308642)
        right(90)
        forward(13.08641975308642)

        for i in range(2):
            begin_fill()
            for i in range(4):
                forward(13.08641975308642)
                right(90)
            end_fill()
            forward(13.08641975308642)
        right(90)
        forward(13.08641975308642)

        begin_fill()
        for i in range(4):
            forward(13.08641975308642)
            right(90)
        end_fill()

        forward(13.08641975308642)
        forward(13.08641975308642)

    def mal_kvad_niz():
        for i in range(4):
            forward(39.25925925925927)
            left(90)
        forward(39.25925925925927)

    def mal_kvad_niz1():
        for i in range(4):
            forward(39.25925925925927)
            right(90)
        forward(39.25925925925927)

    def mal_kvad_stor():
        for i in range(4):
            forward(39.25925925925927)
            right(90)
        forward(39.25925925925927)

    def sred_kvadrat():
        #контур
        for i in range(4):
            forward(117.7777777777778)
            right(90)

        #мал квадрат
        for i in range(4):
            forward(39.25925925925927)
            right(90)

        #мини квадрат
        def mini_kvadrat_2():
            for i in range(3):
                begin_fill()
                for i in range(4):
                    forward(13.08641975308642)
                    right(90)
                end_fill()
                forward(13.08641975308642)

            right(90)
            forward(13.08641975308642)

            for i in range(2):
                begin_fill()
                for i in range(4):
                    forward(13.08641975308642)
                    right(90)
                end_fill()
                forward(13.08641975308642)

            right(90)
            forward(13.08641975308642)

            for i in range(2):
                begin_fill()
                for i in range(4):
                    forward(13.08641975308642)
                    right(90)
                end_fill()
                forward(13.08641975308642)

            right(90)
            forward(13.08641975308642)

            begin_fill()
            for i in range(4):
                forward(13.08641975308642)
                right(90)
            end_fill()
            forward(13.08641975308642*2)
            right(90)


        for i in range(3):
            mini_kvadrat_2()
            forward(39.25925925925927)
        right(180)
        forward(39.25925925925927)
        left(90)
        forward(39.25925925925927)
        left(90)

        for i in range(2):
            mini_kvadrat_2()
            right(90)
            forward(39.25925925925927)
            left(90)
        right(180)
        forward(39.25925925925927)
        right(90)
        forward(39.25925925925927)
        right(90)

        mini_kvadrat_2()
        right(180)
        forward(39.25925925925927)
        right(180)
        mini_kvadrat_2()
        left(90)
        forward(39.25925925925927)
        right(90)
        mini_kvadrat_2()

        left(90)
        forward(39.25925925925927)
        right(90)
        forward(117.7777777777778)

    #Большой квадрат
    for i in range(4):
        right(90)
        forward(1060)
        right(90)
        forward(1060)

    #Маленький квадрат низ
    right(180)
    for i in range(3):
        forward(39.25925925925927)
        left(90)
    mini_kvadrat()
    right(90)
    forward(39.25925925925927)
    left(90)
    for i in range(26):
        mal_kvad_niz()
        left(90)
        forward(39.25925925925927)
        left(90)
        mini_kvadrat()
        right(90)
        forward(39.25925925925927)
        left(90)

    #Маленький квадрат лево
    right(90)
    for i in range(26):
        mal_kvad_stor()
        mini_kvadrat_stor()

    #Маленький квадрат верх
    right(90)
    for i in range(26):
        mal_kvad_stor()
        mini_kvadrat_stor()

    #Маленький квадрат право
    for i in range(26):
        mal_kvad_stor()
        mini_kvadrat_stor()
        right(180)
        forward(39.25925925925927)
        left(90)
        forward(39.25925925925927)
        left(90)

    # 2 ряд низ
    left(180)
    for i in range(12):
        forward(39.25925925925927)
        mal_kvad_niz1()
        mini_kvadrat_stor()
        left(90)
        forward(39.25925925925927)
        left(90)
        mini_kvadrat()
        right(90)
        forward(39.25925925925927)
        left(90)

    forward(39.25925925925927)
    right(90)
    forward(39.25925925925927)

    #2 ряд лево
    for i in range(12):
        mal_kvad_stor()
        mini_kvadrat_stor()
        forward(39.25925925925927)

    #2 ряд верх
    right(90)
    for i in range(12):
        forward(39.25925925925927)
        mal_kvad_stor()
        mini_kvadrat_stor()

    #2 ряд право
    for i in range(12):
        right(90)
        forward(39.25925925925927)
        left(90)
        mal_kvad_stor()
        mini_kvadrat_stor()
        right(180)
        forward(39.25925925925927)
        left(90)
        forward(39.25925925925927)
        left(90)

    #3 ряд низ
    left(90)
    for i in range(3):
        forward(39.25925925925927)
        left(90)
    mini_kvadrat()
    right(90)
    forward(39.25925925925927)
    left(90)
    for i in range(22):
        mal_kvad_niz()
        left(90)
        forward(39.25925925925927)
        left(90)
        mini_kvadrat()
        right(90)
        forward(39.25925925925927)
        left(90)

    #3 ряд лево
    right(90)
    for i in range(22):
        mal_kvad_stor()
        mini_kvadrat_stor()

    #3 ряд верх
    right(90)
    for i in range(23):
        mal_kvad_stor()
        mini_kvadrat_stor()

    #3 ряд право
    right(180)
    forward(39.25925925925927)
    right(180)
    for i in range(22):
        mal_kvad_stor()
        mini_kvadrat_stor()
        right(180)
        forward(39.25925925925927)
        left(90)
        forward(39.25925925925927)
        left(90)

    right(180)
    forward(117.7777777777778)

    #средний квадрат низ
    for i in range(3):
        sred_kvadrat()
        forward(117.7777777777778)

    #средний квадрат лево
    right(180)
    forward(117.7777777777778)
    left(90)
    forward(117.7777777777778)
    left(90)
    for i in range(3):
        sred_kvadrat()
        right(180)
        forward(117.7777777777778)
        left(90)
        forward(117.7777777777778)
        left(90)
        right(90)
        forward(117.7777777777778)
        left(90)

    #средний квадрат верх
    right(180)
    for i in range(2):
        forward(117.7777777777778)
        right(90)

    for i in range(3):
        sred_kvadrat()
        right(180)
        forward(117.7777777777778*3)
        right(180)

    #средний квадрат право
    left(90)
    forward(117.7777777777778)
    right(90)
    forward(117.7777777777778)

    for i in range(3):
        sred_kvadrat()
        left(90)
        forward(117.7777777777778*2)
        left(90)
        forward(117.7777777777778)
        left(180)

    #центр низ
    forward(117.7777777777778)
    right(90)
    forward(117.7777777777778*2)
    left(90)
    for i in range(5):
        sred_kvadrat()

    #центр лево
    right(180)
    forward(117.7777777777778)
    left(90)
    forward(117.7777777777778)
    left(90)
    for i in range(4):
        sred_kvadrat()
        right(180)
        forward(117.7777777777778)
        left(90)
        forward(117.7777777777778)
        left(90)

    #центр верх
    for i in range(2):
        left(90)
        forward(117.7777777777778)
    right(180)

    for i in range(4):
        sred_kvadrat()
        right(180)
        forward(117.7777777777778*2)
        right(180)

    #центр право
    for i in range(2):
        forward(117.7777777777778)
        left(90)
    left(180)

    for i in range(3):
        sred_kvadrat()
        right(180)
        forward(117.7777777777778)
        right(90)
        forward(117.7777777777778)
        right(90)

    update()
    done()

if __name__ == "__main__":
    gubka()
