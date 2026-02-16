import math

def czy_fibonacci(k):
    if k < 0:
        return False

    def kwadrat(n):
        s = int(math.isqrt(n))
        return s * s == n

    return kwadrat(5*k*k + 4) or kwadrat(5*k*k - 4)
#print(czy_fibonacci(0))  # True

#math.isqrt(n) - całkowitą część pierwiastka kwadratowego liczby

#math.isqrt(n) zwraca największą liczbę całkowitą s, taką że s*s <= n. Jest to funkcja dostępna w Pythonie 3.8 i nowszych. W naszym przypadku używamy jej do sprawdzenia, czy 5*k*k + 4 lub 5*k*k - 4 jest kwadratem liczby całkowitej, co jest warunkiem koniecznym dla k bycia liczbą Fibonacciego.

# Przykład n = 841
# s = isqrt(841) = 29
# 29 * 29 = 841 ✔
# czyli kwadrat

# Dlaczego to jest fajne
# Metoda	                    Szybkość
# generowanie Fibonacciego	O(n)
# wzór matematyczny	        O(1)

# Dla dużych liczb różnica jest ogromna.