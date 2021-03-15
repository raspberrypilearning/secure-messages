#!/bin/python3

punteggio = 0
names = input('enter the names of 2 people: ')

for lettera in nomi:
  if lettera in 'aeiou':
    punteggio += 5
  if lettera in 'amici':
    punteggio += 10

print('il vostro livello di amicizia è :', punteggio)

if punteggio > 100:
  print('Siete ottimi amici!')
