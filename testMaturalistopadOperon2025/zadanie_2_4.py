# zadanie 2.4 – Python

# 1. Czytanie danych z pliku
with open("testMaturalistopadoperon2025\przyklad_wielomiany.txt", "r") as f:
    lines = f.readlines()

wielomiany = []

for line in lines:
    numbers = list(map(int, line.strip().split()))
    n = numbers[0]
    wielomiany.append(numbers)

# 2. Obliczanie różnicy liczby mnożeń
def roznica_mnozen(n):
    return n * (n - 1) // 2

max_roznica = -1
wynikowe_wielomiany = []

for w in wielomiany:
    n = w[0]
    r = roznica_mnozen(n)

    if r > max_roznica:
        max_roznica = r
        wynikowe_wielomiany = [w]
    elif r == max_roznica:
        wynikowe_wielomiany.append(w)

# 3. Zapis odpowiedzi do pliku wyniki2.txt
with open("testMaturalistopadoperon2025\wyniki2_4.txt", "w") as f:
    f.write("2.4\n")
    for w in wynikowe_wielomiany:
        f.write(" ".join(map(str, w)) + "\n")
