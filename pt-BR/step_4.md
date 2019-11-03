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

+ Next, you'll need to store the secret `key` in a variable.
    
    ![screenshot](images/messages-key.png)

+ Next, ask the user for a single letter (called a `character`) to encrypt.
    
    ![screenshot](images/messages-character.png)

+ Find the `position` of the `character`.
    
    ![screenshot](images/messages-position.png)

+ You can test the stored `position` by printing it. For example, that character 'e' is at position 4 in the alphabet.
    
    ![screenshot](images/messages-position-test.png)

+ To encrypt the `character`, you should add the `key` to the `position`. This is then stored in a `newPosition` variable.
    
    ![screenshot](images/messages-newposition.png)

+ Add code to print the new character position.
    
    ![screenshot](images/messages-newposition-print.png)

+ Test out your new code. As your `key` is 3, it should add 3 to the `position` and store it in your `newPosition` variable.
    
    For example, letter 'e' is at position 4. To encrypt, you add the `key` (3), giving 7.
    
    ![screenshot](images/messages-newposition-test.png)

+ What happens when you try and encrypt the letter 'y'?
    
    ![screenshot](images/messages-modulus-bug.png)
    
    Notice how the `newPosition` is 27, and there aren't 27 letters in the alphabet!

+ You can use a `%` to tell the new position to go back to position 0 once it gets to position 26.
    
    ![screenshot](images/messages-modulus.png)

+ Finally, you want to print the letter at the new position.
    
    For example, adding the key to the letter 'e' gives 7, and the letter at position 7 of the alphabet is 'h'.
    
    ![screenshot](images/messages-newcharacter.png)

+ Try out your code. You can also remove some of your print statements, just printing the new character at the end.
    
    ![screenshot](images/messages-enc-test.png)