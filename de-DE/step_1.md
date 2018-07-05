## Einführung:

In diesem Projekt lernst du, wie du dein eigenes Verschlüsselungsprogramm erstellen kannst, damit du mit einem Freund geheime Mitteilungen austauschen kannst (senden und empfangen). Dieses Projekt ist mit der Aktivität „Erde an Principia“ auf Seite 16 im Weltraumtagebuch verknüpft.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/402256078c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

### Zusätzliche Informationen für Gruppenleiter

Falls du dieses Projekt ausdrucken musst, verwende die [druckerfreundliche Version](https://projects.raspberrypi.org/en/projects/secret-messages/print).

## \--- collapse \---

## title: Hinweise für Gruppenleiter

## Einführung:

In diesem Projekt lernen Kinder, wie man ein Verschlüsselungsprogramm erstellt, um geheime Nachrichten mit einem Freund zu senden und zu empfangen. Dieses Projekt führt eine Iteration (Schleifenbildung) über eine Textzeichenfolge ein.

## Online-Ressourcen

** Dieses Projekt verwendet Python 3. ** Wir empfehlen die Verwendung von [ trinket ](https://trinket.io/), um Python online zu schreiben. Dieses Projekt enthält die folgenden trinkets:

* [Neues (leeres) Python tinket - jumpto.cc/python-new](http://jumpto.cc/python-new)

Außerdem ist ein trinket mit dem fertig gestellten Projekt verfügbar:

* [‘Secret Messages’ Finished -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

* [‘Friendship Calculator’ Finished -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## Offline-Ressourcen

Dieses Projekt kann [offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) durchgeführt werden, falls gewünscht.

Eine vollständige Version dieses Projekts finden Sie auch im Abschnitt "Freiwillige Ressourcen". Diese enthält:

* messages-finished/messages.py
* messages-finished/friends.py

(Alle oben genannten Ressourcen werden auch zum Download als .zip-Dateien bereitgestellt.)

## Lernziele

* Iteration (Schleifen) über eine String-Variable;
* Die `find()` Methode;
* Der Modulo-Operator (`%`).

Dieses Projekt umfasst Elemente aus den folgenden Teilen des [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum):

* [Kombiniere Programmierkonstrukte, um ein Problem zu lösen.](https://www.raspberrypi.org/curriculum/programming/builder)

## Aufgaben

* Verwende eine Caesar-Chiffre - manuelles Verschlüsseln und Entschlüsseln von Buchstaben und Wörter;
* Variable Schlüssel (key) - erlaubt dem Benutzer, einen selbst gewählten Schlüssel einzugeben;
* Verschlüsseln und Entschlüsseln von Texten - Verschlüsseln und Entschlüsseln ganzer Nachrichten;
* Freundschaftsrechner - Text-Iteration auf ein neues Problem anwenden.

## Häufig gestellte Fragen

* Bei der Suche mit ` find () ` oder ` if char in alphabet: `: Beachte dass bei der Suche die Groß- und Kleinschreibung berücksichtigt wird. Kinder können folgendes benutzen:
    
    ```python
    text = input('Gib hier deinen Text ein: ').lower()
    ```
    
    um die Eingabe vor der Suche in Kleinbuchstaben umzuwandeln.

\--- /collapse \---

## \--- collapse \---

## title: Projektmaterialien

## Projektressourcen

* [.zip-Datei, die alle Projektressourcen enthält](resources/secret-messages-project-resources.zip)
* [Online leeres Python 'trinket'](http://jumpto.cc/python-new)
* [Offline leere Python-Datei](resources/new-new.py)

## Ressourcen für Gruppenleiter

* [.zip-Datei, die alle fertig gestellten Projektressourcen enthält](resources/secret-messages-volunteer-resources.zip)
* [Online fertig gestelltes (Beispiel-) Trinket-Projekt](https://trinket.io/python/402256078c)
* [secret-messages-finished/messages.py](resources/secret-messages-finished-messages.py)
* [Online abgeschlossene Aufgabe 'Freundschaftsrechner'](https://trinket.io/python/2e852cd687)
* [offline abgeschlossene Aufgabe 'Freundschaftsrechner'](resources/friendship-calculator-finished-friends.py)

\--- /collapse \---