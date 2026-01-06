# zadanie 2.5 – Python
# import os
# print(os.getcwd())
# 1. Wczytanie danych
with open("testMaturalistopadoperon2025\przyklad_wielomiany.txt", "r") as f:
    lines = f.readlines()

wielomiany = []
for line in lines:
    w = list(map(int, line.strip().split()))
    wielomiany.append(w)

# 2. Funkcja obliczająca wartość wielomianu dla x = 2
def wartosc_wielomianu(w, x):
    n = w[0]
    wsp = w[1:]
    wynik = 0
    for i in range(n + 1):
        wynik += wsp[i] * (x ** (n - i))
    return wynik

# 3. Sprawdzenie, czy liczba należy do ciągu Fibonacciego
def czy_fibonacci(k):
    if k < 0:
        return False
    a, b = 0, 1
    while a < k:
        a, b = b, a + b
    return a == k

# 4. Szukanie poprawnych wielomianów
wynikowe = []

for w in wielomiany:
    val = wartosc_wielomianu(w, 2)
    if czy_fibonacci(val):
        wynikowe.append(w)

# 5. Dopisanie odpowiedzi do pliku wyniki2.txt
with open("testMaturalistopadoperon2025\wyniki2_5.txt", "a") as f:
    f.write("2.5\n")
    for w in wynikowe:
        f.write(" ".join(map(str, w)) + "\n")
