## Szyfrowanie liter

Napiszmy program Python, aby zaszyfrować pojedynczy znak.

+ Otwórz pusty szablon dla języka Python w edytorze Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Zamiast rysować alfabet w kółku, wypiszmy go jako `alfabet` zmienną.
    
    ![zrzut ekranu](images/messages-alphabet.png)

+ Każda litera alfabetu ma pozycję, zaczynając od pozycji 0. Tak więc litera 'a' znajduje się na pozycji 0 alfabetu, zaś 'c' na pozycji 2.
    
    ![zrzut ekranu](images/messages-array.png)

+ Możesz otrzymać literę ze zmiennej `alfabet` wpisując pozycję w nawiasach kwadratowych.
    
    ![zrzut ekranu](images/messages-alphabet-array.png)
    
    Możesz usunąć `print` kiedy to wypróbujesz.

+ Następnie musisz przechowywać tajny `klucz` w zmiennej.
    
    ![zrzut ekranu](images/messages-key.png)

+ Następnie poproś użytkownika o pojedynczą literę (nazywaną `litera`) do zaszyfrowania.
    
    ![zrzut ekranu](images/messages-character.png)

+ Znajdź `pozycja` dla `litera`.
    
    ![zrzut ekranu](images/messages-position.png)

+ Możesz przetestować zachowaną `pozycja` przez wydrukowanie jej. Na przykład litera 'e' znajduje się na pozycji 4 w alfabecie.
    
    ![zrzut ekranu](images/messages-position-test.png)

+ Aby zaszyfrować `litera`, powinieneś dodać `klucz` do `pozycja`. Wówczas jest ona przechowywana w zmiennej ` nowaPozycja`.
    
    ![zrzut ekranu](images/messages-newposition.png)

+ Dodaj kod, aby wydrukować nową pozycję litery.
    
    ![zrzut ekranu](images/messages-newposition-print.png)

+ Przetestuj swój nowy kod. Jeśli twój `klucz` to 3, powinno dodać 3 do `pozycja` i zachować to w twojej zmiennej `nowaPozycja`.
    
    Na przykład litera 'e' znajduje się na pozycji 4. Aby ją zaszyfrować, dodaje się `klucz` (3), co daje 7.
    
    ![zrzut ekranu](images/messages-newposition-test.png)

+ Co się stanie, gdy spróbujesz zaszyfrować literę 'y'?
    
    ![zrzut ekranu](images/messages-modulus-bug.png)
    
    Zauważ, że `newPosition` to 27, a nie ma 27 liter w alfabecie!

+ Możesz użyć `% ` aby nowa pozycja powróciła do pozycji 0, gdy osiągnie pozycję 26.
    
    ![zrzut ekranu](images/messages-modulus.png)

+ Na koniec, chcesz wydrukować literę na nowej pozycji.
    
    Na przykład, dodanie klucza do litery 'e' daje 7, a literą na pozycji 7 w alfabecie jest 'h'.
    
    ![zrzut ekranu](images/messages-newcharacter.png)

+ Wypróbuj swój kod. Możesz także usunąć niektóre z poleceń drukowania, po prostu drukując nową literę na końcu.
    
    ![zrzut ekranu](images/messages-enc-test.png)