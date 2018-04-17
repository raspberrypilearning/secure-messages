## भूमिका:

इस प्रोजेक्ट में, आप मित्र से गुप्त संदेश प्राप्त करने और भेजने के लिए अपना स्वयं का इनक्रिप्शन प्रोग्राम बनाना सीखेंगे। यह प्रोजेक्ट स्पेस डायरी के पृष्ठ 16 पर "पृथ्वी से प्रिंसिपा" गतिविधि से जुड़ा है।

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/402256078c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

### क्लब लीडर्स के लिए अतिरिक्त जानकारी

यदि आप इस प्रोजेक्ट को प्रिंट करना चाहते हैं, तो कृपया [प्रिंटर के लिए अनुकूल संस्करण](https://projects.raspberrypi.org/en/projects/secret-messages/print) का उपयोग करें।


--- collapse ---
---
title: क्लब लीडर के नोट्स
---


## भूमिका:
इस प्रोजेक्ट में, बच्चे मित्र से गुप्त संदेश प्राप्त करने और भेजने के लिए अपना स्वयं का इनक्रिप्शन प्रोग्राम बनाना सीखेंगे। इस प्रोजेक्ट में टेक्स्ट स्ट्रिंग पर इट्रेशन (लूपिंग) का उपयोग होता है।

## ऑनलाइन संसाधन

__यह प्रोजेक्ट Python 3 का उपयोग करता है।__ हम Python ऑनलाइन लिखने के लिए [trinket](https://trinket.io/) का उपयोग करने की अनुशंसा करते हैं। इस प्रोजेक्ट में निम्नलिखित Trinkets शामिल होते हैं:

+ [नया (खाली) Python ट्रिंकेट -- jumpto.cc/python-new](http://jumpto.cc/python-new)

यहाँ ऐसा ट्रिंकेट भी मौजूद है जिसमें पूर्ण प्रोजेक्ट शामिल है:

+ [‘गुप्त संदेश’ पूर्ण -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

+ [‘मित्रता कैलकुलेटर’ पूर्ण -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## ऑफ़लाइन संसाधन
इस प्रोजेक्ट को [ऑफ़लाइन पूरा किया जा सकता है](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) यदि वरीय हो।

आप इसे पूर्ण प्रोजेक्ट 'स्वैच्छिक संसाधन' भाग में देख सकते हैं, जिसमें ये शामिल हैं:

+ messages-finished/messages.py
+ messages-finished/friends.py

(ऊपर्युक्त सभी संसाधन, प्रोजेक्ट और स्वैच्छिक `.zip` फाइलों के रूप में डाउनलोड योग्य भी होते हैं।)

## अधिगम उद्देश्य
+ स्ट्रिंग वेरिएबल में इट्रेशन (लूपिंग);
+ `find()` विधि;
+ मॉड्यूलर ऑपरेटर (`%`)।

इस प्रोजेक्ट में [Raspberry Pi डिजिटल निर्माण पाठ्यचर्या](http://rpf.io/curriculum) के निम्नलिखित चीज़ों के तत्व शामिल होते हैं:

+ [समस्या का हल करने के लिए प्रोग्रामिंग निर्माण का संयोजन करें।](https://www.raspberrypi.org/curriculum/programming/builder)

## चुनौतियाँ
+ सीज़र साइफर का उपयोग करना – मैनुअल तौर पर वर्णों और शब्दों को इनक्रिप्ट और डिक्रिप्ट करना;
+ वेरिएबल कुंजियाँ – उपयोगकर्ता को चयनित कुंजी इनपुट करने की सुविधा देना;
+ संदेशों को इनक्रिप्ट और डिक्रिप्ट करना – संपूर्ण संदेशों को इनक्रिप्ट और डिक्रिप्ट करना;
+ मित्रता कैलकुलेटर – नई समस्या में टेक्स्ट की इट्रेशन लागू करना।

## अक्सर पूछे जाने वाले प्रश्न
+ जब `find()` या `if char in alphabet:` का उपयोग कर रहे हों, तो ध्यान दें कि खोज केस-संवेदी होती हैं। बच्चे उपयोग कर सकते हैं:

	```python
	message = input("Please enter a message to encrypt: ").lower()
	```

	खोज से पहले इनपुट को छोटे अक्षरों में परिवर्तित करना।

--- /collapse ---


--- collapse ---
---
title: प्रोजेक्ट सामग्री
---
## प्रोजेक्ट संसाधन
* [प्रोजेक्ट के सभी संसाधनों सहित .zip फाइल](resources/secret-messages-project-resources.zip)
* [ऑनलाइन खाली Python Trinket](http://jumpto.cc/python-new)
* [ऑफ़लाइन खाली Python फ़ाइल](resources/new-new.py)

## क्लब लीडर के संसाधन
* [प्रोजेक्ट के सभी पूर्ण संसाधनों सहित .zip फाइल](resources/secret-messages-volunteer-resources.zip)
* [ऑनलाइन पूर्ण ट्रिंकेट प्रोजेक्ट](https://trinket.io/python/402256078c)
* [secret-messages-finished/messages.py](resources/secret-messages-finished-messages.py)
* [ऑनलाइन पूरी की गई 'मित्रता कैलकुलेटर' चुनौती](https://trinket.io/python/2e852cd687)
* [ऑफ़लाइन पूर्ण 'मित्रता कैलकुलेटर' चुनौती](resources/friendship-calculator-finished-friends.py)

--- /collapse ---
