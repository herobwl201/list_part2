from copy import deepcopy
"""

+ set: đc tạo bởi dấu ngoặc nhọn và trong set không thể chứa 
những phần tử trùng lập, set thì không có thứ tự
+ khi dùng so sánh một số thì dùng set nhanh hơn so với list và tuple
+ tuple: là 1 bộ giá trị, là 1 cấu trúc dữ liệu mà có thứ tự,
có thể chứa những phần tử trùng lặp
và đc tạo bởi dấu ngoặc tròn
+ tuple tương tự với list nhưng nó không thể 
thay đổi bản thân nó và giá trị bên trong nó
+ tuple dùng nhiều trong data, csdl

"""

# tuple

tup1 = 1, 2, 3
tup2 = (1, 2, 3)
tup3 = 1,
tup4 = (4,)

print(type(tup1))
print(type(tup2))
print(type(tup3))
print(type(tup4))

# print(tup1[-1])
# tup1[0] = 1000 # run error, b/c tuple không thể thay đổi giá trị của nó

# tup1.append(1000) # run error, tuple ko có thuộc tính append
tup1 += (4, 5, 6, 7, 1)  # thêm giá trị vào cuối tuple, update lại tuple
print(tup1)

# set
set1 = set()
print(len(set1))  # result: 0
set1.add(1)  # thêm 1 vào set trống
set1.add(1)  # thêm 1 vào set trống
set1.add(1)  # thêm 1 vào set trống
set1.add(1)  # thêm 1 vào set trống
set1.add(1)  # thêm 1 vào set trống

print(set1)# result: {1}, vì không thêm vào đc giá trị lặp lại, nó thấy có 1 rồi thì không thêm đc nữa 

set1.update([2, 3, 4, 5])  # update vào set1 giá trị 2, 3, 4, 5
set1.remove(1)  # remove giá trị 1 trong set
print(set1)
set2 = set1.copy()

print(set1 is set2) # result: False. Giải thích: vụ photo từ bản gốc sang bản sao)
print(set1 == set2) # result: True
set1.clear()
print(set1)

set3 ={1,2,3,4}

set1.add("Kenny")
print(type(set3))
print(set1) # result: error, unhashable
# print(set1[-1]) # error: không thể truy cập bằng chỉ số
# set1.remove(1000)

# set 4
set4 = {10, 12, 23, 1, 2,3,-10}
any_value = set4.pop # lấy ra giá trị ngẫu nhiên trong set
print(set4)

# tuple + list
friends = [
    ("Bob", 23),
    ("Anna", 35),
    ("Henry", 34)
]

print(friends[0][1])
print(friends[2])  # or -1

lst = [[1, [2,3]], (2,4)]
lst1=deepcopy(lst) # lệnh copy, lst[:] = lst.remove()
print(lst[0][1])
print(lst[0][1][0])
lst[0][1].append(100)
print(lst1)
print(isinstance(3, int))


print(ord('1') ^ ord('3')) # ord: dùng để mã hóa, ^: dấu XOR, dùng để so sánh, 1 ^ 1 =0, 0 ^ 0 = 0, 1 ^ 0 = 1, 0 ^ 1 = 1
print(abs(-1)) # abs: trị tuyệt đối
print(abs(1+2j))
print(repr('a')) # in ra kèm dấu nháy đơn 'a'
s = 'a'
a = 3
print(f"{s!r}") # <=> repr('a')
print(f"{a!r}") # <=> repr('a')
