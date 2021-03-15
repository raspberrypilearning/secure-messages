#!/bin/python3

puan = 0
names = input('enter the names of 2 people: ')

for harf in isimler:
  if harf in 'aeiou':
    puan += 5
  if harf in 'dostluk':
    puan += 10

print('ikinizin arkadaşlık puanı :', puan)

if puan > 100:
  print('en iyi arkadaşlar!')
