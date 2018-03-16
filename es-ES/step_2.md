## El cifrado Cesar

Un cifrado es un tipo de código secreto en el que  las letras se cambian de posición de modo que nadie pueda leer el contenido del mensaje.

Usarás uno de los cifrados más antiguos y famosos, el __cifrado Cesar__, en nombre de Julio Cesar, 

Antes de comenzar la codificación, intentemos usar el cifrado Cesar para ocultar una palabra.

+ Ocultar palabras se denomina __encriptación__.

	Comencemos encriptando la letra 'a'. Para ello, podemos dibujar el abecedario en un círculo, de este modo:

	![screenshot](images/messages-wheel.png)

+ Para crear una letra encriptada secreta a partir de una normal, necesitarás una clave secreta. Usemos el número 3 como la clave (aunque puedes usar cualquier número que desees).

	Para __encriptar__ la letra 'a', simplemente avanza 3 letras en sentido horario, y obtendrás la letra 'd':

	![screenshot](images/messages-wheel-eg.png)

+ Puedes usar lo que has aprendido para encriptar una palabra completa. Por ejemplo, 'hello' encriptado es 'khoor'. Pruébalo.

	+ h + 3 = __k__
	+ e + 3 = __h__
	+ l + 3 = __o__
	+ l + 3 = __o__
	+ o + 3 = __r__

+ Devolver el texto a la normalidad se denomina __descodificación__. Para descodificar una palabra, simplemente resta la clave en lugar de añadirla.

	+ k - 3 = __h__
	+ h - 3 = __e__
	+ o - 3 = __l__
	+ o - 3 = __l__
	+ r - 3 = __o__	
