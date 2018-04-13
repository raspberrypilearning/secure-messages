## Criptografando cartas

Vamos escrever um programa em Python para criptografar um único caractere.

+ Abra o modelo Trinket em branco do Python: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Em vez de desenhar o alfabeto em um círculo, vamos escrevê-lo como uma variável</code> do alfabeto `.</p>

<p><img src="images/messages-alphabet.png" alt="captura de tela" /></p></li>
<li><p>Cada letra do alfabeto tem uma posição, começando na posição 0. Portanto, a letra 'a' está na posição 0 do alfabeto e 'c' está na posição 2.</p>

<p><img src="images/messages-array.png" alt="captura de tela" /></p></li>
<li><p>Você pode obter uma carta da variável` do alfabeto `escrevendo a posição entre colchetes.</p>

<p><img src="images/messages-alphabet-array.png" alt="captura de tela" /></p>

<p>Você pode excluir as <code>stdements` de impressão depois de ter feito isso.

+ Em seguida, você precisará armazenar a chave secreta `` em uma variável.
    
    ![captura de tela](images/messages-key.png)

+ Em seguida, peça ao usuário uma única letra (chamada de `caractere`) para criptografar.
    
    ![captura de tela](images/messages-character.png)

+ Encontre a `posição` do `personagem`.
    
    ![captura de tela](images/messages-position.png)

+ You can test the stored `position` by printing it. For example, that character 'e' is at position 4 in the alphabet.
    
    ![captura de tela](images/messages-position-test.png)

+ Para criptografar o `caractere`, você deve adicionar `a tecla` à `posição`. Isso é então armazenado em uma variável `newPosition`.
    
    ![captura de tela](images/messages-newposition.png)

+ Adicione o código para imprimir a nova posição de caractere.
    
    ![captura de tela](images/messages-newposition-print.png)

+ Teste seu novo código. Como sua `key` é 3, ela deve adicionar 3 à `` e armazená-la em sua variável `newPosition`.
    
    Por exemplo, a letra 'e' está na posição 4. Para criptografar, você adiciona a `chave` (3), dando 7.
    
    ![captura de tela](images/messages-newposition-test.png)

+ O que acontece quando você tenta e criptografa a letra 'y'?
    
    ![captura de tela](images/messages-modulus-bug.png)
    
    Observe como `newPosition` é 27 e não há 27 letras no alfabeto!

+ Você pode usar um `%` para dizer à nova posição para voltar à posição 0 quando chegar à posição 26.
    
    ![captura de tela](images/messages-modulus.png)

+ Finalmente, você deseja imprimir a carta na nova posição.
    
    Por exemplo, adicionar a chave à letra 'e' dá 7 e a letra na posição 7 do alfabeto é 'h'.
    
    ![captura de tela](images/messages-newcharacter.png)

+ Experimente o seu código. Você também pode remover algumas das suas instruções de impressão, apenas imprimindo o novo caractere no final.
    
    ![captura de tela](images/messages-enc-test.png)