# Ćwiczenie: implementacja grafów - graf prosty

Folder zawiera:

* kod klasy abstrakcyjnej (interfejsu) grafu (`BaseGraph[T]`) będącego definicją ADT dla wszystkich typów grafów
* częściowy, przykładowy kod klasy implementującej graf prosty (nieskierowany, nieważony, bez multikrawędzi i pętelek) w postaci listy sąsiadów, momentami niepoprawny
* kod testów jednostkowych (środowisko `unittest` Pythona)

Ćwiczenie polega na:

1. Naprawieniu i uzupełnieniu kodu klasy `SimpleGraph`, aby spełnione były wszystkie testy. Dodatkowo napisanie metody ładującej dane do grafu na podstawie listy krawędzi ( par węzłów, np. `[('a', 'b'), ('a', 'c'), ..., ('e', 'a')]` ), aby można było w sprawny sposób inicjować większe grafy.

2. Napisaniu własnej klasy, dziedziczącej z `BaseGraph[T]` i implementującej prosty graf w formie macierzy sąsiadów. Napisanie kodu testów weryfikujących tę implementację (większość testów jednostkowych z dostarczonego pliku powinno poprawnie działać bez zmian - za wyjątkiem tych, które jawnie odwołują się do słownika listy sąsiadów)

3. Zaimplementowaniu grafu prostego w formie macierzy incydencji - dla ambitnych - oraz zweryfikowaniu poprawności implementacji testami jednostkowymi.
