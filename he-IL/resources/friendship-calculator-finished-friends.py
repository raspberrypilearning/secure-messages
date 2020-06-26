#!/bin/python3

score = 0
names = input('אנא הזינו שמות של שני אנשים (באנגלית): ')

for character in names:
  if character in 'aeiou':
    score += 5
  if character in 'friend':
    score += 10

print('ציון החברות שלכם הוא:', score)

if score > 100:
  print('החברים הכי טובים!')