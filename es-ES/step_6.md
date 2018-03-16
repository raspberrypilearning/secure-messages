## Encriptar mensajes completos

En lugar de cifrar y descifrar solamente mensajes de un carácter, ¡cambiemos el programa para cifrar mensajes completos!

+ En primer lugar, comprueba que tu código se parece al siguiente:

	![screenshot](images/messages-character-finished.png)

+ Crea una variable para almacenar el nuevo mensaje cifrado.

	![screenshot](images/messages-newmessage.png)

+ Cambia tu código para almacenar el mensaje del usuario y no solamente un carácter.

	![screenshot](images/messages-message.png)

+ Añade un bucle `for` a tu código y sangra el resto del código de modo que se repita para cada carácter del mensaje.

	![screenshot](images/messages-loop.png)

+ Prueba tu código. Deberías ver que cada carácter del mensaje es cifrado e impreso de uno en uno.

	![screenshot](images/messages-loop-test.png)

+ Añadamos cada carácter cifrado a la variable `newMessage`.

	![screenshot](images/messges-message-add-character.png)

+ Podrás `print` `newMessage` según se va cifrando.

	![screenshot](images/messages-print-message-characters.png)

+ Si borras los espacios antes de la sentencia `print`, el mensaje cifrado solamente se visualizará una vez al final. También puedes borrar el código de impresión de las posiciones de los caracteres.

	![screenshot](images/messages-print-message-comment.png)



