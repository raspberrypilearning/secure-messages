#!/bin/python3

sgor = 0
enwau = input('Cofnodwch enwau 2 o bobl: ')

for cymeriad in enwau:
  if cymeriad in 'aeiou':
    sgor += 5
  if cymeriad in 'friend':
    sgor += 10

print('eich sgôr cyfeillgarwch yw :', sgor)

if sgor > 100:
  print('ffrindiau gorau!')