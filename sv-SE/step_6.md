## Kryptera hela meddelanden

Istället för att bara kryptera och dekryptera meddelanden ett tecken åt gången, låt oss ändra programmet för att kryptera hela meddelanden!

+ Kontrollera först att din kod ser ut så här:
    
    ![skärmdump](images/messages-character-finished.png)

+ Skapa en variabel för att lagra det nya krypterade meddelandet.
    
    ![skärmdump](images/messages-newmessage.png)

+ Ändra din kod för att lagra användarens meddelande och inte bara ett tecken.
    
    ![skärmdump](images/messages-message.png)

+ Lägg till en `för` loop till din kod och ange resten av koden så att den upprepas för varje tecken i meddelandet.
    
    ![skärmdump](images/messages-loop.png)

+ Testa din kod. Du bör se att varje tecken i meddelandet är krypterad och skrivs ut en i taget.
    
    ![skärmdump](images/messages-loop-test.png)

+ Låt oss lägga till varje krypterad tecken till din `newMessage` variabel.
    
    ![skärmdump](images/messges-message-add-character.png)

+ Du kan `skriva ut` den `newMessage` som den krypteras.
    
    ![skärmdump](images/messages-print-message-characters.png)

+ Om du tar bort mellanslag före `utgåvan` , kommer det krypterade meddelandet endast att visas en gång i slutet. Du kan även ta bort koden för att skriva ut teckenpositionerna.
    
    ![skärmdump](images/messages-print-message-comment.png)