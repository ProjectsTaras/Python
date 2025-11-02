import turtle

t = turtle.Turtle()
t.speed(0)
t.left(90)  # żółw patrzy w górę

def drzewo(dlugosc):
    if dlugosc < 10:
        return
    t.forward(dlugosc)
    t.left(30)
    drzewo(dlugosc - 10)
    t.right(60)
    drzewo(dlugosc - 10)
    t.left(30)
    t.backward(dlugosc)

drzewo(60)
turtle.done()