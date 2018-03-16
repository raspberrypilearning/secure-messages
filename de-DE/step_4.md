## Buchstaben verschlüsseln

Lass uns ein Python Programm schreiben, um ein einzelnes Zeichen zu verschlüsseln. 

+ Das leere Python Vorlage- Trinket öffnen: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>. 

+ Anstatt das Alphabet in einem Kreis aufzuzeichnen, lass es uns als eine `alphabet` Variable aufschreiben.

	![screenshot](images/messages-alphabet.png)

+ Jeder Buchstabe des Alphabets hat eine Positionsnummer, wir beginnen bei der Positionnummer 0. Das heißt also, dass der Buchstabe 'a' sich bei Positionnummer 0 des Alphabets befindet und der Buchstabe 'c' sich auf der Positionsnummer 2 befindet.

	![screenshot](images/messages-array.png)

+ Du kannst einen Buchstaben aus deiner `alphabet` Variable erhalten, indem du die Positionsnummer in eckigen Klammern schreibst.

	![screenshot](images/messages-alphabet-array.png)

	Du kannst die `print` (drucken) Statements löschen, nachdem du dies ausprobiert hast.

+ Als nächstes musst du den geheimen `key` in einer Variable speichern.

	![screenshot](images/messages-key.png)	

+ Frage dann den Nutzer nach einem einzigen Buchstaben (dies wird `character` (Zeichen) genannt), um dies zu verschlüsseln.

	![screenshot](images/messages-character.png)

+ Finde die `position` (Positionsnummer) des `character` (Zeichens).

	![screenshot](images/messages-position.png)

+ Du kannst die gespeicherte `position` (Positionsnummer) testen, indem du sie ausdruckst. Zum Beispiel, ob sich das Zeichen 'e' bei der Positionsnummer 4 im Alphabet befindet.

	![screenshot](images/messages-position-test.png)

+ Um das `character` (Zeichen) zu verschlüsseln, solltest du den `key` in die `position` (Positionsnummer) hinzufügen.

	![screenshot](images/messages-newposition.png)

+ Teste deinen neuen Code aus. Da unser `key` die 3 ist, sollte er die Ziffer 3 in die `position` (Positionsnummer) addieren und in deiner `newPosition` (neuen Positionsnummer) Variable speichern. 

	Zum Beispiel befindet sich der Buchstabe 'e' auf der Positionsnummer 4. Um dies zu verschlüsseln addierst du den `key` (3), was insgesamt 7 ergibt.

	![screenshot](images/messages-newposition-test.png)

+ Was passiert, wenn du versuchst, den Buchstaben 'y' zu verschlüsseln?

	![screenshot](images/messages-modulus-bug.png)

	Siehst du, dass die `newPosition` (neue Positionsnummer) jetzt 27 beträgt, aber es gibt gar nicht 27 Buchstaben im Alphabet?

+ Du kannst `%` benutzen, um der neuen Positionsnummer mitzuteilen, wieder auf die Positionsnummer 0 zurückzugehen, nachdem sie die Positionsnummer 26 erreicht hat. 

	![screenshot](images/messages-modulus.png)

+ Und zum Schluss solltest du den Buchstaben in der neuen Positionsnummer ausdrucken.

	Zum Beispiel, wenn du den Key zum Buchstaben 'e' addierst, erhältst du 7 und der Buchstabe auf der Positionsnummer 7 des Alphabets ist das 'h'.

	![screenshot](images/messages-newcharacter.png)

+ Probiere deinen neuen Code aus. Du kannst auch manche deiner Drucken-Statements entfernen und einfach nur am Ende das neue Zeichen ausdrucken.

	![screenshot](images/messages-enc-test.png)
