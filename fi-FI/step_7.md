## Lisämerkkejä

Jotkut merkit eivät ole aakkosissa, mikä aiheuttaa virheen.

+ Testaa koodisi joitain merkkejä, jotka eivät ole aakkosissa.
    
    Voit esimerkiksi käyttää viestiä `hi there !!`.
    
    ![kuvakaappaus](images/messages-extra-characters.png)
    
    Huomaa, että tila ja `!` merkkiä on kaikki salattuna kirjaimella "c"!

+ Korjaa tämä, haluat vain kääntää merkin, jos se on aakkosissa. Voit tehdä tämän lisäämällä koodi `if` ja koodattaaksesi loput koodista.
    
    ![kuvakaappaus](images/messages-if.png)

+ Testaa koodi samalla viestillä. Mitä tapahtuu tällä kertaa?
    
    ![kuvakaappaus](images/messages-if-test.png)
    
    Nyt koodi vain ohittaa merkin, jos se ei ole aakkosissa.

+ Olisi parempi, jos koodisi ei salannut mitään aakkosissa, vaan käytti vain alkuperäistä luonnetta.
    
    Lisää `else` -lausunto koodisi, joka vain lisää alkuperäisen merkin salattuun viestiin.
    
    ![kuvakaappaus](images/messages-else.png)

+ Testaa koodi. Sinun pitäisi nähdä, että jokainen merkki aakkosissa on salattu, mutta kaikki muut merkit jäävät yksin!
    
    ![kuvakaappaus](images/messages-else-test.png)