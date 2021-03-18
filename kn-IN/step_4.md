## ಅಕ್ಷರಗಳನ್ನು ಎನ್‌ಕ್ರಿಪ್ಟ್ ಮಾಡಿ

ಒಂದು ಅಕ್ಷರ ಎನ್‌ಕ್ರಿಪ್ಟ್ ಮಾಡಲು ಪೈಥಾನ್ ಯೋಜನೆ ಬರಿಯೋಣ.

+ ಖಾಲಿ Python Trinket ಟೆಂಪ್ಲೆಟ್(ಮಾದರಿತೋರಕ): <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>ಅನ್ನು ತೆರೆಯಿರಿ.

+ ವೃತ್ತದಲ್ಲಿ ವರ್ಣಮಾಲೆಯನ್ನು ಚಿತ್ರಿಸುವ ಬದಲು, ಅದನ್ನು `alphabet` ವೇರಿಯಬಲ್ ಅಂತೆ ಬರೆಯೋಣ.
    
    ![screenshot](images/messages-alphabet.png)

+ ವರ್ಣಮಾಲೆಯ ಪ್ರತಿಯೊಂದು ಅಕ್ಷರವು ಒಂದು ಸ್ಥಾನವನ್ನು ಹೊಂದಿರುತ್ತದೆ, ಅದು 0 ನೇ ಸ್ಥಾನದಿಂದ ಪ್ರಾರಂಭವಾಗುತ್ತದೆ. ಆದ್ದರಿಂದ 'a' ಅಕ್ಷರವು ವರ್ಣಮಾಲೆಯ 0 ನೇ ಸ್ಥಾನದಲ್ಲಿದೆ ಮತ್ತು 'c' 2 ನೇ ಸ್ಥಾನದಲ್ಲಿದೆ.
    
    ![screenshot](images/messages-array.png)

+ ನೀವು ಒಂದು ಪತ್ರವನ್ನು ನಿಮ್ಮ `alphabet` ವೇರಿಯಬಲ್ ಮೂಲಕ, ಸ್ಥಾನವನ್ನು ಚದರ ಆವರಣಗಳಲ್ಲಿ ಬರೆದು ಪಡೆಯಬಹುದು.
    
    ![screenshot](images/messages-alphabet-array.png)
    
    ನೀವು ಒಮ್ಮೆ ಪೆಯತ್ನಿಸಿದ ನಂತರ `print` ವಾಕ್ಯವನ್ನು ಅಳಿಸಬಹುದು.

+ ಮುಂದೆ, ನೀವು ರಹಸ್ಯ`key` ಅನ್ನು ವೇರಿಯೇಬಲ್ನಲ್ಲಿ ಸಂಗ್ರಹಿಸಬೇಕಾಗುತ್ತದೆ.
    
    ![screenshot](images/messages-key.png)

+ ಮುಂದೆ, ಎನ್‌ಕ್ರಿಪ್ಟ್ ಮಾಡಲು ಒಂದೇ ಅಕ್ಷರಕ್ಕಾಗಿ ಬಳಕೆದಾರರನ್ನು ಕೇಳಿ (`character` ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ).
    
    ![screenshot](images/messages-character.png)

+ `character` ನ `position` ಅನ್ನು ಹುಡುಕಿ.
    
    ![screenshot](images/messages-position.png)

+ ನೀವು ಸಂಗ್ರಹಿಸಿದ `position` ಅನ್ನು ಪ್ರಿಂಟ್ ಮಾಡುವ ಮೂಲಕ ಪರೀಕ್ಷಿಸಬಹುದು. ಉದಾಹರಣೆಗೆ, 'e' ಅಕ್ಷರ ವರ್ಣಮಾಲೆಯಲ್ಲಿ 4 ನೇ ಸ್ಥಾನದಲ್ಲಿದೆ.
    
    ![screenshot](images/messages-position-test.png)

+ `character` ಅನ್ನು ಎನ್ಕ್ರಿಪ್ಟ್ ಮಾಡಲು, ನೀವು `key` ಅನ್ನು `position` ಗೆ ಸೇರಿಸಬೇಕು. ನಂತರ `newPosition` ವೇರಿಯಬಲ್ ನಲ್ಲಿ ಸಂಗ್ರಹಿಸಲಾಗುತ್ತದೆ.
    
    ![screenshot](images/messages-newposition.png)

+ ಹೊಸ ಅಕ್ಷರದ ಸ್ಥಾನ ಪ್ರಿಂಟ್ ಮಾಡಲು ಕೋಡ್ ಸೇರಿಸಿ.
    
    ![screenshot](images/messages-newposition-print.png)

+ ನಿಮ್ಮ ಹೊಸ ಕೋಡ್ಅನ್ನು ಪರೀಕ್ಷಿಸಿ. ನಿಮ್ಮ `key` 3 ಆಗಿದ್ದರಿಂದ, ಅದು `position` ಗೆ 3 ಅನ್ನು ಸೇರಿಸಬೇಕು ಮತ್ತು ಅದನ್ನು ನಿಮ್ಮ`newPosition` ವೇರಿಯಬಲ್ ಅಲ್ಲಿ ಸಂಗ್ರಹಿಸಬೆಕು.
    
    ಉದಾಹರಣೆಗೆ 'e' ಅಕ್ಷರ 4ನೇ ಸ್ಥಾನದಲ್ಲಿದೆ. ಎನ್ಕ್ರಿಪ್ಟ್ ಮಾಡಲು `key` (3) ಸೇರಿಸಿ, 7 ನೀಡಲಾಗುತ್ತದೆ.
    
    ![screenshot](images/messages-newposition-test.png)

+ ನೀವು ಅಕ್ಷರ 'y ' ಎನ್ಕ್ರಿಪ್ಟ್ ಮಾಡಲು ಪ್ರಯತ್ನಿಸಿದರೆ ಏನಾಗುತ್ತದ?
    
    ![screenshot](images/messages-modulus-bug.png)
    
    `new position` 27 ಆಗಿದೆ ಎಂಬುದನ್ನು ಗಮನಿಸಿ, ಮತ್ತು ವರ್ಣಮಾಲೆಯಲ್ಲಿ 27 ಅಕ್ಷರಗಳಿಲ್ಲ!

+ ನೀವು `%` ಬಲಿಸಬಹುದು 26 ನೇ ಸ್ಥಾನಕ್ಕೆ ತಲುಪಿದ ನಂತರ 0 ನೇ ಸ್ಥಾನಕ್ಕೆ ಹಿಂತಿರುಗಲು ಹೊಸ ಸ್ಥಾನವನ್ನು ಹೇಳಲು.
    
    ![screenshot](images/messages-modulus.png)

+ ಅಂತಿಮವಾಗಿ, ನೀವು ಅಕ್ಷರವನ್ನು ಹೊಸ ಸ್ಥಾನದಲ್ಲಿ ಪ್ರಿಂಟ್ ಮಾಡಲು ಬಯಸುತ್ತೀರಿ.
    
    ಉದಾಹರಣೆಗೆ, 'e' ಅಕ್ಷರಕ್ಕೆ ಕೀಲಿ ಸೇರಿಸುವುದು 7 ಅನ್ನು ನೀಡುತ್ತದೆ, ಮತ್ತು ವರ್ಣಮಾಲೆಯ 7 ನೇ ಸ್ಥಾನದಲ್ಲಿರುವ ಅಕ್ಷರವು 'h' ಆಗಿದೆ.
    
    ![screenshot](images/messages-newcharacter.png)

+ ನಿಮ್ಮ ಕೋಡ್ ಅನ್ನು ಪ್ರಯತ್ನಿಸಿ. ನಿಮ್ಮ ಕೆಲವು ಪ್ರಿಂಟ್ ಹೇಳಿಕೆಗಳನ್ನು ತೆಗೆದುಹಾಕಬಹುದು, ಕೊನೆಯಲ್ಲಿ ಹೊಸ ಅಕ್ಷರವನ್ನು ಪ್ರಿಂಟ್ ಮಾಡಬಹುದು.
    
    ![screenshot](images/messages-enc-test.png)