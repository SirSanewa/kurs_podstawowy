# Zadanie 0503:

Napisz program, który:
- Wczyta kolejno z klawiatury informacje o znanym muzyku: 
    - imię, 
    - instrument, 
    - ilość nagranych albumów.
- Z przekazanych przez użytkownika danych stworzy słownik 'muzyk' z trzema polami odpowiadającymi wpisanym wartościom.
- Wypisze zawartość słownika na ekran, funkcją `print()`
- Program stworzy "podsumowanie" w stylu poniższego komunikatu i wypisze je na ekran.
    ```
    Frank Zappa nagrał(a) 111 albumów. 
    Jego instrument to: gitara elektryczna.
    ```
    - Komunikat będzie przechowywany w oddzielnej zmiennej i stworzony przy użyciu metody `.format()` lub f-string.
    - Do stworzenia komunikatu można użyć tylko danych wyciągniętych ze słownika.

# Rozszerzenie:
Rozszerz część odpowiedzialną za wczytywanie danych od użytkownika o kolejną informację: czy muzyk jest jeszcze aktywny:
- Użytkownik z klawiatury może wpisać "(t)ak" lub "(n)ie".
    - jeśli użytkownik nie podał zrozumiałej odpowiedzi (jednej z 'tak', 't', 'nie', 'n') to program ma ponowić pytanie i robić tak do momentu otrzymania odpowiedzi, lub przerwania programu z zewnątrz (np. ctrl+c).    
- Wartość odpowiedzi należy przechowywać w słowniku pod nowym kluczem jako zmienną typu bool (`True` lub `False`).
- Zmodyfikuj podsumowanie tak, aby uwzględniało tę informację.
