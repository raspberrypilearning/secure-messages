#!/bin/python3

score = 0
names = input('enter the names of 2 people: ')

for character in names:
  if character in 'aeiou':
    score += 5
  if character in 'friend':
    score += 10

print('당신의 친밀도 점수는 :', score)

if score > 100:
  print('절친이군요!')
