#!/bin/python3

score = 0
names = input('entrer les noms des 2 personnes: ')

for character in names:
  if character in 'aeiou':
    score += 5
  if character in 'friend':
    score += 10

print('ton score amitié est de:', score)

if score > 100:
  print('meilleurs amis!')