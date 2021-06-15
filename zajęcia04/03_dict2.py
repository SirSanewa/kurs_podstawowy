osoba = {'imie': 'Guido', 'nazwisko': 'van Rossum', 'rok_urodzenia': 1906}
print(osoba)

# modyfikujemy istniejący klucz. Guido nie jest taki stary :)
osoba['rok_urodzenia'] = 1956
print(osoba)

# dodajemy nowy klucz
osoba['programista'] = True
print(osoba)

# nie potrzebujemy tego pola
osoba.pop('programista')

# można też tak: (zakomentuj powyżej i odkomentuj poniżej)
# del osoba['programista']

print(osoba)
