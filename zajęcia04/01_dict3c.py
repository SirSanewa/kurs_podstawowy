osoba = {'imie': 'Guido',
         'nazwisko': 'van Rossum',
         'rok_urodzenia': 1956}

# Można też tak, ale nie polecam
for krotka in osoba.items():
    print(krotka)
    print(f'Klucz: {krotka[0]}, wartość: {krotka[1]}')
