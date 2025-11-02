import turtle as Zolw

def Zbior_Cantor(dl, wytnij, n):
    if (n == 0):
        zolw.pd()
        zolw.forward(dl)
        zolw.pu()
    else:
        nowa_dl = dl * (1 - wytnij) / 2
        Zbior_Cantor(nowa_dl, wytnij, n-1)
        zolw.forward(dl * wytnij)
        Zbior_Cantor(nowa_dl, wytnij, n-1)

szerokosc = 600
wysokosc = 400
n = 4

zolw = Zolw.Turtle()
zolw.pu()
zolw.back(szerokosc/2)
zolw.lt(90)
zolw.forward(wysokosc/2)

for i in range(n):
    zolw.rt(90)
    Zbior_Cantor(szerokosc, 1/3, i)
    zolw.back(szerokosc)
    zolw.lt(90)
    zolw.back(wysokosc/(n-1))

Zolw.done()
