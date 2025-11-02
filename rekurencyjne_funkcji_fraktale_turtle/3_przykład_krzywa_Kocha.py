import turtle

t = turtle.Turtle()
t.speed(0)

def koch(dlugosc, poziom):
    if poziom == 0:
        t.forward(dlugosc)
    else:
        dlugosc /= 3.0
        koch(dlugosc, poziom - 1)
        t.left(60)
        koch(dlugosc, poziom - 1)
        t.right(120)
        koch(dlugosc, poziom - 1)
        t.left(60)
        koch(dlugosc, poziom - 1)

t.penup()
t.goto(-150, 0)
t.pendown()
koch(300, 3)

turtle.done()
