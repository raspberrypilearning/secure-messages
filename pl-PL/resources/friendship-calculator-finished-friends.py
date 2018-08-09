#!/bin/python3

wynik = 0
imiona = input('wprowadź imiona 2 ludzi: ')

for litera in imiona:
  if litera in 'aeiou':
    wynik += 5
  if litera in 'przyjaciel':
    wynik += 10

print('wynik twojej przyjaźni to :', wynik)

if wynik > 100:
  print ('najlepsi przyjaciele!')