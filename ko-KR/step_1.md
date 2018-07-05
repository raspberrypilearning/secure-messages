## 들어가며:

이 프로젝트에서는 자신만의 암호화 프로그램을 만들고, 친구와 비밀 메시지를 주고받는 방법을 배웁니다. 

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/402256078c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/messages-finished.png">
</div>

### 교육자들을 위한 추가 정보

이 프로젝트를 인쇄하려면 [인쇄용 문서](https://projects.raspberrypi.org/en/projects/secret-messages/print)를 사용하십시오.

## \--- collapse \---

## title: 교육자 노트

## 들어가며:

In this project, children will learn how to make an encryption program, to send and receive secret messages with a friend. This project introduces iteration (looping) over a text string.

## Online Resources

**이 프로젝트는 파이썬3를 사용합니다.** 파이썬 코드를 온라인에서 작성하기 위해 [Trinket](https://trinket.io/)을 사용하는것을 추천합니다. 이 프로젝트는 다음 Trinket을 포함합니다:

* [새로운 (비어있는) Python Trinket -- jumpto.cc/python-new](http://jumpto.cc/python-new)

완성 된 프로젝트를 포함한 Trinket도 있습니다:

* ['비밀 메시지' 완성본 -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

* ['우정 계산기' 완성본 -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

## 오프라인 자료

원한다면 프로젝트를 [오프라인으로 완성](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/)할 수 있습니다.

You can find the completed project in the 'Volunteer Resources' section, which contains:

* messages-finished/messages.py
* messages-finished/friends.py

(All of the resources above are also downloadable as project and volunteer `.zip` files.)

## 학습 목표

* Iteration (looping) over a string variable;
* `find()` 함수
* 나머지 계산 기호(`%`)

이 프로젝트는 [라즈베리파이 디지털 메이킹 커리큘럼](http://rpf.io/curriculum) 중 아래의 과정에 있는 요소들을 다룹니다.

* [프로그래밍 구조를 결합하여 문제 해결하기](https://www.raspberrypi.org/curriculum/programming/builder)

## 도전과제

* 카이사르 암호 사용해보기 - 문자와 단어를 직접 암호화 하고 해독합니다.
* Variable keys - allowing the user to input a chosen key;
* 메시지 암호화 하고 해독하기 - 전체 메시지를 암호화하고 해독합니다.
* Friendship calculator - applying text iteration to a new problem.

## 자주 물어보는 질문

* When searching using `find()` or `if char in alphabet:`, note that searches are case-sensitive. Children can use:
    
    ```python
    message = input("Please enter a message to encrypt: ").lower()
    ```
    
    to make the input lower case before searching.

\--- /collapse \---

## \--- collapse \---

## title: 프로젝트 자료

## 프로젝트 자료

* [.zip file containing all project resources](resources/secret-messages-project-resources.zip)
* [Online blank Python Trinket](http://jumpto.cc/python-new)
* [Offline blank Python file](resources/new-new.py)

## 교육자를 위한 자료

* [.zip file containing all completed project resources](resources/secret-messages-volunteer-resources.zip)
* [Online completed Trinket project](https://trinket.io/python/402256078c)
* [secret-messages-finished/messages.py](resources/secret-messages-finished-messages.py)
* [Online completed 'Friendship calculator' challenge](https://trinket.io/python/2e852cd687)
* [offline complete 'Friendship calculator' challenge](resources/friendship-calculator-finished-friends.py)

\--- /collapse \---