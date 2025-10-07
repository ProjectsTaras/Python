def krawedz_przecina_lamana(x, y, x0, y0, x1, y1):
    if y0 > y1:
        x0, y0, x1, y1 = x1, y1, x0, y0

    if y < y0 or y > y1:
        return 0

    if y == y1:
        return 0

    if y == y0:
        if y1 > y0:
            if x0 >= x:
                return 1
            else:
                return 0

    t = (y - y0) / float(y1 - y0)
    xp = x0 + t * (x1 - x0)

    return 1 if xp >= x else 0


def punkt_w_wielokacie(x, y, polygon):
    przeciecia = 0
    n = len(polygon)

    for i in range(n):
        x0, y0 = polygon[i]
        x1, y1 = polygon[(i + 1) % n]  # ostatni łączy się z pierwszym
        # jeśli punkt leży dokładnie na krawędzi – zwracamy "na krawędzi"
        if min(x0, x1) <= x <= max(x0, x1) and min(y0, y1) <= y <= max(y0, y1):
            if (x1 - x0) * (y - y0) == (y1 - y0) * (x - x0):
                return "Punkt leży na krawędzi"
        przeciecia += krawedz_przecina_lamana(x, y, x0, y0, x1, y1)

    return "Punkt wewnątrz" if przeciecia % 2 == 1 else "Punkt na zewnątrz"


# --- GŁÓWNY PROGRAM ---
n = int(input("Podaj liczbę wierzchołków polygonu: "))
polygon = []
for i in range(n):
    x, y = map(float, input(f"Podaj współrzędne wierzchołka {i+1} (x y): ").split())
    polygon.append((x, y))

x, y = map(float, input("Podaj współrzędne punktu do sprawdzenia (x y): ").split())

print(punkt_w_wielokacie(x, y, polygon))
