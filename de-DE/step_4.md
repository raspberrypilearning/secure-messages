## Buchstaben verschlüsseln

Lass uns ein Python Programm schreiben, um ein einzelnes Zeichen zu verschlüsseln.

+ Öffne die leere Python Vorlage in trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Anstatt das Alphabet in einem Kreis aufzuzeichnen, lass es uns als String-Variable `alphabet` aufschreiben.
    
    ![screenshot](images/messages-alphabet.png)

+ Jeder Buchstabe des Alphabets hat eine Positionsnummer, wir beginnen bei der Positionsnummer 0. Das heißt also, dass der Buchstabe ‘a’ sich bei Positionsnummer 0 des Alphabets befindet und der Buchstabe ‘c’ sich auf der Positionsnummer 2 befindet.
    
    ![screenshot](images/messages-array.png)

+ Du kannst einen Buchstaben aus deiner Variablen `alphabet` erhalten, indem du die Positionsnummer in eckigen Klammern schreibst.
    
    ![screenshot](images/messages-alphabet-array.png)
    
    Du kannst die `print` Statements (drucken) löschen, nachdem du alles ausprobiert hast.

+ Als nächstes musst du den geheimen Schlüssel in der Variable `key` speichern.
    
    ![screenshot](images/messages-key.png)

+ Frage dann den Nutzer nach einem Buchstaben, um diesen zu verschlüsseln.
    
    ![screenshot](images/messages-character.png)

+ Finde die Positionsnummer (`position`) des Buchstabens (`buchstabe`) im Alphabet.
    
    ![screenshot](images/messages-position.png)

+ Du kannst die gespeicherte Positionsnummer `(position)` testen, indem du sie ausdruckst. Zum Beispiel, ob sich das Zeichen ‘e’ bei der Positionsnummer 4 im Alphabet befindet.
    
    ![screenshot](images/messages-position-test.png)

+ Um den Buchstaben (`buchstabe`) zu verschlüsseln, musst du den Schlüssel (`key`) mit der Positionsnummer (`position`) addieren. Das Ergebnis wird in der Variablen `neuePosition` gespeichert.
    
    ![screenshot](images/messages-newposition.png)

+ Füge nun den Programmcode hinzu, um diese neue Position des Buchstabens auszudrucken.
    
    ![screenshot](images/messages-newposition-print.png)

+ Teste deinen neuen Code aus. Da unser `key` = 3 ist, sollte er die Zahl 3 zu der Positionsnummer (`position`) addieren und in der Variablen `neuePosition` als neue Positionsnummer speichern.
    
    Zum Beispiel befindet sich der Buchstabe ‘e’ auf der Positionsnummer 4. Um dies zu verschlüsseln, addierst du den `key` (3), was insgesamt 7 ergibt.
    
    ![screenshot](images/messages-newposition-test.png)

+ • Was passiert, wenn du versuchst, den Buchstaben ‘y’ zu verschlüsseln?
    
    ![screenshot](images/messages-modulus-bug.png)
    
    Siehst du, dass die neue Positionsnummer (`neuePosition`) jetzt 27 beträgt? Aber es gibt gar nicht 27 Buchstaben im Alphabet!

+ Du kannst den Modulo-Operator `%` benutzen, um der neuen Positionsnummer mitzuteilen, wieder auf die Positionsnummer 0 zurückzugehen, nachdem sie die Positionsnummer 26 erreicht hat.
    
    ![screenshot](images/messages-modulus.png)

+ Und zum Schluss wollen wir den Buchstaben in der neuen Positionsnummer ausdrucken.
    
    Zum Beispiel, wenn du den Schlüssel (key) zur Positionsnummer des Buchstaben ‘e’ addierst, erhältst du 7 und der Buchstabe auf der Positionsnummer 7 des Alphabets ist das ‘h’.
    
    ![screenshot](images/messages-newcharacter.png)

+ Probiere deinen neuen Code aus. Du kannst auch manche deiner print-Statements (Drucken) entfernen und einfach nur am Ende das neue Zeichen ausdrucken.
    
    ![screenshot](images/messages-enc-test.png)