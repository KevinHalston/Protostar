from pwn import *

p = remote("159.65.135.221", 2222)

p.recvuntil(b"> ")
p.sendline(b"1")

def res(msg) -> str:
    test = msg.replace("b'","")
    if ("sub" in msg):
        arr = test.split()
        return str(int(arr[0], 10) - int(arr[2], 10))
    if ("add" in msg):
        arr = test.split()
        return str(int(arr[0], 10) + int(arr[2], 10))
    if ("mul" in msg):
        arr = test.split()
        return str(int(arr[0], 10) * int(arr[2], 10))
    if ("div" in msg):
        arr = test.split()
        return str(int(arr[0], 10) // int(arr[2], 10))

print('27'+'320')
test = ""

count = 0
while (count != 501):
    test = test = p.recvline()
    if (count == 500 ):
        print(test)

    msg = p.recvuntil("?") 
    if (count == 500 ):
        print(msg)

    payload = res(str(msg))
    p.sendline(payload)

    test = p.recvline()
    if (count == 500 ):
        print(test)

    count += 1
