## Encrypting entire messages

Instead of just encrypting and decrypting messages one character at a time, let's change the program to encrypt entire messages!

--- task ---

Firstly, check that your code looks like this:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights:
---
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3

character = input('Please enter a character: ')

position = alphabet.find(character)

new_position = (position + key) % 26

new_character = alphabet[new_position]
print('The new character is: ', new_character)
--- /code ---

--- /task ---

--- task ---

Create a variable to store the new encrypted message.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights:3
---
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
new_message = ''

character = input('Please enter a character: ')

position = alphabet.find(character)

new_position = (position + key) % 26

new_character = alphabet[new_position]
print('The new character is: ', new_character)
--- /code ---

--- /task ---

--- task ---

Change your code to store the user's message and not just one character.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 5
---
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
new_message = ''

message = input('Please enter a message: ')

position = alphabet.find(character)

new_position = (position + key) % 26

new_character = alphabet[new_position]
print('The new character is: ', new_character)
--- /code ---

--- /task ---

--- task ---

Add a `for` loop to your code, and indent the rest of the code so that it is repeated for each character in the message.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 7
---
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
new_message = ''

message = input('Please enter a message: ')

for character in message:
	position = alphabet.find(character)

	new_position = (position + key) % 26

	new_character = alphabet[new_position]
	print('The new character is: ', new_character)
--- /code ---

--- /task ---

--- task ---

Test your code. You should see that each character in the message is encrypted and printed one at a time.

```
Please enter a message: hello
The new character is:  k
The new character is:  h
The new character is:  o
The new character is:  o
The new character is:  r
```

--- /task ---

--- task ---

Let's add each encrypted character to your `new_message` variable.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 14-15
---
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
new_message = ''

message = input('Please enter a message: ')

for character in message:
	position = alphabet.find(character)

	new_position = (position + key) % 26

	new_character = alphabet[new_position]
	print('The new character is: ', new_character)
	new_message += new_character
	print(new_message)
--- /code ---

--- /task ---

--- task ---

If you delete the indentation before the `print` statement, the encrypted message will only be displayed once at the end. You can also delete the code for printing the characters

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 13, 15
---
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
new_message = ''

message = input('Please enter a message: ')

for character in message:
	position = alphabet.find(character)

	new_position = (position + key) % 26

	new_character = alphabet[new_position]

	new_message += new_character
print(new_message)
--- /code ---

--- /task ---




