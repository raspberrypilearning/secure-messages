## تشفير الرسائل ككل

بدلًا من مجرد تشفير الرسائل وفك تشفيرها حرفًا بحرف في كل مرة، لنغيِّر البرنامج لتشفير الرسائل ككل!



+ أولًا، تأكد من التعليمات البرمجية بالشكل التالي:

	![screenshot](images/messages-character-finished.png)

+ أنشئ متغيرًا لتخزين الرسالة الجديدة المشفرة.

	![screenshot](images/messages-newmessage.png)

+ غيِّر التعليمات البرمجية لتخزين رسالة المستخدم بدلًا من تخزين حرف واحد.

	![screenshot](images/messages-message.png)

+ أضف حلقة `for` إلى تعليماتك البرمجية، وأضف مسافة بادئة قبل باقي التعليمات البرمجية بحيث تتكرر مع كل حرف في الرسالة.

	![screenshot](images/messages-loop.png)

+ اختبر التعليمة البرمجية. سترى أن كل حرف في الرسالة قد تم تشفيره وطباعته على حدة.

	![screenshot](images/messages-loop-test.png)

+ لنضِف كل حرف مشفَّر إلى المتغير `newMessage`.

	![screenshot](images/messges-message-add-character.png)

+ يمكنك استخدام `print` لطباعة `newMessage` أثناء تشفيرها.

	![screenshot](images/messages-print-message-characters.png)

+ إذا قمتَ بحذف المسافات الموجودة قبل عبارة `print`، فستظهر رسالتك المشفَّرة مرة واحدة فقط في النهاية. ويمكنك أيضًا حذف التعليمة البرمجية الخاصة بطباعة مواضع الأحرف.

	![screenshot](images/messages-print-message-comment.png)



