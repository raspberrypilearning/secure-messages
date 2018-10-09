#!/bin/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'
neueNachricht = ''
  
nachricht = input('Bitte eine Nachricht eingeben: ')

schluessel = input('Bitte einen Schlüssel eingeben (1-26): ')
schluessel = int(schluessel)

for zeichen in nachricht:
  if zeichen in alphabet:
    position = alphabet.find(zeichen)
    neuePosition = (position + schluessel) % 26
    neuesZeichen = alphabet[neuePosition]
    neueNachricht += neuesZeichen
  else:
    neueNachricht += zeichen

print('Die verschlüsselte Nachricht lautet: ', neueNachricht)