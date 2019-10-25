## Crypter des messages entiers

Au lieu de simplement crypter et décrypter les messages, un caractère à la fois, changeons le programme pour chiffrer des messages entiers!

+ Tout d'abord, vérifie que ton code ressemble à ceci:
    
    ![capture d'écran](images/messages-character-finished.png)

+ Crée une variable pour stocker le nouveau message crypté.
    
    ![capture d'écran](images/messages-newmessage.png)

+ Modifie ton code pour stocker le message de l'utilisateur et non pas un seul caractère.
    
    ![capture d'écran](images/messages-message.png)

+ Ajoute une boucle `for` à ton code et indente le reste du code afin qu'il soit répété pour chaque caractère du message.
    
    ![capture d'écran](images/messages-loop.png)

+ Teste ton code. Tu devrais voir que chaque caractère du message est crypté et imprimé un seul à la fois.
    
    ![capture d'écran](images/messages-loop-test.png)

+ Ajoutons chaque caractère crypté à ta variable `newMessage`.
    
    ![capture d'écran](images/messges-message-add-character.png)

+ Tu peux `afficher` le `newMessage` car il est crypté.
    
    ![capture d'écran](images/messages-print-message-characters.png)

+ Si tu supprimes les espaces avant la déclaration `print`, le message crypté ne sera affiché qu’une fois à la fin. Tu peux également supprimer le code pour imprimer les positions des caractères.
    
    ![capture d'écran](images/messages-print-message-comment.png)