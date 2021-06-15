# Zadanie 0502:
Napisz program, który:

- Będzie miał zadeklarowany string (może być w potrójnych cudzysłowach) zawierający prawdziwy, długi tekst. Przykład: wierszyk dla dzieci, lub tekst krótkiego artykułu.

- Program wykona na tym tekscie kolejno, następujące operacje:
  1. Zamieni wszystkie znaki w tekście na małe litery.
  2. Stworzy z tak przygotowanego tekstu listę zawierającą występujące w tekście wyrazy, w kolejności pojawiania się.
  3. Wypisze ilość wyrazów w tekscie.
  4. Stworzy nową listę, w której znajdą się wszystkie wyrazy w tekście **BEZ POWTÓRZEŃ** i wypisze ilość unikalnych wyrazów w tekście.
  5. Posortuje listę unikalnych wyrazów alfabetycznie.
  6. Stworzy z listy posortowanych wyrazów jednego stringa, w którym wszystkie wyrazy są wypisane po kolei i oddzielone przecinkiem (metoda `.join()`). Wypisze tego stringa na ekran.
  7. Wypisze pierwszy i ostatni wyraz z alfabetycznie posortowanych.

Uporządkuj kod w taki sposób, aby w pierwszej części zbierane były dane na temat analizowanego tekstu, następnie przygotowany był szablon komunikatu do użytkownika, który na koniec wypełniony jest pozyskanymi danymi i wydrukowany na ekran.

## Rozszerzenie:
W prawdziwych tekstach, oprócz liter, znajdziemy również kropki, przecinki i inne znaki, które utrudnią nam powyższą analizę wyrazów w tekście. Przed przed operacjami wypisanymi w punktach powyżej dopisz do programu kod, który usunie z tekstu występujące w nim znaki, które nie są literami. 
