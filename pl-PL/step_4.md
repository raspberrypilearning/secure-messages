## Szyfrowanie liter

Napiszmy program Python, aby zaszyfrować pojedynczy znak.

+ Otwórz pusty szablon dla języka Python w edytorze Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Zamiast rysować alfabet w kółku, wypiszmy go jako zmienną o nazwie `alfabet`.
    
    ![zrzut ekranu](images/messages-alphabet.png)

+ Każda litera alfabetu ma pozycję w ciągu, zaczynając od pozycji 0. Tak więc litera 'a' znajduje się na pozycji 0 alfabetu, zaś 'c' na pozycji 2.
    
    ![zrzut ekranu](images/messages-array.png)

+ Możesz otrzymać literę ze zmiennej `alfabet` wpisując pozycję w nawiasach kwadratowych.
    
    ![zrzut ekranu](images/messages-alphabet-array.png)
    
    You can delete the `print` statements once you've tried this out.

+ Następnie musisz zrobić tak, aby tajny `klucz` został przechowany w zmiennej.
    
    ![zrzut ekranu](images/messages-key.png)

+ Teraz poproś użytkownika o wprowadzenie pojedynczej litery (nazywanej `litera`), która zostanie zaszyfrowana.
    
    ![zrzut ekranu](images/messages-character.png)

+ Znajdź `pozycję` wprowadzonej `litery`.
    
    ![zrzut ekranu](images/messages-position.png)

+ Możesz przetestować zapisaną `pozycję` przez wydrukowanie jej. Na przykład litera 'e' znajduje się na pozycji 4 w alfabecie.
    
    ![zrzut ekranu](images/messages-position-test.png)

+ Aby zaszyfrować `literę`, musisz dodać `klucz` do jej `pozycji`. Następnie trzeba przechować ją w zmiennej o nazwie `nowaPozycja`.
    
    ![zrzut ekranu](images/messages-newposition.png)

+ Dodaj kod, aby wydrukować nową pozycję litery.
    
    ![zrzut ekranu](images/messages-newposition-print.png)

+ Przetestuj swój nowy kod. Jeśli twój `klucz` to 3, program powinien dodać 3 do `pozycji` i zachować to w twojej zmiennej `nowaPozycja`.
    
    Na przykład litera 'e' znajduje się na pozycji 4. Aby ją zaszyfrować, dodaje się `klucz` (3), co daje 7.
    
    ![zrzut ekranu](images/messages-newposition-test.png)

+ Co się stanie, gdy spróbujesz zaszyfrować literę 'y'?
    
    ![zrzut ekranu](images/messages-modulus-bug.png)
    
    Zauważ, że `nowaPozycja` wynosi wtedy 27, a nie ma przecież 27 liter w alfabecie!

+ Można w tym przypadku użyć znaku `%`, który sprawie, że nowa pozycja zostanie przywrócona do pozycji 0, gdy pozycja 26 zostanie osiągnięta.
    
    ![zrzut ekranu](images/messages-modulus.png)

+ Teraz wudrukuje nową pozycję wprowadzonej litery.
    
    Na przykład, dodanie klucza do litery 'e' daje 7, a literą na pozycji 7 w alfabecie jest 'h'.
    
    ![zrzut ekranu](images/messages-newcharacter.png)

+ Wypróbuj swój kod. Możesz także usunąć niektóre z poleceń drukowania i wydrukować jedynie nową literę na końcu.
    
    ![zrzut ekranu](images/messages-enc-test.png)