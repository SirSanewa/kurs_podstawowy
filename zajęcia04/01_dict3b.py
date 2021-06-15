osoba = {'imie': 'Guido',
         'nazwisko': 'van Rossum',
         'rok_urodzenia': 1956}

# Rozpakowywanie krotki dla każdej iteracji pętli
for k, w in osoba.items():
    print(f'Klucz: {k}, wartość: {w}')
