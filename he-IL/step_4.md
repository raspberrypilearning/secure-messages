## הצפנת אותיות

בואו נכתוב תוכנית Python שמצפינה תו אחד.

+ פתחו את תבנית ה-Trinket הריקה של קובץ Python: <a href="http://jumpto.cc/python-new" target="_blank"> jumpto.cc/python-new </a>.

+ במקום לצייר את האלף-בית במעגל, נכתוב אותו כמשתנה `alphabet`.
    
    ![צילום מסך](images/messages-alphabet.png)

+ לכל אות באלף-בית יש מיקום, החל מהמיקום 0. האות 'a' נמצאת במיקום 0 של האלף-בית, ו-'c' נמצאת במיקום 2.
    
    ![צילום מסך](images/messages-array.png)

+ אפשר לקבל אות מהמשתנה `alphabet` על ידי כתיבת המיקום בסוגריים מרובעים.
    
    ![צילום מסך](images/messages-alphabet-array.png)
    
    אתם יכולים למחוק את ה- `print`-ים שהוספתם אחרי שניסיתם את זה.

+ לאחר מכן, נצטרך לשמור את ה-`key` (המפתח) במשתנה.
    
    ![צילום מסך](images/messages-key.png)

+ בשלב הבא, בקשו מהמשתמש אות יחידה (נקראת גם `character` - תו) להצפנה.
    
    ![צילום מסך](images/messages-character.png)

+ מצאו את המיקום (`position`) של התו (`character`).
    
    ![צילום מסך](images/messages-position.png)

+ אתם יכולים לבדוק את ה-`position` המאוחסן על ידי הדפסה למסך. למשל, לבדוק שהאות 'e' היא במיקום ה-4 באלף-בית.
    
    ![צילום מסך](images/messages-position-test.png)

+ כדי להצפין את ה-`character`, אתם צריכים להוסיף את ה-`key` ל-`position`. לאחר מכן התו הזה מאוחסן במשתנה `newPosition`.
    
    ![צילום מסך](images/messages-newposition.png)

+ הוסיפו קוד להדפסת התו החדש למסך.
    
    ![צילום מסך](images/messages-newposition-print.png)

+ בדקו את הקוד החדש שלכם. מכיוון שה-`key` שלכם הוא 3, זה אמור להוסיף 3 ל-`position` ולאחסן את התו במשתנה `newPosition`.
    
    לדוגמה, האות 'e' היא במיקום 4, כדי להצפין אותה, צריך להוסיף את המפתח (3) - מה שנותן 7.
    
    ![צילום מסך](images/messages-newposition-test.png)

+ מה קורה כשמנסים להצפין את האות 'y'?
    
    ![צילום מסך](images/messages-modulus-bug.png)
    
    שימו לב שה-`newPosition` הוא 28, ואין 28 אותיות באלף-בית!

+ אתם יכולים להשתמש ב-`%` כדי להגיד למיקום החדש לחזור ל-0 כשהוא מגיע ל-26.
    
    ![צילום מסך](images/messages-modulus.png)

+ בסופו של דבר, אתם רוצים להדפיס למסך את האות שנמצאת במיקום החדש.
    
    למשל, הוספת המפתח לאות 'e' נותן 7, והאות במיקום 7 באלף-בית היא 'h'.
    
    ![צילום מסך](images/messages-newcharacter.png)

+ נסו את הקוד שלכם. אתם יכולים למחוק חלק מה-print-ים בתוכנית, כך שרק התו החדש יודפס.
    
    ![צילום מסך](images/messages-enc-test.png)