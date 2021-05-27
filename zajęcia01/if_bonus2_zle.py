odpowiedz = input("Tak czy nie? [t/n]: ")

if odpowiedz == 'T' or 't':  # TO NIE ZADZIAŁA! "odpowiedz" równa się 'T' lub True
    print('TAK!')
elif odpowiedz == 'N' or 'n':  # TO NIE ZADZIAŁA!
    print('NIE')
else:
    print('Nie rozumiem')
