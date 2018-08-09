## Wprowadzenie:

W tym projekcie dowiesz się, jak stworzyć swój własny program szyfrujący, aby wysyłać i odbierać tajne wiadomości od przyjaciół. Ten projekt jest powiązany z zadaniem "Ziemia do Principy" na stronie 16 Dziennika Przestrzeni.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/402256078c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

### Dodatkowe informacje dla prowadzących klub

Jeśli chcesz wydrukować ten projekt, użyj [wersji do druku](https://projects.raspberrypi.org/en/projects/secret-messages/print).

## \--- collapse \---

## title: Notatki prowadzącego klub

## Wprowadzenie:

W tym projekcie dzieci dowiedzą się, jak stworzyć program szyfrujący, aby wysyłać i otrzymywać tajne wiadomości od przyjaciół. Ten projekt wprowadza iterację (pętlę) na ciągu tekstowym.

## Zasoby Online

**Ten projekt używa języka Python 3.** Zalecamy użycie edytora [trinket](https://trinket.io/) do pisania kodu w Pythonie online. Ten projekt zawiera następujące edytory Trinket:

* [Nowy (pusty) Python Trinket -- jumpto.cc/python-new](http://jumpto.cc/python-new)

Dostępny jest też szablon zawierający ukończony projekt:

* [Ukończony projekt "Tajne wiadomości" -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

* [Ukończony 'Kalkulator przyjaźni' -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## Zasoby Offline

Ten projekt można także [wykonać offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/).

Ukończony projekt można znaleźć w sekcji "Zasoby dla wolontariuszy", która zawiera:

* messages-finished/messages.py
* messages-finished/friends.py

(Wszystkie powyższe zasoby można również pobrać jako pliki `.zip`.)

## Cele dydaktyczne

* Iteracja (zapętlanie) na zmiennej napisowej;
* Metoda `find()`;
* Operator modułu (`%`).

Projekt ten obejmuje elementy z następujących wątków [Cyfrowego programu nauczania Raspberry Pi](http://rpf.io/curriculum):

* [Połącz konstrukcje programistyczne, aby rozwiązać problem.](https://www.raspberrypi.org/curriculum/programming/builder)

## Wyzwania

* Użyj szyfru Cezara - szyfruj i odszyfrowuj litery i słowa ręcznie;
* Klucz jako zmienna - pozwól użytkownikowi wprowadzić wybrany klucz;
* Szyfrowanie i odszyfrowywanie całych wiadomości;
* Kalkulator przyjaźni - zastosowanie iteracji na tekście do nowego problemu.

## Często zadawane pytania

* Podczas wyszukiwania za pomocą polecenia `find()` lub `if litera in alfabet:` trzeba pamiętać, że w wyszukiwaniach rozróżniana jest wielkość liter. Dzieci mogą użyć:
    
    ```python
    wiadomosc = input("Wprowadź wiadomość do zaszyfrowania:").lower()
    ```
    
    aby wprowadzić małe litery przed wyszukiwaniem.

\--- /collapse \---

## \--- collapse \---

## title: Materiały do projektu

## Zasoby

* [Plik .zip zawierający wszystkie zasoby potrzebne do wykonania projektu](resources/secret-messages-project-resources.zip)
* [Pusty szablon Trinket do języka Python online](http://jumpto.cc/python-new)
* [Pusty plik Python offline](resources/new-new.py)

## Zasoby dla prowadzącego klub

* [Plik .zip zawierający zasoby z ukończonym projektem](resources/secret-messages-volunteer-resources.zip)
* [Ukończony projekt Trinket online](https://trinket.io/python/402256078c)
* [secret-messages-finished/messages.py](resources/secret-messages-finished-messages.py)
* [Ukończone wyzwanie 'Kalkulator przyjaźni' dostępne online](https://trinket.io/python/2e852cd687)
* [Ukończone wyzwanie 'Kalkulator przyjaźni' dostępne offline](resources/friendship-calculator-finished-friends.py)

\--- /collapse \---