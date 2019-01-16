## Mã hóa toàn bộ thư

Thay vì chỉ mã hóa và giải mã thư một ký tự cùng một lúc, hãy thay đổi chương trình để mã hóa toàn bộ thư!

+ Trước tiên, hãy kiểm tra xem mã của bạn có trông giống như sau:
    
    ![ảnh chụp màn hình](images/messages-character-finished.png)

+ Tạo một biến để lưu trữ tin nhắn được mã hóa mới.
    
    ![ảnh chụp màn hình](images/messages-newmessage.png)

+ Thay đổi mã của bạn để lưu trữ thư của người dùng chứ không phải chỉ một ký tự.
    
    ![ảnh chụp màn hình](images/messages-message.png)

+ Thêm vòng lặp `cho` vào mã của bạn và thụt lề phần còn lại của mã để mã được lặp lại cho mỗi ký tự trong thư.
    
    ![ảnh chụp màn hình](images/messages-loop.png)

+ Kiểm tra mã của bạn. Bạn sẽ thấy rằng mỗi ký tự trong tin nhắn được mã hóa và in từng cái một.
    
    ![ảnh chụp màn hình](images/messages-loop-test.png)

+ Hãy thêm mỗi ký tự được mã hóa vào biến `newMessage` của bạn.
    
    ![ảnh chụp màn hình](images/messges-message-add-character.png)

+ Bạn có thể `in` `newMessage` vì nó đang được mã hóa.
    
    ![ảnh chụp màn hình](images/messages-print-message-characters.png)

+ Nếu bạn xóa dấu cách trước câu lệnh `in` , thông báo được mã hóa sẽ chỉ được hiển thị một lần ở cuối. Bạn cũng có thể xóa mã để in các vị trí ký tự.
    
    ![ảnh chụp màn hình](images/messages-print-message-comment.png)