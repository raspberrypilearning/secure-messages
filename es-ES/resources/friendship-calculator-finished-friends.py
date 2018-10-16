#!/bin/python3

puntos = 0
nombres = input('Introduce el nombre de 2 personas: ')

for caracter in nombres:
  if caracter in 'aeiou':
    puntos += 5
  if caracter in 'amigo':
    puntos += 10

print('Vuestro índice de amistad es de: ', puntos)

if puntos > 100:
  print('¡Sois los mejores amigos!')