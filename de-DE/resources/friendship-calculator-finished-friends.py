#! /usr/bin/python3

punkte = 0
namen = input('Gib die Namen von zwei Personen ein: ')

for zeichen in namen:
  if zeichen in 'aeiou':
    punkte += 5
  if zeichen in 'freund':
    punkte += 10

print('Der Freundschaftsindex ist: ', punkte)

if punkte > 100:
  print('Beste Freunde!')