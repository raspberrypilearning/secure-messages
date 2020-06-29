## 对字母进行加密

让我们编写一个Python程序来加密单个字符。

+ 单击链接<a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>，打开一个空白的Python Trinket模版。

+ 与其在圆圈中绘制字母表, 不如将其写入`alphabet`变量中。
    
    ![截图](images/messages-alphabet.png)

+ 字母表中的每个字母都有一个位置，从位置0开始。因此字母“a”位于字母表的第0位，“c”位于第2位。
    
    ![截图](images/messages-array.png)

+ 通过将其位置写在方括号内, 可以从 `alphabet` 变量中获取某个字母。
    
    ![截图](images/messages-alphabet-array.png)
    
    尝试此操作后, 您可以删除 `print` 语句。

+ 接下来，你要将密钥保存在变量`key`中。
    
    ![截图](images/messages-key.png)

+ 接下来，询问用户一个字母（称为变量`character`）进行加密。
    
    ![截图](images/messages-character.png)

+ 找到字母（变量`character`）在字母表中的位置（变量`position`）。
    
    ![截图](images/messages-position.png)

+ 你可以通过显示变量`position`来进行测试。比如，字母”e"在字母表中的位置是4。
    
    ![截图](images/messages-position-test.png)

+ 若要加密字母（变量`character`），你需要将字母的位置（变量`position`）加上密钥的值（变量`key`），然后将其保存到`newPosition`变量中。
    
    ![截图](images/messages-newposition.png)

+ 添加代码以输出新的字符位置。
    
    ![截图](images/messages-newposition-print.png)

+ 测试你的新代码。由于你的`key`（密钥）是3，因此应该将`position`变量加上3并将结果存储在你的`newPosition`变量中。
    
    例如，字母'e'的位置是4，要加密该字母，你应当加上`key`（3）而得到7。
    
    ![截图](images/messages-newposition-test.png)

+ 当你尝试加密字母＇y＇时又会发生什么情况呢？
    
    ![截图](images/messages-modulus-bug.png)
    
    请注意此时 `newPosition` 的值是27，但是字母表中并没有27个字母！

+ 一旦达到位置26，你可以使用`%`操作符重置，从位置0重新开始。
    
    ![截图](images/messages-modulus.png)

+ 最后，你要输出新位置所代表的字母。
    
    比如，字母＇e＇加上密钥后得到7，然后字母表中位置7所代表的字母为＇h＇。
    
    ![截图](images/messages-newcharacter.png)

+ 试试你的代码，你可以删除一些输出的语句，只需要在最后输出加密后的新字符就可以了。
    
    ![截图](images/messages-enc-test.png)