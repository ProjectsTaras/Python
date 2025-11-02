def silnia(n):
	if n > 1: 				        # jeśli n jest większe od 1, to wyznacz n * silnia(n-1)
		return n*silnia(n-1) 	# funkcja wywołuje samą siebie (tworzy swoją kopię)
	return 1 				        # w przeciwnym wypadku zwróć 1 (instrukcja else jest tu zbędna)
print(silnia(4))
