## Şifreli harfler

Hadi bir tek harfi şifrelemek için bir Python programı yazalım.

+ Trinket'ta boş Python şablonunu açın: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Alfabeyi bir daire içine çizmek yerine, onu `alfabe` değişkeni olarak yazalım.
    
    ![ekran görüntüsü](images/messages-alphabet.png)

+ Alfabedeki her harf, 0 konumundan başlayan bir konuma sahiptir. Bu nedenle 'a' harfi alfabenin 0 konumunda ve 'c' harfi 2. konumdadır.
    
    ![ekran görüntüsü](images/messages-array.png)

+ `alfabe` değişkeninizden bir harfe, konumunu köşeli parantezin içine yazarak ulaşabilirsiniz.
    
    ![ekran görüntüsü](images/messages-alphabet-array.png)
    
    Bunu bir kez denedikten sonra `print` komutlarını silebilirsiniz.

+ Daha sonra gizli `anahtarı` bir değişkene kaydetmeniz gerekecek.
    
    ![ekran görüntüsü](images/messages-key.png)

+ Ardından kullanıcıdan şifrelemek bir harf girmesini isteyin (`harf` değişkeni isimli).
    
    ![ekran görüntüsü](images/messages-character.png)

+ `harf` 'in `konum` 'unu bulun.
    
    ![ekran görüntüsü](images/messages-position.png)

+ Veri kaydedilmiş `konum` değişkenini ekrana yazdırarak test edebilirsiniz. Örneğin, 'e' harfi alfabede 5. konumdadır.
    
    ![ekran görüntüsü](images/messages-position-test.png)

+ `harf`i şifrelemek için, `konum` değişkeniyle `anahtar` değişkenini toplamalısınız. Daha sonra elde edilen değer `yenikonum` değişkenine kaydedilir.
    
    ![ekran görüntüsü](images/messages-newposition.png)

+ Harfin yeni konumunu yazdırmak için kod ekleyin.
    
    ![ekran görüntüsü](images/messages-newposition-print.png)

+ Yeni kodunuzu test edin. `anahtar`'ınız 3 olduğundan `konum` değişkenine 3 eklemeli ve bunu `yenikonum` değişkeninde saklanmalı.
    
    Örneğin, 'e' harfi 5 konumunda. Şifrelemek için `anahtar`'la (3) toplarız, 8 sonucunu verir.
    
    ![ekran görüntüsü](images/messages-newposition-test.png)

+ 'Y' harfini şifreleyip denediğinizde neler olur?
    
    ![ekran görüntüsü](images/messages-modulus-bug.png)
    
    Alfabede 30 harf olmadığı halde `yenikonum` değişkeninin nasıl 30 olduğuna dikkat edin!

+ Yeni konum 28 olduğunda tekrar baştaki 0 konumuna dönmesini sağlamak için `%` işaretini kullanabilirsiniz.
    
    ![ekran görüntüsü](images/messages-modulus.png)

+ Son olarak, yeni konumdaki harfi yazdırmak istiyorsunuz.
    
    Örneğin 'e' harfine anahtarı eklediğimizde sonuç 8 oluyordu, alfabedeki 8. konumda ise 'ğ' harfi var.
    
    ![ekran görüntüsü](images/messages-newcharacter.png)

+ Kodunuzu deneyin. Yeni harfi sadece sona yazdıran bazı yazdır komutu satırlarınızı, koddan kaldırabilirsiniz.
    
    ![ekran görüntüsü](images/messages-enc-test.png)