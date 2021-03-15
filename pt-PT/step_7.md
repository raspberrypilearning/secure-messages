## Caracteres extra

Alguns caracteres não estão no alfabeto, o que causa um erro.

+ Testa o teu código com alguns caracteres que não estão no alfabeto.
    
    Por exemplo, tu poderás usar a mensagem `olá!!`.
    
    ![captura de ecrã](images/messages-extra-characters.png)
    
    Observa que os caracteres de espaço e `!` são todos codificados como a letra 'c'!

+ Para corrigir isso, tu só queres traduzir um caractere se estiver no alfabeto. Para fazer isso, adiciona uma instrução `if` ao teu código e indenta o resto do teu código.
    
    ![captura de ecrã](images/messages-if.png)

+ Testa o teu código com a mesma mensagem. O que acontece desta vez?
    
    ![captura de ecrã](images/messages-if-test.png)
    
    Agora, o teu código simplesmente ignora qualquer caractere se não estiver no alfabeto.

+ Seria melhor se o teu código não codificasse qualquer coisa que não estivesse no alfabeto, mas apenas usasse o caractere original.
    
    Adiciona uma instrução `else` ao teu código, que adiciona apenas o caractere original à mensagem codificada.
    
    ![captura de ecrã](images/messages-else.png)

+ Testa o teu código. Tu deves ver que qualquer caractere no alfabeto é codificado, mas quaisquer outros caracteres são ignorados!
    
    ![captura de ecrã](images/messages-else-test.png)