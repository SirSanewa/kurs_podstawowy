# Zadanie 0303
Napisz program, który:
- Wczyta z klawiatury liczbę naturalną (zakładamy, że użytkownik wpisał poprawną liczbę)
- W pętli `for` będzie po kolei sprawdzał wszystkie liczby, które mogą być dzielnikami wprowadzonej liczby.
  - jeśli sprawdzana liczba będzie dzielnikiem, program wypisze komunikat:
  "(liczba) jest podzielna przez (dzielnik)"
  
## Podpowiedzi:
- Jeśli jedna liczba dzieli drugą _bez reszty_ oznacza to, że jest jej dzielnikiem. W Pythonie, aby sprawdzić resztę z dzielenia jednej liczby przez drugą należy użyć operatora `%`.
- Najmniejszym dzielnikiem danej liczby jest 1 a największym ona sama. Aby sprawdzić wszystkie możliwości, należy użyć funkcji `range()` z odpowiednimi parametrami.


## Rozszerzenie 1:
- Zamiast wypisywać dzielniki od razu, dodawaj je do listy
- Po sprawdzeniu wszystkich możliwości wypisz na ekran listę dzielników tej liczby. 

## Rozszerzenie 2:
- Jeśli liczba będzie miała dokładnie dwa dzielniki (1 i siebie samą) oznacza to, że sprawdzana liczba jest liczbą pierwszą. Wypisz tę informację na ekran.