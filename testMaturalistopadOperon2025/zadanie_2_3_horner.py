'''pseudokod - -pseudocode

funkcja horner(n, a, A)
    wynik ← A[n]
    dla i = n-1, n-2, …, 1, 0 wykonuj
        wynik ← wynik · a + A[i]
    zwróć wynik
'''
def horner(n, a, A):
    wynik = A[0]          # odpowiada A[n]
    for i in range(1, n+1):
        wynik = wynik * a + A[i]
    return wynik

print(horner(3, 2, [2, -4, 5, 3]))

