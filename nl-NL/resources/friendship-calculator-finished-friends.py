#!/bin/python3

score = 0
namen = input('geef twee namen: ')

for teken in namen:
  if teken in 'aeiou':
    score += 5
  if teken in 'vriend':
    score += 10

print('je vriendschapsscore is: ', score)

if score > 100:
  print('beste vrienden!')