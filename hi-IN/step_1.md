## परिचय:

इस प्रोजेक्ट में आप सीखेंगे कि एक मित्र के साथ गुप्त संदेश भेजने और प्राप्त करने के लिए, अपना स्वयं का एन्क्रिप्शन प्रोग्राम कैसे बनाया जाए। यह प्रोजेक्ट स्पेस डायरी के पेज 16 पर "अर्थ टू प्रिंसिपिया" एक्टिविटी के साथ जुड़ा हुआ है।

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/402256078c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

### क्लब लीडरों के लिए अतिरिक्त जानकारी

यदि आप इस प्रोजेक्ट को प्रिंट करना चाहते हैं, तो कृपया [प्रिंटर अनुकूल वर्जन](https://projects.raspberrypi.org/en/projects/secret-messages/print) का उपयोग करें।

## \--- collapse \---

## शीर्षक: क्लब नेता नोट्स

## परिचय:

इस प्रोजेक्ट में बच्चे सीखेंगे कि एक मित्र के साथ गुप्त संदेश भेजने और प्राप्त करने के लिए, एन्क्रिप्शन प्रोग्राम कैसे बनाया जाए। यह प्रोजेक्ट एक टेक्स्ट स्ट्रिंग पर आईटरेशन (लूपिंग) का परिचय देता है।

## ऑनलाइन संसाधन

**इस प्रोजेक्ट में पाइथन 3 का उपयोग किया जाता है।**पाइथन को ऑनलाइन लिखने के लिए हम [ट्रिंकेट](https://trinket.io/) का उपयोग करने की सलाह देते हैं। इस प्रोजेक्ट में निम्नलिखित ट्रिंकेट्स हैं:

* [नया (रिक्त) पाइथन ट्रिंकट - jumpto.cc/python-new](http://jumpto.cc/python-new)

एक ऐसा ट्रिंकट भी है जिसमें पूर्ण किया गया प्रोजेक्ट है:

* ['Secret Messages' सम्पूर्ण - trinket.io/python/402256078c](https://trinket.io/python/402256078c)

* ['Friendship Calculator' सम्पूर्ण - trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## ऑफ़लाइन संसाधन

यदि चाहें तो इस प्रोजेक्ट को [ऑफ़लाइन पूरा](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) किया जा सकता है।

आपको 'Volunteer Resources' खंड में इस प्रोजेक्ट का पूर्ण किया गया वर्जन भी मिल सकता है, जिसमें निम्न शामिल हैं:

* messages-finished/messages.py
* messages-finished/friends.py

(उपर्युक्त सभी संसाधन प्रोजेक्ट और स्वयंसेवक `.zip` फ़ाइलों के रूप में भी डाउनलोड किए जा सकते हैं।)

## सीखने के उद्देश्य

* एक स्ट्रिंग वेरिएबल पर आईटरेशन (लूपिंग);
* ` find() ` मेथॅड;
* मॉडुलस ऑपरेटर (`%`)

इस प्रोजेक्ट में [Raspberry Pi डिजिटल निर्माण पाठ्यक्रम](http://rpf.io/curriculum) के निम्नलिखित पहलु सम्मिलित हैं:

* [समस्या को हल करने के लिए प्रोग्रामिंग संरचनाओं का उपयोग करें ।](https://www.raspberrypi.org/curriculum/programming/builder)

## चुनौतियाँ

* सीज़र साइफर का उपयोग करें - मैन्युअल रूप से अक्षरों और शब्दों को एन्क्रिप्ट और डिक्रिप्ट करें;
* वेरिएबल कीज़ - उपयोगकर्ता को एक चुने हुए 'की' को इनपुट करने की अनुमति देता है;
* संदेशों को एन्क्रिप्ट और डिक्रिप्ट करना - पूरे संदेशों को एन्क्रिप्ट और डिक्रिप्ट करना;
* Friendship calculator - एक नई समस्या के लिए टेक्स्ट पुनरावृत्ति को उपयोग करना।

## अक्सर पूछे जाने वाले प्रश्न

* `find()` का उपयोग करते हुए ढूंढें या `if char in alphabet:` का, ध्यान दें कि खोजें केस-संवेदी हैं। बच्चे उपयोग करें:
    
    ```python
    message = input("Please enter a message to encrypt: ").lower()
    ```
    
    इससे इनपुट टेक्स्ट ढूंढ़ने से पहले ही लोअर केस में हो जायेगा

\--- /collapse \---

## \--- collapse \---

## शीर्षक: परियोजना सामग्री

## प्रोजेक्ट संसाधन

* [सभी प्रोजेक्ट संसाधनों वाली .zip फ़ाइल](resources/secret-messages-project-resources.zip)
* [ऑनलाइन रिक्त पाइथन ट्रिंकेट](http://jumpto.cc/python-new)
* [ऑफ़लाइन रिक्त पाइथन फ़ाइल](resources/new-new.py)

## क्लब नेता संसाधन

* [सभी प्रोजेक्ट संसाधनों वाली .zip फ़ाइल](resources/secret-messages-volunteer-resources.zip)
* [ऑनलाइन पूर्ण ट्रिंकेट प्रोजेक्ट](https://trinket.io/python/402256078c)
* [secret-messages-finished/messages.py](resources/secret-messages-finished-messages.py)
* [ऑनलाइन पूर्ण 'Friendship calculator' चुनौती](https://trinket.io/python/2e852cd687)
* [ऑफ़लाइन पूर्ण 'Friendship calculator' चुनौती](resources/friendship-calculator-finished-friends.py)

\--- /collapse \---