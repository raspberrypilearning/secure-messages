## Criptografando cartas

Vamos escrever um programa em Python para criptografar um único caractere.

+ Abra o modelo Trinket em branco do Python: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Em vez de desenhar o alfabeto em um círculo, vamos escrevê-lo como uma variável `alfabeto`.
    
    ![screenshot](images/messages-alphabet.png)

+ Cada letra do alfabeto tem uma posição, começando na posição 0. Portanto, a letra 'a' está na posição 0 do alfabeto e 'c' está na posição 2.
    
    ![screenshot](images/messages-array.png)

+ Você pode obter uma letra da sua variável `alfabeto` escrevendo a posição entre colchetes.
    
    ![screenshot](images/messages-alphabet-array.png)
    
    Você pode excluir as declarações de `print` depois de tentar isso.

+ Em seguida, você precisará armazenar a `chave` secreta em uma variável.
    
    ![screenshot](images/messages-key.png)

+ Em seguida, peça ao usuário uma única letra (chamada de `caractere`) para criptografar.
    
    ![screenshot](images/messages-character.png)

+ Encontre a `posição` do `caractere`.
    
    ![screenshot](images/messages-position.png)

+ Você pode testar a `posição` armazenada imprimindo-a. Por exemplo, o caractere 'e' está na posição 4 do alfabeto.
    
    ![screenshot](images/messages-position-test.png)

+ Para criptografar o `caractere`, você deve adicionar a `chave` à `posição`. Isso é então armazenado na variável `novaPosicao`.
    
    ![screenshot](images/messages-newposition.png)

+ Adicione código para imprimir a nova posição do caractere.
    
    ![screenshot](images/messages-newposition-print.png)

+ Teste seu novo código. Como sua `chave` é 3, ela deve adicionar 3 à variável `posicao` e armazená-la na variável `novaPosicao`.
    
    Por exemplo, a letra 'e' está na posição 4. Para criptografar, você adiciona a `chave` (3), dando 7.
    
    ![screenshot](images/messages-newposition-test.png)

+ O que acontece quando você tenta criptografar a letra 'y'?
    
    ![screenshot](images/messages-modulus-bug.png)
    
    Notice how the `newPosition` is 27, and there aren't 27 letters in the alphabet!

+ You can use a `%` to tell the new position to go back to position 0 once it gets to position 26.
    
    ![screenshot](images/messages-modulus.png)

+ Finally, you want to print the letter at the new position.
    
    For example, adding the key to the letter 'e' gives 7, and the letter at position 7 of the alphabet is 'h'.
    
    ![screenshot](images/messages-newcharacter.png)

+ Try out your code. You can also remove some of your print statements, just printing the new character at the end.
    
    ![screenshot](images/messages-enc-test.png)