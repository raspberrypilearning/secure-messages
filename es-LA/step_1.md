## Introducción:

En este proyecto, aprenderás cómo hacer tu propio programa de cifrado, para enviar y recibir mensajes secretos con un amigo. Este proyecto se enlaza con la actividad "Earth to Principia" en la página 16 del "Space Diary".

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/402256078c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

### Información adicional para los líderes del club

Si necesitas imprimir este proyecto, usa la [versión para imprimir](https://projects.raspberrypi.org/en/projects/secret-messages/print).

## \--- collapse \---

## title: Notas para el líder del club

## Introducción:

En este proyecto, los niños aprenderán a hacer un programa de cifrado, a enviar y recibir mensajes secretos con un amigo. Este proyecto introduce iteración (bucle) sobre una cadena de texto.

## Online Resources

**This project uses Python 3.** We recommend using [trinket](https://trinket.io/) to write Python online. This project contains the following Trinkets:

* [New (blank) Python Trinket -- jumpto.cc/python-new](http://jumpto.cc/python-new)

There is also a trinket containing the finished project:

* [‘Secret Messages’ Finished -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

* [‘Friendship Calculator’ Finished -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## Recursos sin conexión

This project can be [completed offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) if preferred.

You can find the completed project in the 'Volunteer Resources' section, which contains:

* messages-finished/messages.py
* messages-finished/friends.py

(Todos los recursos anteriores también se pueden descargar como archivos `.zip` de proyectos y para voluntarios.)

## Objetivos del Aprendizaje

* Iteration (looping) over a string variable;
* The `find()` method;
* The modulus operator (`%`).

This project covers elements from the following strands of the [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum):

* [Combine programming constructs to solve a problem.](https://www.raspberrypi.org/curriculum/programming/builder)

## Desafíos

* Use a Caesar cipher - encrypt and decrypt letters and words manually;
* Variable keys - allowing the user to input a chosen key;
* Encrypting and decrypting messages - encrypting and decrypting whole messages;
* Friendship calculator - applying text iteration to a new problem.

## Frequently Asked Questions

* When searching using `find()` or `if char in alphabet:`, note that searches are case-sensitive. Children can use:
    
    ```python
    message = input("Please enter a message to encrypt: ").lower()
    ```
    
    to make the input lower case before searching.

\--- /collapse \---

## \--- collapse \---

## title: Project materials

## Recursos del proyecto

* [archivo .zip que contiene todos los recursos del proyecto](resources/secret-messages-project-resources.zip)
* [Online blank Python Trinket](http://jumpto.cc/python-new)
* [Offline blank Python file](resources/new-new.py)

## Recursos del líder del club

* [archivo .zip que contiene todos los recursos del proyecto](resources/secret-messages-volunteer-resources.zip)
* [Online completed Trinket project](https://trinket.io/python/402256078c)
* [secret-messages-finished/messages.py](resources/secret-messages-finished-messages.py)
* [Online completed 'Friendship calculator' challenge](https://trinket.io/python/2e852cd687)
* [offline complete 'Friendship calculator' challenge](resources/friendship-calculator-finished-friends.py)

\--- /collapse \---