#          0      1      2         3             4            5
lista = ['And', 'now', 'for', 'something', 'completely', 'different']
#         -6     -5     -4        -3            -2           -1

print(lista[:3] + lista[3:])  # dostajemy KOPIĘ całej listy
print(lista[:])  # również dostajemy KOPIĘ całej listy

# nowa lista z elementów od przedostatniego do końca
print(lista[-2:])

print(lista[1:6:2])  # można również podać "krok", czyli co który element brać z listy
print(lista[::2])  # można opuszczać liczbę, aby użyta była domyślna
