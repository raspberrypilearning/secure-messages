## ಪರಿಚಯ:

ಈ ಪ್ರೊಜೆಕ್ಟ್, ಅಲ್ಲಿ ನೀವು ನಿಮ್ಮ ಸ್ನೇಹಿತರಿಗೆ secret messages ಕಳಿಸಲು ಮತ್ತು ಪಡೆಯಲು ಒಂದು ಸ್ವಂತ encryption ಪ್ರೋಗ್ರಾಂ ಮಾಡಲು ಕಲಿಯುವಿರಿ. ಈ ಪ್ರೊಜೆಕ್ಟ್ಗೆ"Earth to Principia" activity on page 16 of the Space Diary ಜೊತೆಗೆ ಸಂಬಂಧ ಇದೆ.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/402256078c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

### Club leaders ಗಳಿಗೆ ಹೆಚ್ಚಿನ ಮಾಹಿತಿ

ನೀವು ಈ ಪ್ರೊಜೆಕ್ಟ್ print ಮಾಡಲು [Printer friendly version](https://projects.raspberrypi.org/en/projects/secret-messages/print) ಇದನ್ನು ಬಳಸಿ.

## \--- collapse \---

## ಶೀರ್ಷಿಕೆ: Club leader notes

## ಪರಿಚಯ:

ಈ ಪ್ರೊಜೆಕ್ಟ್, ಅಲ್ಲಿ ಮಕ್ಕಳು ತಮ್ಮ ಸ್ನೇಹಿತರಿಗೆ secret messages ಕಳಿಸಲು ಮತ್ತು ಪಡೆಯಲು ಒಂದು encryption ಪ್ರೋಗ್ರಾಂ ಮಾಡಲು ಕಲಿಯುವಿರಿ. ಈ ಪ್ರೊಜೆಕ್ಟ್iteration (looping) over a text string ಅನ್ನು ಪರಿಚಯಿಸುತ್ತದೆ.

## Online Resources

ಈ ಪ್ರೊಜೆಕ್ಟ್Python 3 ಬಳಸುತ್ತದೆ</strong>. ನಾವು Python online ಬರೆಯಲು [trinket](https://trinket.io/) ಅನ್ನು ಬಳಸಲು ಹೇಳುತ್ತೇವೆ. ಈಪ್ರೊಜೆಕ್ಟ್ ಅಲ್ಲಿ ಹಲವು Trinkets ಇದೆ:

* [New (blank) Python Trinket -- jumpto.cc/python-new](http://jumpto.cc/python-new)

ಪೂರ್ಣಗೊಂಡ ಯೋಜನೆಯನ್ನು ಒಳಗೊಂಡಿರುವ trinket ಸಹ ಇದೆ:

* [‘Secret Messages’ Finished -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

* [‘Friendship Calculator’ Finished -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## Offline Resources

ಈ ಪ್ರೊಜೆಕ್ಟ್ ಅನ್ನು[offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) ಅಲ್ಲಿ ಮುಗಿಸಬಹುದು.

ಈ ಪ್ರೊಜೆಕ್ಟ್ ಅನ್ನುcompleted project in the 'Volunteer Resources' section ಅಲ್ಲಿ ಹುಡುಕಬಹುದು:

* messages-finished/messages.py
* messages-finished/friends.py

(All of the resources above are also downloadable as ಪ್ರೊಜೆಕ್ಟ್ and volunteer `.zip` files.)

## Learning Objectives

* Iteration (looping) over a string variable;
* The `find()` method;
* The modulus operator (`%`).

ಈ ಪ್ರೊಜೆಕ್ಟ್ [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum) ಇದರ ಪಠ್ಯಕ್ರಮವನ್ನು ಅನುಸರಿಸುತ್ತದೆ:

* [Programming constructs ಅನ್ನು ಸಮಸೆಯೆ ಬಗೆಹರಿಸಲು ಒಟ್ಟುಗೂಡಿಸಿ.](https://www.raspberrypi.org/curriculum/programming/builder)

## ಸವಾಲುಗಳು

* ಅಕ್ಷರಗಳು ಮತ್ತು ಪದಗಳನ್ನು manually encrypt ಹಾಗೂ decrypt ಮಾಡಲು Caesar cipher ಬಳಸಿ;
* Variable keys - allowing the user to input a chosen key;
* Encrypting and decrypting messages - encrypting and decrypting whole messages;
* Friendship calculator - applying text iteration to a new problem.

## ಅಕ್ಷರಗಳು ಮತ್ತು ಪದಗನ್ನು manually encrypt ಹಾಗೂ decrypt ಮಾಡಲು Caesar cipher ಬಳಸಿ

* ಹುಡುಕುವ ಮುನ್ನಉಪಯೋಗಿಸಿಕೊಂಡು`find()` ಅಥವಾ `if char in alphabet:`, ಗಮನಿಸಿ ಹುಡುಕುವುದೆಲ್ಲ ಕೇಸ್ ಸೆನ್ಸಿಟಿವ್. ಮಕ್ಕಳು ಉಪಯೋಗಿಸಬಹುದು:
    
    ```python
    message = input("Please enter a message to encrypt: ").lower()
    ```
    
    ಹುಡುಕುವ ಮೊದಲು input lower case ಮಾಡಲು.

\--- /collapse \---

## \--- collapse \---

## ಶೀರ್ಷಿಕೆ: ಪ್ರಾಜೆಕ್ಟ್ ವಸ್ತುಗಳು

## ಪ್ರಾಜೆಕ್ಟ್ ಸಂಪನ್ಮೂಲಗಳು

* [.zip file containing all project resources](resources/secret-messages-project-resources.zip)
* [Online blank Python Trinket](http://jumpto.cc/python-new)
* [ಅಫ್ಲಿನ್ ಖಾಲಿ Python file](resources/new-new.py)

## Club leader resources

* [ಮುಗಿದ ಪ್ರೊಜೆಕ್ಟ್ resources ಇರುವ.zip file](resources/secret-messages-volunteer-resources.zip)
* [ಆನ್ಲೈನ್ ನಂಪೂರ್ಣ Trinket ಯೋಜನೆ](https://trinket.io/python/402256078c)
* [secret-messages-finished/messages.py](resources/secret-messages-finished-messages.py)
* [ಆನ್ಲೈನ್ ಸಂಪೂರ್ಣ 'ಸ್ನೇಹಿತ ಕ್ಯಾಲ್ಕುಲೇಟರ್' ಸವಾಲು](https://trinket.io/python/2e852cd687)
* [ಅಫ್ಲಿನ್ ಸಂಪೂರ್ಣ 'ಸ್ನೇಹಿತ ಕ್ಯಾಲ್ಕುಲೇಟರ್' ಸವಾಲು](resources/friendship-calculator-finished-friends.py)

\--- /collapse \---