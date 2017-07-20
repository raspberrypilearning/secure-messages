--- challenge ---
## Challenge: Use a Caesar cipher
Can you send a secret word to a friend? You'll both need to agree on a secret key before you start.

You could even send entire sentences to each other!

## Step 2: Encrypting letters

Let's write a Python program to encrypt a single character. 



+ Open the blank Python template Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>. 

+ Instead of drawing the alphabet in a circle, let's write it out as an `alphabet` variable.

	![screenshot](images/messages-alphabet.png)

+ Each letter of the alphabet has a position, starting at position 0. So the letter 'a' is at position 0 of the alphabet, and 'c' is at position 2.

	![screenshot](images/messages-array.png)

+ You can get a letter from your `alphabet` variable by writing the position in square brackets.

	![screenshot](images/messages-alphabet-array.png)

	You can delete the `print` ststements once you've tried this out.

+ Next, you'll need to store the secret `key` in a variable.

	![screenshot](images/messages-key.png)	

+ Next, ask the user for a single letter (called a `character`) to encrypt.

	![screenshot](images/messages-character.png)

+ Find the `position` of the `character`.

	![screenshot](images/messages-position.png)

+ You can test the stored `position` by printing it. For example, that character 'e' is at position 4 in the alphabet.

	![screenshot](images/messages-position-test.png)

+ To encrypt the `character`, you should add the `key` to the `position`.

	![screenshot](images/messages-newposition.png)

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




--- /challenge ---### Additional information for club leaders

If you need to print this project, please use the [Printer friendly version](https://projects.raspberry-pi.org/en/projects/secret-messages/print).


--- collapse ---
---
title: Club leader notes
---


## Introduction:
In this project, children will learn how to make an encryption program, to send and receive secret messages with a friend. This project introduces iteration (looping) over a text string.

## Online Resources

__This project uses Python 3.__ We recommend using [trinket](https://trinket.io/) to write Python online. This project contains the following Trinkets:

+ [New (blank) Python Trinket -- jumpto.cc/python-new](http://jumpto.cc/python-new)

There is also a trinket containing the finished project:

+ [‘Secret Messages’ Finished -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

+ [‘Friendship Calculator’ Finished -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## Offline Resources
This project can be [completed offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) if preferred.

You can find the completed project in the 'Volunteer Resources' section, which contains:

+ messages-finished/messages.py
+ messages-finished/friends.py

(All of the resources above are also downloadable as project and volunteer `.zip` files.)

## Learning Objectives
+ Iteration (looping) over a string variable;
+ The `find()` method;
+ The modulus operator (`%`).

This project covers elements from the following strands of the [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum):

+ [Combine programming constructs to solve a problem.](https://www.raspberrypi.org/curriculum/programming/builder)

## Challenges
+ Use a Caesar cipher - encrypy and decrypt letters and words manually;
+ Variable keys - allowing the user to input a chosen key;
+ Encrypting and decrypting messages - encrypting and decrypting whole messages;
+ Friendship calculator - applying text iteration to a new problem.

## Frequently Asked Questions
+ When searching using `find()` or `if char in alphabet:`, note that searches are case-sensitive. Children can use:

	```python
	message = input("Please enter a message to encrypt: ").lower()
	```

	to make the input lower case before searching.

--- /collapse ---


--- collapse ---
---
title: Project materials
---
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

--- /collapse ---