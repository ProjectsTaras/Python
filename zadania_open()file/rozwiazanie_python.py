# Program czyta imiona z pliku names.txt, liczy wystąpienia wybranego imienia
# i zapisuje wynik do pliku wynik.txt.

from collections import Counter

# Ustaw swoje imię i imię sąsiada
my_name = "Franciszek"
neighbor_name = "Hubert"

# Wczytanie imion z pliku
with open("zadania_open()file/names.txt", "r", encoding="utf-8") as file:
    names = [line.strip() for line in file if line.strip()]

# Zliczanie wystąpień każdego imienia
counts = Counter(names)
my_count = counts.get(my_name, 0)
neighbor_count = counts.get(neighbor_name, 0)

# Zapis wyniku
with open("wynik.txt", "w", encoding="utf-8") as out:
    out.write(f"Moje imię: {my_name}\n")
    out.write(f"Liczba wystąpień: {my_count}\n")
    out.write("Imię sąsiada powtórzone:\n")

    # Wpisujemy imię sąsiada tyle razy, ile razy występuje w pliku
    for _ in range(neighbor_count):
        out.write(f"{neighbor_name}\n")

print("Gotowe. Wynik zapisano w pliku wynik.txt")
