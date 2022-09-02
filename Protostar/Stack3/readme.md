# Stack 3

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
  volatile int (*fp)();
  char buffer[64];

  fp = 0;

  gets(buffer);

  if(fp) {
      printf("calling function pointer, jumping to 0x%08x\n", fp);
      fp();
  }
}
```

# Ý tưởng khai thác
Nhìn vào đoạn code có thể thấy rằng khi đẩy lên stack ta sẽ nhảy đến hàm win bằng cách truyền tràn biến buffer bằng địa chỉ của win.

# Kịch bản khai thác

- Bước 1: chúng ta sẽ leak địa chỉ hàm win bằng gdb.

 ![image](https://user-images.githubusercontent.com/91616280/188245479-001f68c1-0068-43dd-bdf0-3d60103c4c86.png)

- Bước 2: chúng ta thực hiện viết payload để truyền chuỗi cần ghi vào.

 ![image](https://user-images.githubusercontent.com/91616280/188245504-fe5416b3-ae74-4186-9a62-9c46faa11c54.png)
![image](https://user-images.githubusercontent.com/91616280/188245545-34e1c622-2869-4ef3-b5df-2fe1d2e155e2.png)

