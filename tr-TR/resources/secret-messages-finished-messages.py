#!/bin/python3

alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
yenimesaj = ''
  
mesaj = input('Lütfen mesajınızı yazın: ')

anahtar = input('Anahtar sayıyı girin (1-29): ')
anahtar = int(anahtar)

for harf in mesaj:
  if harf in alfabe:
    konum = alfabe.find(harf)
    yenikonum = (konum + anahtar) % 29
    yeniharf = alfabe[yenikonum]
    yenimesaj += yeniharf
  else:
    yenimesaj += harf

print('Yeni mesajınız: ', yenimesaj)