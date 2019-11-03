## A cifra de César

Uma cifra é um tipo de código secreto, onde você troca as letras para que ninguém possa ler sua mensagem.

You'll be using one of the oldest and most famous ciphers, the **Caesar cipher**, which is named after Julius Caesar.

Antes de começarmos a programar, vamos tentar usar a cifra de César para esconder uma palavra.

+ Esconder uma palavra é chamado de **criptografia**.
    
    Vamos começar criptografando a letra 'a'. Para fazer isso, podemos desenhar o alfabeto em um círculo, assim:
    
    ![screenshot](images/messages-wheel.png)

+ To make a secret encrypted letter from a normal one, you need to have a secret key. Let's use the number 3 as the key (but you can use any number you like).
    
    To **encrypt** the letter 'a', you just move 3 letters clockwise, which will give you the letter 'd':
    
    ![screenshot](images/messages-wheel-eg.png)

+ You can use what you've learnt to encrypt an entire word. For example, 'hello' encrypted is 'khoor'. Try it yourself.
    
    + h + 3 = **k**
    + e + 3 = **h**
    + l + 3 = **o**
    + l + 3 = **o**
    + o + 3 = **r**

+ Getting text back to normal is called **decryption**. To decrypt a word, just subtract the key instead of adding it:
    
    + k - 3 = **h**
    + h - 3 = **e**
    + o - 3 = **l**
    + o - 3 = **l**
    + r - 3 = **o**