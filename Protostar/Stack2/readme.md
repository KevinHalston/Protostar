# Stack Two

```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];
  char *variable;

  variable = getenv("GREENIE");

  if(variable == NULL) {
      errx(1, "please set the GREENIE environment variable\n");
  }

  modified = 0;

  strcpy(buffer, variable);

  if(modified == 0x0d0a0d0a) {
      printf("you have correctly modified the variable\n");
  } else {
      printf("Try again, you got 0x%08x\n", modified);
  }

}
```
# Ý tưởng khai thác:
Ta có thể thấy Stack2 khá giống với Stack1 vì vậy kịch bản khai thác cũng tương tự nhưng khác ở cách send payload.

# ![image](https://user-images.githubusercontent.com/91616280/188245408-e82350e8-6d30-4e38-bf41-aac81297f813.png)
