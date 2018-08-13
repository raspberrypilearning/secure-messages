## Crittografare interi messaggi

Invece di crittografare e decrittografare i messaggi un solo carattere alla volta, modifichiamo il programma per crittografare interi messaggi!

+ Innanzitutto, controlla che il tuo codice assomigli a questo:
    
    ![screenshot](images/messages-character-finished.png)

+ Creare una variabile per memorizzare il nuovo messaggio crittografato.
    
    ![screenshot](images/messages-newmessage.png)

+ Cambia il tuo codice per memorizzare un'intero messaggio dell'utente e non un solo carattere.
    
    ![screenshot](images/messages-message.png)

+ Aggiungi un ciclo `for` al tuo codice e rientra (indentazione) il resto del codice in modo che venga ripetuto per ogni lettera del messaggio.
    
    ![screenshot](images/messages-loop.png)

+ Prova il tuo codice. Dovresti vedere che ogni carattere nel messaggio è crittografato e stampato uno alla volta.
    
    ![screenshot](images/messages-loop-test.png)

+ Aggiungiamo ogni carattere crittografato alla tua variabile `nuovomessaggio`.
    
    ![screenshot](images/messges-message-add-character.png)

+ Puoi stampare con`print` il `nuovomessaggio` crittografato.
    
    ![screenshot](images/messages-print-message-characters.png)

+ Se elimini gli spazi prima della ` stampa ` dichiarazione, il messaggio crittografato verrà visualizzato solo una volta alla fine. Puoi anche cancellare il codice che stampa le posizioni dei caratteri.
    
    ![screenshot](images/messages-print-message-comment.png)