## वर्णों को इनक्रिप्ट करना

चलिए कैरेक्टर को इनक्रिप्ट करने के लिए पाइथन प्रोग्राम लिखें।



+ खाली Python टेंम्पलेट ट्रिंकेट खोलें: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ वृत्त में अक्षर लिखने के बजाय, चलिए इसे `alphabet` वेरिएबल के रूप में लिखें।

	![screenshot](images/messages-alphabet.png)

+ अक्षर में प्रत्येक वर्ण का स्तर है, यह स्तर 0 से आंरभ होता है। इसलिए वर्ण 'a' अक्षर के शीर्ष स्तर 0 पर होता है, और 'c' स्तर 2 पर होता है।

	![screenshot](images/messages-array.png)

+ आप वर्ग ब्रैकेट्स में स्तर लिखकर अपने `alphabet` वेरिएबल से वर्ण प्राप्त कर सकते हैं।

	![screenshot](images/messages-alphabet-array.png)

	इसका एक बार उपयोग करने पर आप `print` स्टेटमेंट को मिटा सकते हैं।

+ इसके बाद, आपको वेरिएबल में गुप्त `key` (कुंजी) स्टोर करनी होगी।

	![screenshot](images/messages-key.png)

+ इसके बाद, उपयोगकर्ता को वर्ण (`character` (कैरेक्टर)) को इनक्रिप्ट करने के लिए कहें।

	![screenshot](images/messages-character.png)

+ `position` (कैरेक्टर) का `character` (स्तर) ढूँढ़ें।

	![screenshot](images/messages-position.png)

+ आप स्टोर किए गए `position` (स्तर) को प्रिंट करके इसका परीक्षण कर सकते हैं। उदाहरण के लिए, कैरेक्टर 'e' अक्षर में स्तर 4 पर है।

	![screenshot](images/messages-position-test.png)

+ `character` (कैरेक्टर) को इनक्रिप्ट करने के लिए, आपको `position` (स्थिति) में `key` (बटन )  शामिल करनी चाहिए। इसके बाद इसे `newPosition` वेरिएबल में स्टोर किया जाता है।

	![screenshot](images/messages-newposition.png)

+ नए कैरेक्टर के स्तर को प्रिंट करने के लिए कोड जोड़ें। 

	![screenshot](images/messages-newposition-print.png)

+ अपने नए कोड का परीक्षण करें। जैसे आपकी `key` (बटन) 3 है, इसे `position` (स्थिति) में 3 जोड़ना चाहिए और आपके `newPosition` (नई स्थिति) वेरिएबल में स्टोर करना चाहिए।

	उदाहरण के लिए, वर्ण 'e' स्तर 4 पर होता है। इनक्रिप्ट करने के लिए, आप 7 दर्ज करके `key` (बटन) (3) शामिल करते हैं।

	![screenshot](images/messages-newposition-test.png)

+ जब आप वर्ण 'y' को इनक्रिप्ट करने का प्रयास करते हैं, तो क्या होता है?

	![screenshot](images/messages-modulus-bug.png)

	ध्यान दें कि कैसे `newPosition` 27 होता है, और अक्षर में 27 वर्ण नहीं हैं!

+ आप नया स्तर 26 होने पर इसे वापस 0 पर जाने के लिए कहने के लिए `%` का उपयोग करते हैं।

	![screenshot](images/messages-modulus.png)

+ अंततः आप वर्ण को नए स्तर पर प्रिंट करना चाहते हैं।

	उदाहरण के लिए, वर्ण 'e' में कुंजी शामिल करने पर यह 7 देता है, और अक्षर के स्तर 7 पर वर्ण 'h' है।

	![screenshot](images/messages-newcharacter.png)

+ अपने कोड का परीक्षण करें। आप अंत में नया करैक्टर प्रिंट करके, अपनी कुछ प्रिंट स्टेटमेंट्स को हटा भी सकते हैं।

	![screenshot](images/messages-enc-test.png)
