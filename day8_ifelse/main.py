"""
if-elif-else
if <biểu thức so sánh>:
print
"""
if 1 > 0:
    print("1 > 0")
else:
    print("1 <= 0")

print("--------------------")

# n = int(input("n= ")) # kiểm tra n là số dương không
# if n == 0:
#     print("So duong")

'''
n = int(input("n= ")) # kiểm tra n có chia hết cho 3 không?
if n % 3 ==0:
    print("n chia het cho 3")
else:
    print("n khong chia het cho 3")

print("n chia het cho 3" if n % 3 == 0 else "n khong chi het cho 3") # câu lệnh if rút gọn cho ra kết quả tương ứng
'''

print("--------------------")
# a = int(input('a = '))
# b = int(input('b = '))

# Shift + Alt + A
# Tìm số lớn nhất trong hai số
# print(a if a > b else b)

""" m = a

if b > a:
    m = b

print(m) """

print("--------------------")

# Một số hàm có sẵn giúp thực hiện dễ hơn

# Hàm giúp nhập nhiều dữ liệu trên cùng một hàng
# split() mình không truyền vào thì mặc định là n nhiều dấu cách vô tận
a, b = map(int, input().split())
print(a if a < b else b)

# split() mình không truyền vào thì mặc định là n nhiều dấu cách vô tận
a, b = map(float, input().split())
print(a if a < b else b)

# Hàm eval: dùng đánh giá biểu thức nằm bên trong chuỗi

print(eval("1 + 2 ** 4"))  # =17
a, b = map(eval, input().split())  # kiễm tra a, b là bao nhiêu
print(a)
print(b)

lst = list(map(eval, input().split()))  # kiễm tra list
print(lst)

# in ra đúng định dạng mình viết
lst = [1, 2, 3, 4] 
# 1 2 3 4
print(*lst)

print(*lst, sep = "%")

# Hàm format
x = 2.4567
print(format(x, ".2f")) # làm tròn tới 2 chữ số thập phân = 2.46

# Hàm round: làm tròn giá trị
x = 2.456
print(round(x))

print(pow(2,3)) # Hàm lũy thừa 2 ^ 3 = 8

# sorted: nó luôn trả về một danh sách mới được sắp xếp, khác so với sort, sorted tạo ra bản mới
lst = [4,3,2,10]
new_lst = sorted(lst) # sắp xếp theo chiều tăng dần
print(new_lst)
new_lst = sorted(lst, reverse=True) # sắp xếp theo chiều giảm dần
print(new_lst)

# Hàm in ra ASCII của kí tự
char = 'a'

print("ASCII Code:", ord(char)) 

# Ngược lại in từ ASCII ra ký tự
ascii_code = 97
print(chr(ascii_code))

# Hàm list 
s = 'abcd'
print(list(s)) # ['a', 'b', 'c', 'd']

#
lst= list(map(eval,input().split())) # Biến một map object thành list

# Hàm divmod
print(divmod(4,3)) # Result (4//3,4%3)

thuong, phandu = divmod(4,3)
print(thuong)
print(phandu)

# Hàm bin: biểu diễn nhị phân của một số nguyên
int_number = 10
binary_string = bin(int_number)
print(binary_string) # = 0b1010
'''
012345
0b1010
print(binary_string[2:])
'''

# Hàm range: giới hạn số chạy từ 0 -> x
print(list(range(255))) # Tạo list chạy từ 0 -> 255