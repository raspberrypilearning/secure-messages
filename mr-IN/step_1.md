## परिचय:

या प्रकल्पात, तुम्ही स्वतःच कूटबद्धीकरण कार्यक्रम बनवणं शिकाल, मित्रासह गुप्त संदेश पाठ्वण्या आणखी प्राप्त करण्यासाठी. हा प्रकल्प अंतराळ डायरीच्या पृष्ठ 16 वरील "पृथ्वी ते प्रिन्सिपिया" क्रियेशी संबंधित आहे.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/402256078c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

### क्लब नेत्यांसाठी अतिरिक्त माहिती

तुम्हाला जर हा प्रकल्प प्रिंट करायचा असेल तर आपण [प्रिंटर अनुकूल आवृत्ती](https://projects.raspberrypi.org/en/projects/secret-messages/print) चा वापर करू शकता.

## \--- collapse \---

## title: मंडळ प्रमुखासाठी टिप्पणे

## परिचय:

या प्रकल्पात, मुले कूटबद्धीकरण कार्यक्रम, मित्रासह गुप्त संदेश कसा पाठवणं आणखी प्राप्त कर्ण शिकेल. हा प्रकल्प मजकूर स्ट्रिंगवर पुनरावृत्ती (लूपिंग) सादर करतो.

## ऑनलाईन संसाधने

**हा प्रकल्प Python 3 चा वापर करतो.** आम्ही Python ऑनलाइन लिहण्याकरिता [trinket](https://trinket.io/) वापरण्याची शिफारस करतो. या प्रकल्पात पुढील Trinkets आहे:

* [नवीन (रिकामं) Python Trinket -- jumpto.cc/python-new](http://jumpto.cc/python-new)

येथे finished झालेले project असलेले एक trinket देखील आहे:

* ['गुप्त संदेश' पूर्ण -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

* ['मैत्री कॅल्क्युलेटर' पूर्ण -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## ऑफलाइन संसाधने

वाटल्यास हे प्रोजेक्ट [ऑफलाइन पूर्ण केलं जाऊ शकते](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/).

आपण पूर्ण झालेला प्रकल्प शोधू शकता स्वयंसेवक संसाधने('Volunteer Resources') मध्ये, ज्यामध्ये असते:

* messages-finished/messages.py
* messages-finished/friends.py

(वरील सर्व संसाधने प्रोजेक्ट आणि वॉलंटियर `.zip` फाइली म्हणून डाऊनलोड करण्यायोग्य देखील आहेत.)

## शिकण्याचे उद्दिष्टे

* ज्यामध्ये स्ट्रिंग व्हेरिएबलपेक्षा Iteration (looping) असते;
* `find()` मेथड;
* मॉड्यूलस ऑपरेटर (`%`).

ह्या प्रोजेक्ट मध्ये [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum) च्या अभयासक्रमातील पुढील घटकांचा समावेश आहे:

* [समस्या सोडवण्यासाठी प्रोग्रामिंग संकल्पना एकत्र करा.](https://www.raspberrypi.org/curriculum/programming/builder)

## आव्हाने

* सीझर सायफर वापरा - एनक्रिप्ट आणि डिक्रिप्ट अक्षरे आणि शब्द स्वहस्ते;
* व्हेरिएबल की - वापरकर्त्यास निवडलेली की इनपुट करण्याची परवानगी;
* संदेश कूटबद्ध आणि डिक्रिप्ट करणे - संपूर्ण संदेश कूटबद्ध आणि डिक्रिप्ट करणे;
* मैत्री कॅल्क्युलेटर - नवीन समस्येवर मजकूर पुनरावृत्ती लागू करत आहे.

## वारंवार विचारले जाणारे प्रश्न

* जेव्हा शोधात असाल वापरत असताना `find()` or `if char in alphabet:`, लक्षात घ्या की शोध केस-सेन्सेटिव्ह आहेत. मुले वापरू शकतात:
    
    ```python
    message = input("Please enter a message to encrypt: ").lower()
    ```
    
    शोधण्यापूर्वी input लोअर केस बनविणे.

\--- /collapse \---

## \--- collapse \---

## title: प्रकल्प साहित्य

## प्रकल्प संसाधने

* [सर्व प्रकल्पाची संसाधने असलेली .zip फाइल](resources/secret-messages-project-resources.zip)
* [ऑनलाइन रिकामं Python Trinket](http://jumpto.cc/python-new)
* [ऑफलाइन रिकामी Python फाइल](resources/new-new.py)

## क्लब प्रमुख संसाधने

* [सर्व पूर्ण झालेली प्रोजेक्ट संसाधने असलेली .zip फाइल](resources/secret-messages-volunteer-resources.zip)
* [ऑनलाइन पूर्ण झालेले Trinket प्रोजेक्ट](https://trinket.io/python/402256078c)
* [secret-messages-finished/messages.py](resources/secret-messages-finished-messages.py)
* [ऑनलाईन 'मैत्री कॅल्क्युलेटर' पूर्ण झालेला आव्हान](https://trinket.io/python/2e852cd687)
* [ऑनलाईन 'मैत्री कॅल्क्युलेटर' पूर्ण झालेला आव्हान](resources/friendship-calculator-finished-friends.py)

\--- /collapse \---