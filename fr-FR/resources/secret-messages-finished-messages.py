#!/bin/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''
  
message = input('Veuillez entrer un message: ')

key = input('Entrer une clé (1-26): ')
key = int(key)

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character

print('Votre nouveau message est: ', newMessage)