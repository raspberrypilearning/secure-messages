## Uvod:

U ovom projektu naučit ćeš kako napraviti vlastiti program za šifriranje te poslati tajne poruke prijatelju i primiti tajne poruke od prijatelja. Ovaj projekt povezan je s aktivnošću "Earth to Principia" koja se nalazi na stranici 16 web stranice Space Diary.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/402256078c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

### Dodatne informacije za voditelje kluba

Ako želite ispisati ovaj projekt, molimo Vas da koristite [verziju koja je prilagođena za ispis](https://projects.raspberrypi.org/en/projects/secret-messages/print).

## \--- collapse \---

## title: Bilješke za voditelja kluba

## Uvod:

U ovom projektu djeca će naučiti kako napraviti program za šifriranje poruka te izmjenjivati tajne poruke s prijateljem. U projektu se koristi ponavljanje (petlja) nad tekstualnim podacima.

## Online izvori

**U ovom projektu koristi se Python 3.** Predlažemo korištenje [trinketa](https://trinket.io/) za online pisanje u Pythonu. Projekt sadrži sljedeće Trinkete:

* [Novi (prazni) Python Trinket -- jumpto.cc/python-new](http://jumpto.cc/python-new)

Također je uključen i trinket koji sadrži dovršeni projekt:

* [‘Secret Messages’ dovršeni projekt -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

* [‘Friendship Calculator’ dovršeni projekt -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## Offline izvori

Ako želite, ovaj projekt može biti [završen offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/).

Dovršenu verziju projekta možete pronaći i u odjeljku 'Resursi za volontere' koji sadrži:

* messages-finished/messages.py
* messages-finished/friends.py

(Svi spomenuti materijali nalaze se u materijalima projekta i materijalima za volontere, koje je moguće preuzeti kao `.zip` datoteke.)

## Ishodi učenja

* Korištenje naredbi ponavljanja (petlji) nad nizovima znakova;
* Korištenje `find()` metode;
* Korištenje modularnog operatora (`%`).

Ovaj projekt pokriva elemente iz sljedećih dijelova plana i programa [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum):

* [Uporaba različitih programskih struktura za rješavanje problema.](https://www.raspberrypi.org/curriculum/programming/builder)

## Izazovi

* Isprobaj Cezarovu šifru - ručno šifriranje i dešifriranje slova i riječi;
* Promjenjivi ključevi - korisnik unosi odabrani ključ;
* Šifriranje i dešifriranje poruka - šifriranje i dešifriranje cijelih poruka;
* Kalkulator prijateljstva - primjena naredbi ponavljanja nad tekstom na novi problem.

## Često postavljana pitanja

* Prilikom pretraživanja pomoću `find()` ili `if char in alphabet:`, imajte na umu da su metode osjetljive na velika i mala slova. Djeca mogu koristiti:
    
    ```python
    message = input("Unesi poruku za šifriranje: ").lower()
    ```
    
    kako bi unos bio napisan malim slovima prilikom pretrage.

\--- /collapse \---

## \--- collapse \---

## title: Materijali projekta

## Resursi projekta

* [.zip datoteka koja sadrži sve materijale projekta](resources/secret-messages-project-resources.zip)
* [Prazan online Python Trinket](http://jumpto.cc/python-new)
* [Prazna Offline Python datoteka](resources/new-new.py)

## Materijali za voditelja Kluba

* [.zip datoteka koja sadrži sve dovršene materijale projekta](resources/secret-messages-volunteer-resources.zip)
* [Dovršeni online Trinket projekt](https://trinket.io/python/402256078c)
* [secret-messages-finished/messages.py](resources/secret-messages-finished-messages.py)
* [Dovršeni online izazov 'Kalkulator prijateljstva'](https://trinket.io/python/2e852cd687)
* [dovršeni offline izazov 'Kalkulator prijateljstva'](resources/friendship-calculator-finished-friends.py)

\--- /collapse \---