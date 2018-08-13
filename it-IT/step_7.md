## Caratteri Extra

Alcuni caratteri non sono nell'alfabeto, il che causa un errore.

+ Prova il tuo codice con alcuni caratteri che non sono nell'alfabeto.
    
    Ad esempio, potresti usare il messaggio `ciao a tutti!`.
    
    ![screenshot](images/messages-extra-characters.png)
    
    Si noti che lo spazio e il punto escalamativo `!` sono tutti crittografati con la lettera "c"!

+ To fix this, you only want to translate a character if it's in the alphabet. To do this, add an `if` statement to your code, and indent the rest of your code.
    
    ![screenshot](images/messages-if.png)

+ Test your code with the same message. What happens this time?
    
    ![screenshot](images/messages-if-test.png)
    
    Now, your code just skips any character if it's not in the alphabet.

+ It would be better if your code didn't encrypt anything not in the alphabet, but just used the original character.
    
    Add an `else` statement to your code, which just adds the original character to the encrypted message.
    
    ![screenshot](images/messages-else.png)

+ Test your code. You should see that any character in the alphabet is encrypted, but any other characters are left alone!
    
    ![screenshot](images/messages-else-test.png)