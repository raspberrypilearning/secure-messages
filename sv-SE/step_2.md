## Caesar cipher

En chiffer är en typ av hemlig kod, där du byter bokstäverna så att ingen kan läsa ditt meddelande.

Du använder en av de äldsta och mest kända cifrarna, den **Caesar cipher**, som är uppkallad efter Julius Caesar.

Innan vi börjar kodning, låt oss försöka använda Caesar-krypteringen för att dölja ett ord.

+ Att dölja ett ord kallas **kryptering**.
    
    Låt oss börja med att kryptera bokstaven "a". För att göra detta kan vi rita alfabetet i en cirkel, så här:
    
    ![skärmdump](images/messages-wheel.png)

+ För att skapa ett hemligt krypterat brev från en vanlig, måste du ha en hemlig nyckel. Låt oss använda nummer 3 som nyckel (men du kan använda vilket som helst nummer du vill).
    
    För att **kryptera** bokstaven "a" flyttar du bara 3 bokstäver medurs, vilket ger dig bokstaven "d":
    
    ![skärmdump](images/messages-wheel-eg.png)

+ Du kan använda det du har lärt dig för att kryptera ett helt ord. Till exempel "hej" krypterad är "khoor". Prova själv.
    
    + h + 3 = **k**
    + e + 3 = **h**
    + l + 3 = **o**
    + l + 3 = **o**
    + o + 3 = **r**

+ Att få text tillbaka till vanligt kallas **dekryptering**. För att dekryptera ett ord, dra bara av nyckeln istället för att lägga till den:
    
    + k - 3 = **h**
    + h - 3 = **e**
    + o - 3 = **1**
    + o - 3 = **1**
    + r - 3 = **o**