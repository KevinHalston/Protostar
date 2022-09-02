# Câu hỏi:

# Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in 
# thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

# Gợi ý:

# Trong trường hợp dữ liệu đầu vào được cung cấp, bạn hãy chọn cách để người dùng nhập số vào.

test = int(input("Nhap so test : "))

def tinhGiaiThua(x):
    if x == 0:
        return 1
    return x * tinhGiaiThua(x-1)

chuoiSo = []
while test != 0:
    n = int(input("Nhap so de tinh giai thua : "))
    key = tinhGiaiThua(n)
    chuoiSo.append(str(key))
    test -= 1

dauCham = ","
print(dauCham.join(chuoiSo))