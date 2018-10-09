## A cifra de César

Uma cifra é um tipo de código secreto, onde você troca as letras para que ninguém possa ler sua mensagem.

Você estará usando uma das mais antigas e famosas cifras, a **cifra de César**, que leva o nome de Júlio César.

Antes de começarmos a programar, vamos tentar usar a cifra de César para esconder uma palavra.

+ Esconder uma palavra é chamado de **criptografia**.
    
    Vamos começar criptografando a letra 'a'. Para fazer isso, podemos desenhar o alfabeto em um círculo, assim:
    
    ![screenshot](images/messages-wheel.png)

+ Para criar uma carta criptografada secreta a partir de uma carta normal, você precisa ter uma chave secreta. Vamos usar o número 3 como chave (mas você pode usar qualquer número que quiser).
    
    Para **criptografar** a letra 'a', você apenas move 3 letras no sentido horário, o que lhe dará a letra 'd':
    
    ![screenshot](images/messages-wheel-eg.png)

+ Você pode usar o que aprendeu para criptografar uma palavra inteira. Por exemplo, 'amigo' criptografado é 'dpljr'. Tente você mesmo.
    
    + a + 3 = **d**
    + m + 3 = **p**
    + i + 3 = **l**
    + g + 3 = **j**
    + o + 3 = **r**

+ Retornar o texto ao normal é chamado de **decriptografia**. Para descriptografar uma palavra, basta subtrair a chave em vez de adicioná-la:
    
    + d - 3 = **a**
    + p - 3 = **m**
    + l - 3 = **i**
    + j - 3 = **g**
    + r - 3 = **o**