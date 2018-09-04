#!/bin/python3

wyddor = 'abcdefghijklmnopqrstuvwxyz'
Negesnewydd = ''
  
neges = input('Cofnodwch neges: ')

allwedd = input('Cofnodwch allwedd (1-26): ')
allwedd = int(allwedd)

for cymeriad in neges:
  if cymeriad in wyddor:
    safle = wyddor.find(cymeriad)
    Saflenewydd = (safle + allwedd) % 26
    Cymeriadnewydd = wyddor[Saflenewydd]
    Negesnewydd += Cymeriadnewydd
  else:
    Negesnewydd += cymeriad

print('Eich neges newydd yw: ', Negesnewydd)