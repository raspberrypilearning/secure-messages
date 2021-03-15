#!/bin/python3

sgor = 0
names = input('enter the names of 2 people: ')

for cymeriad in enwau:
  if cymeriad in 'aeiou':
    sgor += 5
  if cymeriad in 'friend':
    sgor += 10

print('eich sgôr cyfeillgarwch yw :', sgor)

if sgor > 100:
  print('ffrindiau gorau!')
