#! /usr/bin/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'

neuerText = ''             # 2 einzelne Hochkommata für Leerstring
  
text = input('Gib hier deinen Text ein: ')

key = input('Gib hier deinen Schlüssel (key) ein (1-26): ')
key = int(key)

for buchstabe in text:
  if buchstabe in alphabet:
    position = alphabet.find(buchstabe)
    neuePosition = (position + key) % 26
    neuerBuchstabe = alphabet[neuePosition]
    neuerText += neuerBuchstabe
  else:
    neuerText += buchstabe

print('Der verschlüsselte Text lautet: ', neuerText)