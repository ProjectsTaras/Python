# Edukacyjna wizualizacja prawdziwej agent architecture

Ten mini projekt pokazuje w prosty i czytelny sposob, jak moze dzialac system wieloagentowy. Nie jest to tylko jeden chatbot, ale uporzadkowany proces, w ktorym kilka agentow wykonuje rozne role i przekazuje sobie wyniki.

## Co zawiera projekt

- `multi_agent_demo.py` - wersja konsolowa, pokazujaca kolejne kroki pracy agentow
- `multi_agent_demo.ipynb` - ta sama demonstracja w formacie Jupyter Notebook
- `app.py` - lokalny serwer uruchamiajacy wersje przegladarkowa
- `web/index_pl.html` - polski interfejs demonstracji
- `web/app_pl.js` - logika interfejsu krok po kroku

## Co dokladnie pokazuje demonstracja

Scenariusz:

`Szkola chce zdecydowac, czy warto wdrozyc AI-asystenta wspierajacego uczniow i nauczycieli.`

W systemie dziala 5 agentow:

1. `PlannerAgent` - dzieli zadanie na etapy
2. `BenefitsAgent` - zbiera argumenty za wdrozeniem
3. `RisksAgent` - analizuje ryzyka i ograniczenia
4. `SafetyAgent` - proponuje zasady bezpiecznego korzystania
5. `DecisionAgent` - laczy wyniki i tworzy koncowa rekomendacje

## Jak uruchomic

Wersja konsolowa:

```powershell
python .\multi_agent_demo.py
```

Wersja wizualna w przegladarce:

```powershell
python .\app.py
```

Nastepnie otworz w przegladarce:

`http://127.0.0.1:8000`

## Co widac na stronie

- liste agentow i ich role;
- kolejne kroki wykonania;
- ktory agent jest aktualnie aktywny;
- jakie dane otrzymuje od poprzednich agentow;
- wynik koncowy powstajacy etap po etapie.

## Jak to uczciwie wyjasnic uczniom

To jest `edukacyjna wizualizacja prawdziwej agent architecture`.

Oznacza to, ze projekt naprawde pokazuje kluczowe elementy systemu agentowego:
- podzial zadania na specjalizowane role;
- kolejnosc wykonywania krokow;
- przekazywanie wynikow pomiedzy agentami;
- laczenie wielu etapow w jedna odpowiedz koncowa.

Jednoczesnie jest to wersja dydaktyczna, czyli uproszczona. Agenci nie korzystaja tutaj jeszcze z zewnetrznego API modelu jezykowego, tylko realizuja przygotowany scenariusz demonstracyjny. Dzięki temu uklad pracy agentow jest czytelny, stabilny i latwy do pokazania na lekcji.

## Po co taki projekt na lekcji

Ta demonstracja pomaga pokazac uczniom, ze:
- agent AI to nie tylko okno czatu;
- zlozone zadanie mozna rozbic na role i etapy;
- system wieloagentowy daje wieksza kontrole nad procesem;
- przyszlosc internetu moze opierac sie na wspolpracy wielu wyspecjalizowanych agentow.

## Mozliwy kolejny krok

Jesli bedzie potrzeba, do tego projektu mozna pozniej dodac wersje z prawdziwym modelem AI przez API, tak aby agenci generowali odpowiedzi dynamicznie podczas uruchomienia.
