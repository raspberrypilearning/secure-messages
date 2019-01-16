## Šifrovanje cijelih poruka

Podesimo program da šifruje cijele poruke, umjesto da šifruje i dešifruje jedan po jedan znak!

+ Prvo provjeri da li tvoj kôd izgleda ovako:
    
    ![screenshot](images/messages-character-finished.png)

+ Kreiraj promjenljivu u kojoj ćeš sačuvati novu šifrovanu poruku.
    
    ![screenshot](images/messages-newmessage.png)

+ Izmijeni svoj kôd tako da sačuva korisnikovu poruku, a ne samo jedan znak.
    
    ![screenshot](images/messages-message.png)

+ Svom kôdu dodaj `for` petlju, a zatim uvuci ostatak kôda kako bi se ponavljao za svaki znak poruke.
    
    ![screenshot](images/messages-loop.png)

+ Isprobaj svoj kôd. Trebalo bi da se znakovi poruke šifruju i ispisuju jedan po jedan.
    
    ![screenshot](images/messages-loop-test.png)

+ Dodajmo svaki šifrovani znak u promjenljivu `novaPoruka`.
    
    ![screenshot](images/messges-message-add-character.png)

+ Koristeći naredbu `print`, možeš da ispišeš promjenljivu `novaPoruka` dok se šifruje.
    
    ![screenshot](images/messages-print-message-characters.png)

+ Ako izbrišeš razmake prije naredbe `print`, šifrovana poruka biće prikazana samo jednom na kraju. Možeš da izbrišeš i kôd za ispisivanje pozicija znakova.
    
    ![screenshot](images/messages-print-message-comment.png)