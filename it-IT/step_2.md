## Il cifrario di Cesare

Una cifrario è un tipo di codice segreto, in cui si scambiano le lettere in modo che nessuno possa comprendere il messaggio.

Utilizzerai uno dei cifrari più vecchi e famosi, il **cifrario di Caesar**, che prende il nome da Giulio Cesare.

Prima di iniziare la codifica, proviamo ad usare il cifrario di Cesare per mascherare una parola.

+ L'operazione di mascherare una parola è detta **crittografia**.
    
    Iniziamo con la crittografia della lettera 'a'. Per fare ciò, possiamo disegnare l'alfabeto in un cerchio, come questo:
    
    ![screenshot](images/messages-wheel.png)

+ Per creare una lettera crittografata segreta da una normale, è necessario disporre di una chiave segreta. Usiamo il numero 3 come chiave (ma puoi usare qualsiasi numero che ti piaccia).
    
    To **encrypt** the letter 'a', you just move 3 letters clockwise, which will give you the letter 'd':
    
    ![screenshot](images/messages-wheel-eg.png)

+ You can use what you've learnt to encrypt an entire word. For example, 'hello' encrypted is 'khoor'. Try it yourself.
    
    + h + 3 = **k**
    + e + 3 = **h**
    + l + 3 = **o**
    + l + 3 = **o**
    + o + 3 = **r**

+ Getting text back to normal is called **decryption**. To decrypt a word, just subtract the key instead of adding it:
    
    + k - 3 = **h**
    + h - 3 = **e**
    + o - 3 = **l**
    + o - 3 = **l**
    + r - 3 = **o**