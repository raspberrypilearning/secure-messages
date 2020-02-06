#!/bin/python3

alphabet = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي'
newMessage = ''
  
message = input('الرجاء إدخال رسالة: ')

key = input('أدخل مفتاح (1-28): ')
key = int(key)

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character

print('رسالتك الجديدة هي: ', newMessage)