#Wczytanie danych

with open("testMaturalistopadoperon2025/przyklad_wielomiany.txt") as f:
    wielomiany = [list(map(int, line.split())) for line in f]


#ZADANIE 2.4

max_n = -1
wynik = []

for w in wielomiany:
    n = w[0]

    if n > max_n:
        max_n = n
        wynik = [w]
    elif n == max_n:
        wynik.append(w)
#Zapis odpowiedzi do pliku

with open("testMaturalistopadoperon2025/wyniki2_4v2.txt", "w") as f:
    f.write("2.4\n")
    for w in wynik:
        f.write(" ".join(map(str, w)) + "\n")