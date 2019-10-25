## Le Code de César

Un chiffrement est un type de code secret dans lequel tu permutes les lettres pour que personne ne puisse lire ton message.

Tu utiliseras l’un des plus vieux et des plus célèbres code, le **code de César**, qui porte le nom de Jules César.

Avant de commencer à coder, essayons d’utiliser le code de César pour cacher un mot.

+ Cacher un mot s'appelle un **cryptage** .
    
    Commençons par crypter la lettre 'a'. Pour ce faire, nous pouvons dessiner l'alphabet dans un cercle, comme ceci:
    
    ![capture d'écran](images/messages-wheel.png)

+ Pour créer une lettre cryptée secrète à partir d'une lettre normale, tu dois disposer d'une clé secrète. Utilisons le chiffre 3 comme clé (mais tu peux utiliser le nombre de ton choix).
    
    Pour **crypter** la lettre 'a', tu ne fais que déplacer 3 lettres dans le sens des aiguilles d'une montre, ce qui te donneras la lettre 'd':
    
    ![capture d'écran](images/messages-wheel-eg.png)

+ Tu peux utiliser ce que tu as appris pour crypter un mot entier. Par exemple, "hello" est crypté "khoor". Essaie-le par toi-même.
    
    + h + 3 = **k**
    + e + 3 = **h**
    + l + 3 = **o**
    + l + 3 = **o**
    + o + 3 = **r**

+ La normalisation du texte s'appelle **décryptage** . Pour décrypter un mot, il suffit de soustraire la clé au lieu de l’ajouter:
    
    + k - 3 = **h**
    + h - 3 = **e**
    + o - 3 = **l**
    + o - 3 = **l**
    + r - 3 = **o**