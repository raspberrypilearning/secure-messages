## The Caesar cipher

A cipher is a type of secret code, where you swap the letters around so that no-one can read your message.

You'll be using one of the oldest and most famous ciphers, the __Caesar cipher__, which is named after Julius Caesar.

Before we start coding, let's try using the Caesar cipher to hide a word.



+ Hiding a word is called __encryption__.

	Let's start by encrypting the letter 'a'. To do this, we can draw the alphabet in a circle, like this:

	![screenshot](images/messages-wheel.png)

+ To make a secret encrypted letter from a normal one, you need to have a secret key. Let's use the number 3 as the key (but you can use any number you like).

	To __encrypt__ the letter 'a', you just move 3 letters clockwise, which will give you the letter 'd':

	![screenshot](images/messages-wheel-eg.png)

+ You can use what you've learnt to encrypt an entire word. For example, 'hello' encrypted is 'khoor'. Try it yourself.

	+ h + 3 = __k__
	+ e + 3 = __h__
	+ l + 3 = __o__
	+ l + 3 = __o__
	+ o + 3 = __r__

+ Getting text back to normal is called __decryption__. To decrypt a word, just subtract the key instead of adding it:

	+ k - 3 = __h__
	+ h - 3 = __e__
	+ o - 3 = __l__
	+ o - 3 = __l__
	+ r - 3 = __o__	

