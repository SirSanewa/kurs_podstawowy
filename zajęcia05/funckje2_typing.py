# funkcja, która przyjmująca jeden parametr i zwraca wartość


def dodaj_sto(liczba: int) -> int:
    wynik = liczba + 100
    return wynik


wartosc = 23

nowa_wartosc = dodaj_sto(wartosc)

print(nowa_wartosc)


def dodaj_sto2(liczba: int) -> None:
    wynik = liczba + 100
    print(f'{liczba} + 100 = {wynik}')


wartosc2 = 23

# funkcja, która nie ma wewnątrz swojego bloku wyrażenia `return` zwraca `None`
nowa_wartosc2 = dodaj_sto2(wartosc2)

print(nowa_wartosc2)