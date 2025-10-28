import math

print("podaj wspolczynnik A prostej", end=" ")

A = float(input())

print("podaj wspolczynnik B prostej", end=" ")

B = float(input())

print("podaj wspolczynnik C prostej", end=" ")

C = float(input())

print("podaj wspolrzedna x punktu A", end=" ")

xa = float(input())

print("podaj wspolrzedna y punktu A", end=" ")

ya = float(input())

print("podaj wspolrzedna x punktu B", end=" ")

xb = float(input())

print("podaj wspolrzedna y punktu B", end=" ")

yb = float(input())

lezy = A*xa + B*ya + C
lezy2 = A*xb + B*yb + C

if lezy == 0 and lezy2 == 0:
    print("odcinek lezy na prostej")

else:
    print("odcinek nie lezy na prostej")
