#!/bin/python3

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
nuevoMensaje = ''
  
mensaje = input('Por favor, introduce un mensaje: ')

clave = input('Introduce una clave (1-27): ')
clave = int(clave)

for caracter in mensaje:
  if caracter in alfabeto:
    posicion = alfabeto.find(caracter)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character

print('Your new message is: ', newMessage)