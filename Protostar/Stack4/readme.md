# Stack 4
```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void win()
{
  printf("code flow successfully changed\n");
}

int main(int argc, char **argv)
{
  char buffer[64];

  gets(buffer);
}
```

# Ý tưởng khai thác
Ta sẽ truyền vào 1 chuỗi > số kí tự mà chuỗi buffer được nhập để khi đẩy lên stack thì modified sẽ nhận giá trị mới khác 0

# Kịch bản khai thác

- Bước 1: chúng ta sẽ leak địa chỉ hàm win bằng gdb.
 
 ![image](https://user-images.githubusercontent.com/91616280/188239062-965d13b3-8029-4d0d-afbc-de8677dc4593.png)
 
- Bước 2: tạo payload để tìm ra số byte ở thanh ghi ebp cũ cần ghi đè

![image](https://user-images.githubusercontent.com/91616280/188245874-6bbb687c-2e42-435f-9ba4-4f35c9015927.png)

- Bước 3: Sau đó chúng ta sẽ truyền nó vào 1 file text

![image](https://user-images.githubusercontent.com/91616280/188245886-8c600fe5-d49c-40b5-885e-09d52648bfb3.png)

- Bước 4: chạy với file text đặt b* tại main+21 (leave)  để kiểm tra các thanh ghi
 
![image](https://user-images.githubusercontent.com/91616280/188245917-aa4d0fe0-fdb0-44a4-9c06-050ae72411c7.png)

- Bước 5: kiếm tra trên stack địa chỉ kết thúc của thanh ghi ebp
 
![image](https://user-images.githubusercontent.com/91616280/188245932-57ccad0b-9be6-46d2-9951-44efd36262f4.png)

```
Ta có thể thấy tại địa chỉ 0xbffffd30 chúng ta thiếu 12 byte mới có thể ghi đè hết thanh ghi ebp và trả về địa chỉ hàm win
Vì vậy chúng ta cần ghi đè them 12 byte nữa là 64+12 = 76 byte + ret(win) mới có thể in ra được kết quả mong muốn.

```
- Bước 6 : chỉnh sửa payload và chạy lại file.
 
![image](https://user-images.githubusercontent.com/91616280/188245972-c994de74-8d96-46ec-9b75-1c4ee82a06ba.png)
![image](https://user-images.githubusercontent.com/91616280/188245993-be8afc9b-f307-4bc1-936e-3a197e2e93af.png)

