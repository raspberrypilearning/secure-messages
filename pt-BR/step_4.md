## Criptografando cartas

Vamos escrever um programa em Python para criptografar um único caractere.

+ Abra o modelo Trinket em branco do Python: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Em vez de desenhar o alfabeto em um círculo, vamos escrevê-lo como uma variável `alfabeto`.
    
    ![screenshot](images/messages-alphabet.png)

+ Cada letra do alfabeto tem uma posição, começando na posição 0. Portanto, a letra 'a' está na posição 0 do alfabeto e 'c' está na posição 2.
    
    ![screenshot](images/messages-array.png)

+ Você pode obter uma letra da sua variável `alfabeto` escrevendo a posição entre colchetes.
    
    ![screenshot](images/messages-alphabet-array.png)
    
    You can delete the `print` statements once you've tried this out.

+ Em seguida, você precisará armazenar a `chave` secreta em uma variável.
    
    ![screenshot](images/messages-key.png)

+ Em seguida, peça ao usuário uma única letra (chamada de `caractere`) para criptografar.
    
    ![screenshot](images/messages-character.png)

+ Encontre a `posição` do `caractere`.
    
    ![screenshot](images/messages-position.png)

+ You can test the stored `position` by printing it. For example, that character 'e' is at position 4 in the alphabet.
    
    ![screenshot](images/messages-position-test.png)

+ Para criptografar o `caractere`, você deve adicionar a `chave` à `posição`. Isso é então armazenado em uma variável `novaPosicao`.
    
    ![screenshot](images/messages-newposition.png)

+ Adicione código para imprimir a nova posição do caractere.
    
    ![screenshot](images/messages-newposition-print.png)

+ Teste seu novo código. Como sua `chave` é 3, ela deve adicionar 3 à variável `posicao` e armazená-la em sua variável `novaPosicao`.
    
    Por exemplo, a letra 'e' está na posição 4. Para criptografar, você adiciona a `chave` (3), dando 7.
    
    ![screenshot](images/messages-newposition-test.png)

+ O que acontece quando você tenta criptografar a letra 'y'?
    
    ![screenshot](images/messages-modulus-bug.png)
    
    Observe como `novaPosicao` é 27 e não há 27 letras no alfabeto!

+ Você pode usar um `%` para dizer à nova posição para voltar à posição 0 quando chegar à posição 26.
    
    ![screenshot](images/messages-modulus.png)

+ Finalmente, você deseja mostrar a letra na nova posição.
    
    Por exemplo, adicionar a chave à letra 'e' dá 7 e a letra na posição 7 do alfabeto é 'h'.
    
    ![screenshot](images/messages-newcharacter.png)

+ Experimente o seu código. Você também pode remover algumas das suas instruções de print, apenas imprimindo o novo caractere no final.
    
    ![screenshot](images/messages-enc-test.png)