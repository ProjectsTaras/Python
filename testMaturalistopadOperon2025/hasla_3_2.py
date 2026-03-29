def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

with open("testMaturalistopadOperon2025/hasla.txt", "r", encoding="utf-8") as plik:
    for linia in plik:
        haslo = linia.strip()
        if all(czy_pierwsza(ord(znak)) for znak in haslo):
            print(haslo)

'''
#c++
#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

bool czyPierwsza(int n)
{
    if (n < 2)
        return false;

    for (int i = 2; i <= sqrt(n); i++)
        if (n % i == 0)
            return false;

    return true;
}

int main()
{
    ifstream plik("hasla.txt");
    string haslo;

    while (getline(plik, haslo))
    {
        bool poprawne = true;

        for (int i = 0; i < haslo.length(); i++)
        {
            int kod = (int)haslo[i];

            if (!czyPierwsza(kod))
            {
                poprawne = false;
                break;
            }
        }

        if (poprawne)
            cout << haslo << endl;
    }

    return 0;
}
'''