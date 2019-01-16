## Nhân vật phụ

Một số ký tự không có trong bảng chữ cái, gây ra lỗi.

+ Kiểm tra mã của bạn với một số ký tự không có trong bảng chữ cái.
    
    Ví dụ, bạn có thể sử dụng tin nhắn `hi there !!`.
    
    ![ảnh chụp màn hình](images/messages-extra-characters.png)
    
    Lưu ý rằng không gian và `!` ký tự được mã hóa dưới dạng chữ 'c'!

+ Để khắc phục điều này, bạn chỉ muốn dịch một ký tự nếu nó nằm trong bảng chữ cái. Để thực hiện việc này, hãy thêm câu lệnh `if` vào mã của bạn và thụt lề phần còn lại của mã.
    
    ![ảnh chụp màn hình](images/messages-if.png)

+ Kiểm tra mã của bạn với cùng một thông báo. Điều gì xảy ra lần này?
    
    ![ảnh chụp màn hình](images/messages-if-test.png)
    
    Bây giờ, mã của bạn chỉ bỏ qua bất kỳ ký tự nào nếu nó không có trong bảng chữ cái.

+ Sẽ tốt hơn nếu mã của bạn không mã hóa bất kỳ thứ gì không có trong bảng chữ cái, nhưng chỉ sử dụng ký tự gốc.
    
    Thêm câu lệnh `else` vào mã của bạn, chỉ thêm ký tự gốc vào thư được mã hóa.
    
    ![ảnh chụp màn hình](images/messages-else.png)

+ Kiểm tra mã của bạn. Bạn sẽ thấy rằng bất kỳ ký tự nào trong bảng chữ cái được mã hóa, nhưng bất kỳ ký tự nào khác đều bị bỏ lại một mình!
    
    ![ảnh chụp màn hình](images/messages-else-test.png)