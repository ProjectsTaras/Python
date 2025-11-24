import numpy as np
print(np.__version__)

# Wydrukuj każdy wiersz macierzy jako listę Python
A=np.array([[0,0,1],[1,1,0],[1,1,1]])
print ("A", A)
print (A.dtype)
#suma elementów macierzy
print (np.sum(A))
print (np.sum(A,axis=0)) #suma po kolumnach
print (np.sum(A,axis=1)) #suma po wierszach
#Iloczyn macierzy
B=np.array([[2,1,1],[1,1,1],[0,0,1]])
print("B", B)
print (A.dot(B) ) #macierz A musi mieć tyle kolumn co macierz B wierszy
#LUB
print (np.dot(A,B))
#średnia elementów macierzy
print (np.mean(A))
print (np.mean(A,axis=0)) #średnia po kolumnach
print (np.mean(A,axis=1)) #średnia po wierszach
#maksymalny element macierzy
print (np.max(A))
#Dwie macierze z 3 wierszami i 4 kolumnami. Pierwsza wypełniona zerami, a druga jedynkami.
B = np.zeros((3,4))
C = np.ones((3,4))
print (B)
print (C)
#Macierz jednostkowa 4x4
D = np.eye(4)
print (D)
#Macierz 3x4 z losowymi wartościami
E = np.random.random((3,4))
print (E)

#Tablice jednowymiarowe (1D) w Pythonie to wektory wierszowe, czyli macierze o wymiarze 1 × n.
print (np.ones(10))
print ("Size:"+ str(np.ones(10).size))
#Tablice dwuwymiarowe (2D) w Pythonie to macierze o wymiarze m × n.
#Początkowo masz tablicę 1-wymiarową, którą następnie przekształcasz w tablicę 2-wymiarową za pomocą metody reshape.
A = np.array([0,1,2,1]).reshape((2,2))
print (A)
print ("Shape:"+ str(A.shape)) #A.shape zwraca kształt (wymiary) tablicy NumPy

#Tworzenie tablicy NumPy z listy Python
lista = [10, 20, 30, 40]
tablica = np.array(lista)
print(tablica)
#Tworzenie tablicy NumPy z zagnieżdżonej listy Python (lista list)
lista_zagniezdzona = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tablica_2d = np.array(lista_zagniezdzona)
print(tablica_2d)
#Podstawowe operacje na tablicach NumPy
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
suma = a + b
roznica = b - a
iloczyn = a * b
iloraz = b / a
print("Suma:", suma)
print("Różnica:", roznica)
print("Iloczyn:", iloczyn)
print("Iloraz:", iloraz)
#Indeksowanie i wycinanie tablic NumPy
tablica = np.array([10, 20, 30, 40, 50])
print("Element na indeksie 2:", tablica[2])
print("Elementy od indeksu 1 do 3:", tablica[1:4])
macierz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element na pozycji (1,2):", macierz[1, 2])
print("Druga kolumna macierzy:", macierz[:, 1])
