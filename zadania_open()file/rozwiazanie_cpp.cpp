// Program czyta imiona z pliku names.txt, liczy wystąpienia wybranego imienia
// i zapisuje wynik do pliku wynik.txt.

#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>

int main() {
    // Ustaw swoje imię i imię sąsiada
    std::string myName = "Franciszek";
    std::string neighborName = "Hubert";

    std::ifstream in("names.txt");
    if (!in.is_open()) {
        std::cerr << "Nie można otworzyć pliku names.txt\n";
        return 1;
    }

    std::unordered_map<std::string, int> counts;
    std::string name;

    // Wczytywanie imion i zliczanie wystąpień
    while (std::getline(in, name)) {
        if (!name.empty()) {
            counts[name]++;
        }
    }
    in.close();

    int myCount = counts[myName];
    int neighborCount = counts[neighborName];

    std::ofstream out("wynik.txt");
    if (!out.is_open()) {
        std::cerr << "Nie można utworzyć pliku wynik.txt\n";
        return 1;
    }

    out << "Moje imię: " << myName << "\n";
    out << "Liczba wystąpień: " << myCount << "\n";
    out << "Imię sąsiada powtórzone:" << "\n";

    // Wypisujemy imię sąsiada tyle razy, ile razy występuje w pliku
    for (int i = 0; i < neighborCount; i++) {
        out << neighborName << "\n";
    }

    out.close();
    std::cout << "Gotowe. Wynik zapisano w pliku wynik.txt\n";
    return 0;
}
