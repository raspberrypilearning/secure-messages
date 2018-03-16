## Crytpage de lettres

Écrivons un programme Python pour chiffrer un seul caractère.

+ Ouvre le modèle Trinket vierge pour Python : <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Au lieu de dessiner l'alphabet dans un cercle, écrivons-le comme une variable `alphabet`.

	![capture d'écran](images/messages-alphabet.png)

+ Chaque lettre de l'alphabet à sa position, commençant par position 0. Donc la lettre 'a' est à la position 0 de l'alphabet, et 'c' est à la position 2.

	![capture d'écran](images/messages-array.png)

+ Tu peux chercher une lettre à partir de ta variable `alphabet` en écrivant la position entre des paranthèses carrées.

	![capture d'écran](images/messages-alphabet-array.png)

	Tu peux supprimer les déclarations `print` une fois le code testé.

+ Ensuite, tu auras besoin de stocker la `clé` secrète dans une variable.

	![capture d'écran](images/messages-key.png)

+ Puis demande à l'utilisateur de donner une seule lettre (ici considérée comme un `caractère`) à chiffrer.

	![capture d'écran](images/messages-character.png)

+ Trouve la `position` du `caractère`.

	![capture d'écran](images/messages-position.png)

+ Tu peux tester la `position` stockée en l'imprimant à l'écran. Par exemple, que le caractère 'e' se trouve à la position 4 dans l'alphabet.

	![capture d'écran](images/messages-position-test.png)

+ Pour chiffre le `caractère`, tu devrais ajouter la `clé` à la `position`.

	![capture d'écran](images/messages-newposition.png)

+ Teste ton nouveau code. Puisque ta `key` est 3, ça devrait ajouter 3 à la `position` et le stocker dans une variable `newPosition`.

+ Que se passe-t-il si tu essaies de chiffrer la lettre 'y' ?

	![capture d'écran](images/messages-modulus-bug.png)

	Tu peux remarquer comme la `newPosition` est d'une valeur 27, mais il n'y a pas 27 lettres dans l'alphabet !

+ Tu peux utiliser un symbole `%` pour diren à la nouvelle position de retourner à 0 après la position 26.

	![capture d'écran](images/messages-modulus.png)

+ Enfin, tu veux imprimer la lettre à la nouvelle position.

	Par exemple, ajoutant la clé à la lettre 'e' nous donne 7, et la lettre à position 7  de l'alphabet est 'h'.

	![capture d'écran](images/messages-newcharacter.png)

+ Teste ton code. Tu peux aussi enlever certains des déclarations "print" en imprimant seulement le nouveau caractère à la fin.

	![capture d'écran](images/messages-enc-test.png)
