## Szyfrowanie całych wiadomości

Zamiast szyfrować i odszyfrowywać wiadomości po jednej literze, zmieńmy program tak, aby szyfrować całe wiadomości!

+ Po pierwsze sprawdź, czy Twój kod wygląda następująco:
    
    ![zrzut ekranu](images/messages-character-finished.png)

+ Utwórz zmienną do przechowywania nowej zaszyfrowanej wiadomości.
    
    ![zrzut ekranu](images/messages-newmessage.png)

+ Zmień kod, aby przechować wiadomość użytkownika, a nie tylko jedną literę.
    
    ![zrzut ekranu](images/messages-message.png)

+ Dodaj `for` pętlę do twojego kodu i dodaj wcięcie do reszty kodu, aby powtarzał się dla każdej litery w wiadomości.
    
    ![zrzut ekranu](images/messages-loop.png)

+ Przetestuj swój kod. Powinieneś zobaczyć, że każda litera w wiadomości jest zaszyfrowana i wydrukowana pojedynczo.
    
    ![zrzut ekranu](images/messages-loop-test.png)

+ Dodajmy każdą zaszyfrowaną literę do twojej zmiennej `nowaWiadomosc`.
    
    ![zrzut ekranu](images/messges-message-add-character.png)

+ Możesz `print` `nowaWiadomosc` jak zostanie zaszyfrowana.
    
    ![zrzut ekranu](images/messages-print-message-characters.png)

+ Jeśli usuniesz spacje przed instrukcją `print`, wyświetli się tylko zaszyfrowana wiadomość na końcu. Możesz również usunąć kod drukowania pozycji liter.
    
    ![zrzut ekranu](images/messages-print-message-comment.png)