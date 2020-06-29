#!/bin/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''
  
message = input('請輸入一個訊息: ')

key = input('輸入一個鑰匙 (1-26): ')
key = int(key)

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character

print('你的新訊息是: ', newMessage)