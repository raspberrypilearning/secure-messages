#!/bin/python3

pontos = 0
nomes = input('Insira os nomes de 2 pessoas: ')

for caractere in nomes:
  if caractere in 'aeiou':
    pontos += 5
  if caractere in 'amigo':
    pontos += 10

print('Sua pontuação de amizade é: ', pontos)

if pontos > 100:
  print('Melhores amigos!')