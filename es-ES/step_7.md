## Caracteres adicionales

Algunos caracteres no son letras del abecedario, lo cual causa un error.

+ Prueba tu código con caracteres no existentes en el abecedario.

	Por ejemplo, intenta el mensaje `hi there!!`.

	![screenshot](images/messages-extra-characters.png)

	Ten en cuenta que el espacio y los caracteres `!` son todos encriptados como la letra 'c'.

+ Para solucionarlo, necesitas traducir solamente los caracteres que estén en el abecedario. Para ello, añade una sentencia `if` a tu código y sangra el resto del código.

	![screenshot](images/messages-if.png)

+ Prueba tu código con el mismo mensaje. ¿Qué ocurre ahora?

	![screenshot](images/messages-if-test.png)

	A continuación, tu código simplemente omite los caracteres que no forman parte del abecedario.

+ Idealmente, tu código no cifrará nada que no sea parte del abecedario y, por el contrario, usará el carácter original.

	Añade una sentencia `else` a tu código para que el carácter original sea añadido al mensaje cifrado.

	![screenshot](images/messages-else.png)

+ Prueba tu código. Deberías ver cómo las letras del abecedario son encriptadas pero el resto de caracteres permanecen tal cual.

	![screenshot](images/messages-else-test.png)

