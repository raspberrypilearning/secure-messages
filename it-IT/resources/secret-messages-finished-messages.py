#!/bin/python3

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
nuovomessaggio = ''
  
messaggio = input('Inserisci un messaggio: ')

chiave = input('Dimmi la chiave di cifratura (1-26)')
chiave = int(chiave)

for lettera in messaggio:
  if lettera in alfabeto:
    posizione = alfabeto.find(lettera)
    nuovaposizione = (posizione + chiave) % 26
    nuovocarattere = alfabeto[nuovaposizione]
    nuovomessaggio += nuovocarattere
  else:
    nuovomessaggio += lettera

print('Il nuovo messaggio è: '+ nuovomessaggio)