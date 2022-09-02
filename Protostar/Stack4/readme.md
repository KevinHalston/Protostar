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

# ![image](https://user-images.githubusercontent.com/91616280/188239062-965d13b3-8029-4d0d-afbc-de8677dc4593.png)
