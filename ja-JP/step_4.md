## 文字の暗号化

単一の文字を暗号化するPythonプログラムを作成しましょう。

+ ブランクのPythonテンプレートを開き <a href="http://jumpto.cc/python-new" target="_blank">。Trinket： <a href="http://jumpto.cc/python-new" target="_blank"> jumpto.cc/python-new</a>。</p></li> 
    
    <li>
      <p>
        円でアルファベットを描くのではなく、 <code>アルファベット</code> 変数として書き出しましょう。
      </p>
      <p>
        <img src="images/messages-alphabet.png" alt="スクリーンショット" />
      </p>
    </li>
    
    <li>
      <p>
        アルファベットの各文字には、位置0から始まる位置があります。したがって、文字「a」はアルファベットの位置0にあり、「c」は位置2にあります。
      </p>
      <p>
        <img src="images/messages-array.png" alt="スクリーンショット" />
      </p>
    </li>
    
    <li>
      <p>
        位置を角かっこで書くことによって、 <code>アルファベット</code> 変数から手紙を得ることができます。
      </p>
      <p>
        <img src="images/messages-alphabet-array.png" alt="スクリーンショット" />
      </p>
      <p>
        あなたは削除することができます <code>印刷</code> あなたはこれを試してみた後、ststementsを。
      </p>
    </li>
    
    <li>
      <p>
        次に、秘密の <code>キー</code> を変数に格納する必要があります。
      </p>
      <p>
        <img src="images/messages-key.png" alt="スクリーンショット" />
      </p>
    </li>
    
    <li>
      <p>
        次に、ユーザーに暗号化する</code>文字（ <code>文字</code>と呼ばれる）を尋ねます。
      </p>
      <p>
        <img src="images/messages-character.png" alt="スクリーンショット" />
      </p>
    </li>
    
    <li>
      <p>
        <code>文字</code>の <code>位置</code> を探します。
      </p>
      <p>
        <img src="images/messages-position.png" alt="スクリーンショット" />
      </p>
    </li>
    
    <li>
      <p>
        保存された <code>ポジション</code> を印刷することでテストできます。たとえば、その文字「e」は、アルファベットの4桁目にあります。
      </p>
      <p>
        <img src="images/messages-position-test.png" alt="スクリーンショット" />
      </p>
    </li>
    
    <li>
      <p>
        <code>文字</code>を暗号化するには、 <code>キー</code> を <code>位置</code>追加する必要があります。これは <code>newPosition</code> 変数に格納されます。
      </p>
      <p>
        <img src="images/messages-newposition.png" alt="スクリーンショット" />
      </p>
    </li>
    
    <li>
      <p>
        新しい文字位置を印刷するコードを追加します。
      </p>
      <p>
        <img src="images/messages-newposition-print.png" alt="スクリーンショット" />
      </p>
    </li>
    
    <li>
      <p>
        新しいコードをテストしてください。あなたの <code>キー</code> が3であるので、 <code>位置</code> 3を加え、 <code>newPosition</code> 変数にそれを格納する必要があります。
      </p>
      <p>
        たとえば、文字 'e'は位置4にあります。暗号化するには、 <code>キー</code> （3）を追加して7を付けます。
      </p>
      <p>
        <img src="images/messages-newposition-test.png" alt="スクリーンショット" />
      </p>
    </li>
    
    <li>
      <p>
        「y」という文字を暗号化しようとするとどうなりますか？
      </p>
      <p>
        <img src="images/messages-modulus-bug.png" alt="スクリーンショット" />
      </p>
      <p>
        <code>newPosition</code> が27であり、アルファベットに27文字がないことに注目してください。
      </p>
    </li>
    
    <li>
      <p>
        <code>％</code> を使用して、新しいポジションに、ポジション26に戻るとポジション0に戻るように指示できます。
      </p>
      <p>
        <img src="images/messages-modulus.png" alt="スクリーンショット" />
      </p>
    </li>
    
    <li>
      <p>
        最後に、新しい位置に文字を印刷したいとします。
      </p>
      <p>
        たとえば、文字「e」にキーを追加すると7が、アルファベットの位置7にある文字は「h」になります。
      </p>
      <p>
        <img src="images/messages-newcharacter.png" alt="スクリーンショット" />
      </p>
    </li>
    
    <li>
      <p>
        あなたのコードを試してみてください。最後に新しい文字を印刷するだけで、印刷ステートメントのいくつかを削除することもできます。
      </p>
      <p>
        <img src="images/messages-enc-test.png" alt="スクリーンショット" />
      </p>
    </li></ul>