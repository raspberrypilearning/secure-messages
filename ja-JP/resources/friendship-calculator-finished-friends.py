#!/bin/python3

score = 0
names = input('2人分の名前を入力してください: ')

for character in names:
  if character in 'aeiou':
    score += 5
  if character in 'friend':
    score += 10

print('あなたたちのなかよし点数はこちらです :', score)

if score > 100:
    print('大のなかよしです！')