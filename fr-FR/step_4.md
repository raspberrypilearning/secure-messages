## Crypter des lettres

Écrivons un programme Python pour crypter un seul caractère.

+ Ouvre le modèle de Trinket Python vierge: <a href="https://trinket.io/python/b77c089d40" target="_blank">trinket.io/python/b77c089d40</a>.

+ Au lieu de dessiner l'alphabet dans un cercle, écrivons-le comme une variable `alphabet`.
    
    ![capture d'écran](images/messages-alphabet.png)

+ Chaque lettre de l'alphabet a une position, commençant à la position 0. La lettre "a" est donc à la position 0 de l'alphabet et "c" est à la position 2.
    
    ![capture d'écran](images/messages-array.png)

+ Tu peux recevoir une lettre de ta variable `alphabet` en écrivant la position entre crochets.
    
    ![capture d'écran](images/messages-alphabet-array.png)
    
    Tu peux supprimer les déclarations `print` une fois que tu as essayé cela.

+ Ensuite, tu devras stocker la `clé` secrète dans une variable.
    
    ![capture d'écran](images/messages-key.png)

+ Ensuite, demande à l'utilisateur une seule lettre (appelée `character`s) pour crypter.
    
    ![capture d'écran](images/messages-character.png)

+ Trouve la `position` du `caractère`.
    
    ![capture d'écran](images/messages-position.png)

+ Tu peux tester la `position` enregistrée en l'imprimant. Par exemple, le caractère "e" est à la position 4 de l'alphabet.
    
    ![capture d'écran](images/messages-position-test.png)

+ Pour crypter le `caractère` , tu dois ajouter la `clé` à la `position`. Ceci est ensuite stocké dans une variable `newPosition`.
    
    ![capture d'écran](images/messages-newposition.png)

+ Ajoute du code pour imprimer la nouvelle position du caractère.
    
    ![capture d'écran](images/messages-newposition-print.png)

+ Teste ton nouveau code. Tant que la `clé` vaut 3, il faut ajouter 3 à la `position` et le stocker dans ta variable `newPosition`.
    
    Par exemple, la lettre 'e' se trouve à la position 4. Pour crypter, tu ajoutes la `clé` (3), donnant 7.
    
    ![capture d'écran](images/messages-newposition-test.png)

+ Que se passe-t-il lorsque tu essaies de crypter la lettre 'y'?
    
    ![capture d'écran](images/messages-modulus-bug.png)
    
    Note comment la `newPosition` est 27, et il n'y a pas 27 lettres dans l'alphabet!

+ Tu peux utiliser un `% ` pour indiquer à la nouvelle position de revenir à la position 0 une fois arrivée à la position 26.
    
    ![capture d'écran](images/messages-modulus.png)

+ Enfin, tu souhaites imprimer la lettre à la nouvelle position.
    
    Par exemple, l'ajout de la clé à la lettre "e" donne 7 et la lettre à la position 7 de l'alphabet est "h".
    
    ![capture d'écran](images/messages-newcharacter.png)

+ Essaie ton code. Tu peux également supprimer certaines de tes instructions d'impression, en imprimant simplement le nouveau caractère à la fin.
    
    ![capture d'écran](images/messages-enc-test.png)