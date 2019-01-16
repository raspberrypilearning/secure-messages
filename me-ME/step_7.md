## Dodatni znakovi

Neki znakovi se ne nalaze u abecedi, što uzrokuje grešku.

+ Isprobaj svoj kôd koristeći nekoliko znakova koji se ne nalaze u abecedi.
    
    Na primjer, možeš da upotrijebiš poruku `hej zdravo!!`.
    
    ![screenshot](images/messages-extra-characters.png)
    
    Primijetićeš da su razmak i znak uzvika `!` šifrovani kao slovo 'c'!

+ Da bismo to popravili, program treba da šifruje znak samo ako se nalazi u abecedi. To ćeš napraviti tako što ćeš svom kôdu dodati `if` naredbu, a ostatak kôda uvući.
    
    ![screenshot](images/messages-if.png)

+ Isprobaj svoj kôd koristeći istu poruku. Šta se dešava ovaj put?
    
    ![screenshot](images/messages-if-test.png)
    
    Sada tvoj kôd jednostavno preskače svaki znak koji se ne nalazi u abecedi.

+ Najbolje bi bilo da tvoj kôd ne šifruje znakove koji nisu u abecedi, već jednostavno koristi izvorni znak.
    
    Svom kôdu dodaj `else` naredbu koja će dodati izvorni znak šifrovanoj poruci.
    
    ![screenshot](images/messages-else.png)

+ Isprobaj svoj kôd. Trebalo bi da svi znakovi abecede budu šifrovani, a ostali znakovi da budu u svom izvornom obliku!
    
    ![screenshot](images/messages-else-test.png)