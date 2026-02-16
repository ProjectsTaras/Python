# Otwieramy plik wielomiany.txt i wczytujemy wszystkie wiersze jako listy liczb całkowitych

with open("testMaturalistopadoperon2025/przyklad_wielomiany.txt") as f:
    wielomiany = [list(map(int, line.split())) for line in f]


#ZADANIE 2.4
# Szukamy największego stopnia wielomianu

max_n = -1
wynik = []

for w in wielomiany:
    n = w[0]  # pierwszy element to stopień wielomianu

    if n > max_n:
        max_n = n
        wynik = [w] # nowa lista z aktualnie największym stopniem
    elif n == max_n:
        wynik.append(w) # dodajemy jeśli taki sam stopień
#Zapis odpowiedzi do pliku

with open("testMaturalistopadoperon2025/wyniki2_4v2.txt", "w") as f:
    f.write("2.4\n")
    for w in wynik:
        f.write(" ".join(map(str, w)) + "\n")