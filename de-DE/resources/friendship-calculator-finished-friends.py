#! /usr/bin/python3

Punktzahl = 0
namen = input('Gib die Namen von zwei Personen ein: ').lower()

for buchstabe in namen:
  if buchstabe in 'aeiou':
    Punktzahl += 5
  if Buchstabe in 'freund':
    Punktzahl += 10

print('Der Freundschaftsindex beträgt: ', Punktzahl)

if Punktzahl > 100:
  print('Beste Freunde!')