#from math import *
import math

A = float(input("Podaj A: "))
B = float(input("Podaj B: "))
C = float(input("Podaj C: "))
x0 = float(input("Podaj x0: "))
y0 = float(input("Podaj y0: "))

d = abs(A * x0 + B * y0 + C) / math.sqrt(A**2 + B**2)

print(f"Odległość punktu P od prostej wynosi: {d:.2f}")