## अक्षरे कूटबद्ध करत आहे

चला एक Python कार्यक्रम लिहू एकल वर्ण कूटबद्ध(encrypt) करण्यासाठी.

+ रिक्त Python template Trinket उघडा: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ एका वर्तुळात वर्णमाला रेखाटणेच्या ऐवजी हे `alphabet` व्हेरिएबल म्हणून लिहा.
    
    ![screenshot](images/messages-alphabet.png)

+ वर्णमालाच्या प्रत्येक अक्षराला एक स्थान असते स्थितीची सुरवात 0 वरून होते. तर अक्षर 'अ' हा वर्णमालाच्या 0 स्थितीवर आहे, आणखी 'सी' हा स्थिती २ वर.
    
    ![screenshot](images/messages-array.png)

+ चौकोनी विभागात स्थान लिहून तुम्ही आपल्या `alphabet` चरातून अक्षर मिळवू शकता.
    
    ![screenshot](images/messages-alphabet-array.png)
    
    आपण `print` विधान हटवू शकता एकदा आपण हे करून पाहिले असेल तर.

+ पुढे आपल्याला आवश्यक आहे रहस्य `key` साठवण्याची चल मध्ये.
    
    ![screenshot](images/messages-key.png)

+ पुढे, वापरकर्त्याला एकच अक्षर विचारा(ज्याला `character` म्हणतात) कूटबद्ध करण्यासाठी.
    
    ![screenshot](images/messages-character.png)

+ `character` ची `position` शोधा.
    
    ![screenshot](images/messages-position.png)

+ आपण चाचणी करू शकता संग्रहित `position` छापून. उदाहरणार्थ, ते वर्ण 'e' वर्णमाला 4 व्या स्थानावर आहेत.
    
    ![screenshot](images/messages-position-test.png)

+ `character` कूटबद्ध करण्यासाठी आपण `key` जोडावे `position` वर. हे नंतर `newPosition` चल वर साठवले जाते.
    
    ![screenshot](images/messages-newposition.png)

+ नवीन वर्ण स्तिथी छापण्या साठी कोड जोडा.
    
    ![screenshot](images/messages-newposition-print.png)

+ आपला नवीन कोड तपासून पहा. आपली `key` 3 आहे, त्याने 3 जोडले पाहिजे `position` वर आणि संचित करा आपल्या `newPosition` चल वर.
    
    उदाहरणार्थ, अक्षर 'e' स्थिती 4 वर आहे. कूटबद्ध करण्यासाठी, आपण `key` जोडा(3), जो 7 देतो.
    
    ![screenshot](images/messages-newposition-test.png)

+ काय होते जेव्हा आपण प्रयत्न आणि कूटबद्ध करतो अक्षर 'y' ला?
    
    ![screenshot](images/messages-modulus-bug.png)
    
    `newPosition` हे 27 वर कसे आहे ते पहा, आणि वर्णमालात 27 अक्षरे नसतात!

+ एकदा नवीन स्थितीत 26 वर गेल्यानंतर 0 स्थानावर परत जाण्यासाठी आपण `%` वापरू शकता.
    
    ![screenshot](images/messages-modulus.png)

+ शेवटी, आपल्याला नवीन स्थानावर अक्षर छापायचा आहे.
    
    उदाहरणार्थ, 'e' अक्षराची की जोडल्यास 7 मिळते, आणि अक्षराच्या 7 व्या स्थानावर असलेले अक्षर 'h' आहे.
    
    ![screenshot](images/messages-newcharacter.png)

+ आपला कोड वापरून पहा. आपण आपल्या काही छापलेल विधान काढू शकता, शेवटी शेवटी नवीन कॅरेक्टर प्रिंट करून.
    
    ![screenshot](images/messages-enc-test.png)