## Criptografando mensagens inteiras

Em vez de apenas criptografar e descriptografar mensagens um caractere de cada vez, vamos mudar o programa para criptografar mensagens inteiras!

+ Em primeiro lugar, verifique se o seu código está assim:
    
    ![screenshot](images/messages-character-finished.png)

+ Crie uma variável para armazenar a nova mensagem criptografada.
    
    ![screenshot](images/messages-newmessage.png)

+ Altere seu código para armazenar a mensagem do usuário e não apenas um caractere.
    
    ![screenshot](images/messages-message.png)

+ Adicione um laço `for` ao seu código e recue o restante do código para que ele seja repetido para cada caractere na mensagem.
    
    ![screenshot](images/messages-loop.png)

+ Teste seu código. Você deve ver que cada caractere na mensagem é criptografado e impresso um de cada vez.
    
    ![screenshot](images/messages-loop-test.png)

+ Vamos adicionar cada caractere criptografado à sua variável `novaMensagem`.
    
    ![screenshot](images/messges-message-add-character.png)

+ You can `print` the `newMessage` as it is being encrypted.
    
    ![screenshot](images/messages-print-message-characters.png)

+ If you delete the spaces before the `print` statement, the encrypted message will only be displayed once at the end. You can also delete the code for printing the character positions.
    
    ![screenshot](images/messages-print-message-comment.png)