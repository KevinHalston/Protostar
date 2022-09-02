# Stack 3

# ![image](https://user-images.githubusercontent.com/91616280/188245443-57424efc-04bd-43ec-8966-9c3c76ce100f.png)

# Ý tưởng khai thác
Nhìn vào đoạn code có thể thấy rằng khi đẩy lên stack ta sẽ nhảy đến hàm win bằng cách truyền tràn biến buffer bằng địa chỉ của win.

# Kịch bản khai thác

- Bước 1: chúng ta sẽ leak địa chỉ hàm win bằng gdb.
