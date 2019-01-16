#!/bin/python3

alphabet = 'αβγδεζηθικλμνξοπρστυφχψω'
newMessage = ''
  
message = input('Γράψε ένα μήνυμα: ')

key = input('Δώσε ένα κλείδι (1-24): ')
key = int(key)

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 24
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character

print('Το νέο σου μήνυμα είναι: ', newMessage)