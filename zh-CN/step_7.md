## 其他字符

一些字符不在字母表中，会造成错误。



+ 使用字母表中不存在的一些字符来测试你的代码。

	例如，你可以使用 `hi there!!`（你好！！）这条信息。

	![screenshot](images/messages-extra-characters.png)

	请注意空格和 `!` 字符都被加密为字母“c”！

+ 为解决这个问题，你希望只转换字母表中的字符。为此，向你的代码添加一个 `if`语句，并缩进剩余代码。

	![screenshot](images/messages-if.png)

+ 用同样的信息来测试你的代码。这次会发生什么？

	![screenshot](images/messages-if-test.png)

	现在，你的代码会跳过不在字母表中的字符。

+ 如果你的代码并未对不在字母表中的内容进行加密，而只是使用原来的字符，那就更好了。

	向你的代码添加 `else` 语句，这会将原始字符添加到已加密的信息中。

	![screenshot](images/messages-else.png)

+ 测试你的代码。你会看到字母表中的所有字符已被加密，而其他字符则保持原样！

	![screenshot](images/messages-else-test.png)



