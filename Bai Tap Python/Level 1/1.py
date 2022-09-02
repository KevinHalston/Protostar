# Câu hỏi:

# Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, 
# nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.

a = 2000
b = 3200
j = []
for i in range (a, b+1):
    if i % 7 == 0 and i % 5 != 0:
        j.append(str(i))
print(",".join(j))

str = "."
print(str.join(j))
#append là đẩy vào chuỗi
#.join ddeer in tren 1 dong