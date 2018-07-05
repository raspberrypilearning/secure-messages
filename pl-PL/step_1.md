## Wprowadzenie:

W tym projekcie dowiesz się, jak stworzyć swój własny program szyfrujący, aby wysyłać i odbierać tajne wiadomości z przyjacielem. Ten projekt jest powiązany z działaniem "Ziemia do Principy" na stronie 16 Dziennika Przestrzeni.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/402256078c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

### Dodatkowe informacje dla liderów klubu

Jeśli potrzebujesz wydrukować ten projekt, użyj [Wersja dla drukarek](https://projects.raspberrypi.org/en/projects/secret-messages/print).

## \--- collapse \---

## title: Notatki prowadzącego klub

## Wprowadzenie:

W tym projekcie dzieci dowiedzą się, jak stworzyć program szyfrujący, aby wysyłać i otrzymywać tajne wiadomości z przyjacielem. Ten projekt wprowadza iterację (pętlę) na ciągu tekstowym.

## Zasoby Online

**Ten projekt używa języka Python 3.** Zalecamy użycie edytora [trinket](https://trinket.io/) do pisania kodu w Pythonie online. Ten projekt zawiera następujące edytory Trinket:

* [Nowy (pusty) Python Trinket -- jumpto.cc/python-new](http://jumpto.cc/python-new)

Dostępny jest też szablon zawierający ukończony projekt:

* [Ukończono "Sekretne wiadomości" -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

* ['Kalkulator przyjaźni' Zakończony -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## Zasoby Offline

Ten projekt można także [wykonać offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/).

Możesz znaleźć ukończony projekt w sekcji "Zasoby dla wolontariuszy", która zawiera:

* wiadomości-zakończone/messages.py
* wiadomości-zakończone/friends.py

(Wszystkie powyższe zasoby można również pobrać jako pliki `.zip`.)

## Cele dydaktyczne

* Iteracja (zapętlanie) nad zmienną napisową;
* Metoda `find()`;
* Operator modułu (`%`).

Ten projekt obejmuje elementy z następujących wątków z [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum):

* [Połącz konstrukcje programowania, aby rozwiązać problem.](https://www.raspberrypi.org/curriculum/programming/builder)

## Wyzwania

* Użyj szyfru Cezara - szyfruj i odszyfrowuj litery i słowa ręcznie;
* Klucze zmiennej - pozwalają użytkownikowi wprowadzić wybrany klucz;
* Szyfrowanie i odszyfrowywanie wiadomości - szyfrowanie i odszyfrowywanie całych wiadomości;
* Kalkulator przyjaźni - zastosowanie iteracji tekstowej do nowego problemu.

## Najczęściej Zadawane Pytania

* Podczas wyszukiwania za pomocą `find()` lub `jeśli litera jest w alfabecie:` zauważ, że w wyszukiwaniach rozróżniana jest wielkość liter. Dzieci mogą użyć:
    
    ```python
    wiadomość = input("Proszę wprowadzić wiadomość do zaszyfrowania:").lower()
    ```
    
    aby wprowadzić małe litery przed wyszukiwaniem.

\--- /collapse \---

## \--- collapse \---

## title: Materiały do projektu

## Zasoby projektu

* [Plik .zip zawierający wszystkie zasoby potrzebne do wykonania projektu](resources/secret-messages-project-resources.zip)
* [Pusty szablon Trinket do języka Python online](http://jumpto.cc/python-new)
* [Pusty plik Python offline](resources/new-new.py)

## Zasoby dla lidera klubu

* [Plik .zip zawierający zasoby z ukończonym projektem](resources/secret-messages-volunteer-resources.zip)
* [Ukończony projekt Trinket online](https://trinket.io/python/402256078c)
* [tajne-wiadomości-zakończone/messages.py](resources/secret-messages-finished-messages.py)
* [Ukończono online wyzwanie 'Kalkulator przyjaźni'](https://trinket.io/python/2e852cd687)
* [ukończono offline wyzwanie 'Kalkulator przyjaźni'](resources/friendship-calculator-finished-friends.py)

\--- /collapse \---