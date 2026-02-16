# Obliczanie wartości wielomianu dla x=2 schematem Hornera
def wartosc_wielomianu(w, x):
    n = w[0]
    wsp = w[1:]
    wynik = wsp[0]

    for i in range(1, n + 1):
        wynik = wynik * x + wsp[i]

    return wynik


# Sprawdzanie czy liczba należy do ciągu Fibonacciego
def czy_fibonacci(k):
    if k < 0:
        return False
    a, b = 0, 1
    while a < k:
        a, b = b, a + b
    return a == k


wynik_25 = []

for w in wielomiany:
    val = wartosc_wielomianu(w, 2)
    if czy_fibonacci(val):
        wynik_25.append(w)

# Zapis do pliku
with open("wyniki2_5.txt", "w") as f:
    f.write("2.5\n")
    for w in wynik_25:
        f.write(" ".join(map(str, w)) + "\n")