#!/bin/python3

score = 0
names = input('두 사람의 영어 이름을 입력하시오 : ')

for character in names:
  if character in 'aeiou':
    score += 5
  if character in 'friend':
    score += 10

print('당신의 친밀도 점수는 :', score)

if score > 100:
  print('절친이군요!')