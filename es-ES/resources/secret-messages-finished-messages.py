#!/bin/python3

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
nuevoMensaje = ''
  
mensaje = input('Por favor, introduce un mensaje: ')

clave = input('Introduce una clave (1-27): ')
clave = int(clave)

for caracter in mensaje:
  if caracter in alfabeto:
    posicion = alfabeto.find(caracter)
    nuevaPosicion = (posicion + clave) % 27
    nuevoCaracter = alfabeto[nuevaPosicion]
    nuevoMensaje += nuevoCaracter
  else:
    nuevoMensaje += caracter

print('Tu nuevo mensaje es: ', nuevoMensaje)