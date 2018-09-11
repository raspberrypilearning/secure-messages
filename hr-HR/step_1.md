## Uvod:

U ovom projektu naučit ćeš kako napraviti vlastiti program za šifriranje te poslati tajne poruke prijatelju i primiti tajne poruke od prjatelja. This project ties in with the "Earth to Principia" activity on page 16 of the Space Diary.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/402256078c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

### Dodatne informacije za voditelje kluba

Ako trebate ispisati ovaj projekt, koristite [verziju koja je prilagođena pisaču](https://projects.raspberrypi.org/en/projects/secret-messages/print).

## \--- collapse \---

## title: Bilješke za voditelje Kluba

## Uvod:

U ovom projektu djeca će naučiti kako napraviti program za šifriranje poruka te izmjenjivati tajne poruke s prijateljem. U projektu se koristi iteracija (petlja) nad tekstualnim podacima.

## Online izvori

**U ovom projektu koristi se Python 3.** Predlažemo korištenje [trinketa](https://trinket.io/) za online pisanje u Pythonu. Projekt sadrži sljedeće Trinkete:

* [Novi (prazan) Python Trinket -- jumpto.cc/python-new](http://jumpto.cc/python-new)

Također je uključen i trinket koji sadrži dovršeni projekt:

* [‘Secret Messages’ dovršeni projekt -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

* [‘Friendship Calculator’ dovršen projekt -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## Offline izvori

Ako želite, ovaj projekt možete [izraditi offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/).

Dovršenu verziju projekta možete pronaći i u odjeljku 'Volunteer Resources' koji sadrži:

* messages-finished/messages.py
* messages-finished/friends.py

(Svi spomenuti materijali nalaze se u materijalima projekta i materijalima za volontere, koje je moguće preuzeti kao `.zip` datoteke.)

## Ishodi učenja

* Korištenje iteracija (petlji) nad string varijablama;
* Korištenje `find()` metode;
* Korištenje modularnog operatora (`%`).

Ovaj projekt obuhvaća elemente iz sljedećih dijelova [Raspberry Pi Digital Making](http://rpf.io/curriculum) nastavnog plana i programa:

* [Uporaba različitih programskih struktura za rješavanje problema.](https://www.raspberrypi.org/curriculum/programming/builder)

## Izazovi

* Isprobaj Cezarovu šifru - ručno šifriranje i dešifriranje slova i riječi;
* Promjenjivi ključevi - korisnik unosi odabrani ključ;
* Šifriranje i dešifriranje poruka - šifriranje i dešifriranje cijelih poruka;
* Kalkulator prijateljstva - primjena iteracije nad tekstom na novi problem.

## Često postavljana pitanja

* Prilikom pretraživanja pomoću `find()` ili `if char in alphabet:`, imajte na umu da su metode osjetljive na velika i mala slova. Djeca mogu koristiti:
    
    ```python
    message = input("Unesi poruku za šifriranje: ").lower()
    ```
    
    kako bi unos bio napisan malim slovima prilikom pretrage.

\--- /collapse \---

## \--- collapse \---

## title: Materijali projekta

## Project resources

* [.zip file containing all project resources](resources/secret-messages-project-resources.zip)
* [Online blank Python Trinket](http://jumpto.cc/python-new)
* [Offline blank Python file](resources/new-new.py)

## Club leader resources

* [.zip file containing all completed project resources](resources/secret-messages-volunteer-resources.zip)
* [Online completed Trinket project](https://trinket.io/python/402256078c)
* [secret-messages-finished/messages.py](resources/secret-messages-finished-messages.py)
* [Online completed 'Friendship calculator' challenge](https://trinket.io/python/2e852cd687)
* [offline complete 'Friendship calculator' challenge](resources/friendship-calculator-finished-friends.py)

\--- /collapse \---