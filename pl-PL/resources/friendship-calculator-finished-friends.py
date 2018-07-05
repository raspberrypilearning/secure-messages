#!/bin/python3

wynik = 0
imiona = input('wprowadz imiona 2 ludzi: ')

for litera in wiadomość:
  if litera in 'aeiou':
    wynik + = 5
  if litera in 'przyjaciel':
    wynik + = 10

print('wynik twojej przyjazni to :', wynik)

if wynik > 100:
  print ('najlepsi przyjaciele!')