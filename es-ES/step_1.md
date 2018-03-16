## Introducción:

A través de este proyecto aprenderás a crear tu propio programa de encriptación para intercambiar mensajes secretos con tus amigos. Este proyecto está relacionado con la actividad "Tierra a Principia" de la página 16 del Diario Espacial.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/402256078c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

## Recursos en línea

__Este proyecto usa Python 3.__ Recomendamos usar [trinket](https://trinket.io/) para escribir Python online. Este proyecto contiene los siguientes Trinkets:

+ [Trinket de Python nuevo (en blanco) -- jumpto.cc/python-new](http://jumpto.cc/python-new)

Existe igualmente un trinket que contiene el proyecto terminado:

+ ['Mensajes secretos" terminado -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

+ ['Calculadora de amistad" terminado -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## Recursos offline
Este proyecto puede completarse igualmente [offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/).

Encontrarás el proyecto terminado en la sección 'Recursos voluntarios', la cual incluye:

+ messages-finished/messages.py
+ messages-finished/friends.py

(Todos los recursos anteriores pueden descargarse igualmente como archivos de proyecto y archivos voluntarios en formato `.zip`).

## Objetivos de aprendizaje
+ Iteración (bucles) en una variable de cadena;
+ El método `find()`;
+ El operador de módulo (`%`).

Este proyecto cubre elementos de los siguientes hilos del [Programa digital de Raspberry Pi](http://rpf.io/curriculum):

+ [Combina construcciones de programación para resolver un problema.](https://www.raspberrypi.org/curriculum/programming/builder)

## Retos
+ Usa el cifrado Cesar - cifra y descifra letras y palabras manualmente;
+ Claves de variable - permitir al usuario que introduzca la clave seleccionada;
+ Cifrar y descifrar mensajes - cifrar y descifrar mensajes completos;
+ Calculadora de amistad - aplicación de iteración de texto a un nuevo problema.

## Preguntas frecuentes
+ Al buscar usando `find()` o `if char in alphabet:`, tenga en cuenta que las búsquedas distinguen entre el uso de mayúsculas y minúsculas. Los niños pueden usar:

	```python
	message = input("Introducir mensaje a encriptar: ").lower()
	```

	de modo que la entrada se encuentre en letras minúsculas antes de comenzar la búsqueda.
