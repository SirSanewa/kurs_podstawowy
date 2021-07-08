# UWAGA! Ten przykład jest z premedytacją napisany źle, sprawdź 01_funkcje3ok.py

def dodaj_do_listy_wartosc(element, lista=[]):
    lista.append(element)
    return lista


wynik = dodaj_do_listy_wartosc(1, [])
print(wynik)

wynik = dodaj_do_listy_wartosc(2, [13, 17])
print(wynik)

wynik = dodaj_do_listy_wartosc(1)
print(wynik)

