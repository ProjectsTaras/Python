def ileWystapien(tekst, wzorzec):
    n = len(tekst)
    m = len(wzorzec)
    licznik = 0

    for i in range(n - m + 1):
        j = 0

        while j < m and tekst[i + j] == wzorzec[j]:
            j += 1

        if j == m:
            licznik += 1

    return licznik

print(ileWystapien("ababcabab", "abc"))