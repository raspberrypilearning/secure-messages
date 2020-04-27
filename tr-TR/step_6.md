## Mesajın tamamını şifreleme

Mesajları bir seferde sadece birer harf şifrelemek ve şifresini çözmek yerine, mesajın tamamını şifrelemek için programı değiştirelim!

+ Öncelikle, kodunuzun şöyle görünüp görünmediğini kontrol edin:
    
    ![ekran görüntüsü](images/messages-character-finished.png)

+ Yeni şifreli mesajı saklamak için bir değişken oluşturun.
    
    ![ekran görüntüsü](images/messages-newmessage.png)

+ Bir harf yerine, kullanıcının mesajının hepsini bir değişkene kaydedecek şekilde kodunuzu değiştirin.
    
    ![ekran görüntüsü](images/messages-message.png)

+ `for` döngüsünü ekleyip kodun kalan kısmına girinti yaparak mesajın her harfinde kodun tekrarlanmasını sağlayın.
    
    ![ekran görüntüsü](images/messages-loop.png)

+ Kodunuzu test edin. Mesajdaki her harfin aynı anda şifrelenmiş ve tek seferde ekrana yazılmış olduğunu görmelisiniz.
    
    ![ekran görüntüsü](images/messages-loop-test.png)

+ Hadi şimdi şifrelenmiş her harfi `yenimesaj` değişkeninize ekleyelim.
    
    ![ekran görüntüsü](images/messges-message-add-character.png)

+ `yenimesaj` 'ınızın şifrelenmiş halini `print` komutuyla yazdırabilirsiniz.
    
    ![ekran görüntüsü](images/messages-print-message-characters.png)

+ `print` komutunun önündeki boşlukları silerseniz, şifreli mesaj en sonda sadece bir kez görüntülenecektir. Ayrıca harf konumlarını yazdıran kodu da silebilirsiniz.
    
    ![ekran görüntüsü](images/messages-print-message-comment.png)