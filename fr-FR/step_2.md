## Le Code de Caesar

Un chiffre (en cryptologie) est un type de code secret, où tu inverses des lettres pour que personne ne puisse lire ton message.

Tu vas utiliser une des formes de chiffrement les plus anciennes et les mieux connues au monde, le __Code de Caesar__ (Caesar Cipher en anglais), qui fait référence à Jules Caesar.

Avant de commencer à coder, essayons d'utiliser le Code de Caesar pour cacher un mot.

+ Le fait de cacher un mot s'appelle le __cryptage__.

	Commençons par le cryptage de la lettre 'a'. Pour ce faire, nous pouvons écrire l'alphabet dans un cercle, comme ci--après :

	![capture d'écran](images/messages-wheel.png)

+ Pour transformer une lettre normale dans une lettre chiffrée, il te faut une clé secrète. Utilisons par exemple le chiffre 3 comme clé (mais tu peux utiliser n'importe lequel chiffre que tu veux).

	Pour __chiffrer__ la lettre 'a', tout simplement tu bouges les lettres de 3 places dans le sens d'une montre, ce qui vous donnera la lettre 'd' :

	![capture d'écran](images/messages-wheel-eg.png)

+ Tu peux utiliser ce que tu as appris pour chiffrer un mot entier. Par exemple, 'hello' après chiffrement donne 'khoor'. Essaie-le toi-même.

	+ h + 3 = __k__
	+ e + 3 = __h__
	+ l + 3 = __o__
	+ l + 3 = __o__
	+ o + 3 = __r__

+ Revenir vers le texte d'origine s'appelle __décryptage__. Pour déchiffrer un mot, il suffit de soustraire la clé au lieu de l'ajouter :

	+ k - 3 = __h__
	+ h - 3 = __e__
	+ o - 3 = __l__
	+ o - 3 = __l__
	+ r - 3 = __o__
