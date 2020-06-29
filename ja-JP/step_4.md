## 文字の暗号化

アルファベット1文字を暗号化するPythonプログラムを作成しましょう。

+ 何も入力されていないPythonのTrinketテンプレートを開きます：<a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>

+ 円形に並べてアルファベットを描く代わりに、`alphabet`（アルファベット）変数として書き出しましょう。
    
    ![スクリーンショット](images/messages-alphabet.png)

+ alphabet（アルファベット）変数の各文字には、0から始まる位置が決まっています。たとえば文字「a」はalphabet（アルファベット）変数の0の位置にあり、「c」は2の位置にあります。
    
    ![スクリーンショット](images/messages-array.png)

+ 角かっこ内に位置を指定すると、`alphabet`（アルファベット）変数から1文字取り出せます。
    
    ![スクリーンショット](images/messages-alphabet-array.png)
    
    `print`文は動作を試してみたあとに削除できます。

+ 次に、秘密の `key`（キー番号）を変数に保存する必要があります。
    
    ![スクリーンショット](images/messages-key.png)

+ そして、ユーザーに暗号化する1文字（`character`（文字）と呼ばれる）をたずねます。
    
    ![スクリーンショット](images/messages-character.png)

+ `character`（文字）の `position`（位置）を見つけます。
    
    ![スクリーンショット](images/messages-position.png)

+ 文字の位置は保存されている`position`（位置）を表示することで確認できます。たとえば、文字「e」は、alphabet（アルファベット）変数の4の位置にあります。
    
    ![スクリーンショット](images/messages-position-test.png)

+ `character`（文字）を暗号化するには、`key`（キー番号）を`posision`（位置）に足します。これを`newPosition`（新しい位置）変数に保存します。
    
    ![スクリーンショット](images/messages-newposition.png)

+ 新しい文字の位置を表示するコードを追加します。
    
    ![スクリーンショット](images/messages-newposition-print.png)

+ 新しいコードをテストしてください。`key`（キー番号）が3であるので、`position`（位置）に3を足して、`newPosition`（新しい位置）変数に保存します。
    
    たとえば、文字「e」は4の位置にあります。暗号化するために、 `key`（キー番号、3）を足して7になります。
    
    ![スクリーンショット](images/messages-newposition-test.png)

+ 文字「y」を暗号化しようとするとどうなりますか？
    
    ![スクリーンショット](images/messages-modulus-bug.png)
    
    `newPosition`（新しい位置）は27になり、アルファベットには27文字もないことに注意してください。

+ `%`を使用すると、新しい位置が26の位置に達すると0の位置に戻るようにすることができます。
    
    ![スクリーンショット](images/messages-modulus.png)

+ 最終的には新しい位置の文字を表示したいですね。
    
    たとえば、文字「e」の位置にkey（キー番号）を足すと7になり、alphabet（アルファベット）の7の位置にある文字は「h」になります。
    
    ![スクリーンショット](images/messages-newcharacter.png)

+ コードを試してみてください。print文をいくつか削除して、最後にある新しい文字を表示する文だけにします。
    
    ![スクリーンショット](images/messages-enc-test.png)