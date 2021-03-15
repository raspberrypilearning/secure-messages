## A cifra de César

Uma cifra é um tipo de código secreto, onde tu trocas as letras para que ninguém possa ler a tua mensagem.

Tu estarás a usar uma das mais antigas e famosas cifras, a **cifra de César**, que leva o nome de Júlio César.

Antes de começarmos a codificar, vamos tentar usar a cifra de César para esconder uma palavra.

+ Ocultar uma palavra é chamado de **criptografia**.
    
    Vamos começar codificando a letra 'a'. Para fazer isso, podemos desenhar o alfabeto num círculo, assim:
    
    ![captura de ecrã](images/messages-wheel.png)

+ Para criar uma carta codificada secreta de uma carta normal, precisas de ter uma chave secreta. Vamos usar o número 3 como chave (mas podes usar qualquer número que quiseres).
    
    Para **codificar** a letra 'a', tu apenas moves 3 letras no sentido horário, o que te dará a letra 'd':
    
    ![captura de ecrã](images/messages-wheel-eg.png)

+ Podes usar o que aprendeste para codificar uma palavra inteira. Por exemplo, 'olá' codificado é 'rnd'. Tenta tu mesmo.
    
    + h + 3 = **k**
    + e + 3 = **h**
    + l + 3 = **o**
    + l + 3 = **o**
    + o + 3 = **r**

+ Retornar o texto ao normal é chamado de **descodificação**. Para descodificar uma palavra, basta subtrair a chave em vez de adicioná-la:
    
    + k - 3 = **h**
    + h - 3 = **e**
    + o - 3 = **l**
    + o - 3 = **l**
    + r - 3 = **o**