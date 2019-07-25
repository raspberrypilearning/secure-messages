#!/bin/python3

abeceda = 'abcdefghijklmnopqrstuvwxyz'
novaPoruka = ''
  
poruka = input('Unesi poruku: ')

kljuc = input('Unesi zeljeni kljuc (1-26): ')
kljuc = int (kljuc)

for znak in poruka:
  if znak in abeceda:
    pozicija = abeceda.find(znak)
    novaPozicija = (pozicija + kljuc) % 26
    noviZnak = abeceda[novaPozicija]
    novaPoruka += noviZnak
  else:
    novaPoruka += znak

print('Tvoja nova poruka je: ', novaPoruka)