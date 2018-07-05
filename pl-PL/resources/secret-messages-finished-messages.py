#!/bin/python3

alfabet = 'abcdefghijklmnopqrstuvwxyz' nowaWiadomosc = ''
  
wiadomość = input ('Prosze wprowadzic wiadomosc: ')

klucz = input('Wprowadz klucz (1-26): ')
klucz = int(klucz)

for litera in wiadomość:
  if litera in alfabet:
    pozycja = alfabet.find(litera)
    nowaPozycja = (pozycja + klucz) % 26
    nowaLitera = alfabet[nowaPozycja]
    nowaWiadomość += nowaLitera
  else:
    nowaWiadomość += litera

print ('Twoja nowa wiadomość to: ', nowaWiadomosc)