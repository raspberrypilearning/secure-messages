## Dodatni znakovi

Neki se znakovi ne nalaze u abecedi što uzrokuje grešku.

+ Isprobaj kako radi tvoj kôd kada koristiš neke znakove koji se ne nalaze u abecedi.
    
    Primjerice, možeš napisati poruku `hej bok!!`.
    
    ![screenshot](images/messages-extra-characters.png)
    
    Primijeti da su razmak i znak uskličnika `!` šifrirani kao slovo 'c'!

+ Da bi ovo popravio, program mora prevoditi znak samo ako se nalazi u abecedi. To ćeš popraviti dodavanjem `if` naredbe u kôd i uvlačenjem ostatka kôda.
    
    ![screenshot](images/messages-if.png)

+ Testiraj kôd koristeći istu poruku kao prije. Što se ovaj put događa?
    
    ![screenshot](images/messages-if-test.png)
    
    Sada tvoj kôd preskače svaki znak koji nije u abecedi.

+ Najbolje bi bilo kada tvoj kôd ne bi šifrirao ništa što nije u abecedi, nego jednostavno koristio originalan znak.
    
    Kôdu dodaj `else` naredbu koja će dodati originalni znak šifriranoj poruci.
    
    ![screenshot](images/messages-else.png)

+ Testiraj kôd. Svi znakovi abecede trebali bi biti šifrirani, dok su svi ostali znakovi u originalnom obliku!
    
    ![screenshot](images/messages-else-test.png)