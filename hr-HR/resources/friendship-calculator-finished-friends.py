#!/bin/python3

rezultat = 0
ime = input('Unesi imena dviju osoba: ')

for znak in ime:
  if znak in 'aeiou':
    rezultat += 5
  if znak in 'prijatelj':
    rezultat += 10

print('Vas rezultat prijateljstva je :', rezultat)

if rezultat > 100:
  print('Najbolji prijatelji!')