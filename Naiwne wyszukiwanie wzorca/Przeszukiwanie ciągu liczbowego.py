# Szukanie elementu w tablicy
# Funkcja szukaj(T, szukana) zwraca indeks pierwszego wystąpienia elementu szukana

# Liniowe
# implementuje wyszukiwanie liniowe
# la ciągu nieuporządkowanego

def szukaj(T, szukana):
  n = len(T)
  for i in range(n):
    if T[i] == szukana:
      return i
  return -1

T = [1, 2, 3, 4, 5]
szukana = 10
print(szukaj(T, szukana))
print(szukaj([100, 200, 300, 400], 100))
print(szukaj([10, 20, 30, 40, 50, 60, 70], 70))

"""
To jest wyszukiwanie liniowe:
działa dla dowolnej listy (uporządkowanej i nieuporządkowanej),
złożoność czasowa: O(n).

Jeśli lista jest uporządkowana, można użyć wyszukiwania binarnego,
które ma złożoność O(log n) i działa znacznie szybciej dla dużych danych.
"""

# Binarne
#implementację wyszukiwania binarnego (dla listy uporządkowanej rosnąco)

def szukaj_binarne(T, szukana):
    lewy = 0
    prawy = len(T) - 1

    while lewy <= prawy:
        srodek = (lewy + prawy) // 2

        if T[srodek] == szukana:
            return srodek
        elif T[srodek] < szukana:
            lewy = srodek + 1
        else:
            prawy = srodek - 1

    return -1
print(szukaj_binarne([1, 2, 3, 4, 5], 4))  
print(szukaj_binarne([10, 20, 30, 40, 50, 60, 70], 70))  
print(szukaj_binarne([100, 200, 300, 400], 150))
'''
Jak działa algorytm?
Sprawdzamy środkowy element listy.
Jeśli to nie on:
gdy szukana wartość jest większa → szukamy w prawej połowie,
gdy mniejsza → szukamy w lewej połowie.
Za każdym razem odrzucamy połowę elementów.
'''

#Wyszukiwanie binarne — wersja rekurencyjna

def szukaj_binarne_rek(T, szukana, lewy, prawy):
    if lewy > prawy:
        return -1

    srodek = (lewy + prawy) // 2

    if T[srodek] == szukana:
        return srodek
    elif T[srodek] < szukana:
        return szukaj_binarne_rek(T, szukana, srodek + 1, prawy)
    else:
        return szukaj_binarne_rek(T, szukana, lewy, srodek - 1)
    
T = [10, 20, 30, 40, 50, 60, 70]
print(szukaj_binarne_rek(T, 40, 0, len(T)-1))

# Porównanie czasu działania ⏱
import time

def szukaj_liniowe(T, szukana):
    for i in range(len(T)):
        if T[i] == szukana:
            return i
    return -1

def szukaj_binarne(T, szukana):
    lewy = 0
    prawy = len(T) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if T[srodek] == szukana:
            return srodek
        elif T[srodek] < szukana:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return -1


# Duża lista
T = list(range(1_000_000))
szukana = 999_999

# Pomiar liniowego
start = time.time()
szukaj_liniowe(T, szukana)
print("Liniowe:", time.time() - start)

# Pomiar binarnego
start = time.time()
szukaj_binarne(T, szukana)
print("Binarne:", time.time() - start)

"""
Dlaczego taka różnica?
Liniowe sprawdza maksymalnie 1 000 000 elementów
Binarne potrzebuje około:
log2(1 000 000)≈20
Czyli tylko około 20 porównań zamiast miliona!
"""