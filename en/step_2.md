--- challenge ---
## Challenge: Variable keys
Modify your program, so that the user can enter their own key to use. You'll need to get the user's input, and store it in the `key` variable.

Remember to use the `int()` function to convert the input to a whole number.

You can then use a negative key to decrypt messages!



## Step 2: Encrypting entire messages

Instead of just encrypting and decrypting messages one character at a time, let's change the program to encrypt entire messages!



+ Firstly, check that your code looks like this:

	![screenshot](images/messages-character-finished.png)

+ Create a variable to store the new encrypted message.

	![screenshot](images/messages-newmessage.png)

+ Change your code to store the user's message and not just one character.

	![screenshot](images/messages-message.png)

+ Add a `for` loop to your code, and indent the rest of the code so that it is repeated for each character in the message.

	![screenshot](images/messages-loop.png)

+ Test your code. You should see that each character in the message is encrypted and printed one at a time.

	![screenshot](images/messages-loop-test.png)

+ Let's add each encrypted character to your `newMessage` variable.

	![screenshot](images/messges-message-add-character.png)

+ You can `print` the `newMessage` as it is begin encrypted.

	![screenshot](images/messages-print-message-characters.png)

+ If you delete the spaces before the `print` statement, the encrypted message will only be displayed once at the end. You can also delete the code for printing the character positions.

	![screenshot](images/messages-print-message-comment.png)



## Step 3: Extra characters

Some characters aren't in the alphabet, which causes an error.



+ Test out your code with some characters that aren't in the alphabet.

	For example, you could use the message `hi there!!`.

	![screenshot](images/messages-extra-characters.png)

	Notice that the space and the `!` characters are all encrypted as the letter 'c'!

+ To fix this, you only want to translate a character if it's in the alphabet. To do this, add an `if` statement to your code, and indent the rest of your code.

	![screenshot](images/messages-if.png)

+ Test your code with the same message. What happens this time?

	![screenshot](images/messages-if-test.png)

	Now, your code just skips any character if it's not in the alphabet.

+ It would be better if your code didn't encrypt anything not in the alphabet, but just used the original character.

	Add an `else` statement to your code, which just adds the original character to the encrypted message.

	![screenshot](images/messages-else.png)

+ Test your code. You should see that any character in the alphabet is encrypted, but any other characters are left alone!

	![screenshot](images/messages-else-test.png)




--- /challenge ---