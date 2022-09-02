#include <stdio.h>

int main(){
  char key[8]= {0};
  char flag[39] = "xsmuaw`rp7v^ZltVp7V^P0p:zt7s]@nh96ao;f{";
  char *v5;
  puts("Guest your flag. The flag will be of the form ptitctf{[a-zA-Z0-9]_}");
  printf("Enter your key:");
  for (int i = 0; i < 8; ++i )
    scanf("%hhd", &key[i]);
  for (int j = 0; j < 39; ++j)
  {
    *((char *)&flag + j)^= key[j % 8u];
  }
  printf("flag is : %s\n", &flag);
  return 0;
}