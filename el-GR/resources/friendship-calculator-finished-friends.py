#!/bin/python3

score = 0
names = input('δώσε τα ονόματα 2 ατόμων: ')

for character in names:
  if character in 'αεηιυοω':
    score += 5
  if character in 'φιλοσ':
    score += 10

print('το σκορ φιλίας σου είναι :', score)

if score > 100:
  print('οι καλύτεροι φίλοι!')