#tablica dwuwymiarowa
X = [
    [1, 2],
    [4, 5],
    [7, 8]
]

#wymiary tablicy
print(len(X)) #liczba wierszy
print(len(X[0])) #liczba kolumn w pierwszym wierszu
# dostęp do elementów
#  przykłady dostępu do elementów tablicy dwuwymiarowej
print("--//---")
print(0//3)
print(1//3)
print(2//3)
print(3//3)
print(4//3)
print(5//3)
print(6//3)
print(7//3)
print(8//3)
print("--%---")
print(0%3)
print(1%3)
print(2%3)
print(3%3)
print(4%3)
print(5%3)
print(6%3)
print(7%3)
print(8%3)

"""
•	i = 0 → A[0][0] = 10
•	i = 1 → A[0][1] = 20
•	i = 2 → A[1][0] = 30
•	i = 3 → A[1][1] = 40
"""
# Rekurencja_na_tablicy
"""
Завдання 1. Рекурсія над масивом

Дано рекурсивну функцію tablica, яка має три параметри:
A[1..n, 1..n] — двовимірний масив із n додатних цілих чисел
n — додатне ціле число, що є розміром масиву A
i — додатне ціле число

функція tablica(A, i, n)
    якщо i = n*n
        повернути 0
    w ← (i div n) + 1
    k ← (i mod n) + 1
    повернути A[w, k] + tablica(A, i+1, n)

PL
Zadanie 1. Rekurencja na tablicy
Dana jest funkcja rekurencyjna tablica, która ma trzy parametry:
A[1..n, 1..n] - tablica dwuwymiarowa n × n dodatnich liczb całkowitych
n - dodatnia liczba całkowita będąca rozmiarem tablicy A
i - dodatnia liczba całkowita

funkcja tablica(A, i, n)
  jeżeli i = n*n
    zwróć 0
  w ← (i div n) + 1
  k ← (i mod n) + 1
  zwróć A[w, k] + tablica(A, i+1, n)

Uwaga: Operator mod oznacza resztę z dzielenia, natomiast div - część całkowitą z dzielenia.
"""
#python
A = [[10,20],[30,40]]
def tablica(A, i, n):
    if i == n * n:
        return 0
    w = i // n  # numer wiersza (0..n-1)
    k = i % n  # numer kolumny (0..n-1)
    return A[w][k] + tablica(A, i + 1, n)
print(tablica(A, 0, 2))

#C++
#include <iostream>
'''
using namespace std;

int tablica(int A[][100], int i, int n) {
    // базовий випадок рекурсії
    if (i == n * n)
        return 0;

    int w = i / n;   // номер рядка (0..n-1)
    int k = i % n;   // номер стовпця (0..n-1)

    return A[w][k] + tablica(A, i + 1, n);
}

int main() {
    int n;
    cin >> n;

    int A[100][100];

    // введення матриці
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> A[i][j];

    // починаємо з i = 0
    cout << tablica(A, 0, n);

    return 0;
}
'''

'''
Завдання 1.3. (0-3)
У вигляді псевдокоду або вибраною мовою програмування напиши нерекурсивну функцію tablica2, яка для таблиці A з додатних цілих чисел розміру n × n повертає той самий результат, що й функція tablica(A, 0, n).
Увага:
Твій алгоритм може використовувати виключно змінні, що зберігають цілі числа, і може оперувати лише цілими числами.
У записі дозволяється використовувати тільки арифметичні операції: додавання, віднімання, множення, ділення, цілочисельне ділення, остачу від ділення, а також порівняння чисел, керуючі інструкції, присвоєння значень змінним або власноруч написані функції, які використовують перелічені вище операції.
Заборонено використовувати вбудовані функції та оператори, не перелічені вище, зокрема — функцію tablica.

⚠️	Складність: O(n²) — як і в рекурсивній версії

PL
Zadanie 1.3. (0-3)
W postaci pseudokodu lub w wybranym języku programowania napisz nierekurencyjną funkcję tablica2,
która dla tablicy A dodatnich liczb całkowitych o rozmiarze n × n zwróci ten sam wynik, co funkcja tablica(A, 0, n).

Uwaga:
Twój algorytm może używać wyłącznie zmiennych przechowujących liczby całkowite oraz może operować wyłącznie na liczbach całkowitych.
W zapisie możesz wykorzystać tylko następujące operacje:
dodawanie, odejmowanie, mnożenie, dzielenie, dzielenie całkowite, resztę z dzielenia, porównywanie liczb, instrukcje sterujące, przypisania do zmiennych
lub samodzielnie napisane funkcje, wykorzystujące wyżej wymienione operacje.
Zabronione jest używanie funkcji wbudowanych oraz operatorów innych niż wymienione, w tym - funkcji tablica.

Specyfikacja
Dane:
A[1..n, 1..n] - tablica dwuwymiarowa n × n dodatnich liczb całkowitych
n - dodatnia liczba całkowita będąca rozmiarem tablicy A
i - dodatnia liczba całkowita
Wynik:
dodatnia liczba całkowita
'''

def tablica2(A, n):
    wynik = 0
    i = 0
    while i < n * n:
        w = i // n
        k = i % n
        wynik = wynik + A[w][k]
        i = i + 1
    return wynik
print(tablica2(A, 2))

#c++
'''
int tablica2(int A[][100], int n)
{
    int wynik = 0;
    int i = 0;

    while (i < n * n)
    {
        int w = i / n;
        int k = i % n;
        wynik = wynik + A[w][k];
        i = i + 1;
    }

    return wynik;
}

#⚠️ Розмір [100] — умовний

'''