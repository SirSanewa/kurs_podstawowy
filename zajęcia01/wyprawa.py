odpowiedz = input("Wprowadz ilość przejechanych kilometrów: ")

dystans = int(odpowiedz)

spalanie_na_100 = 8
cena_benzyny = 5.02
koszt = dystans * spalanie_na_100 / 100 * cena_benzyny
print("Koszt wyprawy to:", koszt)
