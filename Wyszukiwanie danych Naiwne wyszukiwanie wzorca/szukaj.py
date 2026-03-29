def szukaj(text, wzorzec):
    dlt, dlw = len(text), len(wzorzec)
    wynik = []

    if dlw > dlt:
        return False

    for i in range(dlt - dlw + 1):
        dopasowano = True

        for j in range(dlw):
            if text[i + j] != wzorzec[j]:
                dopasowano = False
                break

        if dopasowano:
            wynik.append(i)

    return wynik if wynik else False