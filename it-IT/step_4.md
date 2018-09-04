## Crittografia di lettere

Scriviamo un programma Python per criptare un singolo carattere dell'alfabeto.

+ Apri un modello vuoto di Python su Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Invece di disegnare l'alfabeto in un cerchio, scriviamolo come variabile `alfabeto`.
    
    ![screenshot](images/messages-alphabet.png)

+ Ogni lettera dell'alfabeto ha una posizione, a partire dalla posizione 0. Quindi la lettera 'a' è nella posizione 0 dell'alfabeto, e la lettera 'c' è in posizione 2.
    
    ![screenshot](images/messages-array.png)

+ Puoi ottenere una lettera dalla tua variabile `alfabeto` scrivendo la posizione tra parentesi quadre.
    
    ![screenshot](images/messages-alphabet-array.png)
    
    È possibile eliminare il comando `print` una volta che hai provato.

+ Successivamente dovrai memorizzare la `chiave segreta` in una variabile.
    
    ![screenshot](images/messages-key.png)

+ Ora chiedi all'utente una singola lettera (chiamata `carattere`) da criptare.
    
    ![screenshot](images/messages-character.png)

+ Trova la `posizione` del `carattere`.
    
    ![screenshot](images/messages-position.png)

+ È possibile verificare la `posizione` memorizzata usando "print". Ad esempio, quel carattere 'e' è in posizione 4 dell'alfabeto.
    
    ![screenshot](images/messages-position-test.png)

+ Per criptare il `carattere`, dovresti sommare `la chiave` alla sua `posizione`. Questo viene quindi memorizzato in una variabile denominata `nuovaposizione`.
    
    ![screenshot](images/messages-newposition.png)

+ Aggiungi del codice per visualizzare la posizione del nuovo carattere.
    
    ![screenshot](images/messages-newposition-print.png)

+ Prova il tuo nuovo codice. Poichè la tua `chiave` è 3, dovrebbe aggiungere 3 alla `posizione` e salvare il valore nella tua variabile `nuovaposizione`.
    
    Ad esempio, la lettera 'e' è in posizione 4. Per criptare si aggiunge la `chiave` (3) ottenendo 7.
    
    ![screenshot](images/messages-newposition-test.png)

+ Cosa succede quando provi a crittografare la lettera "y"?
    
    ![screenshot](images/messages-modulus-bug.png)
    
    Nota che la `nuovaposizione` vale 27, ma non ci sono 27 lettere nell'alfabeto!

+ Puoi usare l'operatore modulo `%` per dire alla nuova posizione di tornare alla posizione 0 una volta raggiunta la posizione 26.
    
    ![screenshot](images/messages-modulus.png)

+ Infine vogliamo mostrare la lettera nella nuova posizione.
    
    Ad esempio, aggiungendo la chiave alla lettera "e" si ottiene 7, e la lettera nella posizione 7 dell'alfabeto è "h".
    
    ![screenshot](images/messages-newcharacter.png)

+ Prova il tuo codice. Puoi anche rimuovere alcuni dei comandi "print", e mostrare solo il nuovo carattere alla fine.
    
    ![screenshot](images/messages-enc-test.png)