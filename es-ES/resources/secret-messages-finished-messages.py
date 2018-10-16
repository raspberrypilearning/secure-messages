#!/bin/python3

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
nuevoMensaje = ''
  
mensaje = input('Por favor, introduce un mensaje: ')

clave = input('Introduce una clave (1-27): ')
key = int(key)

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character

print('Your new message is: ', newMessage)