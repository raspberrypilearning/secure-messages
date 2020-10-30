#!/bin/python3

puntos = 0
nombres = input('Escribe el nombre de 2 personas: ')

for caracter in nombres:
  if caracter in 'aeiou':
    puntos += 5
  if caracter in 'amigo':
    puntos += 10

print('Tu índice de amistad es de: ', puntos)

if puntos > 100:
  print('¡Ustedes son los mejores amigos!')