## Extra characters

Some characters aren't in the alphabet, which causes an error.

--- task ---

Test out your code with some characters that aren't in the alphabet.

For example, you could use the message `hi there!!`.

```
Please enter a message: hi there!!
klcwkhuhcc
```

Notice that the space and the `!` characters are all encrypted as the letter 'c'!

--- /task ---

--- task ---

To fix this, you only want to translate a character if it's in the alphabet. To do this, add an `if` statement to your code, and indent the rest of your code.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 8
---
for character in message:
    if character in alphabet:
    	position = alphabet.find(character)
    
    	new_position = (position + key) % 26
    
    	new_character = alphabet[new_position]
    
    	new_message += new_character
print(new_message)
--- /code ---

--- /task ---

--- task ---

Test your code with the same message. What happens this time?

```
Please enter a message: hi there!!
klwkhuh
```

Now, your code just skips any character if it's not in the alphabet.

--- /task ---

--- task ---

It would be better if your code didn't encrypt anything not in the alphabet, but just used the original character.

Add an `else` statement to your code, which just adds the original character to the encrypted message.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 16-17
---
for character in message:
    if character in alphabet:
    	position = alphabet.find(character)
    
    	new_position = (position + key) % 26
    
    	new_character = alphabet[new_position]
    
    	new_message += new_character
    else:
        new_message += character
print(new_message)
--- /code ---

--- /task ---

--- task ---
Test your code. You should see that any character in the alphabet is encrypted, but any other characters are left alone!

```
Please enter a message: hi there!!
kl wkhuh!!
```
--- /task ---



