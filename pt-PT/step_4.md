## Codificando cartas

Vamos escrever um programa em Python para codificar um único caractere.

+ Abre o modelo Trinket em branco do Python: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Em vez de desenhar o alfabeto num círculo, vamos escrevê-lo como uma variável</code> do alfabeto `.</p>

<p><img src="images/messages-alphabet.png" alt="captura de ecrã" /></p></li>
<li><p>Cada letra do alfabeto tem uma posição, começando na posição 0. Portanto, a letra 'a' está na posição 0 do alfabeto e 'c' está na posição 2.</p>

<p><img src="images/messages-array.png" alt="captura de ecrã" /></p></li>
<li><p>Podes obter uma letra da variável` do alfabeto `escrevendo a posição entre colchetes.</p>

<p><img src="images/messages-alphabet-array.png" alt="captura de ecrã" /></p>

<p>Podes excluir as declarações <code>print` depois de experimentar isto.

+ Em seguida, vais precisar de guardar a `chave` secreta numa variável.
    
    ![captura de ecrã](images/messages-key.png)

+ Em seguida, pede ao utilizador uma única letra (chamada de `caractere`) para codificar.
    
    ![captura de ecrã](images/messages-character.png)

+ Encontre a `posição` do `caractere`.
    
    ![captura de ecrã](images/messages-position.png)

+ Podes testar a posição ` armazenada ` imprimindo-a. Por exemplo, esse caractere 'e' está na posição 4 do alfabeto.
    
    ![captura de ecrã](images/messages-position-test.png)

+ Para codificar o `caractere`, deves adicionar a `chave` à `posição`. Isso é então guardado numa variável `novaPosicao`.
    
    ![captura de ecrã](images/messages-newposition.png)

+ Adiciona o código para imprimir a nova posição do caractere.
    
    ![captura de ecrã](images/messages-newposition-print.png)

+ Testa o teu novo código. Como a tua `chave` é 3, ela deve adicionar 3 à `posição` e armazená-la na tua variável `novaPosicao`.
    
    Por exemplo, a letra 'e' está na posição 4. Para codificar, deves adicionar a `chave` (3), dando 7.
    
    ![captura de ecrã](images/messages-newposition-test.png)

+ O que acontece quando tentas e codificas a letra 'y'?
    
    ![captura de ecrã](images/messages-modulus-bug.png)
    
    Observa como `novaPosicao` é 27 e não há 27 letras no alfabeto!

+ Tu podes usar um `%` para dizer à nova posição para voltar à posição 0 quando chegar à posição 26.
    
    ![captura de ecrã](images/messages-modulus.png)

+ Finalmente, tu queres imprimir a letra na nova posição.
    
    Por exemplo, adicionar a chave à letra 'e' dá 7 e a letra na posição 7 do alfabeto é 'h'.
    
    ![captura de ecrã](images/messages-newcharacter.png)

+ Experimenta o teu código. Podes também remover algumas das tuas instruções de impressão, apenas imprimindo o novo caractere no final.
    
    ![captura de ecrã](images/messages-enc-test.png)