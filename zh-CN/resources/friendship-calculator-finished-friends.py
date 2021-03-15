#!/bin/python3

score = 0
names = input('enter the names of 2 people: ')

for character in names:
  if character in 'aeiou':
    score += 5
  if character in '朋友':
    score += 10

print('你们的友情分数是：', score)

if score > 100:
  print('最好的朋友！')
