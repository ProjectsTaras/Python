#include <iostream>
#include <string>
using namespace std;

int ileWystapien(string tekst, string wzorzec) {
    int n = tekst.length();
    int m = wzorzec.length();
    int licznik = 0;

    for(int i = 0; i <= n - m; i++) {
        int j = 0;

        while(j < m && tekst[i + j] == wzorzec[j]) {
            j++;
        }

        if(j == m) {
            licznik++;
        }
    }

    return licznik;
}