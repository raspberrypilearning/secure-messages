#!/bin/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz';
newMessage = ''
  
message = input('メッセージを入力してください: ')

key = input('キー番号(1～26)を入力してください: ')
key = int(key)

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character

print('新しいメッセージはこちらです: ', newMessage)