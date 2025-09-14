A = float(input("Podaj A: "))
B = float(input("Podaj B: "))
C = float(input("Podaj C: "))

xA = float(input("Podaj xA: "))
yA = float(input("Podaj yA: "))
xB = float(input("Podaj xB: "))
yB = float(input("Podaj yB: "))

# Sprawdzenie
warunekA = A * xA + B * yA + C
warunekB = A * xB + B * yB + C

if warunekA == 0 and warunekB == 0:
    print("Odcinek |AB| leży na prostej.")
else:
    print("Odcinek |AB| NIE leży na prostej.")

#okokok