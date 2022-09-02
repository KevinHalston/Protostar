# Câu hỏi:

# Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in 
# thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

# Gợi ý:

# Trong trường hợp dữ liệu đầu vào được cung cấp, bạn hãy chọn cách để người dùng nhập số vào.

test = int(input("Nhap so test : "))
str_1 = []

while test != 0:
    n = int(input("Nhap so muon tinh giai thua : "))
    a = 1
    i = 1
    for i in range (1, n+1):
        a *= i
    str_1.append(str(a))
    test -= 1
    
x = ","
print(x.join(str_1))
