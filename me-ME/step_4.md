## Šifrovanje slova

Napišimo Python program za šifrovanje jednog znaka.

+ Otvori prazan Python šablon u Trinketu: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Umjesto da crtamo abecedu u krugu, napišimo je kao promjenljivu `abeceda`.
    
    ![screenshot](images/messages-alphabet.png)

+ Svako slovo abecede ima svoju poziciju, počevši od pozicije 0. Dakle, slovo 'a' je na poziciji 0 abecede, a 'c' je na poziciji 2.
    
    ![screenshot](images/messages-array.png)

+ Možeš da ispišeš slovo koje se nalazi u promjenljivoj `abeceda` tako što ćeš upisati njegovu poziciju unutar uglastih zagrada.
    
    ![screenshot](images/messages-alphabet-array.png)
    
    Kada ovo isprobaš, možeš da izbrišeš naredbe `print`.

+ Zatim treba da sačuvaš tajni `ključ` u promjenljivoj.
    
    ![screenshot](images/messages-key.png)

+ Sada pitaj korisnika da unese jedno slovo (odnosno `znak`) koji će biti šifrovan.
    
    ![screenshot](images/messages-character.png)

+ Pronađi `poziciju` tog `znaka`.
    
    ![screenshot](images/messages-position.png)

+ Možeš da isprobaš sačuvanu `poziciju` tako što ćeš je ispisati. Na primjer, provjeri da li je znak 'e' na poziciji 4 u abecedi.
    
    ![screenshot](images/messages-position-test.png)

+ Za šifrovanje `znaka` treba `poziciji` da dodaš `ključ`. Zatim to sačuvaj u promjenljivoj `novaPozicija`.
    
    ![screenshot](images/messages-newposition.png)

+ Dodaj kôd kojim ćeš ispisati novu poziciju znaka.
    
    ![screenshot](images/messages-newposition-print.png)

+ Isprobaj svoj novi kôd. Pošto je tvoj `ključ` broj 3, `poziciji` bi trebalo da bude dodat broj 3, a zatim sačuvan u tvojoj promjenljivoj `novaPozicija`.
    
    Na primjer, slovo 'e' je na poziciji 4. Da ga šifruješ, dodaješ `ključ` (3), što daje 7.
    
    ![screenshot](images/messages-newposition-test.png)

+ Šta se dešava kada pokušaš da šifruješ slovo 'y'?
    
    ![screenshot](images/messages-modulus-bug.png)
    
    Primjećuješ li da je `novaPozicija` 27, a u engleskoj abecedi nema 27 slova!

+ Možeš da koristiš `%` kako bi se nova pozicija, nakon što dođe do pozicije 26, vratila na poziciju 0.
    
    ![screenshot](images/messages-modulus.png)

+ Na kraju, želimo da ispišemo slovo koje se nalazi na novoj poziciji.
    
    Na primjer, kada dodamo ključ slovu 'e' dobićemo 7, a slovo koje se nalazi na poziciji 7 u abecedi je 'h'.
    
    ![screenshot](images/messages-newcharacter.png)

+ Isprobaj svoj kôd. Možeš i da ukloniš neke od svojih print naredbi i da ispišeš samo novi znak na kraju.
    
    ![screenshot](images/messages-enc-test.png)