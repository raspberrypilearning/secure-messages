## Extra tecken

Vissa tecken finns inte i alfabetet, vilket orsakar ett fel.

+ Testa din kod med några tecken som inte finns i alfabetet.
    
    Till exempel kan du använda meddelandet `hej där !!`.
    
    ![skärmdump](images/messages-extra-characters.png)
    
    Observera att utrymmet och `!` tecken är alla krypterade som bokstaven "c"!

+ För att fixa det här vill du bara översätta ett tecken om det finns i alfabetet. För att göra detta lägger du till ett `om` meddelande till din kod och anger resten av koden.
    
    ![skärmdump](images/messages-if.png)

+ Testa din kod med samma meddelande. Vad händer den här gången?
    
    ![skärmdump](images/messages-if-test.png)
    
    Nu springer din kod bara på ett tecken om det inte finns i alfabetet.

+ Det skulle vara bättre om din kod inte krypterade något inte i alfabetet, men använde bara den ursprungliga karaktären.
    
    Lägg till ett `annat` meddelande till din kod, som bara lägger till den ursprungliga karaktären för det krypterade meddelandet.
    
    ![skärmdump](images/messages-else.png)

+ Testa din kod. Du bör se att alla tecken i alfabetet är krypterade, men andra tecken lämnas ensamma!
    
    ![skärmdump](images/messages-else-test.png)