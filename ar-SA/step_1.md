## المقدمة:

في هذه المشروع ستتعلم كيفية صنع برنامج التشفير الخاص بك لإرسال واستلام الرسائل السرية مع صديق. هذا المشروع مرتبط بنشاط "Earth to Principia" في الصفحة 16 من Space Diary.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/402256078c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

### معلومات إضافية لقادة النادي

إذا كنت بحاجة إلى طباعة هذا المشروع، فيُرجى استخدام [النسخة القابلة للطباعة](https://projects.raspberrypi.org/en/projects/secret-messages/print).

## \--- collapse \---

## title: ملاحظات قادة النادي

## مقدمة:

في هذا المشروع، سيتعلم الأطفال كيفية إنشاء برنامج تشفير، لإرسال واستلام الرسائل السرية مع صديق. يقدم هذا المشروع التكرار (حلقات) على سلسلة نصية.

## الموارد المتوفرة على الإنترنت

**يستخدم هذا المشروع Python 3.** نوصي باستخدام [trinket](https://trinket.io/) لكتابة لغة Python على الانترنت. يحتوى هذا المشروع على Trinkets التالية:

* [Python Trinket جديد (فارغ) -- jumpto.cc/python-new](http://jumpto.cc/python-new)

هناك أيضًا trinket تحتوي على المشروع المكتمل:

* ["رسائل سرية" مكتمل -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

* ["حاسبة الصداقة" مكتمل -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## الموارد المتوفرة دون اتصال بالإنترنت

يمكنك إكمال هذا المشروع [ دون اتصال بالإنترنت](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) إذا كنت تفضل ذلك.

يمكنك العثور على النسخة المكتملة من هذا المشروع في قسم "موارد المتطوعين"، و الذي يحتوي على:

* messages-finished/messages.py
* messages-finished/friends.py

(جميع الموارد المذكورة أعلاه قابلة للتنزيل أيضًا كملفات `.zip` للمشاريع والمتطوعين)

## أهداف التعلم

* التكرار (حلقات) على نص متغير؛
* طريقة `()find `؛
* معامل باقى القسمة (`%`).

يتناول هذا المشروع عناصر من معايير المناهج الرقمية الخاصة بـ [Raspberry Pi](http://rpf.io/curriculum):

* [دمج الإنشاءات البرمجية لحل مشكلة.](https://www.raspberrypi.org/curriculum/programming/builder)

## التحديات

* استخدام شفرة قيصر - تشفير وفك تشفير الحروف والكلمات يدويا؛
* مفاتيح المتغيرات - السماح للمستخدم بإدخال مفتاح مختار؛
* تشفير الرسائل وفك تشفيرها - تشفير وفك تشفير الرسائل بأكملها؛
* حاسبة الصداقة - تطبيق تكرار النص على مشكلة جديدة.

## الأسئلة الشائعة

* عند البحث باستخدام `()find `او ` :if char in alphabet `، لاحظ أن عمليات البحث حساسة لحالة الأحرف. يمكن للأطفال استخدام:
    
    ```python
    ()message = input("الرجاء ادخال رسالة لتشفيرها: ").lower
    ```
    
    لجعل الإدخال بحالة الأحرف الصغيرة قبل البحث (في حالة استخدام اللغة الانكليزية).

\--- /collapse \---

## \--- collapse \---

## title: مواد المشروع

## موارد المشروع

* [ملف.zip يحتوي على جميع موارد المشروع](resources/secret-messages-project-resources.zip)
* [Python Trinket فارغ على الانترنت](http://jumpto.cc/python-new)
* [ملف Python فارغ بدون الاتصال بالانترنت](resources/new-new.py)

## موارد قادة النادي

* [ملف.zip يحتوي على جميع موارد المشروع المكتملة](resources/secret-messages-volunteer-resources.zip)
* [مشروع Trinket المكتمل على الإنترنت](https://trinket.io/python/402256078c)
* [secret-messages-finished/messages.py](resources/secret-messages-finished-messages.py)
* [تحدي "حاسبة الصداقة" مكتمل على الانترنت](https://trinket.io/python/2e852cd687)
* [تحدي "حاسبة الصداقة" مكتمل بدون الاتصال بالانترنت](resources/friendship-calculator-finished-friends.py)

\--- /collapse \---