#!/bin/python3

rezultat = 0
imena = input('Unesi imena dviju osoba: ')

for znak in imena:
  if znak in 'aeiou':
    rezultat += 5
  if znak in 'prijatelj':
    rezultat += 10

print('Vaš rezultat prijateljstva je: ', rezultat)

if rezultat > 100:
  print('Najbolji prijatelji!')