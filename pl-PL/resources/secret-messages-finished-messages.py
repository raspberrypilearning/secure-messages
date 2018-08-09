#!/bin/python3

alfabet = 'abcdefghijklmnopqrstuvwxyz' 
nowaWiadomosc = ''
  
wiadomosc = input('Wprowadź wiadomość: ')

klucz = input('Wprowadź klucz (1-26): ')
klucz = int(klucz)

for litera in wiadomosc:
  if litera in alfabet:
    pozycja = alfabet.find(litera)
    nowaPozycja = (pozycja + klucz) % 26
    nowaLitera = alfabet[nowaPozycja]
    nowaWiadomosc += nowaLitera
  else:
    nowaWiadomosc += litera

print('Twoja nowa wiadomość to: ', nowaWiadomosc)