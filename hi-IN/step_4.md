## वर्णों को इनक्रिप्ट करना

आइए एक अक्षर को एन्क्रिप्ट करने के लिए पायथन प्रोग्राम लिखें।

+ रिक्त पायथन टेंपलेट ट्रिंकेट खोलें: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ किसी वृत्त में वर्णमाला बनाने के बजाय, इसे `alphabet` वेरिएबल के रूप में लिखते हैं ।
    
    ![स्क्रीनशॉट](images/messages-alphabet.png)

+ वर्णमाला के प्रत्येक अक्षर की एक position होती है । position 0 पर शुरू होती है। इसलिए अक्षर 'a' वर्णमाला के स्थान पर 0 है, और 'c' स्थान 2 पर है।
    
    ![स्क्रीनशॉट](images/messages-array.png)

+ आप अपने ` alphabet ` वेरिएबल कोष्ठक में स्थिति लिखकर एक अक्षर पा सकते हैं।
    
    ![स्क्रीनशॉट](images/messages-alphabet-array.png)
    
    एक बार जब आप इसे आज़मा लें, आप `print` हटा सकते हैं।

+ इसके बाद, आपको गुप्त `key` एक वेरिएबल में रखनी होगी।
    
    ![स्क्रीनशॉट](images/messages-key.png)

+ इसके बाद एन्क्रिप्ट करने के लिए उपयोगकर्ता से एक अक्षर के लिए पूछें (जिसे `character` कहा जाता है ) ।
    
    ![स्क्रीनशॉट](images/messages-character.png)

+ `character` की `position` का पता लगाएं।
    
    ![स्क्रीनशॉट](images/messages-position.png)

+ आप संग्रहित `position` को छापकर इसका परीक्षण कर सकते हैं। उदाहरण के लिए, वह वर्ण 'e' वर्णमाला में स्थिति 4 पर है।
    
    ![स्क्रीनशॉट](images/messages-position-test.png)

+ `character` एन्क्रिप्ट करने के लिए आप `position` में `key` जोड़ें। इसे तब `newPosition` वेरिएबल में संग्रहित करें।
    
    ![स्क्रीनशॉट](images/messages-newposition.png)

+ नई character position प्रिंट करने के लिए कोड लिखें।
    
    ![स्क्रीनशॉट](images/messages-newposition-print.png)

+ अपने नए कोड का परीक्षण करें। अपनी `key` 3 है, इसलिए इसे 3 को `position` में जोड़ना चाहिए और इसे अपने `newPosition` वेरिएबल में संग्रहीत करना चाहिए।
    
    उदाहरण के लिए, 'e' position 4 पर है। एन्क्रिप्ट करने के लिए, आप `key` (3) जोड़ें, जो कि आपको 7 दे।
    
    ![स्क्रीनशॉट](images/messages-newposition-test.png)

+ जब आप 'y' अक्षर को एन्क्रिप्ट करके देखते हैं तो क्या होता है?
    
    ![स्क्रीनशॉट](images/messages-modulus-bug.png)
    
    ध्यान दें कि कैसे `newPosition` 27 है, और वर्णमाला में 27 अक्षर नहीं हैं!

+ एक बार position 26 पर पहुंचने क बाद, 0 position पर वापस जाने के लिए, new position के साथ `%` का उपयोग कर सकते हैं ।
    
    ![स्क्रीनशॉट](images/messages-modulus.png)

+ अंत में, आप new position में अक्षर को प्रिंट करें।
    
    उदाहरण के लिए, 'e' अक्षर में key जोड़ने से 7 मिलता है, और वर्णमाला में 7 की position में अक्षर 'h' है।
    
    ![स्क्रीनशॉट](images/messages-newcharacter.png)

+ अपना कोड आज़माएं। आप अपने कुछ प्रिंट स्टेटमेंट हटा भी सकते हैं, बस अंत में नए अक्षर को प्रिंट कर सकते हैं।
    
    ![स्क्रीनशॉट](images/messages-enc-test.png)