## संपूर्ण संदेश कूटबद्ध करत आहे

संदेशांना एका वेळी फक्त एक वर्ण कूटबद्ध (encrypting) आणि डिक्रिप्ट (decrypting) करण्याऐवजी, संपूर्ण संदेश कूटबद्ध करण्यासाठी प्रोग्राम बदलूया!

+ प्रथम, आपला कोड असा दिसतो हे तपासा:
    
    ![screenshot](images/messages-character-finished.png)

+ नवीन कूटबद्ध संदेश संचयित करण्यासाठी एक व्हेरिएबल तयार करा.
    
    ![screenshot](images/messages-newmessage.png)

+ वापरकर्त्याचा संदेश संचयित करण्यासाठी आपला कोड बदला, फक्त एक वर्ण नाही.
    
    ![screenshot](images/messages-message.png)

+ आपल्या कोडमध्ये `for` loop जोडा, आणि उर्वरित कोड इंडेंट करा जेणेकरून संदेशातील प्रत्येक वर्णासाठी त्याची पुनरावृत्ती होईल.
    
    ![screenshot](images/messages-loop.png)

+ आपला कोड तपासा. संदेशामधील प्रत्येक वर्ण एकावेळी कूटबद्ध व मुद्रित केलेला दिसेल.
    
    ![screenshot](images/messages-loop-test.png)

+ चला आपल्या प्रत्येक एन्क्रिप्टेड वर्ण मध्ये `newMessage` चल जोडा.
    
    ![screenshot](images/messges-message-add-character.png)

+ आपण हे `newMessage` `print` करू शकता जसे की ते कूटबद्ध केले जात आहे.
    
    ![screenshot](images/messages-print-message-characters.png)

+ जर आपण मोकळी जागा हटवली `print` विधानाच्या आधी, एन्क्रिप्टेड संदेश शेवटी एकदाच दिसेल. वर्ण स्थिती प्रिंट करण्यासाठी कोड तुम्ही डिलीट करू शकता.
    
    ![screenshot](images/messages-print-message-comment.png)