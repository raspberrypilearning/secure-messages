## Kryptera bokstäver

Låt oss skriva ett Python-program för att kryptera en enda karaktär.

+ Öppna den tomma Python-mallen. Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ I stället för att dra alfabetet i en cirkel, låt oss skriva ut som en `alfabet` variabel.
    
    ![skärmdump](images/messages-alphabet.png)

+ Varje bokstav i alfabetet har en position som börjar vid position 0. Så bokstaven "a" är i position 0 i alfabetet och "c" är i position 2.
    
    ![skärmdump](images/messages-array.png)

+ Du kan få ett brev från ditt `alfabet` variabel genom att skriva positionen i fyrkantiga parenteser.
    
    ![skärmdump](images/messages-alphabet-array.png)
    
    Du kan ta bort `utgåvorna` när du har provat det här.

+ Därefter måste du lagra den hemliga `tangenten` i en variabel.
    
    ![skärmdump](images/messages-key.png)

+ Därefter, fråga användaren för ett enda brev (kallat en `tecken`) för att kryptera.
    
    ![skärmdump](images/messages-character.png)

+ Hitta `position` av `tecken`.
    
    ![skärmdump](images/messages-position.png)

+ Du kan testa det lagrade `läget` genom att skriva ut det. Till exempel är det tecknet "e" i position 4 i alfabetet.
    
    ![skärmdump](images/messages-position-test.png)

+ För att kryptera `tecknet`, bör du lägga till `tangenten` till `positionen`. Detta lagras sedan i en `newPosition` variabel.
    
    ![skärmdump](images/messages-newposition.png)

+ Lägg till kod för att skriva ut den nya teckenpositionen.
    
    ![skärmdump](images/messages-newposition-print.png)

+ Testa din nya kod. Eftersom din `tangent` är 3, borde den lägga till 3 till `positionen` och lagra den i din `newPosition` variabel.
    
    Till exempel är bokstaven "e" i position 4. För att kryptera lägger du till `tangenten` (3) och ger 7.
    
    ![skärmdump](images/messages-newposition-test.png)

+ Vad händer när du försöker kryptera bokstaven "y"?
    
    ![skärmdump](images/messages-modulus-bug.png)
    
    Lägg märke till hur `newPosition` är 27, och det finns inte 27 bokstäver i alfabetet!

+ Du kan använda en `%` att berätta om den nya positionen att gå tillbaka till position 0 när den kommer till position 26.
    
    ![skärmdump](images/messages-modulus.png)

+ Slutligen vill du skriva brevet på den nya positionen.
    
    Till exempel lägger nyckeln till bokstaven "e" 7, och bokstaven i alfabetets position 7 är "h".
    
    ![skärmdump](images/messages-newcharacter.png)

+ Prova din kod. Du kan också ta bort några av dina utskriftsdeklarationer, bara skriva ut den nya karaktären i slutet.
    
    ![skärmdump](images/messages-enc-test.png)