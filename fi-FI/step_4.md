## Kirjeiden salaaminen

Kirjoita Python-ohjelma salakirjoittamaan yksittäinen merkki.

+ Avaa tyhjä Python-mallipohja Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Piirretään aakkosia ympyrään kirjoittamalla sen `alfanmuunnelmaksi`.
    
    ![kuvakaappaus](images/messages-alphabet.png)

+ Jokaisella aakkosten kirjaimella on paikka, joka alkaa paikasta 0. Niinpä kirjain "a" on aakkoston sijainnissa 0 ja "c" on kohdassa 2.
    
    ![kuvakaappaus](images/messages-array.png)

+ Voit saada kirjeen `aakkosen` muuttujasta kirjoittamalla sijainnin hakasulkeissa.
    
    ![kuvakaappaus](images/messages-alphabet-array.png)
    
    Voit poistaa `tulostaa` lauseketta, kun olet kokeillut tätä.

+ Seuraavaksi sinun on tallennettava salainen `avain` muuttujaan.
    
    ![kuvakaappaus](images/messages-key.png)

+ Seuraavaksi pyydä käyttäjää kirjoittamaan yksi kirjain (kutsutaan `merkiksi`) salaamaan.
    
    ![kuvakaappaus](images/messages-character.png)

+ Etsi `asema` `merkistä`.
    
    ![kuvakaappaus](images/messages-position.png)

+ Voit testata tallennetun `aseman` tulostamalla. Esimerkiksi kyseinen merkki "e" on kirjaimella 4.
    
    ![kuvakaappaus](images/messages-position-test.png)

+ Salaa `merkki`, lisää `näppäimistö` `asemaan`. Sitten tämä tallennetaan `newPosition` -muuttujalle.
    
    ![kuvakaappaus](images/messages-newposition.png)

+ Lisää koodi, jos haluat tulostaa uuden merkin sijainnin.
    
    ![kuvakaappaus](images/messages-newposition-print.png)

+ Testaa uusi koodi. Koska `näppäin` on 3, sen pitäisi lisätä 3 `asemaan` ja tallentaa sen `uutta positiota` -muuttujaan.
    
    Esimerkiksi kirjain "e" on kohdassa 4. Salaamiseksi lisäät `näppäimen` (3), antamalla 7.
    
    ![kuvakaappaus](images/messages-newposition-test.png)

+ Mitä tapahtuu, kun yrität salata kirjaimen "y"?
    
    ![kuvakaappaus](images/messages-modulus-bug.png)
    
    Huomaa, miten `newPosition` on 27, eikä aakkossa ole 27 kirjainta!

+ Voit käyttää `%` kertoa uuden sijainnin palataksesi asentoon 0, kun se siirtyy kohtaan 26.
    
    ![kuvakaappaus](images/messages-modulus.png)

+ Lopuksi haluat tulostaa kirjeen uuteen paikkaan.
    
    Esimerkiksi lisäämällä avain kirjaimeen "e" saadaan 7, ja aakkoksen kirjaimella 7 on kirjain "h".
    
    ![kuvakaappaus](images/messages-newcharacter.png)

+ Kokeile koodia. Voit myös poistaa joitakin tulostusilmoituksia, vain tulostaa uuden merkin loppuun.
    
    ![kuvakaappaus](images/messages-enc-test.png)