#!/bin/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''
  
message = input('请输入一条英文消息：')

key = input('请输入一个密钥 (1-26)：')
key = int(key)

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character

print('你的加密后的新消息是：', newMessage)