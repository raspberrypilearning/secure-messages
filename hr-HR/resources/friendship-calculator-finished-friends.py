#!/bin/python3

rezultat = 0
names = input('enter the names of 2 people: ')

for znak in ime:
  if znak in 'aeiou':
    rezultat += 5
  if znak in 'prijatelj':
    rezultat += 10

print('Vas rezultat prijateljstva je :', rezultat)

if rezultat > 100:
  print('Najbolji prijatelji!')
