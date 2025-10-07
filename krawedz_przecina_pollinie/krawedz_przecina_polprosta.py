def krawedz_przecina_polprosta(x, y, x0, y0, x1, y1):
    if y1 == y0:               # Jeśli odcinek jest poziomy
        return 0

    if (y0 > y and y1 > y) or (y0 < y and y1 < y):
        # Jeśli odcinek leży całkowicie powyżej lub poniżej punktu (x, y)
        return 0

    if x0 < x and x1 < x:
        # Jeśli oba końce odcinka leżą na lewo od punktu (x, y)
        return 0

    if x0 >= x and x1 >= x:
        # Jeśli oba końce odcinka leżą na prawo lub dokładnie w punkcie x
        return 1

    # Obliczamy współrzędną X punktu przecięcia odcinka z prostą y
    t = (y - y0) / float(y1 - y0)
    xp = x0 + t * (x1 - x0)   # xp — punkt przecięcia z prostą y

    if xp >= x:   # Jeśli punkt przecięcia leży na prawo lub dokładnie w (x, y)
        return 1
    else:
        return 0
print(krawedz_przecina_polprosta(1, 1, 0, 0, 2, 2))