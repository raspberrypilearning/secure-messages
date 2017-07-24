## Encrypting entire messages

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



