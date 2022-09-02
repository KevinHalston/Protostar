# Stack 1

```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];

  if(argc == 1) {
      errx(1, "please specify an argument\n");
  }

  modified = 0;
  strcpy(buffer, argv[1]);

  if(modified == 0x61626364) {
      printf("you have correctly got the variable to the right value\n");
  } else {
      printf("Try again, you got 0x%08x\n", modified);
  }
}
```

# Ý tưởng khai thác
Như stack0 chúng ta sẽ truyền vào 1 chuỗi 64 kí tự kèm them giá trị của modified = \x64\x63\x62\x61 vào trong chuỗi đó từ đó có thể thay đổi giá trị của modified.

# Kịch bản khai thác

# ![image](https://user-images.githubusercontent.com/91616280/188239943-59378c4f-919d-4260-8484-978ca6d5f2ae.png)

