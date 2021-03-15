#!/bin/python3

pontos = 0
names = input('enter the names of 2 people: ')

for caractere in nomes:
  if caractere in 'aeiou':
    pontos += 5
  if caractere in 'amigo':
    pontos += 10

print('A tua pontuação de amizade é: ', pontos)

if pontos> 100:
  print('Os melhores amigos!')
