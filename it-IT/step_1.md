## Introduzione:

In questo progetto, imparerai come creare il tuo programma di crittografia, per scambiare messaggi segreti con un amico. This project ties in with the "Earth to Principia" activity on page 16 of the Space Diary.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/d01021756f?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

### Ulteriori informazioni per gli organizzatori dei club

Se intendete stampare questo progetto, cliccate su [Versione stampabile](https://projects.raspberrypi.org/it-IT/projects/secret-messages/print).

--- collapse ---
---
title: Note per i leader del club
---
## Introduzione:

In questo progetto, i bambini impareranno come creare un programma di crittografia, per scambiare messaggi segreti con un amico. Questo progetto introduce l'iterazione (looping) su una stringa di testo.

## Risorse online

**Questo progetto utilizza Python 3.** Consigliamo di utilizzare [Trinket](https://trinket.io/) per scrivere in linguaggio Python online:

* [Nuovo (vuoto) Python Trinket -- jumpto.cc/python-new](http://jumpto.cc/python-new)

C'è anche un file su Trinket contenente il progetto finito:

* ['Messaggi segreti' Finito - trinket.io/python/d01021756f](https://trinket.io/python/d01021756f)

* ['Calcolatrice dell'amicizia' Finito - trinket.io/python/676f1929aa](https://trinket.io/python/676f1929aa)

## Risorse offline

Questo progetto può anche essere [completato offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/).

Potete anche trovare una versione completa di questo progetto nella sezione 'Risorse per i volontari', che contiene:

* messages-finished/messages.py
* messages-finished/friends.py

(Tutte le risorse sopracitate sono anche scaricabili come file progetto e volontario `.zip `.)

## Obiettivi di apprendimento

* Iterazione (looping) su una variabile stringa;
* Il metodo `find()`;
* L'operatore modulo (`%`).

Questo progetto include elementi tratti dalle seguenti componenti del [Digital Making Curriculum di Raspberry Pi](http://rpf.io/curriculum):

* [Combinare i costrutti base di un linguaggio di programmazione per risolvere un problema.](https://www.raspberrypi.org/curriculum/programming/builder)

## Sfide

* Usa un cifrario di Cesare: cripta e decripta lettere e parole manualmente;
* Chiavi variabili: consentono all'utente di inserire una chiave a scelta;
* Criptare e decriptare messaggi - criptare e decriptare interi messaggi;
* Calcolatrice dell'amicizia - applica l'iterazione del testo a un nuovo problema.

## Domande frequenti

* Durante la ricerca con `find()` o `if lettera in alfabeto:`, nota che le ricerche fanno distinzione tra maiuscole e minuscole. I bambini possono usare:
    
    ```python
    messaggio = input("Inserisci un messaggio da criptare:").lower()
    ```
    
    per convertire l'input in minuscolo prima della ricerca.

--- /collapse ---

--- collapse ---
---
title: Materiali del progetto
---
## Risorse del progetto

* [File .zip con tutte le risorse del progetto](resources/secret-messages-project-resources.zip)
* [Trinket online vuoto per Python](http://jumpto.cc/python-new)
* [File vuoto da scaricare per Python](resources/new-new.py)

## Risorse per gli organizzatori del club

* [File .zip con tutte le risorse del progetto completate](resources/secret-messages-volunteer-resources.zip)
* [Trinket online completato](https://trinket.io/python/d01021756f)
* [secret-messages-finished/messages.py](resources/secret-messages-finished-messages.py)
* [Sfida "Calcolatrice dell'amicizia" completata online](https://trinket.io/python/676f1929aa)
* [sfida "Calcolatrice dell'amicizia" completa da scaricare](resources/friendship-calculator-finished-friends.py)

--- /collapse ---