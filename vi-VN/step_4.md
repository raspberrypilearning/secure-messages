## Mã hóa thư

Hãy viết một chương trình Python để mã hóa một ký tự đơn.

+ Mở mẫu Python Trinket trống: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>.

+ Thay vì vẽ bảng chữ cái trong một vòng tròn, hãy viết nó ra dưới dạng biến `bảng chữ cái`.
    
    ![ảnh chụp màn hình](images/messages-alphabet.png)

+ Mỗi chữ cái của bảng chữ cái có một vị trí, bắt đầu từ vị trí 0. Vì vậy, chữ 'a' ở vị trí 0 của bảng chữ cái, và 'c' ở vị trí 2.
    
    ![ảnh chụp màn hình](images/messages-array.png)

+ Bạn có thể nhận được một lá thư từ biến `bảng chữ cái` của bạn bằng cách viết vị trí trong dấu ngoặc vuông.
    
    ![ảnh chụp màn hình](images/messages-alphabet-array.png)
    
    Bạn có thể xóa các câu lệnh `print` khi bạn đã thử điều này.

+ Tiếp theo, bạn sẽ cần lưu trữ bí mật `khóa` trong một biến.
    
    ![ảnh chụp màn hình](images/messages-key.png)

+ Tiếp theo, yêu cầu người dùng cho một chữ cái duy nhất (được gọi là `ký tự`) để mã hóa.
    
    ![ảnh chụp màn hình](images/messages-character.png)

+ Tìm các `vị trí` của `nhân vật`.
    
    ![ảnh chụp màn hình](images/messages-position.png)

+ Bạn có thể kiểm tra vị trí `được lưu trữ` bằng cách in nó. Ví dụ: ký tự 'e' đó ở vị trí 4 trong bảng chữ cái.
    
    ![ảnh chụp màn hình](images/messages-position-test.png)

+ Để mã hóa `nhân vật`, bạn nên thêm `chìa khóa` đến `vị trí`. Điều này sau đó được lưu trữ trong một biến `newPosition`.
    
    ![ảnh chụp màn hình](images/messages-newposition.png)

+ Thêm mã để in vị trí ký tự mới.
    
    ![ảnh chụp màn hình](images/messages-newposition-print.png)

+ Kiểm tra mã mới của bạn. Như bạn `chìa khóa` là 3, cần thêm 3 đến `vị trí` và lưu nó trong bạn `newPosition` biến.
    
    Ví dụ, chữ 'e' ở vị trí 4. Để mã hóa, bạn thêm phím `` (3), cho 7.
    
    ![ảnh chụp màn hình](images/messages-newposition-test.png)

+ Điều gì xảy ra khi bạn thử và mã hóa chữ 'y'?
    
    ![ảnh chụp màn hình](images/messages-modulus-bug.png)
    
    Lưu ý cách `newPosition` là 27 và không có 27 chữ cái trong bảng chữ cái!

+ Bạn có thể sử dụng `%` để cho vị trí mới quay trở lại vị trí 0 khi nó đến vị trí 26.
    
    ![ảnh chụp màn hình](images/messages-modulus.png)

+ Cuối cùng, bạn muốn in thư ở vị trí mới.
    
    Ví dụ: thêm khóa vào chữ 'e' cho 7 và chữ cái ở vị trí 7 của bảng chữ cái là 'h'.
    
    ![ảnh chụp màn hình](images/messages-newcharacter.png)

+ Hãy thử mã của bạn. Bạn cũng có thể xóa một số câu lệnh in của mình, chỉ cần in ký tự mới ở cuối.
    
    ![ảnh chụp màn hình](images/messages-enc-test.png)