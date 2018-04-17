## تشفير الأحرف

لنكتب برنامج Python لتشفير حرف واحد.



افتح Trinket الذي يحتوي على قالب Python فارغ: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ بدلًا من كتابة الأحرف الأبجدية في دائرة، لنكتبها كمتغير `alphabet`.

	![screenshot](images/messages-alphabet.png)

+ لكل حرف من الأحرف الأبجدية موضع، بدءًا من الموضع 0. أي أن الحرف 'a' عند الموضع 0 من الأحرف الأبجدية، والحرف 'c' عند الموضع 2.

	![screenshot](images/messages-array.png)

+ يمكنك الحصول على حرف من المتغير `alphabet` بكتابة موضع هذا الحرف بين قوسين مربعين.

	![screenshot](images/messages-alphabet-array.png)

	يمكنك حذف عبارات `print` بعد انتهائك من اختبار هذا المتغير.

+ ستحتاج بعد ذلك إلى تخزين المفتاح `key` السري في متغير.

	![screenshot](images/messages-key.png)

+ بعد ذلك، اطلب من المستخدم إدخال حرف واحد (ويُسمى`character`) لتشفيره.

	![screenshot](images/messages-character.png)

+ ابحث عن `position` الخاص بالحرف `character`.

	![screenshot](images/messages-position.png)

+ يمكنك اختبار `position` الذي تم تخزينه عن طريق طباعته. على سبيل المثال، موضع الحرف 'e' هذا هو 4 في الأحرف الأبجدية.

	![screenshot](images/messages-position-test.png)

+ لتشفير `character`، يجب أن تجمع `key` و`position`. ثم يتم تخزين ذلك في متغير `newPosition`.

	![screenshot](images/messages-newposition.png)

+ أضف تعليمة برمجية لطباعة موضع الحرف الجديد. 

	![screenshot](images/messages-newposition-print.png)

+ اختبر التعليمة البرمجية الجديدة. لأن قيمة `key` هي 3، ستضيف هذه التعليمة البرمجية القيمة 3 إلى `position` وتخزِّن ذلك في متغير `newPosition`.

	على سبيل المثال، الحرف 'e' عند الموضع 4. لتشفيره، ستضيفُ `key`، أيْ (3)، وتحصل على 7.

	![screenshot](images/messages-newposition-test.png)

+ ماذا يحدث عندما تحاول تشفير الحرف 'y'؟

	![screenshot](images/messages-modulus-bug.png)

	لاحظ أن `newPosition` أصبح 27، ولا يوجد 27 حرفًا في الأحرف الأبجدية الإنجليزية!

+ يمكنك استخدام عامل `%` لتطلب من `newPosition` العودة إلى الموضع 0 بمجرد أن يصل إلى الموضع 26.

	![screenshot](images/messages-modulus.png)

+ وأخيرًا، ستحتاج إلى طباعة الحرف الموجود عند الموضع الجديد.

	على سبيل المثال، بإضافة المفتاح إلى الحرف 'e'، ستحصل على الموضع 7، والحرف الموجود عند الموضع 7 في الأحرف الأبجدية هو 'h'.

	![screenshot](images/messages-newcharacter.png)

+ اختبر التعليمة البرمجية. يمكنك أيضًا حذف بعض عبارات 'print' لطباعة الحرف الجديد فقط في النهاية.

	![screenshot](images/messages-enc-test.png)
