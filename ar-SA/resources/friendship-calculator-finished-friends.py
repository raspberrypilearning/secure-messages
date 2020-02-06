#!/bin/python3

score = 0
names = input('أدخل أسماء شخصين: ')

for character in names:
  if character in 'اوي':
      score += 5
  if character in 'صديق':
    score += 10

print('درجة صداقتك هي:', score)

if score > 100:
  print('أفضل الأصدقاء!')