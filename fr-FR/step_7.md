## Plus de caractères

Quelques caractères ne sont pas dans l'alphabet, ce qui donne une erreur.

+ Teste ton code avec quelques caractères qui ne sont pas dans l'alphabet.

	Par exemple, tu pourrais utiliser le message `hi there!!`.

	![capture d'écran](images/messages-extra-characters.png)

	Remarque que les caractères espace et `!` sont tous chiffrés comme la lettre 'c' !

+ Afin de régler cette anomalie, tu dois seulement traduire le caractère s'il se trouve dans l'alphabet. Pour faire cela, ajoute une déclaration `if` dans ton code, et décale le reste de ton code.

	![capture d'écran](images/messages-if.png)

+ Teste ton code avec le même message. Que se passe-t-il cette fois-ci ?

	![capture d'écran](images/messages-if-test.png)

	Maintenant, ton code ignore tout caractère qui ne figure pas dans l'alphabet.

+ Ça serait mieux si ton code ne chiffrerait pas des choses qui ne sont pas dans l'alphabet, mais laissera le caractère d'origine.

	Ajoute une déclaration `else` dans ton code, qui ajoute simplement le caractère original au message chiffré.

	![capture d'écran](images/messages-else.png)

+ Teste ton code. Tu devrais voir que tout caractère se trouvant dans l'alphabet est chiffré, mais touts les autres caractères sont laissés tels quels !

	![capture d'écran](images/messages-else-test.png)
