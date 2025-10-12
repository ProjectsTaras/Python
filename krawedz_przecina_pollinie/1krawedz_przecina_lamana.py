def krawedz_przecina_lamana(x, y, x0, y0, x1, y1):
    # Uporządkuj wierzchołki tak, by y0 <= y1 (łatwiej sprawdzać)
    if y0 > y1:
        x0, y0, x1, y1 = x1, y1, x0, y0

    # 1. Odrzucamy odcinki leżące całkiem powyżej lub poniżej
    if y < y0 or y > y1:
        return 0

    # 2. Specjalny przypadek: półprosta przechodzi przez wierzchołek
    if y == y1:
        # Nie liczymy przecięcia dla górnego wierzchołka,
        # żeby uniknąć podwójnego zliczania
        return 0

    if y == y0:
        # Jeśli punkt P leży dokładnie na dolnym wierzchołku,
        # liczymy przecięcie tylko wtedy, gdy krawędź "wchodzi w górę"
        # (czyli drugi koniec odcinka jest wyżej)
        if y1 > y0:
            if x0 >= x:
                return 1
            else:
                return 0

    # 3. Obliczamy współrzędną X przecięcia
    t = (y - y0) / float(y1 - y0)
    xp = x0 + t * (x1 - x0)

    # 4. Sprawdzamy, czy przecięcie jest po prawej stronie
    return 1 if xp >= x else 0

print(krawedz_przecina_lamana(1, 1, 0, 0, 2, 2))