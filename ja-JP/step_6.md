## メッセージ全体を暗号化する

メッセージを一度に1文字ずつ暗号化と復号化するのではなく、メッセージ全体を暗号化するようにプログラムを変更しましょう！

+ まず、コードが次のようになっていることを確認します。
    
    ![スクリーンショット](images/messages-character-finished.png)

+ 新しい暗号化されたメッセージを格納する変数を作成します。
    
    ![スクリーンショット](images/messages-newmessage.png)

+ 1文字だけでなくユーザーのメッセージを格納するようにコードを変更します。
    
    ![スクリーンショット](images/messages-message.png)

+ あなたのコードに</code> ループのために `を加えて、メッセージの各文字に対してそれが繰り返されるように残りのコードをインデントします。</p>

<p><img src="images/messages-loop.png" alt="スクリーンショット" /></p></li>
<li><p>コードをテストします。メッセージの各文字は暗号化され、一度に1つずつ印刷されることがわかります。</p>

<p><img src="images/messages-loop-test.png" alt="スクリーンショット" /></p></li>
<li><p>暗号化された各文字を <code>newMessage` 変数に追加しましょう。
    
    ![スクリーンショット](images/messges-message-add-character.png)

+ You can `print` the `newMessage` as it is being encrypted.
    
    ![スクリーンショット](images/messages-print-message-characters.png)

+ `print` ステートメントの前のスペースを削除すると、暗号化されたメッセージは最後に1回だけ表示されます。また、文字位置を印刷するためのコードを削除することもできます。
    
    ![スクリーンショット](images/messages-print-message-comment.png)