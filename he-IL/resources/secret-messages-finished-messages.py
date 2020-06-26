#!/bin/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''
  
message = input('אנא הזינו הודעה באנגלית: ')

key = input('אנא הזינו מפתח (1-26): ')
key = int(key)

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character

print('ההודעה החדשה שלכם היא: ', newMessage)