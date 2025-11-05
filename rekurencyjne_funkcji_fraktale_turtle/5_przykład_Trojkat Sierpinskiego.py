import turtle as zolw

def przesuniecie(zolw, x, y):
    zolw.up()
    zolw.goto(x, y)
    zolw.down()

def rysuj_trojkat(zolw, punkty):
    przesuniecie(zolw, punkty[0][0], punkty[0][1])
    zolw.goto(punkty[1][0], punkty[1][1])
    zolw.goto(punkty[2][0], punkty[2][1])
    zolw.goto(punkty[0][0], punkty[0][1])

def wyznacz_srodek(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(zolw, punkty, stopnie):
    rysuj_trojkat(zolw, punkty)
    if stopnie > 0:
        sierpinski(zolw, (punkty[0], wyznacz_srodek(punkty[0], punkty[1]), wyznacz_srodek(punkty[0], punkty[2])), stopnie - 1)
        sierpinski(zolw, (punkty[1], wyznacz_srodek(punkty[0], punkty[1]), wyznacz_srodek(punkty[1], punkty[2])), stopnie - 1)
        sierpinski(zolw, (punkty[2], wyznacz_srodek(punkty[2], punkty[1]), wyznacz_srodek(punkty[2], punkty[0])), stopnie - 1)

zolw = zolw.Turtle()
zolw.speed(0)

lista_punktow = [[-100, -50], [0, 100], [100, -50]]
sierpinski(zolw, lista_punktow, 3)

#zolw.exitonclick()
#zolw.done()
