## Introdução:

Neste projeto, você aprenderá como criar seu próprio programa de criptografia, para trocar mensagens secretas com um amigo. This project ties in with the "Earth to Principia" activity on page 16 of the Space Diary.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/402256078c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

### Informação adicional para líderes de clube

Se você precisar imprimir este projeto, use a [versão para impressão](https://projects.raspberrypi.org/en/projects/secret-messages/print).

## \--- collapse \---

## title: Notas do líder do clube

## Introdução:

Neste projeto, as crianças aprenderão como fazer um programa de criptografia, trocar mensagens secretas com um amigo. Este projeto introduz iteração (repetição) sobre uma cadeia de texto.

## Recursos Online

**Este projeto usa o Python 3.** Recomendamos usar o [trinket](https://trinket.io/) para escrever Python online. Este projeto contém os seguintes Trinkets:

* [Novo Trinket Python (em branco) - jumpto.cc/python-new](http://jumpto.cc/python-new)

Há também um trinket contendo o projeto finalizado:

* [‘Secret Messages’ Finished -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

* [‘Friendship Calculator’ Finished -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## Offline Resources

This project can be [completed offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) if preferred.

You can find the completed project in the 'Volunteer Resources' section, which contains:

* messages-finished/messages.py
* messages-finished/friends.py

(All of the resources above are also downloadable as project and volunteer `.zip` files.)

## Learning Objectives

* Iteration (looping) over a string variable;
* The `find()` method;
* The modulus operator (`%`).

This project covers elements from the following strands of the [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum):

* [Combine programming constructs to solve a problem.](https://www.raspberrypi.org/curriculum/programming/builder)

## Challenges

* Use a Caesar cipher - encrypt and decrypt letters and words manually;
* Variable keys - allowing the user to input a chosen key;
* Encrypting and decrypting messages - encrypting and decrypting whole messages;
* Friendship calculator - applying text iteration to a new problem.

## Frequently Asked Questions

* When searching using `find()` or `if char in alphabet:`, note that searches are case-sensitive. Children can use:
    
    ```python
    message = input("Please enter a message to encrypt: ").lower()
    ```
    
    to make the input lower case before searching.

\--- /collapse \---

## \--- collapse \---

## title: Project materials

## Project resources

* [.zip file containing all project resources](resources/secret-messages-project-resources.zip)
* [Online blank Python Trinket](http://jumpto.cc/python-new)
* [Offline blank Python file](resources/new-new.py)

## Club leader resources

* [.zip file containing all completed project resources](resources/secret-messages-volunteer-resources.zip)
* [Online completed Trinket project](https://trinket.io/python/402256078c)
* [secret-messages-finished/messages.py](resources/secret-messages-finished-messages.py)
* [Online completed 'Friendship calculator' challenge](https://trinket.io/python/2e852cd687)
* [offline complete 'Friendship calculator' challenge](resources/friendship-calculator-finished-friends.py)

\--- /collapse \---