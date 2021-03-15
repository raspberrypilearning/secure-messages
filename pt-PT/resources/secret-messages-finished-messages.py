#!/bin/python3

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
novaMensagem = ''
  
mensagem = input('Por favor digita uma mensagem: ')

chave = input('Digita uma chave (1-26): ')
chave = int(chave)

for caractere in mensagem:
  if caractere in alfabeto:
    posicao = alfabeto.find(caractere)
    novaPosicao = (posicao + chave) % 26
    novoCaractere = alfabeto[novaPosicao]
    novaMensagem += novoCaractere
  else:
    novaMensagem += caractere

print('A tua nova mensagem é: ', novaMensagem)