## 对字母进行加密

让我们编写一个 Python 程序来加密单个字符。



+ 打开空白 Python 模版 Trinket：<a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>。

+ 让我们将字母表写出来作为 `alphabet` 变量，而不是将其画在圆中。

	![screenshot](images/messages-alphabet.png)

+ 字母表中的每个字母都有一个位置，从位置 0 开始。因此，字母“a”在字母表中位于位置 0，“c”位于位置 2。

	![screenshot](images/messages-array.png)

+ 你可以通过在方括号内填写位置来从 `alphabet` 变量中获取一个字母。

	![screenshot](images/messages-alphabet-array.png)

	你在试过之后就可以删除 `print` 语句。

+ 接下来，你将需要在变量中储存秘密 `key`（密钥）。

	![screenshot](images/messages-key.png)

+ 然后，询问用户需要加密的字母（被称为 `character`（字符））。

	![screenshot](images/messages-character.png)

+ 找到该 `character`（字符）的 `position`（位置）。

	![screenshot](images/messages-position.png)

+ 你可以将所储存的 `position`（位置）打印出来以进行测试。例如，字符“e”位于字母表中的位置 4。

	![screenshot](images/messages-position-test.png)

+ 要加密 `character`（字符），你需要向 `position`（位置）添加 `key`（密钥）。它随后会被储存在 `newPosition` 变量中。

	![screenshot](images/messages-newposition.png)

+ 添加代码来打印出新字符的位置。 

	![screenshot](images/messages-newposition-print.png)

+ 测试你的新代码。由于你的 `key`（密钥）为 3，因此应将 `position`（位置）加上 3 并储存在你的 `newPosition` 变量中。

	例如，字母“e”位于位置 4。为进行加密，你需要加上 `key` (3)，得出 7。

	![screenshot](images/messages-newposition-test.png)

+ 你尝试加密字母“y”的话会发生什么？

	![screenshot](images/messages-modulus-bug.png)

	请注意 `newPosition` 现在变为 27，而在字母表中并没有 27 个字母！

+ 你可以使用 `%` 来告诉新位置，一旦到达位置 26，即返回位置 0。

	![screenshot](images/messages-modulus.png)

+ 最后，你想要打印出新位置的字母。

	例如，向字母“e”添加密钥得出 7，字母表中位置 7 的字母为“h”。

	![screenshot](images/messages-newcharacter.png)

+ 试试你的代码。你还可以移除某些打印语句，只在最后打印出新字符。

	![screenshot](images/messages-enc-test.png)
