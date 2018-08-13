## Caratteri Extra

Alcuni caratteri non sono nell'alfabeto, il che causa un errore.

+ Prova il tuo codice con alcuni caratteri che non sono nell'alfabeto.
    
    Ad esempio, potresti usare il messaggio `ciao a tutti!`.
    
    ![screenshot](images/messages-extra-characters.png)
    
    Si noti che lo spazio e il punto escalamativo `!` sono tutti crittografati con la lettera "c"!

+ Per risolvere questo problema, devi solo tradurre un carattere se è nell'alfabeto. Per fare ciò, aggiungi un istruzione `if` e rientra con il il resto del codice.
    
    ![screenshot](images/messages-if.png)

+ Prova il tuo codice con lo stesso messaggio. Cosa succede questa volta?
    
    ![screenshot](images/messages-if-test.png)
    
    Ora, il tuo codice salta qualsiasi carattere se non è nell'alfabeto.

+ Sarebbe meglio se il tuo codice non criptasse nulla non presente nell'alfabeto, ma mantenesse il carattere originale.
    
    Aggiungi un'istruzione `else` al tuo codice, che aggiunga semplicemente il carattere originale al messaggio crittografato.
    
    ![screenshot](images/messages-else.png)

+ Prova il tuo codice. Dovresti vedere che qualsiasi carattere nell'alfabeto è crittografato, ma tutti gli altri caratteri restano inalterati!
    
    ![screenshot](images/messages-else-test.png)