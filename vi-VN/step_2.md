## Mật mã Caesar

Mật mã là một loại mã bí mật, nơi bạn trao đổi các chữ cái xung quanh để không ai có thể đọc tin nhắn của bạn.

Bạn sẽ sử dụng một trong những mật mã lâu đời nhất và nổi tiếng nhất, mật mã **Caesar**, được đặt tên theo Julius Caesar.

Trước khi chúng tôi bắt đầu viết mã, hãy thử sử dụng mật mã Caesar để ẩn một từ.

+ Ẩn một từ được gọi là **mã hóa**.
    
    Hãy bắt đầu bằng cách mã hóa chữ 'a'. Để làm điều này, chúng ta có thể vẽ bảng chữ cái theo hình tròn, như sau:
    
    ![ảnh chụp màn hình](images/messages-wheel.png)

+ Để tạo một thư được mã hóa bí mật từ một ký tự bình thường, bạn cần có một khóa bí mật. Hãy sử dụng số 3 làm khóa (nhưng bạn có thể sử dụng bất kỳ số nào bạn thích).
    
    Để **mã hóa** chữ cái 'a', bạn chỉ cần di chuyển 3 chữ cái theo chiều kim đồng hồ, nó sẽ cho bạn chữ 'd':
    
    ![ảnh chụp màn hình](images/messages-wheel-eg.png)

+ Bạn có thể sử dụng những gì bạn đã học để mã hóa toàn bộ một từ. Ví dụ, 'hello' được mã hóa là 'kho'. Hãy thử nó cho mình.
    
    + h + 3 = **k**
    + e + 3 = **h**
    + l + 3 = **o**
    + l + 3 = **o**
    + o + 3 = **r**

+ Lấy văn bản trở lại bình thường được gọi là **giải mã**. Để giải mã một từ, chỉ cần trừ phím thay vì thêm nó:
    
    + k - 3 = **h**
    + h - 3 = **e**
    + o - 3 = **l**
    + o - 3 = **l**
    + r - 3 = **o**