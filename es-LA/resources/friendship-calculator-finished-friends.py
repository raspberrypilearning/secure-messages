#!/bin/python3

puntos = 0
names = input('enter the names of 2 people: ')

for caracter in nombres:
  if caracter in 'aeiou':
    puntos += 5
  if caracter in 'amigo':
    puntos += 10

print('Tu índice de amistad es de: ', puntos)

if puntos > 100:
  print('¡Ustedes son los mejores amigos!')
